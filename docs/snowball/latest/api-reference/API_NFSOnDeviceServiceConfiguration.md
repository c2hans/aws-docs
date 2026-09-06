---
source_url: https://docs.aws.amazon.com/snowball/latest/api-reference/API_NFSOnDeviceServiceConfiguration.html
---

# NFSOnDeviceServiceConfiguration
<a name="API_NFSOnDeviceServiceConfiguration"></a>

**Note**
 AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/) for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/) for secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/).

An object that represents the metadata and configuration settings for the NFS (Network File System) service on an AWS Snowball Edge device.

## Contents
<a name="API_NFSOnDeviceServiceConfiguration_Contents"></a>

 ** StorageLimit **   <a name="Snowball-Type-NFSOnDeviceServiceConfiguration-StorageLimit"></a>
The maximum NFS storage for one Snowball Edge device.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** StorageUnit **   <a name="Snowball-Type-NFSOnDeviceServiceConfiguration-StorageUnit"></a>
The scale unit of the NFS storage on the device.
Valid values: TB.
Type: String
Valid Values: `TB`
Required: No

## See Also
<a name="API_NFSOnDeviceServiceConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/snowball-2016-06-30/NFSOnDeviceServiceConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/snowball-2016-06-30/NFSOnDeviceServiceConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/snowball-2016-06-30/NFSOnDeviceServiceConfiguration)
