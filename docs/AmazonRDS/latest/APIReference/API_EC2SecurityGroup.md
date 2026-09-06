---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_EC2SecurityGroup.html
---

# EC2SecurityGroup
<a name="API_EC2SecurityGroup"></a>

This data type is used as a response element in the following actions:
+  `AuthorizeDBSecurityGroupIngress`
+  `DescribeDBSecurityGroups`
+  `RevokeDBSecurityGroupIngress`

## Contents
<a name="API_EC2SecurityGroup_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** EC2SecurityGroupId **
Specifies the id of the EC2 security group.
Type: String
Required: No

 ** EC2SecurityGroupName **
Specifies the name of the EC2 security group.
Type: String
Required: No

 ** EC2SecurityGroupOwnerId **
Specifies the AWS ID of the owner of the EC2 security group specified in the `EC2SecurityGroupName` field.
Type: String
Required: No

 ** Status **
Provides the status of the EC2 security group. Status can be "authorizing", "authorized", "revoking", and "revoked".
Type: String
Required: No

## See Also
<a name="API_EC2SecurityGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/EC2SecurityGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/EC2SecurityGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/EC2SecurityGroup)
