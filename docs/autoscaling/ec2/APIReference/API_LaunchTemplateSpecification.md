---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_LaunchTemplateSpecification.html
---

# LaunchTemplateSpecification
<a name="API_LaunchTemplateSpecification"></a>

Describes the launch template and the version of the launch template that Amazon EC2 Auto Scaling uses to launch Amazon EC2 instances. For more information about launch templates, see [Launch templates](https://docs.aws.amazon.com/autoscaling/ec2/userguide/launch-templates.html) in the *Amazon EC2 Auto Scaling User Guide*.

## Contents
<a name="API_LaunchTemplateSpecification_Contents"></a>

 ** LaunchTemplateId **
The ID of the launch template. To get the template ID, use the Amazon EC2 [DescribeLaunchTemplates](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeLaunchTemplates.html) API operation. New launch templates can be created using the Amazon EC2 [CreateLaunchTemplate](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateLaunchTemplate.html) API.
Conditional: You must specify either a `LaunchTemplateId` or a `LaunchTemplateName`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** LaunchTemplateName **
The name of the launch template. To get the template name, use the Amazon EC2 [DescribeLaunchTemplates](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeLaunchTemplates.html) API operation. New launch templates can be created using the Amazon EC2 [CreateLaunchTemplate](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateLaunchTemplate.html) API.
Conditional: You must specify either a `LaunchTemplateId` or a `LaunchTemplateName`.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 128.
Pattern: `[a-zA-Z0-9\(\)\.\-/_]+`
Required: No

 ** Version **
The version number, `$Latest`, or `$Default`. To get the version number, use the Amazon EC2 [DescribeLaunchTemplateVersions](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeLaunchTemplateVersions.html) API operation. New launch template versions can be created using the Amazon EC2 [CreateLaunchTemplateVersion](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateLaunchTemplateVersion.html) API. If the value is `$Latest`, Amazon EC2 Auto Scaling selects the latest version of the launch template when launching instances. If the value is `$Default`, Amazon EC2 Auto Scaling selects the default version of the launch template when launching instances. The default value is `$Default`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

## See Also
<a name="API_LaunchTemplateSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-2011-01-01/LaunchTemplateSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-2011-01-01/LaunchTemplateSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-2011-01-01/LaunchTemplateSpecification)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
