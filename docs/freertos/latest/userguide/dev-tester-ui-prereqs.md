---
source_url: https://docs.aws.amazon.com/freertos/latest/userguide/dev-tester-ui-prereqs.html
---

# Set up the prerequisites to run the FreeRTOS qualification suite
<a name="dev-tester-ui-prereqs"></a>

This section describes the prerequisites for testing microcontrollers with AWS IoT Device Tester.

**Topics**
+ [Use a supported web browser](#idt-ui-supported-web-browser)
+ [Download FreeRTOS](#ui-download-afr)
+ [Download IDT for FreeRTOS](#ui-download-dev-tester-afr)
+ [Create and configure an AWS account](#ui-config-aws-account)
+ [AWS IoT Device Tester managed policy](#ui-managed-policy)

## Use a supported web browser
<a name="idt-ui-supported-web-browser"></a>

The IDT-FreeRTOS UI supports the following web browsers.

| Browser | Version |
| --- | --- |
| Google Chrome | Latest three major versions |
| Mozilla Firefox | Latest three major versions |
| Microsoft Edge | Latest three major versions |
| Apple Safari for macOS | Latest three major versions |

We recommend that you use Google Chrome or Mozilla Firefox for a better experience.

**Note**
The IDT-FreeRTOS UI doesn't support Microsoft Internet Explorer.

## Download FreeRTOS
<a name="ui-download-afr"></a>

You can download a release of FreeRTOS from [GitHub](https://github.com/aws/amazon-freertos) with the following command:

```
git clone --branch <{{FREERTOS_RELEASE_VERSION}}> --recurse-submodules https://github.com/aws/amazon-freertos.git
cd amazon-freertos
git submodule update --checkout --init --recursive
```

where <FREERTOS\_RELEASE\_VERSION> is a version of FreeRTOS (for example, 202007.00) corresponding to an IDT version listed in [Supported versions of AWS IoT Device Tester](dev-test-versions-afr.md). This ensures you have the full source code, including submodules, and are using the correct version of IDT for your version of FreeRTOS, and vice versa.

Windows has a path length limitation of 260 characters. The path structure of FreeRTOS is many levels deep, so if you're using Windows, keep your file paths under the 260-character limit. For example, clone FreeRTOS to `C:\FreeRTOS` rather than `C:\Users\username\programs\projects\myproj\FreeRTOS\`.

### Considerations for LTS qualification (qualification for FreeRTOS that uses LTS libraries)
<a name="ui-lts-qualification-dev-tester-afr"></a>
+ In order for your microcontroller to be designated as supporting long-term support (LTS) based versions of FreeRTOS in the AWS Partner Device Catalog, you must provide a manifest file. For more information, see the [FreeRTOS Qualification Checklist](https://docs.aws.amazon.com/freertos/latest/qualificationguide/afq-checklist.html) in the *FreeRTOS Qualification Guide*.
+ In order to validate that your microcontroller supports LTS based versions of FreeRTOS and qualify it for submission to the AWS Partner Device Catalog, you must use AWS IoT Device Tester (IDT) with FreeRTOS Qualification (FRQ) test suite version v1.4.x.
+ Support for LTS based versions of FreeRTOS is limited to the 202012.xx version of FreeRTOS.

## Download IDT for FreeRTOS
<a name="ui-download-dev-tester-afr"></a>

Every version of FreeRTOS has a corresponding version of IDT for FreeRTOS for performing qualification tests. Download the appropriate version of IDT for FreeRTOS from [Supported versions of AWS IoT Device Tester](dev-test-versions-afr.md).

Extract IDT for FreeRTOS to a location on the file system where you have read and write permissions. Because Microsoft Windows has a character limit for the path length, extract IDT for FreeRTOS into a root directory such as `C:\` or `D:\`.

**Note**
We recommend that you extract the IDT package to a local drive.Allowing multiple users to run IDT from a shared location, such as an NFS directory or a Windows network shared folder, might result in the system not responding or data corruption.

## Create and configure an AWS account
<a name="ui-config-aws-account"></a>

### Sign up for an AWS account
<a name="sign-up-for-aws"></a>

To get started with AWS, you need an AWS account. For information about creating an AWS account, see [Getting started with an AWS account](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html) in the *AWS Account Management Reference Guide*.

## AWS IoT Device Tester managed policy
<a name="ui-managed-policy"></a>

To enable device tester to run and to collect metrics, the `AWSIoTDeviceTesterForFreeRTOSFullAccess` managed policy contains the following permissions:
+ `iot-device-tester:SupportedVersion`

  Grants permission to get the list of FreeRTOS versions and test suite versions supported by IDT, so that they're available from the AWS CLI.
+ `iot-device-tester:LatestIdt`

  Grants permission to get the latest AWS IoT Device Tester version that is available for download.
+ `iot-device-tester:CheckVersion`

  Grants permission to check that a combination of product, test suite, and AWS IoT Device Tester versions are compatible.
+ `iot-device-tester:DownloadTestSuite`

  Grants permission to AWS IoT Device Tester to download test suites.
+ `iot-device-tester:SendMetrics`

  Grants permission to publish AWS IoT Device Tester usage metrics data.
