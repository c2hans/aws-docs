---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-dlm-lifecyclepolicy-action.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DLM::LifecyclePolicy Action
<a name="aws-properties-dlm-lifecyclepolicy-action"></a>

**[Event-based policies only]** Specifies an action for an event-based policy.

## Syntax
<a name="aws-properties-dlm-lifecyclepolicy-action-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-dlm-lifecyclepolicy-action-syntax.json"></a>

```
{
  "[CrossRegionCopy](#cfn-dlm-lifecyclepolicy-action-crossregioncopy)" : {{[ CrossRegionCopyAction, ... ]}},
  "[Name](#cfn-dlm-lifecyclepolicy-action-name)" : {{String}}
}
```

### YAML
<a name="aws-properties-dlm-lifecyclepolicy-action-syntax.yaml"></a>

```
  [CrossRegionCopy](#cfn-dlm-lifecyclepolicy-action-crossregioncopy): {{
    - CrossRegionCopyAction}}
  [Name](#cfn-dlm-lifecyclepolicy-action-name): {{String}}
```

## Properties
<a name="aws-properties-dlm-lifecyclepolicy-action-properties"></a>

`CrossRegionCopy`  <a name="cfn-dlm-lifecyclepolicy-action-crossregioncopy"></a>
The rule for copying shared snapshots across Regions.
*Required*: Yes
*Type*: Array of [CrossRegionCopyAction](aws-properties-dlm-lifecyclepolicy-crossregioncopyaction.md)
*Minimum*: `0`
*Maximum*: `3`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-dlm-lifecyclepolicy-action-name"></a>
A descriptive name for the action.
*Required*: Yes
*Type*: String
*Pattern*: `[0-9A-Za-z _-]+`
*Minimum*: `0`
*Maximum*: `120`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
