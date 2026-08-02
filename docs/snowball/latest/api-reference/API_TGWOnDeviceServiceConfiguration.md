---
source_url: https://docs.aws.amazon.com/snowball/latest/api-reference/API_TGWOnDeviceServiceConfiguration.html
---

# TGWOnDeviceServiceConfiguration
<a name="API_TGWOnDeviceServiceConfiguration"></a>

**Note**
 AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/) for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/) for secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/).

An object that represents the metadata and configuration settings for the Storage Gateway service Tape Gateway type on an AWS Snowball Edge device.

**Note**
The Tape Gateway service is no longer available on Snow Family devices.

## Contents
<a name="API_TGWOnDeviceServiceConfiguration_Contents"></a>

 ** StorageLimit **   <a name="Snowball-Type-TGWOnDeviceServiceConfiguration-StorageLimit"></a>
The maximum number of virtual tapes to store on one Snowball Edge device. Due to physical resource limitations, this value must be set to 80 for Snowball Edge.
The Tape Gateway service is no longer available on Snow Family devices.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** StorageUnit **   <a name="Snowball-Type-TGWOnDeviceServiceConfiguration-StorageUnit"></a>
The scale unit of the virtual tapes on the device.
The Tape Gateway service is no longer available on Snow Family devices.
Type: String
Valid Values: `TB`
Required: No

## See Also
<a name="API_TGWOnDeviceServiceConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/snowball-2016-06-30/TGWOnDeviceServiceConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/snowball-2016-06-30/TGWOnDeviceServiceConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/snowball-2016-06-30/TGWOnDeviceServiceConfiguration)
