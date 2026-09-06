---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_InstanceFamilyCreditSpecification.html
---

# InstanceFamilyCreditSpecification
<a name="API_InstanceFamilyCreditSpecification"></a>

Describes the default credit option for CPU usage of a burstable performance instance family.

## Contents
<a name="API_InstanceFamilyCreditSpecification_Contents"></a>

 ** cpuCredits **
The default credit option for CPU usage of the instance family. Valid values are `standard` and `unlimited`.
Type: String
Required: No

 ** instanceFamily **
The instance family.
Type: String
Valid Values: `t2 | t3 | t3a | t4g`
Required: No

## See Also
<a name="API_InstanceFamilyCreditSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/InstanceFamilyCreditSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/InstanceFamilyCreditSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/InstanceFamilyCreditSpecification)
