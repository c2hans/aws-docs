---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kinesisanalyticsv2-application-runconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KinesisAnalyticsV2::Application RunConfiguration
<a name="aws-properties-kinesisanalyticsv2-application-runconfiguration"></a>

Describes the starting parameters for an Managed Service for Apache Flink application.

## Syntax
<a name="aws-properties-kinesisanalyticsv2-application-runconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kinesisanalyticsv2-application-runconfiguration-syntax.json"></a>

```
{
  "[ApplicationRestoreConfiguration](#cfn-kinesisanalyticsv2-application-runconfiguration-applicationrestoreconfiguration)" : {{ApplicationRestoreConfiguration}},
  "[FlinkRunConfiguration](#cfn-kinesisanalyticsv2-application-runconfiguration-flinkrunconfiguration)" : {{FlinkRunConfiguration}}
}
```

### YAML
<a name="aws-properties-kinesisanalyticsv2-application-runconfiguration-syntax.yaml"></a>

```
  [ApplicationRestoreConfiguration](#cfn-kinesisanalyticsv2-application-runconfiguration-applicationrestoreconfiguration): {{
    ApplicationRestoreConfiguration}}
  [FlinkRunConfiguration](#cfn-kinesisanalyticsv2-application-runconfiguration-flinkrunconfiguration): {{
    FlinkRunConfiguration}}
```

## Properties
<a name="aws-properties-kinesisanalyticsv2-application-runconfiguration-properties"></a>

`ApplicationRestoreConfiguration`  <a name="cfn-kinesisanalyticsv2-application-runconfiguration-applicationrestoreconfiguration"></a>
Describes the restore behavior of a restarting application.
*Required*: No
*Type*: [ApplicationRestoreConfiguration](aws-properties-kinesisanalyticsv2-application-applicationrestoreconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FlinkRunConfiguration`  <a name="cfn-kinesisanalyticsv2-application-runconfiguration-flinkrunconfiguration"></a>
Describes the starting parameters for a Managed Service for Apache Flink application.
*Required*: No
*Type*: [FlinkRunConfiguration](aws-properties-kinesisanalyticsv2-application-flinkrunconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
