---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-athena-workgroup-monitoringconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Athena::WorkGroup MonitoringConfiguration
<a name="aws-properties-athena-workgroup-monitoringconfiguration"></a>

Contains the configuration settings for managed log persistence, delivering logs to Amazon S3 buckets, Amazon CloudWatch log groups etc.

## Syntax
<a name="aws-properties-athena-workgroup-monitoringconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-athena-workgroup-monitoringconfiguration-syntax.json"></a>

```
{
  "[CloudWatchLoggingConfiguration](#cfn-athena-workgroup-monitoringconfiguration-cloudwatchloggingconfiguration)" : {{CloudWatchLoggingConfiguration}},
  "[ManagedLoggingConfiguration](#cfn-athena-workgroup-monitoringconfiguration-managedloggingconfiguration)" : {{ManagedLoggingConfiguration}},
  "[S3LoggingConfiguration](#cfn-athena-workgroup-monitoringconfiguration-s3loggingconfiguration)" : {{S3LoggingConfiguration}}
}
```

### YAML
<a name="aws-properties-athena-workgroup-monitoringconfiguration-syntax.yaml"></a>

```
  [CloudWatchLoggingConfiguration](#cfn-athena-workgroup-monitoringconfiguration-cloudwatchloggingconfiguration): {{
    CloudWatchLoggingConfiguration}}
  [ManagedLoggingConfiguration](#cfn-athena-workgroup-monitoringconfiguration-managedloggingconfiguration): {{
    ManagedLoggingConfiguration}}
  [S3LoggingConfiguration](#cfn-athena-workgroup-monitoringconfiguration-s3loggingconfiguration): {{
    S3LoggingConfiguration}}
```

## Properties
<a name="aws-properties-athena-workgroup-monitoringconfiguration-properties"></a>

`CloudWatchLoggingConfiguration`  <a name="cfn-athena-workgroup-monitoringconfiguration-cloudwatchloggingconfiguration"></a>
Configuration settings for delivering logs to Amazon CloudWatch log groups.
*Required*: No
*Type*: [CloudWatchLoggingConfiguration](aws-properties-athena-workgroup-cloudwatchloggingconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ManagedLoggingConfiguration`  <a name="cfn-athena-workgroup-monitoringconfiguration-managedloggingconfiguration"></a>
Configuration settings for managed log persistence.
*Required*: No
*Type*: [ManagedLoggingConfiguration](aws-properties-athena-workgroup-managedloggingconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3LoggingConfiguration`  <a name="cfn-athena-workgroup-monitoringconfiguration-s3loggingconfiguration"></a>
Configuration settings for delivering logs to Amazon S3 buckets.
*Required*: No
*Type*: [S3LoggingConfiguration](aws-properties-athena-workgroup-s3loggingconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
