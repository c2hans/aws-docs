---
source_url: https://docs.aws.amazon.com/freertos/latest/userguide/dg-ota-initial-firmware.html
---

# Installing the initial firmware
<a name="dg-ota-initial-firmware"></a>

To update firmware, you must install an initial version of the firmware that uses the OTA Agent library to listen for OTA update jobs. If you are not running FreeRTOS, skip this step. You must copy your OTA Agent implementation onto your devices instead.

**Topics**
+ [Install the initial version of firmware on the Texas Instruments CC3220SF-LAUNCHXL](burn-initial-firmware-ti.md)
+ [Install the initial version of firmware on the Espressif ESP32](burn-initial-firmware-esp.md)
+ [Install the initial version of firmware on the Nordic nRF52840 DK](burn-initial-firmware-nordic.md)
+ [Initial firmware on the Windows simulator](burn-initial-firmware-windows.md)
+ [Install the initial version of firmware on a custom board](burn-initial-firmware-other.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for FreeRTOS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query freertos` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
