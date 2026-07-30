---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-hoursofoperation-recurrencepattern.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::HoursOfOperation RecurrencePattern
<a name="aws-properties-connect-hoursofoperation-recurrencepattern"></a>

Specifies the detailed pattern for event recurrence. Use this to define complex scheduling rules such as "every 2nd Tuesday of the month" or "every 3 months on the 15th".

## Syntax
<a name="aws-properties-connect-hoursofoperation-recurrencepattern-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-hoursofoperation-recurrencepattern-syntax.json"></a>

```
{
  "[ByMonth](#cfn-connect-hoursofoperation-recurrencepattern-bymonth)" : {{[ Integer, ... ]}},
  "[ByMonthDay](#cfn-connect-hoursofoperation-recurrencepattern-bymonthday)" : {{[ Integer, ... ]}},
  "[ByWeekdayOccurrence](#cfn-connect-hoursofoperation-recurrencepattern-byweekdayoccurrence)" : {{[ Integer, ... ]}},
  "[Frequency](#cfn-connect-hoursofoperation-recurrencepattern-frequency)" : {{String}},
  "[Interval](#cfn-connect-hoursofoperation-recurrencepattern-interval)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-connect-hoursofoperation-recurrencepattern-syntax.yaml"></a>

```
  [ByMonth](#cfn-connect-hoursofoperation-recurrencepattern-bymonth): {{
    - Integer}}
  [ByMonthDay](#cfn-connect-hoursofoperation-recurrencepattern-bymonthday): {{
    - Integer}}
  [ByWeekdayOccurrence](#cfn-connect-hoursofoperation-recurrencepattern-byweekdayoccurrence): {{
    - Integer}}
  [Frequency](#cfn-connect-hoursofoperation-recurrencepattern-frequency): {{String}}
  [Interval](#cfn-connect-hoursofoperation-recurrencepattern-interval): {{Integer}}
```

## Properties
<a name="aws-properties-connect-hoursofoperation-recurrencepattern-properties"></a>

`ByMonth`  <a name="cfn-connect-hoursofoperation-recurrencepattern-bymonth"></a>
Specifies which month the event should occur in (1-12, where 1=January, 12=December). Used with YEARLY frequency to schedule events in specific month.
Note: It does not accept multiple values in the same list
*Required*: No
*Type*: Array of Integer
*Minimum*: `1`
*Maximum*: `12`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ByMonthDay`  <a name="cfn-connect-hoursofoperation-recurrencepattern-bymonthday"></a>
Specifies which day of the month the event should occur on (1-31). Used with MONTHLY or YEARLY frequency to schedule events on specific date within a month.
 Examples: [15] for events on the 15th of each month, [-1] for events on the last day of month.
Note: It does not accept multiple values in the same list. If a specified day doesn't exist in a particular month (e.g., day 31 in February), the event will be skipped for that month. This field cannot be used simultaneously with ByWeekdayOccurrence as they represent different scheduling approaches (specific dates vs. relative weekday positions).
*Required*: No
*Type*: Array of Integer
*Minimum*: `-1`
*Maximum*: `31`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ByWeekdayOccurrence`  <a name="cfn-connect-hoursofoperation-recurrencepattern-byweekdayoccurrence"></a>
Specifies which occurrence of a weekday within the month the event should occur on. Must be used with MONTHLY or YEARLY frequency.
Example: 2 corresponds to second occurrence of the weekday in the month. -1 corresponds to last occurrence of the weekday in the month
The weekday itself is specified separately in the HoursOfOperationConfig. Example: To schedule the recurring event for the 2nd Thursday of April every year, set ByWeekdayOccurrence=[2], Day=THURSDAY, ByMonth=[4], Frequency: YEARLY and INTERVAL=1.
*Required*: No
*Type*: Array of Integer
*Minimum*: `0 | -1`
*Maximum*: `1 | 4`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Frequency`  <a name="cfn-connect-hoursofoperation-recurrencepattern-frequency"></a>
Defines how often the pattern repeats. This is the base unit for the recurrence schedule and works in conjunction with the Interval field to determine the exact repetition sequence.
*Required*: No
*Type*: String
*Allowed values*: `WEEKLY | MONTHLY | YEARLY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Interval`  <a name="cfn-connect-hoursofoperation-recurrencepattern-interval"></a>
Specifies the number of frequency units between each occurrence. Must be a positive integer.
 Examples: To repeat every week, set Interval=1 with WEEKLY frequency. To repeat every two months, set Interval=2 with MONTHLY frequency.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `6`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
