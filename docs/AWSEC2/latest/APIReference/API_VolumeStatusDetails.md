---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_VolumeStatusDetails.html
---

# VolumeStatusDetails
<a name="API_VolumeStatusDetails"></a>

Describes a volume status.

## Contents
<a name="API_VolumeStatusDetails_Contents"></a>

 ** name **
The name of the volume status.
+  `io-enabled` - Indicates the volume I/O status. For more information, see [Amazon EBS volume status checks](https://docs.aws.amazon.com/ebs/latest/userguide/monitoring-volume-checks.html).
+  `io-performance` - Indicates the volume performance status. For more information, see [Amazon EBS volume status checks](https://docs.aws.amazon.com/ebs/latest/userguide/monitoring-volume-checks.html).
+  `initialization-state` - Indicates the status of the volume initialization process. For more information, see [Initialize Amazon EBS volumes](https://docs.aws.amazon.com/ebs/latest/userguide/initalize-volume.html).
Type: String
Valid Values: `io-enabled | io-performance | initialization-state`
Required: No

 ** status **
The intended status of the volume status.
Type: String
Required: No

## See Also
<a name="API_VolumeStatusDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/VolumeStatusDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/VolumeStatusDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/VolumeStatusDetails)
