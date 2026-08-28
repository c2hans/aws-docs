---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsAutoScalingAutoScalingGroupLaunchTemplateLaunchTemplateSpecification.html
---

# AwsAutoScalingAutoScalingGroupLaunchTemplateLaunchTemplateSpecification
<a name="API_AwsAutoScalingAutoScalingGroupLaunchTemplateLaunchTemplateSpecification"></a>

Details about the launch template to use.

## Contents
<a name="API_AwsAutoScalingAutoScalingGroupLaunchTemplateLaunchTemplateSpecification_Contents"></a>

 ** LaunchTemplateId **   <a name="securityhub-Type-AwsAutoScalingAutoScalingGroupLaunchTemplateLaunchTemplateSpecification-LaunchTemplateId"></a>
The identifier of the launch template. You must specify either `LaunchTemplateId` or `LaunchTemplateName`.
Type: String
Pattern: `.*\S.*`
Required: No

 ** LaunchTemplateName **   <a name="securityhub-Type-AwsAutoScalingAutoScalingGroupLaunchTemplateLaunchTemplateSpecification-LaunchTemplateName"></a>
The name of the launch template. You must specify either `LaunchTemplateId` or `LaunchTemplateName`.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Version **   <a name="securityhub-Type-AwsAutoScalingAutoScalingGroupLaunchTemplateLaunchTemplateSpecification-Version"></a>
Identifies the version of the launch template. You can specify a version identifier, or use the values `$Latest` or `$Default`.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsAutoScalingAutoScalingGroupLaunchTemplateLaunchTemplateSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsAutoScalingAutoScalingGroupLaunchTemplateLaunchTemplateSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsAutoScalingAutoScalingGroupLaunchTemplateLaunchTemplateSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsAutoScalingAutoScalingGroupLaunchTemplateLaunchTemplateSpecification)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
