---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DBClusterAssociatedRole.html
---

# DBClusterAssociatedRole
<a name="API_DBClusterAssociatedRole"></a>

Contains information about an AWS Identity and Access Management (IAM) role to associate with a DB cluster. You can specify this structure in the `AssociatedRoles` parameter of [CreateDBCluster](API_CreateDBCluster.md), [RestoreDBClusterFromS3](API_RestoreDBClusterFromS3.md), [RestoreDBClusterFromSnapshot](API_RestoreDBClusterFromSnapshot.md), and [RestoreDBClusterToPointInTime](API_RestoreDBClusterToPointInTime.md).

## Contents
<a name="API_DBClusterAssociatedRole_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** RoleArn **
The Amazon Resource Name (ARN) of the IAM role to associate with the DB cluster.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z-]*:iam::[0-9]*:role/.*`
Required: Yes

 ** FeatureName **
The name of the feature associated with the IAM role. For information about supported feature names, see [DBEngineVersion](API_DBEngineVersion.md).
Type: String
Required: No

## See Also
<a name="API_DBClusterAssociatedRole_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/DBClusterAssociatedRole)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/DBClusterAssociatedRole)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/DBClusterAssociatedRole)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Relational Database Service (RDS). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
