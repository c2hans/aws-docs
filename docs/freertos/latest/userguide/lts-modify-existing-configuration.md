---
source_url: https://docs.aws.amazon.com/freertos/latest/userguide/lts-modify-existing-configuration.html
---

# Modify an existing configuration
<a name="lts-modify-existing-configuration"></a>

If you have already set up configuration files for IDT for FreeRTOS, you can use the IDT for FreeRTOS UI to modify your existing configuration. The existing configuration files must be located in the `{{devicetester-extract-location}}/config` directory.

**To modify a configuration**

1. In the IDT for FreeRTOS UI, open the navigation menu, and choose **Edit existing configuration**.

   The configuration dashboard displays information about your existing configuration settings. If a configuration is incorrect or unavailable, the status for that configuration is `Error validating configuration`.
![Configuration screen with device, AWS account, FreeRTOS implementation, PKCS labels and echo server, over-the-air updates, and test run settings sections showing valid status.](https://docs.aws.amazon.com/freertos/latest/userguide/images/modify-existing-configuration.png)

1. To modify an existing configuration setting, complete the following steps:

   1. Choose the name of a configuration setting to open its settings page.

   1. Modify the settings, and then choose **Save** to regenerate the corresponding configuration file.

1. To modify the IDT for FreeRTOS test run settings, choose **IDT test run settings** in the edit view:
![IDT test run settings dialog with options for test selection, skipping test groups, timeout multiplier, and stopping on first failure.](https://docs.aws.amazon.com/freertos/latest/userguide/images/idt-testrun-settings.png)

After you finish modifying your configuration, verify that all of your configuration settings pass validation. If the status for each configuration setting is `Valid`, you can run your qualification tests with this configuration.
