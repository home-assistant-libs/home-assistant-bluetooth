"""The bluetooth integration service info."""

from typing import TYPE_CHECKING, Any, Dict, Final, List, Optional, Type, TypeVar

if TYPE_CHECKING:
    from bleak.backends.device import BLEDevice
    from bleak.backends.scanner import AdvertisementData

_BluetoothServiceInfoSelfT = TypeVar(
    "_BluetoothServiceInfoSelfT", bound="BluetoothServiceInfo"
)

_BluetoothServiceInfoBleakSelfT = TypeVar(
    "_BluetoothServiceInfoBleakSelfT", bound="BluetoothServiceInfoBleak"
)
SOURCE_LOCAL: Final = "local"


class BaseServiceInfo:
    """Base class for discovery ServiceInfo."""


class BluetoothServiceInfo(BaseServiceInfo):
    """Prepared info from bluetooth entries."""

    __slots__ = (
        "name",
        "address",
        "rssi",
        "manufacturer_data",
        "service_data",
        "service_uuids",
        "source",
    )

    def __init__(
        self,
        name: Any,  # may be a pyobjc object
        address: Any,  # may be a pyobjc object
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
        cls: Type[_BluetoothServiceInfoSelfT],
        device: "BLEDevice",
        advertisement_data: "AdvertisementData",
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

    @property
    def manufacturer(self) -> Optional[str]:
        """Convert manufacturer data to a string."""
        from bleak.backends._manufacturers import (
            MANUFACTURERS,  # pylint: disable=import-outside-toplevel
        )

        for manufacturer in self.manufacturer_data:
            if manufacturer in MANUFACTURERS:
                name: str = MANUFACTURERS[manufacturer]
                return name
        return None

    @property
    def manufacturer_id(self) -> Optional[int]:
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

    __slots__ = ("device", "advertisement", "connectable", "time")

    def __init__(
        self,
        name: Any,  # may be a pyobjc object
        address: Any,  # may be a pyobjc object
        rssi: int,
        manufacturer_data: Dict[int, bytes],
        service_data: Dict[str, bytes],
        service_uuids: List[str],
        source: str,
        device: "BLEDevice",
        advertisement: "AdvertisementData",
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
        cls: Type[_BluetoothServiceInfoBleakSelfT],
        source: str,
        device: "BLEDevice",
        advertisement_data: "AdvertisementData",
        monotonic_time: float,
        connectable: bool,
    ) -> _BluetoothServiceInfoBleakSelfT:
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

    @classmethod
    def from_device_and_advertisement_data(
        cls: Type[_BluetoothServiceInfoBleakSelfT],
        device: "BLEDevice",
        advertisement_data: "AdvertisementData",
        source: str,
        time: float,
        connectable: bool,
    ) -> _BluetoothServiceInfoBleakSelfT:
        """Create a BluetoothServiceInfoBleak from a device and advertisement."""
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
            time,
        )
