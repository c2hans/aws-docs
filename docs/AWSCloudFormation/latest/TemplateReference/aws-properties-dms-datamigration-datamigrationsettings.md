---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-dms-datamigration-datamigrationsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DMS::DataMigration DataMigrationSettings
<a name="aws-properties-dms-datamigration-datamigrationsettings"></a>

Options for configuring a data migration, including whether to enable CloudWatch logs, and the selection rules to use to include or exclude database objects from the migration.

## Syntax
<a name="aws-properties-dms-datamigration-datamigrationsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-dms-datamigration-datamigrationsettings-syntax.json"></a>

```
{
  "[CloudwatchLogsEnabled](#cfn-dms-datamigration-datamigrationsettings-cloudwatchlogsenabled)" : {{Boolean}},
  "[NumberOfJobs](#cfn-dms-datamigration-datamigrationsettings-numberofjobs)" : {{Integer}},
  "[SelectionRules](#cfn-dms-datamigration-datamigrationsettings-selectionrules)" : {{String}}
}
```

### YAML
<a name="aws-properties-dms-datamigration-datamigrationsettings-syntax.yaml"></a>

```
  [CloudwatchLogsEnabled](#cfn-dms-datamigration-datamigrationsettings-cloudwatchlogsenabled): {{Boolean}}
  [NumberOfJobs](#cfn-dms-datamigration-datamigrationsettings-numberofjobs): {{Integer}}
  [SelectionRules](#cfn-dms-datamigration-datamigrationsettings-selectionrules): {{String}}
```

## Properties
<a name="aws-properties-dms-datamigration-datamigrationsettings-properties"></a>

`CloudwatchLogsEnabled`  <a name="cfn-dms-datamigration-datamigrationsettings-cloudwatchlogsenabled"></a>
Whether to enable CloudWatch logging for the data migration.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NumberOfJobs`  <a name="cfn-dms-datamigration-datamigrationsettings-numberofjobs"></a>
The number of parallel jobs that trigger parallel threads to unload the tables from the source, and then load them to the target.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SelectionRules`  <a name="cfn-dms-datamigration-datamigrationsettings-selectionrules"></a>
A JSON-formatted string that defines what objects to include and exclude from the migration.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
