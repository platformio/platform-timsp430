# TI MSP430: development platform for [PlatformIO](http://platformio.org)
[![Build Status](https://travis-ci.org/platformio/platform-timsp430.svg?branch=develop)](https://travis-ci.org/platformio/platform-timsp430)
[![Build status](https://ci.appveyor.com/api/projects/status/rak8taqp0jqrmi53/branch/develop?svg=true)](https://ci.appveyor.com/project/ivankravets/platform-timsp430/branch/develop)

MSP430 microcontrollers (MCUs) from Texas Instruments (TI) are 16-bit, RISC-based, mixed-signal processors designed for ultra-low power. These MCUs offer the lowest power consumption and the perfect mix of integrated peripherals for thousands of applications.

* [Home](http://platformio.org/platforms/timsp430) (home page in PlatformIO Platform Registry)
* [Documentation](http://docs.platformio.org/page/platforms/timsp430.html) (advanced usage, packages, boards, frameworks, etc.)

# Usage

1. [Install PlatformIO](http://platformio.org)
2. Create PlatformIO project and configure a platform option in [platformio.ini](http://docs.platformio.org/page/projectconf.html) file:

## Stable version

```ini
[env:stable]
platform = timsp430
board = ...
...
```

## Development version

```ini
[env:development]
platform = https://github.com/platformio/platform-timsp430.git
board = ...
...
```

# Configuration

Please navigate to [documentation](http://docs.platformio.org/page/platforms/timsp430.html).

