---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_AthenaParameters.html
---

# AthenaParameters
<a name="API_AthenaParameters"></a>

Parameters for Amazon Athena.

## Contents
<a name="API_AthenaParameters_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ConsumerAccountRoleArn **   <a name="QS-Type-AthenaParameters-ConsumerAccountRoleArn"></a>
Use `ConsumerAccountRoleArn` to perform cross-account Athena access. This is an IAM role ARN in the same AWS account as the Athena resources you want to access. Provide this along with `RoleArn` to enable role-chaining, where Amazon Quick Sight first assumes the `RoleArn` and then assumes the `ConsumerAccountRoleArn` to access Athena resources.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: No

 ** IdentityCenterConfiguration **   <a name="QS-Type-AthenaParameters-IdentityCenterConfiguration"></a>
An optional parameter that configures IAM Identity Center authentication to grant Quick Sight access to your workgroup.
This parameter can only be specified if your Quick Sight account is configured with IAM Identity Center.
Type: [IdentityCenterConfiguration](API_IdentityCenterConfiguration.md) object
Required: No

 ** RoleArn **   <a name="QS-Type-AthenaParameters-RoleArn"></a>
Use the `RoleArn` structure to override an account-wide role for a specific Athena data source. For example, say an account administrator has turned off all Athena access with an account-wide role. The administrator can then use `RoleArn` to bypass the account-wide role and allow Athena access for the single Athena data source that is specified in the structure, even if the account-wide role forbidding Athena access is still active.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: No

 ** WorkGroup **   <a name="QS-Type-AthenaParameters-WorkGroup"></a>
The workgroup that Amazon Athena uses.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

## See Also
<a name="API_AthenaParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/AthenaParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/AthenaParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/AthenaParameters)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
