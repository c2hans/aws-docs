---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-customerprofiles-domain-jobschedule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CustomerProfiles::Domain JobSchedule
<a name="aws-properties-customerprofiles-domain-jobschedule"></a>

The day and time when do you want to start the Identity Resolution Job every week.

## Syntax
<a name="aws-properties-customerprofiles-domain-jobschedule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-customerprofiles-domain-jobschedule-syntax.json"></a>

```
{
  "[DayOfTheWeek](#cfn-customerprofiles-domain-jobschedule-dayoftheweek)" : {{String}},
  "[Time](#cfn-customerprofiles-domain-jobschedule-time)" : {{String}}
}
```

### YAML
<a name="aws-properties-customerprofiles-domain-jobschedule-syntax.yaml"></a>

```
  [DayOfTheWeek](#cfn-customerprofiles-domain-jobschedule-dayoftheweek): {{String}}
  [Time](#cfn-customerprofiles-domain-jobschedule-time): {{String}}
```

## Properties
<a name="aws-properties-customerprofiles-domain-jobschedule-properties"></a>

`DayOfTheWeek`  <a name="cfn-customerprofiles-domain-jobschedule-dayoftheweek"></a>
The day when the Identity Resolution Job should run every week.
*Required*: Yes
*Type*: String
*Allowed values*: `SUNDAY | MONDAY | TUESDAY | WEDNESDAY | THURSDAY | FRIDAY | SATURDAY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Time`  <a name="cfn-customerprofiles-domain-jobschedule-time"></a>
The time when the Identity Resolution Job should run every week.
*Required*: Yes
*Type*: String
*Pattern*: `^([0-9]|0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$`
*Minimum*: `3`
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
