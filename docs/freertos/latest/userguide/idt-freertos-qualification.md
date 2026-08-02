---
source_url: https://docs.aws.amazon.com/freertos/latest/userguide/idt-freertos-qualification.html
---

# IDT with FreeRTOS qualification suite 1.0 (FRQ 1.0)
<a name="idt-freertos-qualification"></a>

**Important**
As of October 2022, AWS IoT Device Tester for AWS IoT FreeRTOS Qualification (FRQ) 1.0 does not generate signed qualification reports. You cannot qualify new AWS IoT FreeRTOS devices to list in the [AWS Partner Device Catalog ](https://partners.amazonaws.com/qualified-devices)through the [AWS Device Qualification Program](http://aws.amazon.com/partners/programs/dqp/) using IDT FRQ 1.0 versions. While you can't qualify FreeRTOS devices using IDT FRQ 1.0, you can continue to test your FreeRTOS devices with FRQ 1.0. We recommend that you use [IDT FRQ 2.0](https://docs.aws.amazon.com/freertos/latest/userguide/lts-idt-freertos-qualification.html) to qualify and list FreeRTOS devices in the [AWS Partner Device Catalog](https://partners.amazonaws.com/qualified-devices).

 You can use IDT for FreeRTOS qualification to verify that the FreeRTOS operating system works locally on your device and can communicate with AWS IoT. Specifically, it verifies that the porting layer interfaces for the FreeRTOS libraries are implemented correctly. It also performs end-to-end tests with AWS IoT Core. For example, it verifies your board can send and receive MQTT messages and process them correctly. The tests run by IDT for FreeRTOS are defined in the [FreeRTOS GitHub repository](https://github.com/aws/amazon-freertos).

The tests run as embedded applications that are flashed onto your board. The application binary images include FreeRTOS, the semiconductor vendor’s ported FreeRTOS interfaces, and board device drivers. The purpose of the tests is to verify the ported FreeRTOS interfaces function correctly on top of the device drivers.

IDT for FreeRTOS generates test reports that you can submit to AWS IoT to add your hardware to the AWS Partner Device Catalog. For more information, see [AWS Device Qualification Program](https://aws.amazon.com/partners/dqp/).

IDT for FreeRTOS runs on a host computer (Windows, macOS, or Linux) that is connected to the board to be tested. IDT executes test cases and aggregates results. It also provides a command line interface to manage test execution.

In addition to testing devices, IDT for FreeRTOS creates resources (for example, AWS IoT things, FreeRTOS groups, Lambda functions, and so on) to facilitate the qualification process. To create these resources, IDT for FreeRTOS uses the AWS credentials configured in the `config.json` to make API calls on your behalf. These resources are provisioned at various times during a test.

When you run IDT for FreeRTOS on your host computer, it performs the following steps:

1. Loads and validates your device and credentials configuration.

1. Performs selected tests with the required local and cloud resources.

1. Cleans up local and cloud resources.

1. Generates tests reports that indicate if your board passed the tests required for qualification.

**Topics**
+ [Setup the 1.0 qualification prerequisites](dev-tester-prereqs.md)
+ [First test of your microcontroller board](qual-steps.md)
+ [Use the IDT user interface to run the FreeRTOS qualification suite](device-tester-ui.md)
+ [Run Bluetooth Low Energy tests](afr-bridgekeeper-dt-bt.md)
+ [Run the FreeRTOS qualification suite](run-tests.md)
+ [View the IDT for FreeRTOS results](view-results-frq.md)
+ [Interpret the IDT for FreeRTOS results](interpreting-results-frq.md)
+ [View the IDT for FreeRTOS logs](view-logs-frq.md)
