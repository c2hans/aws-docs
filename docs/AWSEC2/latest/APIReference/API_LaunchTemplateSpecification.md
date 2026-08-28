---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_LaunchTemplateSpecification.html
---

# LaunchTemplateSpecification
<a name="API_LaunchTemplateSpecification"></a>

Describes the launch template to use.

## Contents
<a name="API_LaunchTemplateSpecification_Contents"></a>

 ** LaunchTemplateId **
The ID of the launch template.
You must specify either the launch template ID or the launch template name, but not both.
Type: String
Required: No

 ** LaunchTemplateName **
The name of the launch template.
You must specify either the launch template ID or the launch template name, but not both.
Type: String
Required: No

 ** Version **
The launch template version number, `$Latest`, or `$Default`.
A value of `$Latest` uses the latest version of the launch template.
A value of `$Default` uses the default version of the launch template.
Default: The default version of the launch template.
Type: String
Required: No

## See Also
<a name="API_LaunchTemplateSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/LaunchTemplateSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/LaunchTemplateSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/LaunchTemplateSpecification)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
