---
source_url: https://docs.aws.amazon.com/freertos/latest/userguide/idt-support-policy.html
---

# Understand the support policy for AWS IoT Device Tester
<a name="idt-support-policy"></a>

**Important**
As of October 2022, AWS IoT Device Tester for AWS IoT FreeRTOS Qualification (FRQ) 1.0 does not generate signed qualification reports. You cannot qualify new AWS IoT FreeRTOS devices to list in the [AWS Partner Device Catalog ](https://partners.amazonaws.com/qualified-devices)through the [AWS Device Qualification Program](http://aws.amazon.com/partners/programs/dqp/) using IDT FRQ 1.0 versions. While you can't qualify FreeRTOS devices using IDT FRQ 1.0, you can continue to test your FreeRTOS devices with FRQ 1.0. We recommend that you use [IDT FRQ 2.0](https://docs.aws.amazon.com/freertos/latest/userguide/lts-idt-freertos-qualification.html) to qualify and list FreeRTOS devices in the [AWS Partner Device Catalog](https://partners.amazonaws.com/qualified-devices).

 AWS IoT Device Tester for FreeRTOS is a test automation tool to validate FreeRTOS port to devices. Additionally you can [qualify](https://aws.amazon.com/partners/programs/dqp/) your FreeRTOS devices and list them on the [AWS Partner Device Catalog](https://partners.amazonaws.com/qualified-devices) . The AWS IoT Device Tester for FreeRTOS supports validation and qualification of FreeRTOS Long Term Supported (LTS) libraries available on GitHub at [FreeRTOS/FreeRTOS-LTS ](https://github.com/FreeRTOS/FreeRTOS-LTS), and FreeRTOS mainline available at [FreeRTOS/FreeRTOS](https://github.com/FreeRTOS/FreeRTOS). We recommend that you use the most recent versions of both the FreeRTOS and AWS IoT Device Tester for FreeRTOS to validate and qualify your devices.

 For FreeRTOS-LTS, IDT supports the validation and qualification of FreeRTOS 202210 LTS version. See here for more information on [FreeRTOS LTS releases](https://www.freertos.org/lts-libraries.html) and their maintenance time line. Once the support period of these LTS releases ends, you can still continue validation, but IDT will not generate a report, that will allow you to submit your device for qualification.

 For the mainline FreeRTOS available at [FreeRTOS/FreeRTOS ](https://github.com/FreeRTOS/FreeRTOS), we support the validation and qualification of all the versions released in the past six months, or the previous two versions of FreeRTOS if released more than six months apart. See here for [currently supported versions]( https://docs.aws.amazon.com//freertos/latest/userguide/dev-test-versions-afr.html). For unsupported versions of FreeRTOS, you can still continue validation, but IDT will not generate a report, that will allow you to submit your device for qualification.

 See [Supported versions of AWS IoT Device Tester](dev-test-versions-afr.md) for the latest supported IDT and FreeRTOS versions. You can use any of the supported versions of AWS IoT Device Tester with the corresponding version of FreeRTOS to test or qualify your device. If you continue to use the [Unsupported IDT versions for FreeRTOS](idt-unsupported-versions-afr.md), you will not receive the latest bug fixes or updates.

 For questions about the support policy, contact [AWS Customer Support](https://aws.amazon.com/contact-us/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for FreeRTOS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query freertos` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
