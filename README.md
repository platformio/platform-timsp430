# TI MSP430: development platform for [PlatformIO](https://platformio.org)

[![Build Status](https://github.com/platformio/platform-timsp430/workflows/Examples/badge.svg)](https://github.com/platformio/platform-timsp430/actions)

NOTE: the default toolchain for MSP430 platformIO is still on GCC version 4.6.3, which means C++0x. This github fork uses the radically more modern GCC compiler: https://github.com/maxgerhardt/pio-toolchaintimsp430-new.git      
(i'm not sure, but i believe all/most-of-what maxgethardt did was just add a package.json file to the opensource GCC toolchain from TI: https://www.ti.com/tool/MSP430-GCC-OPENSOURCE ).       
I have almost no idea what i'm doing when it comes to compilers, so when i got a few linker errors, i just googled and found '-fno-rtti' as an extra argument to fix things. It does at least compile for me now, actual hardware testing still TBD.

MSP430 microcontrollers (MCUs) from Texas Instruments (TI) are 16-bit, RISC-based, mixed-signal processors designed for ultra-low power. These MCUs offer the lowest power consumption and the perfect mix of integrated peripherals for thousands of applications.

* [Home](https://registry.platformio.org/platforms/platformio/timsp430) (home page in the PlatformIO Registry)
* [Documentation](https://docs.platformio.org/page/platforms/timsp430.html) (advanced usage, packages, boards, frameworks, etc.)

# Usage

1. [Install PlatformIO](https://platformio.org)
2. Create PlatformIO project and configure a platform option in [platformio.ini](https://docs.platformio.org/page/projectconf.html) file:

## Stable version

```ini
[env:stable]
platform = timsp430
board = ...
platform_packages = toolchain-timsp430@https://github.com/maxgerhardt/pio-toolchaintimsp430-new.git  ; uses a newer GCC version from TI (old toolchain was C++0x)
build_flags = '-fno-rtti' ; not sure what it does or why it helps, but it does. google: https://en.wikipedia.org/wiki/Run-time_type_information
...
```

## Development version

```ini
[env:development]
platform = https://github.com/platformio/platform-timsp430.git
board = ...
platform_packages = toolchain-timsp430@https://github.com/maxgerhardt/pio-toolchaintimsp430-new.git  ; uses a newer GCC version from TI (old toolchain was C++0x)
build_flags = '-fno-rtti' ; not sure what it does or why it helps, but it does. google: https://en.wikipedia.org/wiki/Run-time_type_information
...
```

# Configuration

Please navigate to [documentation](https://docs.platformio.org/page/platforms/timsp430.html).

