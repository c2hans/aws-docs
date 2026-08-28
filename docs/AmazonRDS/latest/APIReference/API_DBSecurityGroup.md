---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DBSecurityGroup.html
---

# DBSecurityGroup
<a name="API_DBSecurityGroup"></a>

Contains the details for an Amazon RDS DB security group.

This data type is used as a response element in the `DescribeDBSecurityGroups` action.

## Contents
<a name="API_DBSecurityGroup_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** DBSecurityGroupArn **
The Amazon Resource Name (ARN) for the DB security group.
Type: String
Required: No

 ** DBSecurityGroupDescription **
Provides the description of the DB security group.
Type: String
Required: No

 ** DBSecurityGroupName **
Specifies the name of the DB security group.
Type: String
Required: No

 ** EC2SecurityGroups.EC2SecurityGroup.N **
Contains a list of `EC2SecurityGroup` elements.
Type: Array of [EC2SecurityGroup](API_EC2SecurityGroup.md) objects
Required: No

 ** IPRanges.IPRange.N **
Contains a list of `IPRange` elements.
Type: Array of [IPRange](API_IPRange.md) objects
Required: No

 ** OwnerId **
Provides the AWS ID of the owner of a specific DB security group.
Type: String
Required: No

 ** VpcId **
Provides the VpcId of the DB security group.
Type: String
Required: No

## See Also
<a name="API_DBSecurityGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/DBSecurityGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/DBSecurityGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/DBSecurityGroup)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Relational Database Service (RDS). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
