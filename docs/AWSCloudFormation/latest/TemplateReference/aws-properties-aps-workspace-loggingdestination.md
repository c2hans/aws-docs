---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-aps-workspace-loggingdestination.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::APS::Workspace LoggingDestination
<a name="aws-properties-aps-workspace-loggingdestination"></a>

The logging destination in an Amazon Managed Service for Prometheus workspace.

## Syntax
<a name="aws-properties-aps-workspace-loggingdestination-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-aps-workspace-loggingdestination-syntax.json"></a>

```
{
  "[CloudWatchLogs](#cfn-aps-workspace-loggingdestination-cloudwatchlogs)" : {{CloudWatchLogDestination}},
  "[Filters](#cfn-aps-workspace-loggingdestination-filters)" : {{LoggingFilter}}
}
```

### YAML
<a name="aws-properties-aps-workspace-loggingdestination-syntax.yaml"></a>

```
  [CloudWatchLogs](#cfn-aps-workspace-loggingdestination-cloudwatchlogs): {{
    CloudWatchLogDestination}}
  [Filters](#cfn-aps-workspace-loggingdestination-filters): {{
    LoggingFilter}}
```

## Properties
<a name="aws-properties-aps-workspace-loggingdestination-properties"></a>

`CloudWatchLogs`  <a name="cfn-aps-workspace-loggingdestination-cloudwatchlogs"></a>
Configuration details for logging to CloudWatch Logs.
*Required*: Yes
*Type*: [CloudWatchLogDestination](aws-properties-aps-workspace-cloudwatchlogdestination.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Filters`  <a name="cfn-aps-workspace-loggingdestination-filters"></a>
Filtering criteria that determine which queries are logged.
*Required*: Yes
*Type*: [LoggingFilter](aws-properties-aps-workspace-loggingfilter.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
