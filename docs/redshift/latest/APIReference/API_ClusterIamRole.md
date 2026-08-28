---
source_url: https://docs.aws.amazon.com/redshift/latest/APIReference/API_ClusterIamRole.html
---

# ClusterIamRole
<a name="API_ClusterIamRole"></a>

An AWS Identity and Access Management (IAM) role that can be used by the associated Amazon Redshift cluster to access other AWS services.

## Contents
<a name="API_ClusterIamRole_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ApplyStatus **
A value that describes the status of the IAM role's association with an Amazon Redshift cluster.
The following are possible statuses and descriptions.
+  `in-sync`: The role is available for use by the cluster.
+  `adding`: The role is in the process of being associated with the cluster.
+  `removing`: The role is in the process of being disassociated with the cluster.
Type: String
Length Constraints: Maximum length of 2147483647.
Required: No

 ** IamRoleArn **
The Amazon Resource Name (ARN) of the IAM role, for example, `arn:aws:iam::123456789012:role/RedshiftCopyUnload`.
Type: String
Length Constraints: Maximum length of 2147483647.
Required: No

## See Also
<a name="API_ClusterIamRole_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/ClusterIamRole)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/ClusterIamRole)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/ClusterIamRole)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
