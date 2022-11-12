"""The bluetooth integration service info."""
from __future__ import annotations

import dataclasses
from functools import cached_property
from typing import Any, Final, TypeVar

from bleak.backends.device import BLEDevice
from bleak.backends.scanner import AdvertisementData

_BluetoothServiceInfoSelfT = TypeVar(
    "_BluetoothServiceInfoSelfT", bound="BluetoothServiceInfo"
)

_BluetoothServiceInfoBleakSelfT = TypeVar(
    "_BluetoothServiceInfoBleakSelfT", bound="BluetoothServiceInfoBleak"
)
SOURCE_LOCAL: Final = "local"


@dataclasses.dataclass
class BaseServiceInfo:
    """Base class for discovery ServiceInfo."""


@dataclasses.dataclass
class BluetoothServiceInfo(BaseServiceInfo):
    """Prepared info from bluetooth entries."""

    name: str
    address: str
    rssi: int
    manufacturer_data: dict[int, bytes]
    service_data: dict[str, bytes]
    service_uuids: list[str]
    source: str

    @classmethod
    def from_advertisement(
        cls: type[_BluetoothServiceInfoSelfT],
        device: BLEDevice,
        advertisement_data: AdvertisementData,
        source: str,
    ) -> _BluetoothServiceInfoSelfT:
        """Create a BluetoothServiceInfo from an advertisement."""
        return cls(
            name=advertisement_data.local_name or device.name or device.address,
            address=device.address,
            rssi=advertisement_data.rssi,
            manufacturer_data=advertisement_data.manufacturer_data,
            service_data=advertisement_data.service_data,
            service_uuids=advertisement_data.service_uuids,
            source=source,
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


@dataclasses.dataclass
class BluetoothServiceInfoBleak(BluetoothServiceInfo):
    """BluetoothServiceInfo with bleak data.

    Integrations may need BLEDevice and AdvertisementData
    to connect to the device without having bleak trigger
    another scan to translate the address to the system's
    internal details.
    """

    device: BLEDevice
    advertisement: AdvertisementData
    connectable: bool
    time: float

    def as_dict(self) -> dict[str, Any]:
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
        cls: type[_BluetoothServiceInfoBleakSelfT],
        source: str,
        device: BLEDevice,
        advertisement_data: AdvertisementData,
        monotonic_time: float,
        connectable: bool,
    ) -> _BluetoothServiceInfoBleakSelfT:
        """Create a BluetoothServiceInfoBleak from a scanner."""
        return cls(
            name=advertisement_data.local_name or device.name or device.address,
            address=device.address,
            rssi=advertisement_data.rssi,
            manufacturer_data=advertisement_data.manufacturer_data,
            service_data=advertisement_data.service_data,
            service_uuids=advertisement_data.service_uuids,
            source=source,
            device=device,
            advertisement=advertisement_data,
            connectable=connectable,
            time=monotonic_time,
        )
