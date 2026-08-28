---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-odb-cloudexadatainfrastructure-maintenancewindow.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ODB::CloudExadataInfrastructure MaintenanceWindow
<a name="aws-properties-odb-cloudexadatainfrastructure-maintenancewindow"></a>

The scheduling details for the maintenance window. Patching and system updates take place during the maintenance window.

## Syntax
<a name="aws-properties-odb-cloudexadatainfrastructure-maintenancewindow-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-odb-cloudexadatainfrastructure-maintenancewindow-syntax.json"></a>

```
{
  "[CustomActionTimeoutInMins](#cfn-odb-cloudexadatainfrastructure-maintenancewindow-customactiontimeoutinmins)" : {{Integer}},
  "[DaysOfWeek](#cfn-odb-cloudexadatainfrastructure-maintenancewindow-daysofweek)" : {{[ String, ... ]}},
  "[HoursOfDay](#cfn-odb-cloudexadatainfrastructure-maintenancewindow-hoursofday)" : {{[ Integer, ... ]}},
  "[IsCustomActionTimeoutEnabled](#cfn-odb-cloudexadatainfrastructure-maintenancewindow-iscustomactiontimeoutenabled)" : {{Boolean}},
  "[LeadTimeInWeeks](#cfn-odb-cloudexadatainfrastructure-maintenancewindow-leadtimeinweeks)" : {{Integer}},
  "[Months](#cfn-odb-cloudexadatainfrastructure-maintenancewindow-months)" : {{[ String, ... ]}},
  "[PatchingMode](#cfn-odb-cloudexadatainfrastructure-maintenancewindow-patchingmode)" : {{String}},
  "[Preference](#cfn-odb-cloudexadatainfrastructure-maintenancewindow-preference)" : {{String}},
  "[WeeksOfMonth](#cfn-odb-cloudexadatainfrastructure-maintenancewindow-weeksofmonth)" : {{[ Integer, ... ]}}
}
```

### YAML
<a name="aws-properties-odb-cloudexadatainfrastructure-maintenancewindow-syntax.yaml"></a>

```
  [CustomActionTimeoutInMins](#cfn-odb-cloudexadatainfrastructure-maintenancewindow-customactiontimeoutinmins): {{Integer}}
  [DaysOfWeek](#cfn-odb-cloudexadatainfrastructure-maintenancewindow-daysofweek): {{
    - String}}
  [HoursOfDay](#cfn-odb-cloudexadatainfrastructure-maintenancewindow-hoursofday): {{
    - Integer}}
  [IsCustomActionTimeoutEnabled](#cfn-odb-cloudexadatainfrastructure-maintenancewindow-iscustomactiontimeoutenabled): {{Boolean}}
  [LeadTimeInWeeks](#cfn-odb-cloudexadatainfrastructure-maintenancewindow-leadtimeinweeks): {{Integer}}
  [Months](#cfn-odb-cloudexadatainfrastructure-maintenancewindow-months): {{
    - String}}
  [PatchingMode](#cfn-odb-cloudexadatainfrastructure-maintenancewindow-patchingmode): {{String}}
  [Preference](#cfn-odb-cloudexadatainfrastructure-maintenancewindow-preference): {{String}}
  [WeeksOfMonth](#cfn-odb-cloudexadatainfrastructure-maintenancewindow-weeksofmonth): {{
    - Integer}}
```

## Properties
<a name="aws-properties-odb-cloudexadatainfrastructure-maintenancewindow-properties"></a>

`CustomActionTimeoutInMins`  <a name="cfn-odb-cloudexadatainfrastructure-maintenancewindow-customactiontimeoutinmins"></a>
The custom action timeout in minutes for the maintenance window.
*Required*: No
*Type*: Integer
*Minimum*: `15`
*Maximum*: `120`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DaysOfWeek`  <a name="cfn-odb-cloudexadatainfrastructure-maintenancewindow-daysofweek"></a>
The days of the week when maintenance can be performed.
*Required*: No
*Type*: Array of String
*Allowed values*: `MONDAY | TUESDAY | WEDNESDAY | THURSDAY | FRIDAY | SATURDAY | SUNDAY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HoursOfDay`  <a name="cfn-odb-cloudexadatainfrastructure-maintenancewindow-hoursofday"></a>
The hours of the day when maintenance can be performed.
*Required*: No
*Type*: Array of Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IsCustomActionTimeoutEnabled`  <a name="cfn-odb-cloudexadatainfrastructure-maintenancewindow-iscustomactiontimeoutenabled"></a>
Indicates whether custom action timeout is enabled for the maintenance window.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LeadTimeInWeeks`  <a name="cfn-odb-cloudexadatainfrastructure-maintenancewindow-leadtimeinweeks"></a>
The lead time in weeks before the maintenance window.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `4`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Months`  <a name="cfn-odb-cloudexadatainfrastructure-maintenancewindow-months"></a>
The months when maintenance can be performed.
*Required*: No
*Type*: Array of String
*Allowed values*: `JANUARY | FEBRUARY | MARCH | APRIL | MAY | JUNE | JULY | AUGUST | SEPTEMBER | OCTOBER | NOVEMBER | DECEMBER`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PatchingMode`  <a name="cfn-odb-cloudexadatainfrastructure-maintenancewindow-patchingmode"></a>
The patching mode for the maintenance window.
*Required*: No
*Type*: String
*Allowed values*: `ROLLING | NONROLLING`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Preference`  <a name="cfn-odb-cloudexadatainfrastructure-maintenancewindow-preference"></a>
The preference for the maintenance window scheduling.
*Required*: No
*Type*: String
*Allowed values*: `NO_PREFERENCE | CUSTOM_PREFERENCE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WeeksOfMonth`  <a name="cfn-odb-cloudexadatainfrastructure-maintenancewindow-weeksofmonth"></a>
The weeks of the month when maintenance can be performed.
*Required*: No
*Type*: Array of Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
