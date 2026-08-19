---
source_url: https://docs.aws.amazon.com/freertos/latest/userguide/dev-tester-prereqs.html
---

# Setup the 1.0 qualification prerequisites
<a name="dev-tester-prereqs"></a>

This section describes the prerequisites for testing microcontrollers with AWS IoT Device Tester.

## Download FreeRTOS
<a name="download-afr"></a>

You can download a release of FreeRTOS from [GitHub](https://github.com/aws/amazon-freertos) with the following command:

```
git clone --branch <{{FREERTOS_RELEASE_VERSION}}> --recurse-submodules https://github.com/aws/amazon-freertos.git
cd amazon-freertos
git submodule update --checkout --init --recursive
```

where <FREERTOS\_RELEASE\_VERSION> is a version of FreeRTOS (for example, 202007.00) corresponding to an IDT version listed in [Supported versions of AWS IoT Device Tester](dev-test-versions-afr.md). This ensures you have the full source code, including submodules, and are using the correct version of IDT for your version of FreeRTOS, and vice versa.

Windows has a path length limitation of 260 characters. The path structure of FreeRTOS is many levels deep, so if you are using Windows, keep your file paths under the 260-character limit. For example, clone FreeRTOS to `C:\FreeRTOS` rather than `C:\Users\username\programs\projects\myproj\FreeRTOS\`.

### FreeRTOS qualification with LTS libraries
<a name="lts-qualification-dev-tester-afr"></a>
+ In order for your microcontroller to be designated as supporting long-term support (LTS) based versions of FreeRTOS in the AWS Partner Device Catalog, you must provide a manifest file. For more information, see the [ FreeRTOS Qualification Checklist](https://docs.aws.amazon.com/freertos/latest/qualificationguide/afq-checklist.html) in the *FreeRTOS Qualification Guide*.
+ In order to validate that your microcontroller supports LTS based versions of FreeRTOS and qualify it for submission to the AWS Partner Device Catalog, you must use AWS IoT Device Tester (IDT) with FreeRTOS Qualification (FRQ) test suite version v1.4.x.
+ Support for LTS based versions of FreeRTOS is limited to the 202012.xx version of FreeRTOS.

## Download IDT for FreeRTOS
<a name="download-dev-tester-afr"></a>

Every version of FreeRTOS has a corresponding version of IDT for FreeRTOS to perform qualification tests. Download the appropriate version of IDT for FreeRTOS from [Supported versions of AWS IoT Device Tester](dev-test-versions-afr.md).

Extract IDT for FreeRTOS to a location on the file system where you have read and write permissions. Because Microsoft Windows has a character limit for the path length, extract IDT for FreeRTOS into a root directory such as `C:\` or `D:\`.

**Note**
We don't recommend that multiple users run IDT from a shared location, such as an NFS directory or a Windows network shared folder. This may result in crashes or data corruption. We recommend that you extract the IDT package to a local drive.

## Create and configure an AWS account
<a name="config-aws-account"></a>

### Sign up for an AWS account
<a name="sign-up-for-aws"></a>

To get started with AWS, you need an AWS account. For information about creating an AWS account, see [Getting started with an AWS account](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html) in the *AWS Account Management Reference Guide*.

## AWS IoT Device Tester managed policy
<a name="managed-policy"></a>

The `AWSIoTDeviceTesterForFreeRTOSFullAccess` managed policy contains the following AWS IoT Device Tester permissions for version checking, auto update features, and collection of metrics.
+ `iot-device-tester:SupportedVersion`

  Grants AWS IoT Device Tester permission to fetch the list of supported products, test suites and IDT versions.
+ `iot-device-tester:LatestIdt`

  Grants AWS IoT Device Tester permission to fetch the latest IDT version available for download.
+ `iot-device-tester:CheckVersion`

  Grants AWS IoT Device Tester permission to check version compatibility for IDT, test suites and products.
+ `iot-device-tester:DownloadTestSuite`

  Grants AWS IoT Device Tester permission to download test suite updates.
+ `iot-device-tester:SendMetrics`

  Grants AWS permission to collect metrics about AWS IoT Device Tester internal usage.

## (Optional) Install the AWS Command Line Interface
<a name="install-cli"></a>

You might prefer to use the AWS CLI to perform some operations. If you don't have the AWS CLI installed, follow the instructions at [Install the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/installing.html).

Configure the AWS CLI for the AWS Region you want to use by running **aws configure** from a command line. For information about the AWS Regions that support IDT for FreeRTOS, see [AWS Regions and Endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html#amazon-freertos-ota-control). For more information about **aws configure** see [ Quick configuration with **aws configure**](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html#cli-configure-quickstart-config).
