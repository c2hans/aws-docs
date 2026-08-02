---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsEc2NetworkAclAssociation.html
---

# AwsEc2NetworkAclAssociation
<a name="API_AwsEc2NetworkAclAssociation"></a>

An association between the network ACL and a subnet.

## Contents
<a name="API_AwsEc2NetworkAclAssociation_Contents"></a>

 ** NetworkAclAssociationId **   <a name="securityhub-Type-AwsEc2NetworkAclAssociation-NetworkAclAssociationId"></a>
The identifier of the association between the network ACL and the subnet.
Type: String
Pattern: `.*\S.*`
Required: No

 ** NetworkAclId **   <a name="securityhub-Type-AwsEc2NetworkAclAssociation-NetworkAclId"></a>
The identifier of the network ACL.
Type: String
Pattern: `.*\S.*`
Required: No

 ** SubnetId **   <a name="securityhub-Type-AwsEc2NetworkAclAssociation-SubnetId"></a>
The identifier of the subnet that is associated with the network ACL.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsEc2NetworkAclAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsEc2NetworkAclAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsEc2NetworkAclAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsEc2NetworkAclAssociation)
