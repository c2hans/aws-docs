---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsIamPolicyDetails.html
---

# AwsIamPolicyDetails
<a name="API_AwsIamPolicyDetails"></a>

Represents an IAM permissions policy.

## Contents
<a name="API_AwsIamPolicyDetails_Contents"></a>

 ** AttachmentCount **   <a name="securityhub-Type-AwsIamPolicyDetails-AttachmentCount"></a>
The number of users, groups, and roles that the policy is attached to.
Type: Integer
Required: No

 ** CreateDate **   <a name="securityhub-Type-AwsIamPolicyDetails-CreateDate"></a>
When the policy was created.
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
Type: String
Pattern: `.*\S.*`
Required: No

 ** DefaultVersionId **   <a name="securityhub-Type-AwsIamPolicyDetails-DefaultVersionId"></a>
The identifier of the default version of the policy.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Description **   <a name="securityhub-Type-AwsIamPolicyDetails-Description"></a>
A description of the policy.
Type: String
Pattern: `.*\S.*`
Required: No

 ** IsAttachable **   <a name="securityhub-Type-AwsIamPolicyDetails-IsAttachable"></a>
Whether the policy can be attached to a user, group, or role.
Type: Boolean
Required: No

 ** Path **   <a name="securityhub-Type-AwsIamPolicyDetails-Path"></a>
The path to the policy.
Type: String
Pattern: `.*\S.*`
Required: No

 ** PermissionsBoundaryUsageCount **   <a name="securityhub-Type-AwsIamPolicyDetails-PermissionsBoundaryUsageCount"></a>
The number of users and roles that use the policy to set the permissions boundary.
Type: Integer
Required: No

 ** PolicyId **   <a name="securityhub-Type-AwsIamPolicyDetails-PolicyId"></a>
The unique identifier of the policy.
Type: String
Pattern: `.*\S.*`
Required: No

 ** PolicyName **   <a name="securityhub-Type-AwsIamPolicyDetails-PolicyName"></a>
The name of the policy.
Type: String
Pattern: `.*\S.*`
Required: No

 ** PolicyVersionList **   <a name="securityhub-Type-AwsIamPolicyDetails-PolicyVersionList"></a>
List of versions of the policy.
Type: Array of [AwsIamPolicyVersion](API_AwsIamPolicyVersion.md) objects
Required: No

 ** UpdateDate **   <a name="securityhub-Type-AwsIamPolicyDetails-UpdateDate"></a>
When the policy was most recently updated.
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsIamPolicyDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsIamPolicyDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsIamPolicyDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsIamPolicyDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
