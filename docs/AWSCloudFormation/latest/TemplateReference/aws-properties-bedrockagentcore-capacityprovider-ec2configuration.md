---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-capacityprovider-ec2configuration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::CapacityProvider Ec2Configuration
<a name="aws-properties-bedrockagentcore-capacityprovider-ec2configuration"></a>

<a name="aws-properties-bedrockagentcore-capacityprovider-ec2configuration-description"></a>The `Ec2Configuration` property type specifies Property description not available. for an [AWS::BedrockAgentCore::CapacityProvider](aws-resource-bedrockagentcore-capacityprovider.md).

## Syntax
<a name="aws-properties-bedrockagentcore-capacityprovider-ec2configuration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-capacityprovider-ec2configuration-syntax.json"></a>

```
{
  "[LaunchTemplateSource](#cfn-bedrockagentcore-capacityprovider-ec2configuration-launchtemplatesource)" : {{LaunchTemplateSource}},
  "[LifecycleConfiguration](#cfn-bedrockagentcore-capacityprovider-ec2configuration-lifecycleconfiguration)" : {{InstanceLifecycleConfiguration}},
  "[RootVolume](#cfn-bedrockagentcore-capacityprovider-ec2configuration-rootvolume)" : {{RootVolumeConfiguration}},
  "[Volumes](#cfn-bedrockagentcore-capacityprovider-ec2configuration-volumes)" : {{[ VolumeConfiguration, ... ]}},
  "[VpcConfiguration](#cfn-bedrockagentcore-capacityprovider-ec2configuration-vpcconfiguration)" : {{VpcConfiguration}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-capacityprovider-ec2configuration-syntax.yaml"></a>

```
  [LaunchTemplateSource](#cfn-bedrockagentcore-capacityprovider-ec2configuration-launchtemplatesource): {{
    LaunchTemplateSource}}
  [LifecycleConfiguration](#cfn-bedrockagentcore-capacityprovider-ec2configuration-lifecycleconfiguration): {{
    InstanceLifecycleConfiguration}}
  [RootVolume](#cfn-bedrockagentcore-capacityprovider-ec2configuration-rootvolume): {{
    RootVolumeConfiguration}}
  [Volumes](#cfn-bedrockagentcore-capacityprovider-ec2configuration-volumes): {{
    - VolumeConfiguration}}
  [VpcConfiguration](#cfn-bedrockagentcore-capacityprovider-ec2configuration-vpcconfiguration): {{
    VpcConfiguration}}
```

## Properties
<a name="aws-properties-bedrockagentcore-capacityprovider-ec2configuration-properties"></a>

`LaunchTemplateSource`  <a name="cfn-bedrockagentcore-capacityprovider-ec2configuration-launchtemplatesource"></a>
Property description not available.
*Required*: Yes
*Type*: [LaunchTemplateSource](aws-properties-bedrockagentcore-capacityprovider-launchtemplatesource.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`LifecycleConfiguration`  <a name="cfn-bedrockagentcore-capacityprovider-ec2configuration-lifecycleconfiguration"></a>
Property description not available.
*Required*: No
*Type*: [InstanceLifecycleConfiguration](aws-properties-bedrockagentcore-capacityprovider-instancelifecycleconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RootVolume`  <a name="cfn-bedrockagentcore-capacityprovider-ec2configuration-rootvolume"></a>
Property description not available.
*Required*: No
*Type*: [RootVolumeConfiguration](aws-properties-bedrockagentcore-capacityprovider-rootvolumeconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Volumes`  <a name="cfn-bedrockagentcore-capacityprovider-ec2configuration-volumes"></a>
Property description not available.
*Required*: No
*Type*: Array of [VolumeConfiguration](aws-properties-bedrockagentcore-capacityprovider-volumeconfiguration.md)
*Maximum*: `5`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VpcConfiguration`  <a name="cfn-bedrockagentcore-capacityprovider-ec2configuration-vpcconfiguration"></a>
Property description not available.
*Required*: Yes
*Type*: [VpcConfiguration](aws-properties-bedrockagentcore-capacityprovider-vpcconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
