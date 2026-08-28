---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsRdsDbClusterAssociatedRole.html
---

# AwsRdsDbClusterAssociatedRole
<a name="API_AwsRdsDbClusterAssociatedRole"></a>

An IAM role that is associated with the Amazon RDS DB cluster.

## Contents
<a name="API_AwsRdsDbClusterAssociatedRole_Contents"></a>

 ** RoleArn **   <a name="securityhub-Type-AwsRdsDbClusterAssociatedRole-RoleArn"></a>
The ARN of the IAM role.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Status **   <a name="securityhub-Type-AwsRdsDbClusterAssociatedRole-Status"></a>
The status of the association between the IAM role and the DB cluster. Valid values are as follows:
+  `ACTIVE`
+  `INVALID`
+  `PENDING`
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsRdsDbClusterAssociatedRole_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsRdsDbClusterAssociatedRole)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsRdsDbClusterAssociatedRole)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsRdsDbClusterAssociatedRole)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
