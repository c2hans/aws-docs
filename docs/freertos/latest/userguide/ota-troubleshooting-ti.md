---
source_url: https://docs.aws.amazon.com/freertos/latest/userguide/ota-troubleshooting-ti.html
---

# Troubleshoot OTA updates with the Texas Instruments CC3220SF Launchpad
<a name="ota-troubleshooting-ti"></a>

The CC3220SF Launchpad platform provides a software tamper-detection mechanism. It uses a security alert counter that is incremented whenever there is an integrity violation. The device is locked when the security alert counter reaches a predetermined threshold (the default is 15) and the host receives the `SL_ERROR_DEVICE_LOCKED_SECURITY_ALERT` asynchronous event. The locked device then has limited accessibility. To recover the device, you can reprogram it or use the restore-to-factory process to revert to the factory image. You should program the desired behavior by updating the asynchronous event handler in `network_if.c`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for FreeRTOS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query freertos` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
