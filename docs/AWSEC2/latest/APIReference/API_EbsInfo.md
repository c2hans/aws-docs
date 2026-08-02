---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_EbsInfo.html
---

# EbsInfo
<a name="API_EbsInfo"></a>

Describes the Amazon EBS features supported by the instance type.

## Contents
<a name="API_EbsInfo_Contents"></a>

 ** attachmentLimitType **
Indicates whether the instance type features a shared or dedicated Amazon EBS volume attachment limit. For more information, see [Amazon EBS volume limits for Amazon EC2 instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/volume_limits.html) in the *Amazon EC2 User Guide*.
Type: String
Valid Values: `shared | dedicated`
Required: No

 ** EbsCardSet.N **
Describes the EBS cards available for the instance type.
Type: Array of [EbsCardInfo](API_EbsCardInfo.md) objects
Required: No

 ** ebsOptimizedInfo **
Describes the optimized EBS performance for the instance type.
Type: [EbsOptimizedInfo](API_EbsOptimizedInfo.md) object
Required: No

 ** ebsOptimizedSupport **
Indicates whether the instance type is Amazon EBS-optimized. For more information, see [Amazon EBS-optimized instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSOptimized.html) in *Amazon EC2 User Guide*.
Type: String
Valid Values: `unsupported | supported | default`
Required: No

 ** encryptionSupport **
Indicates whether Amazon EBS encryption is supported.
Type: String
Valid Values: `unsupported | supported`
Required: No

 ** maximumEbsAttachments **
Indicates the maximum number of Amazon EBS volumes that can be attached to the instance type. For more information, see [Amazon EBS volume limits for Amazon EC2 instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/volume_limits.html) in the *Amazon EC2 User Guide*.
Type: Integer
Required: No

 ** maximumEbsCards **
Indicates the number of EBS cards supported by the instance type.
Type: Integer
Required: No

 ** nvmeSupport **
Indicates whether non-volatile memory express (NVMe) is supported.
Type: String
Valid Values: `unsupported | supported | required`
Required: No

## See Also
<a name="API_EbsInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/EbsInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/EbsInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/EbsInfo)
