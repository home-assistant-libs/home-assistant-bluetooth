# CHANGELOG



## v1.12.2 (2024-06-24)

### Fix

* fix: fix license classifier (#40) ([`02b5bef`](https://github.com/home-assistant-libs/home-assistant-bluetooth/commit/02b5bef13e40db62f8fb045fc28c48977eba88a8))


## v1.12.1 (2024-06-07)

### Fix

* fix: make tests compatible with habluetooth&gt;=3 (#39)

Co-authored-by: J. Nick Koston &lt;nick@koston.org&gt; ([`e73c77d`](https://github.com/home-assistant-libs/home-assistant-bluetooth/commit/e73c77d40d6bf90f19b7aa4cf6e7cba6ba608e86))


## v1.12.0 (2024-01-11)

### Feature

* feat: finish transition to github trusted actions for releases (#35) ([`fdcc42f`](https://github.com/home-assistant-libs/home-assistant-bluetooth/commit/fdcc42f89f02408f1544766d6e8e67bdcd0359d4))

### Fix

* fix: release workflow with python3.11 (#37) ([`4517907`](https://github.com/home-assistant-libs/home-assistant-bluetooth/commit/4517907a49a3ad9686f1381e2ee9c6a3a53f2d4c))

* fix: python version in release upload workflow (#36) ([`4bd2e90`](https://github.com/home-assistant-libs/home-assistant-bluetooth/commit/4bd2e90fa8d7060169365fd5480638e0daa9964b))

* fix: bump python-semantic-release to fix release process (#33) ([`02cb578`](https://github.com/home-assistant-libs/home-assistant-bluetooth/commit/02cb57895cf44f47fb8835916661d6f59010550c))

* fix: switch to github trusted publishing to fix release (#32) ([`d90ff3d`](https://github.com/home-assistant-libs/home-assistant-bluetooth/commit/d90ff3d7ca7734d2dcf3d381de3497f92fde13bf))


## v1.11.1 (2024-01-09)

### Fix

* fix: bump minimum python to 3.11 to fix resolver (#31) ([`ffacca4`](https://github.com/home-assistant-libs/home-assistant-bluetooth/commit/ffacca41bc3f7545816dacc8e6da01659609cb24))


## v1.11.0 (2023-12-11)

### Feature

* feat: make home_assistant_bluetooth a wrapper around habluetooth (#29) ([`e161eaa`](https://github.com/home-assistant-libs/home-assistant-bluetooth/commit/e161eaad96a036a14b588db0a5df70b6ecf624a7))


## v1.10.4 (2023-10-18)

### Fix

* fix: reduce size of wheels by excluding generated .c files (#27) ([`2792c58`](https://github.com/home-assistant-libs/home-assistant-bluetooth/commit/2792c5858a4db350e37c71cead5be972b6dfbac2))


## v1.10.3 (2023-08-27)

### Fix

* fix: rebuild wheels with cython 3.0.2 (#26) ([`2d0b3ff`](https://github.com/home-assistant-libs/home-assistant-bluetooth/commit/2d0b3ff3e1609b1691b078806f2585d08e96ffa3))


## v1.10.2 (2023-07-25)

### Fix

* fix: relax type requirements for cython3 (#25) ([`aee3b26`](https://github.com/home-assistant-libs/home-assistant-bluetooth/commit/aee3b26eff4648cba67a8801acb2d1627c7942dd))


## v1.10.1 (2023-07-24)

### Fix

* fix: update python-semantic-release to fix release process (#24) ([`8c60e43`](https://github.com/home-assistant-libs/home-assistant-bluetooth/commit/8c60e4364e351e10844ad7f49a8f7acade1b9cd1))


## v1.10.0 (2023-04-24)

### Feature

* feat: optimize from_device_and_advertisement_data (#21) ([`72bd815`](https://github.com/home-assistant-libs/home-assistant-bluetooth/commit/72bd815ae2694b8f88d62ff2039ef221daf243c9))


## v1.9.3 (2023-02-14)

### Fix

* fix: missing c extensions with newer poetry (#18)

fix for breaking change in poetry https://github.com/python-poetry/poetry-core/pull/318 ([`866236a`](https://github.com/home-assistant-libs/home-assistant-bluetooth/commit/866236aeb52c2b6b3da67ac9b06df7904a464351))


## v1.9.2 (2023-01-04)

### Fix

* fix: make MANUFACTURERS import late (#17) ([`c783cd8`](https://github.com/home-assistant-libs/home-assistant-bluetooth/commit/c783cd82623b4317601ab7c5486950a31e1bf9aa))


## v1.9.1 (2023-01-02)

### Fix

* fix: make bleak a dev requirement (#16) ([`0506ca4`](https://github.com/home-assistant-libs/home-assistant-bluetooth/commit/0506ca4e341e9ed4607c8be9fab167dd2dc429b6))


## v1.9.0 (2022-12-10)

### Feature

* feat: add from_device_and_advertisement_data classmethod to BluetoothServiceInfoBleak (#15)

* feat: add from_device_and_advertisement_data classmethod to BluetoothServiceInfoBleak

* feat: add from_device_and_advertisement_data classmethod to BluetoothServiceInfoBleak

* fix: drop macOS from the CI since there is nothing macOS specific here and pyobjc is currently broken ([`c231594`](https://github.com/home-assistant-libs/home-assistant-bluetooth/commit/c2315946d75350c2848c00dec144b9ab198e629e))


## v1.8.1 (2022-11-16)

### Fix

* fix: name collision with build that prevented PEP517 builds (#14) ([`032552d`](https://github.com/home-assistant-libs/home-assistant-bluetooth/commit/032552d9d35306d406853d0473ba4b1c08963c95))


## v1.8.0 (2022-11-15)

### Feature

* feat: cythonize the models (#12) ([`e65e000`](https://github.com/home-assistant-libs/home-assistant-bluetooth/commit/e65e000084b55c404cffa8745fa87c774e294c6c))


## v1.7.0 (2022-11-14)

### Feature

* feat: move BluetoothServiceInfoBleak out of the bluetooth integration (#10) ([`fbc3d8e`](https://github.com/home-assistant-libs/home-assistant-bluetooth/commit/fbc3d8e240291ccc7c4ced7d9ae962d8407c4da0))


## v1.6.0 (2022-10-14)

### Feature

* feat: update for bleak 0.19 (#9) ([`e872338`](https://github.com/home-assistant-libs/home-assistant-bluetooth/commit/e87233872e8f059b86878de474fc733a8806c6fd))


## v1.5.1 (2022-10-04)

### Fix

* fix: revert freeze BluetoothServiceInfo dataclass (#8) ([`c4cb1ab`](https://github.com/home-assistant-libs/home-assistant-bluetooth/commit/c4cb1ab320196a8540fe06b3a34720e89d759cbd))


## v1.5.0 (2022-10-04)

### Feature

* feat: freeze BluetoothServiceInfo dataclass (#7) ([`fafdd2a`](https://github.com/home-assistant-libs/home-assistant-bluetooth/commit/fafdd2ac1a84506f7a3c51dba5426f1ded747e58))


## v1.4.0 (2022-07-20)

### Feature

* feat: add typevar to enable better subclassing (#6) ([`9a9b75d`](https://github.com/home-assistant-libs/home-assistant-bluetooth/commit/9a9b75d49e0849bcf87e48ba17d463358d296629))


## v1.3.0 (2022-07-16)

### Feature

* feat: add additional docs on the data format (#5) ([`40445c6`](https://github.com/home-assistant-libs/home-assistant-bluetooth/commit/40445c6c0f2f2dc2592c6263782db044e4e87b72))


## v1.2.0 (2022-07-16)

### Feature

* feat: add a basic readme (#3) ([`486895b`](https://github.com/home-assistant-libs/home-assistant-bluetooth/commit/486895bf83450f26877f6f92262a82810043a941))


## v1.1.2 (2022-07-16)

### Unknown

* 1.1.2 (#2)

Co-authored-by: semantic-release &lt;semantic-release&gt; ([`4247f9a`](https://github.com/home-assistant-libs/home-assistant-bluetooth/commit/4247f9a263668a9afabc65dfe8f151b1291c9d3a))


## v1.1.1 (2022-07-16)


## v1.1.0 (2022-07-15)

### Feature

* feat: add the models (#1) ([`b5a92db`](https://github.com/home-assistant-libs/home-assistant-bluetooth/commit/b5a92dbcc9facb9d162608f71e55eaca619aa163))
