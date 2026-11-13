---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-devopsagent-association-capabilityconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DevOpsAgent::Association CapabilityConfiguration
<a name="aws-properties-devopsagent-association-capabilityconfiguration"></a>

<a name="aws-properties-devopsagent-association-capabilityconfiguration-description"></a>The `CapabilityConfiguration` property type specifies Property description not available. for an [AWS::DevOpsAgent::Association](aws-resource-devopsagent-association.md).

## Syntax
<a name="aws-properties-devopsagent-association-capabilityconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-devopsagent-association-capabilityconfiguration-syntax.json"></a>

```
{
  "[Enabled](#cfn-devopsagent-association-capabilityconfiguration-enabled)" : {{Boolean}},
  "[TriggerFilterGroups](#cfn-devopsagent-association-capabilityconfiguration-triggerfiltergroups)" : {{[ TriggerFilterGroup, ... ]}}
}
```

### YAML
<a name="aws-properties-devopsagent-association-capabilityconfiguration-syntax.yaml"></a>

```
  [Enabled](#cfn-devopsagent-association-capabilityconfiguration-enabled): {{Boolean}}
  [TriggerFilterGroups](#cfn-devopsagent-association-capabilityconfiguration-triggerfiltergroups): {{
    - TriggerFilterGroup}}
```

## Properties
<a name="aws-properties-devopsagent-association-capabilityconfiguration-properties"></a>

`Enabled`  <a name="cfn-devopsagent-association-capabilityconfiguration-enabled"></a>
Property description not available.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TriggerFilterGroups`  <a name="cfn-devopsagent-association-capabilityconfiguration-triggerfiltergroups"></a>
Property description not available.
*Required*: No
*Type*: Array of [TriggerFilterGroup](aws-properties-devopsagent-association-triggerfiltergroup.md)
*Minimum*: `1`
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
