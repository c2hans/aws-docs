---
source_url: https://docs.aws.amazon.com/greengrass/v2/APIReference/API_CoreDevice.html
---

# CoreDevice
<a name="API_CoreDevice"></a>

Contains information about a Greengrass core device, which is an AWS IoT thing that runs the AWS IoT Greengrass Core software.

## Contents
<a name="API_CoreDevice_Contents"></a>

 ** architecture **   <a name="greengrassv2-Type-CoreDevice-architecture"></a>
The computer architecture of the core device.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** coreDeviceThingName **   <a name="greengrassv2-Type-CoreDevice-coreDeviceThingName"></a>
The name of the core device. This is also the name of the AWS IoT thing.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** lastStatusUpdateTimestamp **   <a name="greengrassv2-Type-CoreDevice-lastStatusUpdateTimestamp"></a>
The time at which the core device's status last updated, expressed in ISO 8601 format.
Type: Timestamp
Required: No

 ** platform **   <a name="greengrassv2-Type-CoreDevice-platform"></a>
The operating system platform that the core device runs.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** runtime **   <a name="greengrassv2-Type-CoreDevice-runtime"></a>
The runtime for the core device. The runtime can be:
+  `aws_nucleus_classic`
+  `aws_nucleus_lite`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** status **   <a name="greengrassv2-Type-CoreDevice-status"></a>
The status of the core device. Core devices can have the following statuses:
+  `HEALTHY` – The AWS IoT Greengrass Core software and all components run on the core device without issue.
+  `UNHEALTHY` – The AWS IoT Greengrass Core software or a component is in a failed state on the core device.
Type: String
Valid Values: `HEALTHY | UNHEALTHY`
Required: No

## See Also
<a name="API_CoreDevice_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/greengrassv2-2020-11-30/CoreDevice)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/greengrassv2-2020-11-30/CoreDevice)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/greengrassv2-2020-11-30/CoreDevice)
