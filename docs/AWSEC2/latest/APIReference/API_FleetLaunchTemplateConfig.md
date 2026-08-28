---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_FleetLaunchTemplateConfig.html
---

# FleetLaunchTemplateConfig
<a name="API_FleetLaunchTemplateConfig"></a>

Describes a launch template and overrides.

## Contents
<a name="API_FleetLaunchTemplateConfig_Contents"></a>

 ** launchTemplateSpecification **
The launch template.
Type: [FleetLaunchTemplateSpecification](API_FleetLaunchTemplateSpecification.md) object
Required: No

 ** Overrides.N **
Any parameters that you specify override the same parameters in the launch template.
Type: Array of [FleetLaunchTemplateOverrides](API_FleetLaunchTemplateOverrides.md) objects
Required: No

## See Also
<a name="API_FleetLaunchTemplateConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/FleetLaunchTemplateConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/FleetLaunchTemplateConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/FleetLaunchTemplateConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
