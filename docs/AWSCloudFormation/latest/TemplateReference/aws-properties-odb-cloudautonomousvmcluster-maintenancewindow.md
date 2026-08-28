---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-odb-cloudautonomousvmcluster-maintenancewindow.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ODB::CloudAutonomousVmCluster MaintenanceWindow
<a name="aws-properties-odb-cloudautonomousvmcluster-maintenancewindow"></a>

The scheduling details for the maintenance window. Patching and system updates take place during the maintenance window.

## Syntax
<a name="aws-properties-odb-cloudautonomousvmcluster-maintenancewindow-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-odb-cloudautonomousvmcluster-maintenancewindow-syntax.json"></a>

```
{
  "[DaysOfWeek](#cfn-odb-cloudautonomousvmcluster-maintenancewindow-daysofweek)" : {{[ String, ... ]}},
  "[HoursOfDay](#cfn-odb-cloudautonomousvmcluster-maintenancewindow-hoursofday)" : {{[ Integer, ... ]}},
  "[LeadTimeInWeeks](#cfn-odb-cloudautonomousvmcluster-maintenancewindow-leadtimeinweeks)" : {{Integer}},
  "[Months](#cfn-odb-cloudautonomousvmcluster-maintenancewindow-months)" : {{[ String, ... ]}},
  "[Preference](#cfn-odb-cloudautonomousvmcluster-maintenancewindow-preference)" : {{String}},
  "[WeeksOfMonth](#cfn-odb-cloudautonomousvmcluster-maintenancewindow-weeksofmonth)" : {{[ Integer, ... ]}}
}
```

### YAML
<a name="aws-properties-odb-cloudautonomousvmcluster-maintenancewindow-syntax.yaml"></a>

```
  [DaysOfWeek](#cfn-odb-cloudautonomousvmcluster-maintenancewindow-daysofweek): {{
    - String}}
  [HoursOfDay](#cfn-odb-cloudautonomousvmcluster-maintenancewindow-hoursofday): {{
    - Integer}}
  [LeadTimeInWeeks](#cfn-odb-cloudautonomousvmcluster-maintenancewindow-leadtimeinweeks): {{Integer}}
  [Months](#cfn-odb-cloudautonomousvmcluster-maintenancewindow-months): {{
    - String}}
  [Preference](#cfn-odb-cloudautonomousvmcluster-maintenancewindow-preference): {{String}}
  [WeeksOfMonth](#cfn-odb-cloudautonomousvmcluster-maintenancewindow-weeksofmonth): {{
    - Integer}}
```

## Properties
<a name="aws-properties-odb-cloudautonomousvmcluster-maintenancewindow-properties"></a>

`DaysOfWeek`  <a name="cfn-odb-cloudautonomousvmcluster-maintenancewindow-daysofweek"></a>
The days of the week when maintenance can be performed.
*Required*: No
*Type*: Array of String
*Allowed values*: `MONDAY | TUESDAY | WEDNESDAY | THURSDAY | FRIDAY | SATURDAY | SUNDAY`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`HoursOfDay`  <a name="cfn-odb-cloudautonomousvmcluster-maintenancewindow-hoursofday"></a>
The hours of the day when maintenance can be performed.
*Required*: No
*Type*: Array of Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`LeadTimeInWeeks`  <a name="cfn-odb-cloudautonomousvmcluster-maintenancewindow-leadtimeinweeks"></a>
The lead time in weeks before the maintenance window.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `4`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Months`  <a name="cfn-odb-cloudautonomousvmcluster-maintenancewindow-months"></a>
The months when maintenance can be performed.
*Required*: No
*Type*: Array of String
*Allowed values*: `JANUARY | FEBRUARY | MARCH | APRIL | MAY | JUNE | JULY | AUGUST | SEPTEMBER | OCTOBER | NOVEMBER | DECEMBER`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Preference`  <a name="cfn-odb-cloudautonomousvmcluster-maintenancewindow-preference"></a>
The preference for the maintenance window scheduling.
*Required*: No
*Type*: String
*Allowed values*: `NO_PREFERENCE | CUSTOM_PREFERENCE`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`WeeksOfMonth`  <a name="cfn-odb-cloudautonomousvmcluster-maintenancewindow-weeksofmonth"></a>
The weeks of the month when maintenance can be performed.
*Required*: No
*Type*: Array of Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
