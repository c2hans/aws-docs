---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsIamInstanceProfile.html
---

# AwsIamInstanceProfile
<a name="API_AwsIamInstanceProfile"></a>

Information about an instance profile.

## Contents
<a name="API_AwsIamInstanceProfile_Contents"></a>

 ** Arn **   <a name="securityhub-Type-AwsIamInstanceProfile-Arn"></a>
The ARN of the instance profile.
Type: String
Pattern: `.*\S.*`
Required: No

 ** CreateDate **   <a name="securityhub-Type-AwsIamInstanceProfile-CreateDate"></a>
Indicates when the instance profile was created.
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
Type: String
Pattern: `.*\S.*`
Required: No

 ** InstanceProfileId **   <a name="securityhub-Type-AwsIamInstanceProfile-InstanceProfileId"></a>
The identifier of the instance profile.
Type: String
Pattern: `.*\S.*`
Required: No

 ** InstanceProfileName **   <a name="securityhub-Type-AwsIamInstanceProfile-InstanceProfileName"></a>
The name of the instance profile.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Path **   <a name="securityhub-Type-AwsIamInstanceProfile-Path"></a>
The path to the instance profile.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Roles **   <a name="securityhub-Type-AwsIamInstanceProfile-Roles"></a>
The roles associated with the instance profile.
Type: Array of [AwsIamInstanceProfileRole](API_AwsIamInstanceProfileRole.md) objects
Required: No

## See Also
<a name="API_AwsIamInstanceProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsIamInstanceProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsIamInstanceProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsIamInstanceProfile)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
