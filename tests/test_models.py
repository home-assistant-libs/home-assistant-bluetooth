from __future__ import annotations

import time

from bleak.backends.device import BLEDevice

from home_assistant_bluetooth import (
    SOURCE_LOCAL,
    BluetoothServiceInfo,
    BluetoothServiceInfoBleak,
)

from . import generate_advertisement_data


def test_model():
    service_info = BluetoothServiceInfo(
        name="Test",
        address="00:00:00:00:00:00",
        rssi=0,
        manufacturer_data={97: b"\x00\x00\x00\x00\x00\x00"},
        service_data={},
        service_uuids=[],
        source=SOURCE_LOCAL,
    )

    assert service_info.manufacturer == "RDA Microelectronics"
    assert service_info.manufacturer_id == 97

    service_info = BluetoothServiceInfo(
        name="Test",
        address="00:00:00:00:00:00",
        rssi=0,
        manufacturer_data={954547: b"\x00\x00\x00\x00\x00\x00"},
        service_data={},
        service_uuids=[],
        source=SOURCE_LOCAL,
    )

    assert service_info.manufacturer is None
    assert service_info.manufacturer_id == 954547


def test_model_from_bleak():
    switchbot_device = BLEDevice("44:44:33:11:23:45", "wohand")
    switchbot_adv = generate_advertisement_data(
        local_name="wohand", service_uuids=["cba20d00-224d-11e6-9fb8-0002a5d5c51b"]
    )
    service_info = BluetoothServiceInfo.from_advertisement(
        switchbot_device, switchbot_adv, SOURCE_LOCAL
    )

    assert service_info.service_uuids == ["cba20d00-224d-11e6-9fb8-0002a5d5c51b"]
    assert service_info.name == "wohand"
    assert service_info.source == SOURCE_LOCAL
    assert service_info.manufacturer is None
    assert service_info.manufacturer_id is None


def test_model_from_scanner():
    switchbot_device = BLEDevice("44:44:33:11:23:45", "wohand")
    switchbot_adv = generate_advertisement_data(
        local_name="wohand", service_uuids=["cba20d00-224d-11e6-9fb8-0002a5d5c51b"]
    )
    now = time.monotonic()
    service_info = BluetoothServiceInfoBleak.from_scan(
        SOURCE_LOCAL, switchbot_device, switchbot_adv, now, True
    )

    assert service_info.service_uuids == ["cba20d00-224d-11e6-9fb8-0002a5d5c51b"]
    assert service_info.name == "wohand"
    assert service_info.source == SOURCE_LOCAL
    assert service_info.manufacturer is None
    assert service_info.manufacturer_id is None
    assert service_info.time == now
    assert service_info.connectable is True

    safe_as_dict = service_info.as_dict()
    assert safe_as_dict == {
        "address": "44:44:33:11:23:45",
        "advertisement": switchbot_adv,
        "device": switchbot_device,
        "connectable": True,
        "manufacturer_data": {},
        "name": "wohand",
        "rssi": -127,
        "service_data": {},
        "service_uuids": ["cba20d00-224d-11e6-9fb8-0002a5d5c51b"],
        "source": "local",
        "time": now,
    }
