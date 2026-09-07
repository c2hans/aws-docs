---
source_url: https://docs.aws.amazon.com/freertos/latest/userguide/lts-create-new-configuration.html
---

# Create a new configuration
<a name="lts-create-new-configuration"></a>

If you're a first-time user, you must create a new configuration to set up the JSON configuration files that IDT for FreeRTOS requires to run tests. You can then run tests or modify the created configuration.

For examples of the `config.json`, `device.json`, and `userdata.json` files, see [First test of your microcontroller board](lts-qual-steps.md).

**To create a new configuration**

1. In the IDT for FreeRTOS UI, open the navigation menu, and choose **Create new configuration**.
![Device Tester for FreeRTOS interface with "Create new configuration" button and information about automated self-testing of microcontrollers.](https://docs.aws.amazon.com/freertos/latest/userguide/images/gsg-create-configuration.png)

1. Follow the configuration wizard to enter the IDT configuration settings used to run qualification tests. The wizard configures the following settings in JSON configuration files located in the `{{devicetester-extract-location}}/config` directory.
   + **Device settings** – The device pool settings for the devices to be tested. These settings are configured in the `id` and `sku` fields, and the **devices** block for the device pool in the `config.json` file.
![Device Tester for FreeRTOS configuration screen with Identifier and SKU fields for configuring a device pool, device settings options like connectivity method, key provisioning, PKCS #11 settings, device details input fields, and controls to add devices or identifiers.](https://docs.aws.amazon.com/freertos/latest/userguide/images/gsg-device-settings.png)
   + **AWS account settings** – The AWS account information that IDT for FreeRTOS uses to create AWS resources during test runs. These settings are configured in the `config.json` file.
![AWS account settings page with fields for account region, credentials location as file or environment, and profile name](https://docs.aws.amazon.com/freertos/latest/userguide/images/gsg-account-settings.png)
   + **FreeRTOS implementation** – The absolute path to the FreeRTOS repository and ported code, and the FreeRTOS version you want to run IDT FRQ on. The paths to the execution and parameter config header files from the `FreeRTOS-Libraries-Integration-Tests` GitHub repository. The build and flash commands for your hardware that allow IDT to build and flash tests onto your board automatically. These settings are configured in the `userdata.json` file.
![FreeRTOS implementation configuration section with repository paths, test execution paths, FreeRTOS version, build tool details, and flash tool settings.](https://docs.aws.amazon.com/freertos/latest/userguide/images/gsg-implementation-settings.png)
   + **PKCS \#11 labels and Echo server** – The [PKCS \#11](https://docs.aws.amazon.com/freertos/latest/portingguide/afr-porting-pkcs.html) labels that correspond to the keys provisioned in your hardware based on the key functionality and key provisioning method. The echo server configuration settings for the Transport Interface tests. These settings are configured in the `userdata.json` and `device.json` files.
![PKCS #11 labels and Echo server configurations with input fields for key labels, key generation method, and server port number](https://docs.aws.amazon.com/freertos/latest/userguide/images/gsg-pkcs11-settings.png)
   + **Over-the-air (OTA) updates** – The settings that control OTA functionality tests. These settings are configured in the `features` block of the `device.json` and `userdata.json` files.
![OTA update config options: skip tests, data protocols, firmware paths, PAL cert path, code signing, hash/sign algorithms, trusted/untrusted signer certs, signer cert file, compile signer cert, signer platform.](https://docs.aws.amazon.com/freertos/latest/userguide/images/gsg-ota-settings.png)

1. On the **Review** page, verify your configuration information.
![Configuration created dialog for Device Tester for FreeRTOS, showing details about creating a new test configuration with options to edit or run tests.](https://docs.aws.amazon.com/freertos/latest/userguide/images/gsg-configuration-created.png)

After you finish reviewing your configuration, to run your qualification tests, choose **Run tests**.
