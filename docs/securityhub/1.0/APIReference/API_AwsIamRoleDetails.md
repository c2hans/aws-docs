---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsIamRoleDetails.html
---

# AwsIamRoleDetails
<a name="API_AwsIamRoleDetails"></a>

Contains information about an IAM role, including all of the role's policies.

## Contents
<a name="API_AwsIamRoleDetails_Contents"></a>

 ** AssumeRolePolicyDocument **   <a name="securityhub-Type-AwsIamRoleDetails-AssumeRolePolicyDocument"></a>
The trust policy that grants permission to assume the role.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 131072.
Pattern: `[\u0009\u000A\u000D\u0020-\u007E\u00A1-\u00FF]+`
Required: No

 ** AttachedManagedPolicies **   <a name="securityhub-Type-AwsIamRoleDetails-AttachedManagedPolicies"></a>
The list of the managed policies that are attached to the role.
Type: Array of [AwsIamAttachedManagedPolicy](API_AwsIamAttachedManagedPolicy.md) objects
Required: No

 ** CreateDate **   <a name="securityhub-Type-AwsIamRoleDetails-CreateDate"></a>
Indicates when the role was created.
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
Type: String
Pattern: `.*\S.*`
Required: No

 ** InstanceProfileList **   <a name="securityhub-Type-AwsIamRoleDetails-InstanceProfileList"></a>
The list of instance profiles that contain this role.
Type: Array of [AwsIamInstanceProfile](API_AwsIamInstanceProfile.md) objects
Required: No

 ** MaxSessionDuration **   <a name="securityhub-Type-AwsIamRoleDetails-MaxSessionDuration"></a>
The maximum session duration (in seconds) that you want to set for the specified role.
Type: Integer
Required: No

 ** Path **   <a name="securityhub-Type-AwsIamRoleDetails-Path"></a>
The path to the role.
Type: String
Pattern: `.*\S.*`
Required: No

 ** PermissionsBoundary **   <a name="securityhub-Type-AwsIamRoleDetails-PermissionsBoundary"></a>
Information about the policy used to set the permissions boundary for an IAM principal.
Type: [AwsIamPermissionsBoundary](API_AwsIamPermissionsBoundary.md) object
Required: No

 ** RoleId **   <a name="securityhub-Type-AwsIamRoleDetails-RoleId"></a>
The stable and unique string identifying the role.
Type: String
Pattern: `.*\S.*`
Required: No

 ** RoleName **   <a name="securityhub-Type-AwsIamRoleDetails-RoleName"></a>
The friendly name that identifies the role.
Type: String
Pattern: `.*\S.*`
Required: No

 ** RolePolicyList **   <a name="securityhub-Type-AwsIamRoleDetails-RolePolicyList"></a>
The list of inline policies that are embedded in the role.
Type: Array of [AwsIamRolePolicy](API_AwsIamRolePolicy.md) objects
Required: No

## See Also
<a name="API_AwsIamRoleDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsIamRoleDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsIamRoleDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsIamRoleDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
