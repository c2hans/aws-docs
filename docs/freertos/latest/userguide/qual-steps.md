---
source_url: https://docs.aws.amazon.com/freertos/latest/userguide/qual-steps.html
---

# First test of your microcontroller board
<a name="qual-steps"></a>

You can use IDT for FreeRTOS to test as you port the FreeRTOS interfaces. After you have ported the FreeRTOS interfaces for your board’s device drivers, you use AWS IoT Device Tester to run the qualification tests on your microcontroller board.

## Add library porting layers
<a name="add-port-layer"></a>

 To port FreeRTOS for your device, follow the instructions in the [FreeRTOS Porting Guide](https://docs.aws.amazon.com/freertos/latest/portingguide/).

## Configure your AWS credentials
<a name="cfg-aws-afr"></a>

You need to configure your AWS credentials for AWS IoT Device Tester to communicate with the AWS Cloud. For more information, see [Set up AWS Credentials and Region for Development](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/setup-credentials.html). Valid AWS credentials must be specified in the `{{devicetester_extract_location}}/devicetester_afreertos_{{[win|mac|linux]}}/configs/config.json` configuration file.

**Topics**
+ [Add library porting layers](#add-port-layer)
+ [Configure your AWS credentials](#cfg-aws-afr)
+ [Create a device pool in IDT for FreeRTOS](cfg-dt-dp.md)
+ [Configure build, flash, and test settings](cfg-dt-ud.md)
