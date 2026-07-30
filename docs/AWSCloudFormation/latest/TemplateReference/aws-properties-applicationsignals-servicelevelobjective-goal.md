---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-applicationsignals-servicelevelobjective-goal.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ApplicationSignals::ServiceLevelObjective Goal
<a name="aws-properties-applicationsignals-servicelevelobjective-goal"></a>

This structure contains the attributes that determine the goal of an SLO. This includes the time period for evaluation and the attainment threshold.

## Syntax
<a name="aws-properties-applicationsignals-servicelevelobjective-goal-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-applicationsignals-servicelevelobjective-goal-syntax.json"></a>

```
{
  "[AttainmentGoal](#cfn-applicationsignals-servicelevelobjective-goal-attainmentgoal)" : {{Number}},
  "[Interval](#cfn-applicationsignals-servicelevelobjective-goal-interval)" : {{Interval}},
  "[WarningThreshold](#cfn-applicationsignals-servicelevelobjective-goal-warningthreshold)" : {{Number}}
}
```

### YAML
<a name="aws-properties-applicationsignals-servicelevelobjective-goal-syntax.yaml"></a>

```
  [AttainmentGoal](#cfn-applicationsignals-servicelevelobjective-goal-attainmentgoal): {{Number}}
  [Interval](#cfn-applicationsignals-servicelevelobjective-goal-interval): {{
    Interval}}
  [WarningThreshold](#cfn-applicationsignals-servicelevelobjective-goal-warningthreshold): {{Number}}
```

## Properties
<a name="aws-properties-applicationsignals-servicelevelobjective-goal-properties"></a>

`AttainmentGoal`  <a name="cfn-applicationsignals-servicelevelobjective-goal-attainmentgoal"></a>
The threshold that determines if the goal is being met.
If this is a period-based SLO, the attainment goal is the percentage of good periods that meet the threshold requirements to the total periods within the interval. For example, an attainment goal of 99.9% means that within your interval, you are targeting 99.9% of the periods to be in healthy state.
If this is a request-based SLO, the attainment goal is the percentage of requests that must be successful to meet the attainment goal.
If you omit this parameter, 99 is used to represent 99% as the attainment goal.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Interval`  <a name="cfn-applicationsignals-servicelevelobjective-goal-interval"></a>
The time period used to evaluate the SLO. It can be either a calendar interval or rolling interval.
If you omit this parameter, a rolling interval of 7 days is used.
*Required*: No
*Type*: [Interval](aws-properties-applicationsignals-servicelevelobjective-interval.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WarningThreshold`  <a name="cfn-applicationsignals-servicelevelobjective-goal-warningthreshold"></a>
The percentage of remaining budget over total budget that you want to get warnings for. If you omit this parameter, the default of 50.0 is used.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
