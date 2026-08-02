---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_InstanceStorageInfo.html
---

# InstanceStorageInfo
<a name="API_InstanceStorageInfo"></a>

Describes the instance store features that are supported by the instance type.

## Contents
<a name="API_InstanceStorageInfo_Contents"></a>

 ** Disks.N **
Describes the disks that are available for the instance type.
Type: Array of [DiskInfo](API_DiskInfo.md) objects
Required: No

 ** encryptionSupport **
Indicates whether data is encrypted at rest.
Type: String
Valid Values: `unsupported | required`
Required: No

 ** nvmeSupport **
Indicates whether non-volatile memory express (NVMe) is supported.
Type: String
Valid Values: `unsupported | supported | required`
Required: No

 ** totalSizeInGB **
The total size of the disks, in GB.
Type: Long
Required: No

## See Also
<a name="API_InstanceStorageInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/InstanceStorageInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/InstanceStorageInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/InstanceStorageInfo)
