---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsIamInstanceProfileRole.html
---

# AwsIamInstanceProfileRole
<a name="API_AwsIamInstanceProfileRole"></a>

Information about a role associated with an instance profile.

## Contents
<a name="API_AwsIamInstanceProfileRole_Contents"></a>

 ** Arn **   <a name="securityhub-Type-AwsIamInstanceProfileRole-Arn"></a>
The ARN of the role.
Type: String
Pattern: `.*\S.*`
Required: No

 ** AssumeRolePolicyDocument **   <a name="securityhub-Type-AwsIamInstanceProfileRole-AssumeRolePolicyDocument"></a>
The policy that grants an entity permission to assume the role.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 131072.
Pattern: `[\u0009\u000A\u000D\u0020-\u007E\u00A1-\u00FF]+`
Required: No

 ** CreateDate **   <a name="securityhub-Type-AwsIamInstanceProfileRole-CreateDate"></a>
Indicates when the role was created.
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
Type: String
Pattern: `.*\S.*`
Required: No

 ** Path **   <a name="securityhub-Type-AwsIamInstanceProfileRole-Path"></a>
The path to the role.
Type: String
Pattern: `.*\S.*`
Required: No

 ** RoleId **   <a name="securityhub-Type-AwsIamInstanceProfileRole-RoleId"></a>
The identifier of the role.
Type: String
Pattern: `.*\S.*`
Required: No

 ** RoleName **   <a name="securityhub-Type-AwsIamInstanceProfileRole-RoleName"></a>
The name of the role.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsIamInstanceProfileRole_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsIamInstanceProfileRole)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsIamInstanceProfileRole)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsIamInstanceProfileRole)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
