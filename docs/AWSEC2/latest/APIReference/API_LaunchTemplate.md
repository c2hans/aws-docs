---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_LaunchTemplate.html
---

# LaunchTemplate
<a name="API_LaunchTemplate"></a>

Describes a launch template.

## Contents
<a name="API_LaunchTemplate_Contents"></a>

 ** createdBy **
The principal that created the launch template.
Type: String
Required: No

 ** createTime **
The time launch template was created.
Type: Timestamp
Required: No

 ** defaultVersionNumber **
The version number of the default version of the launch template.
Type: Long
Required: No

 ** latestVersionNumber **
The version number of the latest version of the launch template.
Type: Long
Required: No

 ** launchTemplateId **
The ID of the launch template.
Type: String
Required: No

 ** launchTemplateName **
The name of the launch template.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 128.
Pattern: `[a-zA-Z0-9\(\)\.\-/_]+`
Required: No

 ** operator **
The entity that manages the launch template.
Type: [OperatorResponse](API_OperatorResponse.md) object
Required: No

 ** TagSet.N **
The tags for the launch template.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## See Also
<a name="API_LaunchTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/LaunchTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/LaunchTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/LaunchTemplate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
