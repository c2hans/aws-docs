---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_VpcEncryptionControlExclusions.html
---

# VpcEncryptionControlExclusions
<a name="API_VpcEncryptionControlExclusions"></a>

Describes the exclusion configurations for various resource types in VPC Encryption Control.

For more information, see [Enforce VPC encryption in transit](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-encryption-controls.html) in the *Amazon VPC User Guide*.

## Contents
<a name="API_VpcEncryptionControlExclusions_Contents"></a>

 ** egressOnlyInternetGateway **
The exclusion configuration for egress-only internet gateway traffic.
Type: [VpcEncryptionControlExclusion](API_VpcEncryptionControlExclusion.md) object
Required: No

 ** elasticFileSystem **
The exclusion configuration for Elastic File System traffic.
Type: [VpcEncryptionControlExclusion](API_VpcEncryptionControlExclusion.md) object
Required: No

 ** internetGateway **
The exclusion configuration for internet gateway traffic.
Type: [VpcEncryptionControlExclusion](API_VpcEncryptionControlExclusion.md) object
Required: No

 ** lambda **
The exclusion configuration for Lambda function traffic.
Type: [VpcEncryptionControlExclusion](API_VpcEncryptionControlExclusion.md) object
Required: No

 ** natGateway **
The exclusion configuration for NAT gateway traffic.
Type: [VpcEncryptionControlExclusion](API_VpcEncryptionControlExclusion.md) object
Required: No

 ** virtualPrivateGateway **
The exclusion configuration for virtual private gateway traffic.
Type: [VpcEncryptionControlExclusion](API_VpcEncryptionControlExclusion.md) object
Required: No

 ** vpcLattice **
The exclusion configuration for VPC Lattice traffic.
Type: [VpcEncryptionControlExclusion](API_VpcEncryptionControlExclusion.md) object
Required: No

 ** vpcPeering **
The exclusion configuration for VPC peering connection traffic.
Type: [VpcEncryptionControlExclusion](API_VpcEncryptionControlExclusion.md) object
Required: No

## See Also
<a name="API_VpcEncryptionControlExclusions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/VpcEncryptionControlExclusions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/VpcEncryptionControlExclusions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/VpcEncryptionControlExclusions)
