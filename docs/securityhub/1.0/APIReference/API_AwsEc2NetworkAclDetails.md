---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsEc2NetworkAclDetails.html
---

# AwsEc2NetworkAclDetails
<a name="API_AwsEc2NetworkAclDetails"></a>

Contains details about an Amazon EC2 network access control list (ACL).

## Contents
<a name="API_AwsEc2NetworkAclDetails_Contents"></a>

 ** Associations **   <a name="securityhub-Type-AwsEc2NetworkAclDetails-Associations"></a>
Associations between the network ACL and subnets.
Type: Array of [AwsEc2NetworkAclAssociation](API_AwsEc2NetworkAclAssociation.md) objects
Required: No

 ** Entries **   <a name="securityhub-Type-AwsEc2NetworkAclDetails-Entries"></a>
The set of rules in the network ACL.
Type: Array of [AwsEc2NetworkAclEntry](API_AwsEc2NetworkAclEntry.md) objects
Required: No

 ** IsDefault **   <a name="securityhub-Type-AwsEc2NetworkAclDetails-IsDefault"></a>
Whether this is the default network ACL for the VPC.
Type: Boolean
Required: No

 ** NetworkAclId **   <a name="securityhub-Type-AwsEc2NetworkAclDetails-NetworkAclId"></a>
The identifier of the network ACL.
Type: String
Pattern: `.*\S.*`
Required: No

 ** OwnerId **   <a name="securityhub-Type-AwsEc2NetworkAclDetails-OwnerId"></a>
The identifier of the AWS account that owns the network ACL.
Type: String
Pattern: `.*\S.*`
Required: No

 ** VpcId **   <a name="securityhub-Type-AwsEc2NetworkAclDetails-VpcId"></a>
The identifier of the VPC for the network ACL.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsEc2NetworkAclDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsEc2NetworkAclDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsEc2NetworkAclDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsEc2NetworkAclDetails)
