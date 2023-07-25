# Changelog

<!--next-version-placeholder-->

## v1.10.2 (2023-07-25)

### Fix

* Relax type requirements for cython3 ([#25](https://github.com/home-assistant-libs/home-assistant-bluetooth/issues/25)) ([`aee3b26`](https://github.com/home-assistant-libs/home-assistant-bluetooth/commit/aee3b26eff4648cba67a8801acb2d1627c7942dd))

## v1.10.1 (2023-07-24)

### Fix

* Update python-semantic-release to fix release process ([#24](https://github.com/home-assistant-libs/home-assistant-bluetooth/issues/24)) ([`8c60e43`](https://github.com/home-assistant-libs/home-assistant-bluetooth/commit/8c60e4364e351e10844ad7f49a8f7acade1b9cd1))

## v1.10.0 (2023-04-24)
### Feature
* Optimize from_device_and_advertisement_data ([#21](https://github.com/home-assistant-libs/home-assistant-bluetooth/issues/21)) ([`72bd815`](https://github.com/home-assistant-libs/home-assistant-bluetooth/commit/72bd815ae2694b8f88d62ff2039ef221daf243c9))

## v1.9.3 (2023-02-14)
### Fix
* Missing c extensions with newer poetry ([#18](https://github.com/home-assistant-libs/home-assistant-bluetooth/issues/18)) ([`866236a`](https://github.com/home-assistant-libs/home-assistant-bluetooth/commit/866236aeb52c2b6b3da67ac9b06df7904a464351))

## v1.9.2 (2023-01-04)
### Fix
* Make MANUFACTURERS import late ([#17](https://github.com/home-assistant-libs/home-assistant-bluetooth/issues/17)) ([`c783cd8`](https://github.com/home-assistant-libs/home-assistant-bluetooth/commit/c783cd82623b4317601ab7c5486950a31e1bf9aa))

## v1.9.1 (2023-01-02)
### Fix
* Make bleak a dev requirement ([#16](https://github.com/home-assistant-libs/home-assistant-bluetooth/issues/16)) ([`0506ca4`](https://github.com/home-assistant-libs/home-assistant-bluetooth/commit/0506ca4e341e9ed4607c8be9fab167dd2dc429b6))

## v1.9.0 (2022-12-10)
### Feature
* Add from_device_and_advertisement_data classmethod to BluetoothServiceInfoBleak ([#15](https://github.com/home-assistant-libs/home-assistant-bluetooth/issues/15)) ([`c231594`](https://github.com/home-assistant-libs/home-assistant-bluetooth/commit/c2315946d75350c2848c00dec144b9ab198e629e))

## v1.8.1 (2022-11-16)
### Fix
* Name collision with build that prevented PEP517 builds ([#14](https://github.com/home-assistant-libs/home-assistant-bluetooth/issues/14)) ([`032552d`](https://github.com/home-assistant-libs/home-assistant-bluetooth/commit/032552d9d35306d406853d0473ba4b1c08963c95))

## v1.8.0 (2022-11-15)
### Feature
* Cythonize the models ([#12](https://github.com/home-assistant-libs/home-assistant-bluetooth/issues/12)) ([`e65e000`](https://github.com/home-assistant-libs/home-assistant-bluetooth/commit/e65e000084b55c404cffa8745fa87c774e294c6c))

## v1.7.0 (2022-11-14)
### Feature
* Move BluetoothServiceInfoBleak out of the bluetooth integration ([#10](https://github.com/home-assistant-libs/home-assistant-bluetooth/issues/10)) ([`fbc3d8e`](https://github.com/home-assistant-libs/home-assistant-bluetooth/commit/fbc3d8e240291ccc7c4ced7d9ae962d8407c4da0))

## v1.6.0 (2022-10-14)
### Feature
* Update for bleak 0.19 ([#9](https://github.com/home-assistant-libs/home-assistant-bluetooth/issues/9)) ([`e872338`](https://github.com/home-assistant-libs/home-assistant-bluetooth/commit/e87233872e8f059b86878de474fc733a8806c6fd))

## v1.5.1 (2022-10-04)
### Fix
* Revert freeze BluetoothServiceInfo dataclass ([#8](https://github.com/home-assistant-libs/home-assistant-bluetooth/issues/8)) ([`c4cb1ab`](https://github.com/home-assistant-libs/home-assistant-bluetooth/commit/c4cb1ab320196a8540fe06b3a34720e89d759cbd))

## v1.5.0 (2022-10-04)
### Feature
* Freeze BluetoothServiceInfo dataclass ([#7](https://github.com/home-assistant-libs/home-assistant-bluetooth/issues/7)) ([`fafdd2a`](https://github.com/home-assistant-libs/home-assistant-bluetooth/commit/fafdd2ac1a84506f7a3c51dba5426f1ded747e58))

## v1.4.0 (2022-07-20)
### Feature
* Add typevar to enable better subclassing ([#6](https://github.com/home-assistant-libs/home-assistant-bluetooth/issues/6)) ([`9a9b75d`](https://github.com/home-assistant-libs/home-assistant-bluetooth/commit/9a9b75d49e0849bcf87e48ba17d463358d296629))

## v1.3.0 (2022-07-16)
### Feature
* Add additional docs on the data format ([#5](https://github.com/home-assistant-libs/home-assistant-bluetooth/issues/5)) ([`40445c6`](https://github.com/home-assistant-libs/home-assistant-bluetooth/commit/40445c6c0f2f2dc2592c6263782db044e4e87b72))

## v1.2.0 (2022-07-16)
### Feature
* Add a basic readme ([#3](https://github.com/home-assistant-libs/home-assistant-bluetooth/issues/3)) ([`486895b`](https://github.com/home-assistant-libs/home-assistant-bluetooth/commit/486895bf83450f26877f6f92262a82810043a941))

## v1.1.0 (2022-07-15)
### Feature
* Add the models ([#1](https://github.com/home-assistant-libs/home-assistant-bluetooth/issues/1)) ([`b5a92db`](https://github.com/home-assistant-libs/home-assistant-bluetooth/commit/b5a92dbcc9facb9d162608f71e55eaca619aa163))
