---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-devopsagent-association-capabilityconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DevOpsAgent::Association CapabilityConfiguration

The configuration of a single capability.

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
Specifies whether the capability is enabled for this association.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TriggerFilterGroups`  <a name="cfn-devopsagent-association-capabilityconfiguration-triggerfiltergroups"></a>
The filter groups that control when the capability starts automatically. The capability starts when any group matches. If you omit this property, every applicable event starts the capability. The agent keeps the filter groups while the capability is turned off, so the same trigger behavior applies when you turn it on again.
*Required*: No
*Type*: Array of [TriggerFilterGroup](aws-properties-devopsagent-association-triggerfiltergroup.md)
*Minimum*: `1`
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
