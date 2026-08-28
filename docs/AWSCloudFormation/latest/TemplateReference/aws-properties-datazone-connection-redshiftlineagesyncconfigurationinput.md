---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datazone-connection-redshiftlineagesyncconfigurationinput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataZone::Connection RedshiftLineageSyncConfigurationInput
<a name="aws-properties-datazone-connection-redshiftlineagesyncconfigurationinput"></a>

The Amaon Redshift lineage sync configuration.

## Syntax
<a name="aws-properties-datazone-connection-redshiftlineagesyncconfigurationinput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datazone-connection-redshiftlineagesyncconfigurationinput-syntax.json"></a>

```
{
  "[Enabled](#cfn-datazone-connection-redshiftlineagesyncconfigurationinput-enabled)" : {{Boolean}},
  "[Schedule](#cfn-datazone-connection-redshiftlineagesyncconfigurationinput-schedule)" : {{LineageSyncSchedule}}
}
```

### YAML
<a name="aws-properties-datazone-connection-redshiftlineagesyncconfigurationinput-syntax.yaml"></a>

```
  [Enabled](#cfn-datazone-connection-redshiftlineagesyncconfigurationinput-enabled): {{Boolean}}
  [Schedule](#cfn-datazone-connection-redshiftlineagesyncconfigurationinput-schedule): {{
    LineageSyncSchedule}}
```

## Properties
<a name="aws-properties-datazone-connection-redshiftlineagesyncconfigurationinput-properties"></a>

`Enabled`  <a name="cfn-datazone-connection-redshiftlineagesyncconfigurationinput-enabled"></a>
Specifies whether the Amaon Redshift lineage sync configuration is enabled.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Schedule`  <a name="cfn-datazone-connection-redshiftlineagesyncconfigurationinput-schedule"></a>
The schedule of the Amaon Redshift lineage sync configuration.
*Required*: No
*Type*: [LineageSyncSchedule](aws-properties-datazone-connection-lineagesyncschedule.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
