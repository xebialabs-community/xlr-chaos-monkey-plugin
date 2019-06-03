# Chaos Monkey for XL Release

[![Build Status][xlr-chaos-monkey-plugin-travis-image]][xlr-chaos-monkey-plugin-travis-url]
![GitHub release](https://img.shields.io/github/release/xebialabs-community/xlr-chaos-monkey-plugin.svg)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/69e1ca3ab3a14a30bb60499becbb61dc)](https://www.codacy.com/app/ndebuhr/xlr-chaos-monkey-plugin?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=xebialabs-community/xlr-chaos-monkey-plugin&amp;utm_campaign=Badge_Grade)
[![License: MIT][xlr-chaos-monkey-plugin-license-image]][xlr-chaos-monkey-plugin-license-url]
[![Github All Releases][xlr-chaos-monkey-plugin-downloads-image]][xlr-chaos-monkey-plugin-releases-url]
[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-blue.svg)](https://github.com/RichardLitt/standard-readme)

> Randomly fail XLR tasks to encourage continuous improvement and resilient systems [https://principlesofchaos.org/](https://principlesofchaos.org/)

## Installation

### Requirements

1. XL Release 8.0+

### Building the plugin
The gradle wrapper facilitates building the plugin.  Use the following command to build using [Gradle](https://gradle.org/):
```bash
./gradlew clean build
```
The built plugin, along with other files from the build, can then be found in the _build_ folder.

### Adding the plugin to XL Release

Download the latest version of the plugin from the [releases page][xlr-chaos-monkey-plugin-releases-url].  The plugin can then be installed through the graphical interface or the server backend.  For additional detail, please refer to [the docs.xebialabs.com documentation on XLR plugin installation](https://docs.xebialabs.com/xl-release/how-to/install-or-remove-xl-release-plugins.html)

### Configuration

Configurations are at the task level.  No global/folder configurations are required.

## Usage

Tasks included in this plugin:
1. Unstable Task
1. Fail Task In Phase
1. Fail Task In Release

### Unstable Task
This task will fail a user-defined percentage of the time.

### Fail Task In Phase
Within the same phase as the Chaos Monkey task, set a random pending or planned task to fail.  If there are no pending or planned tasks remaining in the phase, then the Chaos Monkey task itself will fail.

### Fail Task In Release
Set a random pending or planned task in the release to fail.  If there are no pending or planned tasks remaining in the release, then the Chaos Monkey task itself will fail.

## Contributing

Please review the contributing guidelines for _xebialabs-community_ at [http://xebialabs-community.github.io/](http://xebialabs-community.github.io/)

## License

This community plugin is licensed under the [MIT license][xlr-chaos-monkey-plugin-license-url]

See license in [LICENSE.md](LICENSE.md)

[xlr-chaos-monkey-plugin-travis-image]: https://travis-ci.org/xebialabs-community/xlr-chaos-monkey-plugin.svg?branch=master
[xlr-chaos-monkey-plugin-travis-url]: https://travis-ci.org/xebialabs-community/xlr-chaos-monkey-plugin
[xlr-chaos-monkey-plugin-license-image]: https://img.shields.io/badge/license-MIT-yellow.svg
[xlr-chaos-monkey-plugin-license-url]: https://opensource.org/licenses/MIT
[xlr-chaos-monkey-plugin-downloads-image]: https://img.shields.io/github/downloads/xebialabs-community/xlr-chaos-monkey-plugin/total.svg
[xlr-chaos-monkey-plugin-releases-url]: https://github.com/xebialabs-community/xlr-chaos-monkey-plugin/releases