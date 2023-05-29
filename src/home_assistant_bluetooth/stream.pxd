import cython

from .models cimport BluetoothServiceInfoBleak


cdef object NO_RSSI_VALUE

cdef object _int
cdef object _float
cdef object _str

cdef object AdvertisementData
cdef object BLEDevice

cdef class BluetoothAdvertisementStream:
    """Stream of BluetoothAdvertisement."""

    cdef object _connectable
    cdef str _source
    cdef cython.dict _details
    cdef cython.dict _previous

    @cython.locals(
        prev_discovery=BluetoothServiceInfoBleak,
        prev_service_uuids=cython.list,
        prev_service_data=cython.dict,
        prev_manufacturer_data=cython.dict,
        prev_name=str
    )
    cpdef BluetoothServiceInfoBleak process(
        self,
        object monotonic_time,
        str address,
        object rssi,
        str local_name,
        cython.list service_uuids,
        cython.dict service_data,
        cython.dict manufacturer_data,
        object tx_power,
        cython.dict details,
    )
