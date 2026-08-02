---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_VpcEncryptionControlExclusion.html
---

# VpcEncryptionControlExclusion
<a name="API_VpcEncryptionControlExclusion"></a>

Describes an exclusion configuration for VPC Encryption Control.

For more information, see [Enforce VPC encryption in transit](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-encryption-controls.html) in the *Amazon VPC User Guide*.

## Contents
<a name="API_VpcEncryptionControlExclusion_Contents"></a>

 ** state **
The current state of the exclusion configuration.
Type: String
Valid Values: `enabling | enabled | disabling | disabled`
Required: No

 ** stateMessage **
A message providing additional information about the exclusion state.
Type: String
Required: No

## See Also
<a name="API_VpcEncryptionControlExclusion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/VpcEncryptionControlExclusion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/VpcEncryptionControlExclusion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/VpcEncryptionControlExclusion)
