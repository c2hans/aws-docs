---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-devopsagent-association-triggerfiltergroup.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DevOpsAgent::Association TriggerFilterGroup
<a name="aws-properties-devopsagent-association-triggerfiltergroup"></a>

A group of trigger conditions. The group matches when all of its conditions pass. Specify at least one condition.

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
The webhook events that start the capability. The condition passes when the event is one of the listed events.
`PULL_REQUEST_READY_FOR_REVIEW`: a pull request or merge request is created, updated, or marked ready for review while it isn't a draft. `PULL_REQUEST_DRAFT`: a pull request or merge request is created or updated while it is a draft.
*Required*: No
*Type*: Array of String
*Allowed values*: `PULL_REQUEST_READY_FOR_REVIEW | PULL_REQUEST_DRAFT`
*Minimum*: `1`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetBranches`  <a name="cfn-devopsagent-association-triggerfiltergroup-targetbranches"></a>
The condition on the target branch of the pull request or merge request. The condition passes when the target branch matches one of the patterns.
*Required*: No
*Type*: [PatternFilter](aws-properties-devopsagent-association-patternfilter.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
