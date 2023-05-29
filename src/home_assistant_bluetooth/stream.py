"""Process a bluetooth advertisement stream."""
from typing import Any

from bleak.backends.device import BLEDevice
from bleak.backends.scanner import AdvertisementData

from .models import BluetoothServiceInfoBleak
from .time import monotonic_time_coarse

NO_RSSI_VALUE = -127

_float = float  # avoid cython conversion since we always want a pyfloat
_int = int  # avoid cython conversion since we always want a pyint
_str = str  # avoid cython conversion since we always want a pystr


class BluetoothAdvertisementStream:
    """Stream of BluetoothAdvertisement."""

    def __init__(self, connectable: bool, source: str, details: dict[Any, Any]) -> None:
        """Initialize a bluetooth service info stream."""
        self._connectable = connectable
        self._source = source
        self._details = details
        self._previous: dict[str, BluetoothServiceInfoBleak] = {}

    def process(
        self,
        address: _str,
        rssi: _int,
        local_name: _str | None,
        service_uuids: list[str],
        service_data: dict[str, bytes],
        manufacturer_data: dict[int, bytes],
        tx_power: _int | None,
        details: dict[Any, Any],
    ) -> BluetoothServiceInfoBleak:
        """Create a new BluetoothServiceInfoBleak from incoming data and previous discovery."""
        monotonic_time = monotonic_time_coarse()
        prev_discovery = self._previous.get(address)
        if prev_discovery:
            # Merge the new data with the old data
            # to function the same as BlueZ which
            # merges the dicts on PropertiesChanged
            prev_service_uuids = prev_discovery.service_uuids
            prev_service_data = prev_discovery.service_data
            prev_manufacturer_data = prev_discovery.manufacturer_data
            prev_name = prev_discovery.name

            if local_name and prev_name and len(prev_name) > len(local_name):
                local_name = prev_name

            if service_uuids and service_uuids != prev_service_uuids:
                service_uuids = list(set(service_uuids + prev_service_uuids))
            elif not service_uuids:
                service_uuids = prev_service_uuids

            if service_data and service_data != prev_service_data:
                service_data = {**prev_service_data, **service_data}
            elif not service_data:
                service_data = prev_service_data

            if manufacturer_data and manufacturer_data != prev_manufacturer_data:
                manufacturer_data = {**prev_manufacturer_data, **manufacturer_data}
            elif not manufacturer_data:
                manufacturer_data = prev_manufacturer_data
            #
            # Bleak updates the BLEDevice via create_or_update_device.
            # We need to do the same to ensure integrations that already
            # have the BLEDevice object get the updated details when they
            # change.
            #
            # https://github.com/hbldh/bleak/blob/222618b7747f0467dbb32bd3679f8cfaa19b1668/bleak/backends/scanner.py#L203
            #
            device = prev_discovery.device
            device.name = local_name
            device.details = ({**self._details, **details},)
            # pylint: disable-next=protected-access
            device._rssi = rssi  # deprecated, will be removed in newer bleak
        else:
            device = BLEDevice(
                address,
                local_name,
                {**self._details, **details},
                rssi,  # deprecated, will be removed in newer bleak
            )

        advertisement_data = AdvertisementData(
            None if local_name == "" else local_name,
            manufacturer_data,
            service_data,
            service_uuids,
            NO_RSSI_VALUE if tx_power is None else tx_power,
            rssi,
            (),
        )
        bluetooth_service_info_bleak = BluetoothServiceInfoBleak(
            local_name or address,
            address,
            rssi,
            manufacturer_data,
            service_data,
            service_uuids,
            self._source,
            device,
            advertisement_data,
            self._connectable,
            monotonic_time,
        )
        self._previous[address] = bluetooth_service_info_bleak
        return bluetooth_service_info_bleak
