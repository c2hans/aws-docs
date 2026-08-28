---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-timestream-scheduledquery-targetconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Timestream::ScheduledQuery TargetConfiguration
<a name="aws-properties-timestream-scheduledquery-targetconfiguration"></a>

Configuration used for writing the output of a query.

## Syntax
<a name="aws-properties-timestream-scheduledquery-targetconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-timestream-scheduledquery-targetconfiguration-syntax.json"></a>

```
{
  "[TimestreamConfiguration](#cfn-timestream-scheduledquery-targetconfiguration-timestreamconfiguration)" : {{TimestreamConfiguration}}
}
```

### YAML
<a name="aws-properties-timestream-scheduledquery-targetconfiguration-syntax.yaml"></a>

```
  [TimestreamConfiguration](#cfn-timestream-scheduledquery-targetconfiguration-timestreamconfiguration): {{
    TimestreamConfiguration}}
```

## Properties
<a name="aws-properties-timestream-scheduledquery-targetconfiguration-properties"></a>

`TimestreamConfiguration`  <a name="cfn-timestream-scheduledquery-targetconfiguration-timestreamconfiguration"></a>
Configuration needed to write data into the Timestream database and table.
*Required*: Yes
*Type*: [TimestreamConfiguration](aws-properties-timestream-scheduledquery-timestreamconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
