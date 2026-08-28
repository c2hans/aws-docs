---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DBShardGroup.html
---

# DBShardGroup
<a name="API_DBShardGroup"></a>

Contains the details for an Amazon RDS DB shard group.

## Contents
<a name="API_DBShardGroup_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ComputeRedundancy **
Specifies whether to create standby DB shard groups for the DB shard group. Valid values are the following:
+ 0 - Creates a DB shard group without a standby DB shard group. This is the default value.
+ 1 - Creates a DB shard group with a standby DB shard group in a different Availability Zone (AZ).
+ 2 - Creates a DB shard group with two standby DB shard groups in two different AZs.
Type: Integer
Required: No

 ** DBClusterIdentifier **
The name of the primary DB cluster for the DB shard group.
Type: String
Required: No

 ** DBShardGroupArn **
The Amazon Resource Name (ARN) for the DB shard group.
Type: String
Required: No

 ** DBShardGroupIdentifier **
The name of the DB shard group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z](?:-?[a-zA-Z0-9]+)*`
Required: No

 ** DBShardGroupResourceId **
The AWS Region-unique, immutable identifier for the DB shard group.
Type: String
Required: No

 ** Endpoint **
The connection endpoint for the DB shard group.
Type: String
Required: No

 ** MaxACU **
The maximum capacity of the DB shard group in Aurora capacity units (ACUs).
Type: Double
Required: No

 ** MinACU **
The minimum capacity of the DB shard group in Aurora capacity units (ACUs).
Type: Double
Required: No

 ** PubliclyAccessible **
Indicates whether the DB shard group is publicly accessible.
When the DB shard group is publicly accessible, its Domain Name System (DNS) endpoint resolves to the private IP address from within the DB shard group's virtual private cloud (VPC). It resolves to the public IP address from outside of the DB shard group's VPC. Access to the DB shard group is ultimately controlled by the security group it uses. That public access isn't permitted if the security group assigned to the DB shard group doesn't permit it.
When the DB shard group isn't publicly accessible, it is an internal DB shard group with a DNS name that resolves to a private IP address.
For more information, see [CreateDBShardGroup](API_CreateDBShardGroup.md).
This setting is only for Aurora Limitless Database.
Type: Boolean
Required: No

 ** Status **
The status of the DB shard group.
Type: String
Required: No

 ** TagList.Tag.N **
A list of tags.
For more information, see [Tagging Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.html) in the *Amazon RDS User Guide* or [Tagging Amazon Aurora and Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Tagging.html) in the *Amazon Aurora User Guide*.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## See Also
<a name="API_DBShardGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/DBShardGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/DBShardGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/DBShardGroup)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Relational Database Service (RDS). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
