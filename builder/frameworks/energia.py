# Copyright 2014-present PlatformIO <contact@platformio.org>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Energia

Energia Wiring-based framework enables pretty much anyone to start easily
creating microcontroller-based projects and applications. Its easy-to-use
libraries and functions provide developers of all experience levels to start
blinking LEDs, buzzing buzzers and sensing sensors more quickly than ever
before.

http://energia.nu/reference/
"""

from os.path import isdir, join

from SCons.Script import DefaultEnvironment

env = DefaultEnvironment()
platform = env.PioPlatform()

FRAMEWORK_DIR = platform.get_package_dir("framework-energiamsp430")
FRAMEWORK_VERSION = platform.get_package_version("framework-energiamsp430")
assert isdir(FRAMEWORK_DIR)

board = env.BoardConfig()

variants_dir = join(
    "$PROJECT_DIR", board.get("build.variants_dir")) if board.get(
        "build.variants_dir", "") else join(FRAMEWORK_DIR, "variants")

env.Append(
    CPPDEFINES=[
        ("ARDUINO", 10807),
        ("ENERGIA", int(FRAMEWORK_VERSION.split(".")[1]))
    ],

    CPPPATH=[
        join(FRAMEWORK_DIR, "cores", env.BoardConfig().get("build.core")),
        join(variants_dir, board.get("build.variant")),
        join(platform.get_package_dir(
            "toolchain-timsp430"), "msp430-elf", "include")
    ],

    LIBSOURCE_DIRS=[
        join(FRAMEWORK_DIR, "libraries")
    ]
)

#
# Target: Build Core Library
#

libs = []

libs.append(env.BuildLibrary(
    join("$BUILD_DIR", "FrameworkEnergia"),
    join(FRAMEWORK_DIR, "cores", board.get("build.core"))
))

env.Append(LIBS=libs)
