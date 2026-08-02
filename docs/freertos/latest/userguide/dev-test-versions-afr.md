---
source_url: https://docs.aws.amazon.com/freertos/latest/userguide/dev-test-versions-afr.html
---

# Supported versions of AWS IoT Device Tester
<a name="dev-test-versions-afr"></a>

This topic lists supported versions of AWS IoT Device Tester for FreeRTOS. As a best practice, we recommend that you use the latest version of IDT for FreeRTOS that supports your target version of FreeRTOS. Each version of IDT for FreeRTOS has one or more corresponding versions of FreeRTOS that it supports. We recommend that you download a new version of IDT for FreeRTOS when a new version of FreeRTOS is released.

By downloading the software, you agree to the AWS IoT Device Tester License Agreement contained in the download archive.

**Note**
When you use AWS IoT Device Tester for FreeRTOS, we recommend that you update to the latest patch release of the most recent FreeRTOS-LTS version.

**Important**
As of October 2022, AWS IoT Device Tester for AWS IoT FreeRTOS Qualification (FRQ) 1.0 doesn't generate signed qualification reports. You can't qualify new AWS IoT FreeRTOS devices to list in the [AWS Partner Device Catalog](https://partners.amazonaws.com/qualified-devices) through the [AWS Device Qualification Program](http://aws.amazon.com/partners/programs/dqp/) using IDT FRQ 1.0 versions. While you can't qualify FreeRTOS devices using IDT FRQ 1.0, you can continue to test your FreeRTOS devices with FRQ 1.0. We recommend that you use [IDT FRQ 2.0](https://docs.aws.amazon.com/freertos/latest/userguide/lts-idt-freertos-qualification.html) to qualify and list FreeRTOS devices in the [AWS Partner Device Catalog](https://partners.amazonaws.com/qualified-devices).

## Latest version of AWS IoT Device Tester for FreeRTOS
<a name="idt-latest-version-afr"></a>

Use the following links to download the latest versions of IDT for FreeRTOS.

**Latest version of AWS IoT Device Tester for FreeRTOS**

| **AWS IoT Device Tester version** | **Test suite versions** | **Supported FreeRTOS versions** | **Download links** | **Release date** | **Release notes** |
| --- | --- | --- | --- | --- | --- |
| IDT v4.9.0 | FRQ\_2.5.0 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/freertos/latest/userguide/dev-test-versions-afr.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/freertos/latest/userguide/dev-test-versions-afr.html)  | 2023.04.04 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/freertos/latest/userguide/dev-test-versions-afr.html)  |

**Note**
We don't recommend that multiple users run IDT from a shared location, such as an NFS directory or a Windows network shared folder. This practice might result in crashes or data corruption. We recommend that you extract the IDT package to a local drive and run the IDT binary on your local workstation.

## Earlier IDT versions for FreeRTOS
<a name="idt-prev-versions-afr"></a>

The following earlier versions of IDT for FreeRTOS are also supported.

**Earlier versions of AWS IoT Device Tester for FreeRTOS**

| **AWS IoT Device Tester version** | **Test suite versions** | **Supported FreeRTOS versions** | **Download links** | **Release date** | **Release notes** |
| --- | --- | --- | --- | --- | --- |
| IDT v4.8.1 | FRQ\_2.4.0 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/freertos/latest/userguide/dev-test-versions-afr.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/freertos/latest/userguide/dev-test-versions-afr.html)  | 2023.01.23 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/freertos/latest/userguide/dev-test-versions-afr.html)  |
| IDT v4.6.0 | FRQ\_2.3.0 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/freertos/latest/userguide/dev-test-versions-afr.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/freertos/latest/userguide/dev-test-versions-afr.html)  | 2022.11.16 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/freertos/latest/userguide/dev-test-versions-afr.html)  |
| IDT v4.5.11 | FRQ\_2.2.0 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/freertos/latest/userguide/dev-test-versions-afr.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/freertos/latest/userguide/dev-test-versions-afr.html)  | 2022.10.14 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/freertos/latest/userguide/dev-test-versions-afr.html)  |

For more information, see [Understand the support policy for AWS IoT Device Tester](idt-support-policy.md).
