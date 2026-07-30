---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-applicationsignals-servicelevelobjective-exclusionwindow.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ApplicationSignals::ServiceLevelObjective ExclusionWindow
<a name="aws-properties-applicationsignals-servicelevelobjective-exclusionwindow"></a>

The time window to be excluded from the SLO performance metrics.

## Syntax
<a name="aws-properties-applicationsignals-servicelevelobjective-exclusionwindow-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-applicationsignals-servicelevelobjective-exclusionwindow-syntax.json"></a>

```
{
  "[Reason](#cfn-applicationsignals-servicelevelobjective-exclusionwindow-reason)" : {{String}},
  "[RecurrenceRule](#cfn-applicationsignals-servicelevelobjective-exclusionwindow-recurrencerule)" : {{RecurrenceRule}},
  "[StartTime](#cfn-applicationsignals-servicelevelobjective-exclusionwindow-starttime)" : {{String}},
  "[Window](#cfn-applicationsignals-servicelevelobjective-exclusionwindow-window)" : {{Window}}
}
```

### YAML
<a name="aws-properties-applicationsignals-servicelevelobjective-exclusionwindow-syntax.yaml"></a>

```
  [Reason](#cfn-applicationsignals-servicelevelobjective-exclusionwindow-reason): {{String}}
  [RecurrenceRule](#cfn-applicationsignals-servicelevelobjective-exclusionwindow-recurrencerule): {{
    RecurrenceRule}}
  [StartTime](#cfn-applicationsignals-servicelevelobjective-exclusionwindow-starttime): {{String}}
  [Window](#cfn-applicationsignals-servicelevelobjective-exclusionwindow-window): {{
    Window}}
```

## Properties
<a name="aws-properties-applicationsignals-servicelevelobjective-exclusionwindow-properties"></a>

`Reason`  <a name="cfn-applicationsignals-servicelevelobjective-exclusionwindow-reason"></a>
The reason for the time exclusion windows. For example, maintenance.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RecurrenceRule`  <a name="cfn-applicationsignals-servicelevelobjective-exclusionwindow-recurrencerule"></a>
The recurrence rule for the time exclusion window.
*Required*: No
*Type*: [RecurrenceRule](aws-properties-applicationsignals-servicelevelobjective-recurrencerule.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StartTime`  <a name="cfn-applicationsignals-servicelevelobjective-exclusionwindow-starttime"></a>
The start time of the time exclusion window.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Window`  <a name="cfn-applicationsignals-servicelevelobjective-exclusionwindow-window"></a>
The time exclusion window.
*Required*: Yes
*Type*: [Window](aws-properties-applicationsignals-servicelevelobjective-window.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
