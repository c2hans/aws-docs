---
source_url: https://docs.aws.amazon.com/freertos/latest/userguide/idt-programmatic-download.html
---

# Download IDT for FreeRTOS
<a name="idt-programmatic-download"></a>

This topic describes the options to download IDT for FreeRTOS. You can either use one of the following software download links or you can follow instructions to programmatically download IDT.

**Important**
As of October 2022, AWS IoT Device Tester for AWS IoT FreeRTOS Qualification (FRQ) 1.0 does not generate signed qualification reports. You cannot qualify new AWS IoT FreeRTOS devices to list in the [AWS Partner Device Catalog ](https://partners.amazonaws.com/qualified-devices)through the [AWS Device Qualification Program](http://aws.amazon.com/partners/programs/dqp/) using IDT FRQ 1.0 versions. While you can't qualify FreeRTOS devices using IDT FRQ 1.0, you can continue to test your FreeRTOS devices with FRQ 1.0. We recommend that you use [IDT FRQ 2.0](https://docs.aws.amazon.com/freertos/latest/userguide/lts-idt-freertos-qualification.html) to qualify and list FreeRTOS devices in the [AWS Partner Device Catalog](https://partners.amazonaws.com/qualified-devices).

**Topics**
+ [Download IDT manually](#idt-download-options)
+ [Download IDT programmatically](idt-programmatic-download-process.md)

By downloading the software, you agree to the AWS IoT Device Tester License Agreement contained in the download archive.

**Note**
IDT does not support being run by multiple users from a shared location, such as an NFS directory or a Windows network shared folder. We recommend that you extract the IDT package to a local drive and run the IDT binary on your local workstation.

## Download IDT manually
<a name="idt-download-options"></a>

This topic lists supported versions of IDT for FreeRTOS. As a best practice, we recommend that you use the latest version of AWS IoT Device Tester that supports your target version of FreeRTOS. New releases of FreeRTOS might require you to download a new version of AWS IoT Device Tester. You receive a notification when you start a test run if AWS IoT Device Tester is not compatible with the version of FreeRTOS you are using.

See [Supported versions of AWS IoT Device Tester](dev-test-versions-afr.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for FreeRTOS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query freertos` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
