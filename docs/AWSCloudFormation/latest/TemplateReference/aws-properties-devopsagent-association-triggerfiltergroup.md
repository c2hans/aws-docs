---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-devopsagent-association-triggerfiltergroup.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DevOpsAgent::Association TriggerFilterGroup
<a name="aws-properties-devopsagent-association-triggerfiltergroup"></a>

<a name="aws-properties-devopsagent-association-triggerfiltergroup-description"></a>The `TriggerFilterGroup` property type specifies Property description not available. for an [AWS::DevOpsAgent::Association](aws-resource-devopsagent-association.md).

## Syntax
<a name="aws-properties-devopsagent-association-triggerfiltergroup-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-devopsagent-association-triggerfiltergroup-syntax.json"></a>

```
{
  "[Events](#cfn-devopsagent-association-triggerfiltergroup-events)" : {{[ String, ... ]}},
  "[TargetBranches](#cfn-devopsagent-association-triggerfiltergroup-targetbranches)" : {{PatternFilter}}
}
```

### YAML
<a name="aws-properties-devopsagent-association-triggerfiltergroup-syntax.yaml"></a>

```
  [Events](#cfn-devopsagent-association-triggerfiltergroup-events): {{
    - String}}
  [TargetBranches](#cfn-devopsagent-association-triggerfiltergroup-targetbranches): {{
    PatternFilter}}
```

## Properties
<a name="aws-properties-devopsagent-association-triggerfiltergroup-properties"></a>

`Events`  <a name="cfn-devopsagent-association-triggerfiltergroup-events"></a>
Property description not available.
*Required*: No
*Type*: Array of String
*Allowed values*: `PULL_REQUEST_READY_FOR_REVIEW | PULL_REQUEST_DRAFT`
*Minimum*: `1`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetBranches`  <a name="cfn-devopsagent-association-triggerfiltergroup-targetbranches"></a>
Property description not available.
*Required*: No
*Type*: [PatternFilter](aws-properties-devopsagent-association-patternfilter.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
