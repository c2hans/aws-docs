---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ssmcontacts-rotation-shiftcoverage.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SSMContacts::Rotation ShiftCoverage
<a name="aws-properties-ssmcontacts-rotation-shiftcoverage"></a>

Information about the days of the week that the on-call rotation coverage includes.

## Syntax
<a name="aws-properties-ssmcontacts-rotation-shiftcoverage-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ssmcontacts-rotation-shiftcoverage-syntax.json"></a>

```
{
  "[CoverageTimes](#cfn-ssmcontacts-rotation-shiftcoverage-coveragetimes)" : {{[ CoverageTime, ... ]}},
  "[DayOfWeek](#cfn-ssmcontacts-rotation-shiftcoverage-dayofweek)" : {{String}}
}
```

### YAML
<a name="aws-properties-ssmcontacts-rotation-shiftcoverage-syntax.yaml"></a>

```
  [CoverageTimes](#cfn-ssmcontacts-rotation-shiftcoverage-coveragetimes): {{
    - CoverageTime}}
  [DayOfWeek](#cfn-ssmcontacts-rotation-shiftcoverage-dayofweek): {{String}}
```

## Properties
<a name="aws-properties-ssmcontacts-rotation-shiftcoverage-properties"></a>

`CoverageTimes`  <a name="cfn-ssmcontacts-rotation-shiftcoverage-coveragetimes"></a>
The start and end times of the shift.
*Required*: Yes
*Type*: Array of [CoverageTime](aws-properties-ssmcontacts-rotation-coveragetime.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DayOfWeek`  <a name="cfn-ssmcontacts-rotation-shiftcoverage-dayofweek"></a>
A list of days on which the schedule is active.
*Required*: Yes
*Type*: String
*Allowed values*: `MON | TUE | WED | THU | FRI | SAT | SUN`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
