---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-logs-scheduledquery-destinationconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Logs::ScheduledQuery DestinationConfiguration
<a name="aws-properties-logs-scheduledquery-destinationconfiguration"></a>

Configuration for where to deliver scheduled query results. Specifies the destination type and associated settings for result delivery.

## Syntax
<a name="aws-properties-logs-scheduledquery-destinationconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-logs-scheduledquery-destinationconfiguration-syntax.json"></a>

```
{
  "[S3Configuration](#cfn-logs-scheduledquery-destinationconfiguration-s3configuration)" : {{S3Configuration}}
}
```

### YAML
<a name="aws-properties-logs-scheduledquery-destinationconfiguration-syntax.yaml"></a>

```
  [S3Configuration](#cfn-logs-scheduledquery-destinationconfiguration-s3configuration): {{
    S3Configuration}}
```

## Properties
<a name="aws-properties-logs-scheduledquery-destinationconfiguration-properties"></a>

`S3Configuration`  <a name="cfn-logs-scheduledquery-destinationconfiguration-s3configuration"></a>
Configuration for delivering query results to Amazon S3.
*Required*: No
*Type*: [S3Configuration](aws-properties-logs-scheduledquery-s3configuration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
