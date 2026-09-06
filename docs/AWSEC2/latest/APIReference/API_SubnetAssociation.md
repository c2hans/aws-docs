---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_SubnetAssociation.html
---

# SubnetAssociation
<a name="API_SubnetAssociation"></a>

Describes the subnet association with the transit gateway multicast domain.

## Contents
<a name="API_SubnetAssociation_Contents"></a>

 ** state **
The state of the subnet association.
Type: String
Valid Values: `pendingAcceptance | associating | associated | disassociating | disassociated | rejected | failed`
Required: No

 ** subnetId **
The ID of the subnet.
Type: String
Required: No

## See Also
<a name="API_SubnetAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/SubnetAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/SubnetAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/SubnetAssociation)
