---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-imagebuilder-distributionconfiguration-fastlaunchlaunchtemplatespecification.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ImageBuilder::DistributionConfiguration FastLaunchLaunchTemplateSpecification
<a name="aws-properties-imagebuilder-distributionconfiguration-fastlaunchlaunchtemplatespecification"></a>

Identifies the launch template that the associated Windows AMI uses for launching an instance when faster launching is enabled.

**Note**
You can specify either the `launchTemplateName` or the `launchTemplateId`, but not both.

## Syntax
<a name="aws-properties-imagebuilder-distributionconfiguration-fastlaunchlaunchtemplatespecification-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-imagebuilder-distributionconfiguration-fastlaunchlaunchtemplatespecification-syntax.json"></a>

```
{
  "[LaunchTemplateId](#cfn-imagebuilder-distributionconfiguration-fastlaunchlaunchtemplatespecification-launchtemplateid)" : {{String}},
  "[LaunchTemplateName](#cfn-imagebuilder-distributionconfiguration-fastlaunchlaunchtemplatespecification-launchtemplatename)" : {{String}},
  "[LaunchTemplateVersion](#cfn-imagebuilder-distributionconfiguration-fastlaunchlaunchtemplatespecification-launchtemplateversion)" : {{String}}
}
```

### YAML
<a name="aws-properties-imagebuilder-distributionconfiguration-fastlaunchlaunchtemplatespecification-syntax.yaml"></a>

```
  [LaunchTemplateId](#cfn-imagebuilder-distributionconfiguration-fastlaunchlaunchtemplatespecification-launchtemplateid): {{String}}
  [LaunchTemplateName](#cfn-imagebuilder-distributionconfiguration-fastlaunchlaunchtemplatespecification-launchtemplatename): {{String}}
  [LaunchTemplateVersion](#cfn-imagebuilder-distributionconfiguration-fastlaunchlaunchtemplatespecification-launchtemplateversion): {{String}}
```

## Properties
<a name="aws-properties-imagebuilder-distributionconfiguration-fastlaunchlaunchtemplatespecification-properties"></a>

`LaunchTemplateId`  <a name="cfn-imagebuilder-distributionconfiguration-fastlaunchlaunchtemplatespecification-launchtemplateid"></a>
The ID of the launch template to use for faster launching for a Windows AMI.
*Required*: No
*Type*: String
*Pattern*: `^lt-[a-z0-9-_]{17}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LaunchTemplateName`  <a name="cfn-imagebuilder-distributionconfiguration-fastlaunchlaunchtemplatespecification-launchtemplatename"></a>
The name of the launch template to use for faster launching for a Windows AMI.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LaunchTemplateVersion`  <a name="cfn-imagebuilder-distributionconfiguration-fastlaunchlaunchtemplatespecification-launchtemplateversion"></a>
The version of the launch template to use for faster launching for a Windows AMI.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
