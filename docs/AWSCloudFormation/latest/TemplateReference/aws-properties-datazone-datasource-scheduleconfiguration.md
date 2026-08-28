---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datazone-datasource-scheduleconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataZone::DataSource ScheduleConfiguration
<a name="aws-properties-datazone-datasource-scheduleconfiguration"></a>

The details of the schedule of the data source runs.

## Syntax
<a name="aws-properties-datazone-datasource-scheduleconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datazone-datasource-scheduleconfiguration-syntax.json"></a>

```
{
  "[Schedule](#cfn-datazone-datasource-scheduleconfiguration-schedule)" : {{String}},
  "[Timezone](#cfn-datazone-datasource-scheduleconfiguration-timezone)" : {{String}}
}
```

### YAML
<a name="aws-properties-datazone-datasource-scheduleconfiguration-syntax.yaml"></a>

```
  [Schedule](#cfn-datazone-datasource-scheduleconfiguration-schedule): {{String}}
  [Timezone](#cfn-datazone-datasource-scheduleconfiguration-timezone): {{String}}
```

## Properties
<a name="aws-properties-datazone-datasource-scheduleconfiguration-properties"></a>

`Schedule`  <a name="cfn-datazone-datasource-scheduleconfiguration-schedule"></a>
The schedule of the data source runs.
*Required*: No
*Type*: String
*Pattern*: `cron\((\b[0-5]?[0-9]\b) (\b2[0-3]\b|\b[0-1]?[0-9]\b) (.*){1,5} (.*){1,5} (.*){1,5} (.*){1,5}\)`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Timezone`  <a name="cfn-datazone-datasource-scheduleconfiguration-timezone"></a>
The timezone of the data source run.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
