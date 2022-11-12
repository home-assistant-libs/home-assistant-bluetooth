"""The bluetooth integration service info."""

import dataclasses
from functools import cached_property
from typing import Any, Dict, List, Final, TypeVar

from bleak.backends.device import BLEDevice
from bleak.backends.scanner import AdvertisementData

_BluetoothServiceInfoSelfT = TypeVar(
    "_BluetoothServiceInfoSelfT", bound="BluetoothServiceInfo"
)
SOURCE_LOCAL: Final = "local"


class BaseServiceInfo:
    """Base class for discovery ServiceInfo."""


class BluetoothServiceInfo(BaseServiceInfo):
    """Prepared info from bluetooth entries."""

    def __init__(
        self,
        name: str,
        address: str,
        rssi: int,
        manufacturer_data: Dict[int, bytes],
        service_data: Dict[str, bytes],
        service_uuids: List[str],
        source: str,
    ) -> None:
        """Initialize a bluetooth service info."""
        self.name = name
        self.address = address
        self.rssi = rssi
        self.manufacturer_data = manufacturer_data
        self.service_data = service_data
        self.service_uuids = service_uuids
        self.source = source

    @classmethod
    def from_advertisement(
        cls: type[_BluetoothServiceInfoSelfT],
        device: BLEDevice,
        advertisement_data: AdvertisementData,
        source: str,
    ) -> _BluetoothServiceInfoSelfT:
        """Create a BluetoothServiceInfo from an advertisement."""
        return cls(
            advertisement_data.local_name or device.name or device.address,
            device.address,
            advertisement_data.rssi,
            advertisement_data.manufacturer_data,
            advertisement_data.service_data,
            advertisement_data.service_uuids,
            source,
        )

    @cached_property
    def manufacturer(self) -> str | None:
        """Convert manufacturer data to a string."""
        from bleak.backends._manufacturers import (  # pylint: disable=import-outside-toplevel
            MANUFACTURERS,
        )

        for manufacturer in self.manufacturer_data:
            if manufacturer in MANUFACTURERS:
                name: str = MANUFACTURERS[manufacturer]
                return name
        return None

    @cached_property
    def manufacturer_id(self) -> int | None:
        """Get the first manufacturer id."""
        for manufacturer in self.manufacturer_data:
            return manufacturer
        return None


class BluetoothServiceInfoBleak(BluetoothServiceInfo):
    """BluetoothServiceInfo with bleak data.

    Integrations may need BLEDevice and AdvertisementData
    to connect to the device without having bleak trigger
    another scan to translate the address to the system's
    internal details.
    """

    def __init__(
        self,
        name: str,
        address: str,
        rssi: int,
        manufacturer_data: Dict[int, bytes],
        service_data: Dict[str, bytes],
        service_uuids: List[str],
        source: str,
        device: BLEDevice,
        advertisement: AdvertisementData,
        connectable: bool,
        time: float,
    ) -> None:
        self.name = name
        self.address = address
        self.rssi = rssi
        self.manufacturer_data = manufacturer_data
        self.service_data = service_data
        self.service_uuids = service_uuids
        self.source = source
        self.device = device
        self.advertisement = advertisement
        self.connectable = connectable
        self.time = time

    def as_dict(self) -> Dict[str, Any]:
        """Return as dict.

        The dataclass asdict method is not used because
        it will try to deepcopy pyobjc data which will fail.
        """
        return {
            "name": self.name,
            "address": self.address,
            "rssi": self.rssi,
            "manufacturer_data": self.manufacturer_data,
            "service_data": self.service_data,
            "service_uuids": self.service_uuids,
            "source": self.source,
            "advertisement": self.advertisement,
            "device": self.device,
            "connectable": self.connectable,
            "time": self.time,
        }

    @classmethod
    def from_scan(
        cls: "BluetoothServiceInfoBleak",
        source: str,
        device: BLEDevice,
        advertisement_data: AdvertisementData,
        monotonic_time: float,
        connectable: bool,
    ) -> "BluetoothServiceInfoBleak":
        """Create a BluetoothServiceInfoBleak from a scanner."""
        return cls(
            advertisement_data.local_name or device.name or device.address,
            device.address,
            advertisement_data.rssi,
            advertisement_data.manufacturer_data,
            advertisement_data.service_data,
            advertisement_data.service_uuids,
            source,
            device,
            advertisement_data,
            connectable,
            monotonic_time,
        )
