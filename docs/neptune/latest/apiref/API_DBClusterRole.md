---
source_url: https://docs.aws.amazon.com/neptune/latest/apiref/API_DBClusterRole.html
---

# DBClusterRole
<a name="API_DBClusterRole"></a>

Describes an Amazon Identity and Access Management (IAM) role that is associated with a DB cluster.

## Contents
<a name="API_DBClusterRole_Contents"></a>

 ** FeatureName **
The name of the feature associated with the Amazon Identity and Access Management (IAM) role. For the list of supported feature names, see [DescribeDBEngineVersions](API_DescribeDBEngineVersions.md).
Type: String
Required: No

 ** RoleArn **
The Amazon Resource Name (ARN) of the IAM role that is associated with the DB cluster.
Type: String
Required: No

 ** Status **
Describes the state of association between the IAM role and the DB cluster. The Status property returns one of the following values:
+  `ACTIVE` - the IAM role ARN is associated with the DB cluster and can be used to access other Amazon services on your behalf.
+  `PENDING` - the IAM role ARN is being associated with the DB cluster.
+  `INVALID` - the IAM role ARN is associated with the DB cluster, but the DB cluster is unable to assume the IAM role in order to access other Amazon services on your behalf.
Type: String
Required: No

## See Also
<a name="API_DBClusterRole_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptune-2014-10-31/DBClusterRole)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-2014-10-31/DBClusterRole)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptune-2014-10-31/DBClusterRole)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Neptune. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
