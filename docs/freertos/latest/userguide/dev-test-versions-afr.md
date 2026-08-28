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
| IDT v4.9.0 | FRQ\_2.5.0 |  + 202112.00<br />+ 202212.00<br />+ 202212.01<br />+ All patches of FreeRTOS 202210-LTS that use FreeRTOS LTS libraries.  |  + [ Linux](https://docs.aws.amazon.com/freertos/latest/userguide/freertos/devicetester_freertos_4.9.0_testsuite_2.5.0_linux.zip) <br />+ [ macOS](https://docs.aws.amazon.com/freertos/latest/userguide/freertos/devicetester_freertos_4.9.0_testsuite_2.5.0_mac.zip) <br />+ [ Windows](https://docs.aws.amazon.com/freertos/latest/userguide/freertos/devicetester_freertos_4.9.0_testsuite_2.5.0_win.zip)   | 2023.04.04 |  +  Supports testing against FreeRTOS **202112**, **202212**, **202212.01** and all patches of FreeRTOS **202210-LTS** that uses FreeRTOS libraries. See [README.md](https://github.com/FreeRTOS/FreeRTOS-Libraries-Integration-Tests/blob/main/README.md) for more information. You must include the patch version for FreeRTOS-LTS in your `manifest.yml`. <br />+  Improved run time of OTA E2E tests. <br />+  Limits number of devices listed in `device.json` to 1. <br />+   Minor bug fixes and improvements.    |

**Note**
We don't recommend that multiple users run IDT from a shared location, such as an NFS directory or a Windows network shared folder. This practice might result in crashes or data corruption. We recommend that you extract the IDT package to a local drive and run the IDT binary on your local workstation.

## Earlier IDT versions for FreeRTOS
<a name="idt-prev-versions-afr"></a>

The following earlier versions of IDT for FreeRTOS are also supported.

**Earlier versions of AWS IoT Device Tester for FreeRTOS**

| **AWS IoT Device Tester version** | **Test suite versions** | **Supported FreeRTOS versions** | **Download links** | **Release date** | **Release notes** |
| --- | --- | --- | --- | --- | --- |
| IDT v4.8.1 | FRQ\_2.4.0 |  + 202112.00<br />+ 202212.00<br />+ 202212.01<br />+ All patches of FreeRTOS 202210-LTS that use FreeRTOS LTS libraries.  |  + [ Linux](https://docs.aws.amazon.com/freertos/latest/userguide/freertos/devicetester_freertos_4.8.1_testsuite_2.4.0_linux.zip) <br />+ [ macOS](https://docs.aws.amazon.com/freertos/latest/userguide/freertos/devicetester_freertos_4.8.1_testsuite_2.4.0_mac.zip) <br />+ [ Windows](https://docs.aws.amazon.com/freertos/latest/userguide/freertos/devicetester_freertos_4.8.1_testsuite_2.4.0_win.zip)   | 2023.01.23 |  +  See [ README.MD](https://github.com/FreeRTOS/FreeRTOS-Libraries-Integration-Tests/blob/main/README.md) for further information. You must include the patch version for FreeRTOS-LTS in your `manifest.yml`. <br />+   Minor bug fixes and improvements.    |
| IDT v4.6.0 | FRQ\_2.3.0 |  + 202112.00<br />+ 202212.00<br />+ 202212.01<br />+ 202210-LTS that use FreeRTOS LTS libraries.  |  +  [ Linux](https://docs.aws.amazon.com/freertos/latest/userguide/freertos/devicetester_freertos_4.6.0_testsuite_2.3.0_linux.zip) <br />+  [ macOS](https://docs.aws.amazon.com/freertos/latest/userguide/freertos/devicetester_freertos_4.6.0_testsuite_2.3.0_mac.zip) <br />+  [ Windows](https://docs.aws.amazon.com/freertos/latest/userguide/freertos/devicetester_freertos_4.6.0_testsuite_2.3.0_win.zip)   | 2022.11.16 |  +  See [ README.MD](https://github.com/FreeRTOS/FreeRTOS-Libraries-Integration-Tests/blob/main/README.md) for further information. You must include the patch version for FreeRTOS-LTS in your `manifest.yml`.  <br />+  For more information about what's included in the FreeRTOS **202210-LTS** release, see the [CHANGELOG.md](https://github.com/FreeRTOS/FreeRTOS-LTS/blob/202210-LTS/CHANGELOG.md) file on GitHub. <br />+  Adds the ability to configure and run AWS IoT Device Tester for FreeRTOS through a web based user interface. See [UI for IDT for FreeRTOS qualification suite 2.0 (FRQ 2.0)](lts-device-tester-ui.md) to get started. <br />+  Adds an option to retain the modified copies of the source code created and used at runtime for post-test debugging. See [Configure build, flash, and test settings](lts-cfg-dt-ud.md) for more information.  <br />+  Adds IDT Client SDK support for Java. For more information about the IDT Client SDK, see [Develop and run your own IDT test suites](idt-custom-tests.md).    |
| IDT v4.5.11 | FRQ\_2.2.0 |  + 202112.00<br />+ 202212.00<br />+ 202212.01<br />+ 202210-LTS that use FreeRTOS LTS libraries.  |  +  [ Linux](https://docs.aws.amazon.com/freertos/latest/userguide/freertos/devicetester_freertos_4.5.11_testsuite_2.2.0_linux.zip) <br />+  [ macOS](https://docs.aws.amazon.com/freertos/latest/userguide/freertos/devicetester_freertos_4.5.11_testsuite_2.2.0_mac.zip) <br />+  [ Windows](https://docs.aws.amazon.com/freertos/latest/userguide/freertos/devicetester_freertos_4.5.11_testsuite_2.2.0_win.zip)   | 2022.10.14 |  +  See [ README.MD](https://github.com/FreeRTOS/FreeRTOS-Libraries-Integration-Tests/blob/main/README.md) for further information. You must include the patch version for FreeRTOS-LTS in your `manifest.yml`.  <br />+  For more information about what's included in the FreeRTOS **202210-LTS** release, see the [CHANGELOG.md](https://github.com/FreeRTOS/FreeRTOS-LTS/blob/202210-LTS/CHANGELOG.md) file on GitHub. <br />+  Minor bug fixes and improvements.   |

For more information, see [Understand the support policy for AWS IoT Device Tester](idt-support-policy.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for FreeRTOS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query freertos` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
