---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AssociatedKmsKey.html
---

# AssociatedKmsKey
<a name="API_AssociatedKmsKey"></a>

Describes an AWS KMS key that is associated with an Amazon EBS snapshot, in addition to the key the snapshot is encrypted under. An associated key provides a second way to access the snapshot's data for cross-account sharing and copying.

## Contents
<a name="API_AssociatedKmsKey_Contents"></a>

 ** kmsKeyId **
The Amazon Resource Name (ARN) of the associated AWS KMS key.
Type: String
Required: No

## See Also
<a name="API_AssociatedKmsKey_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/AssociatedKmsKey)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/AssociatedKmsKey)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/AssociatedKmsKey)
