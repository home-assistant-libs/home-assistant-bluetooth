
import cython


cdef object BLEDevice
cdef object AdvertisementData

cdef object _float
cdef object _BluetoothServiceInfoBleakSelfT
cdef object _BluetoothServiceInfoSelfT

cdef class BaseServiceInfo:
    """Base class for discovery ServiceInfo."""


cdef class BluetoothServiceInfo(BaseServiceInfo):
    """Prepared info from bluetooth entries."""

    cdef public str name
    cdef public str address
    cdef public object rssi
    cdef public cython.dict manufacturer_data
    cdef public cython.dict service_data
    cdef public cython.list service_uuids
    cdef public str source


cdef class BluetoothServiceInfoBleak(BluetoothServiceInfo):
    """BluetoothServiceInfo with bleak data."""

    cdef public object device
    cdef public object advertisement
    cdef public object connectable
    cdef public object time
