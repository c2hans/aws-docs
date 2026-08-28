---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kinesisanalyticsv2-application-applicationmaintenanceconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KinesisAnalyticsV2::Application ApplicationMaintenanceConfiguration
<a name="aws-properties-kinesisanalyticsv2-application-applicationmaintenanceconfiguration"></a>

Specifies the maintenance configuration for a Amazon Managed Service for Apache Flink.

## Syntax
<a name="aws-properties-kinesisanalyticsv2-application-applicationmaintenanceconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kinesisanalyticsv2-application-applicationmaintenanceconfiguration-syntax.json"></a>

```
{
  "[ApplicationMaintenanceWindowStartTime](#cfn-kinesisanalyticsv2-application-applicationmaintenanceconfiguration-applicationmaintenancewindowstarttime)" : {{String}}
}
```

### YAML
<a name="aws-properties-kinesisanalyticsv2-application-applicationmaintenanceconfiguration-syntax.yaml"></a>

```
  [ApplicationMaintenanceWindowStartTime](#cfn-kinesisanalyticsv2-application-applicationmaintenanceconfiguration-applicationmaintenancewindowstarttime): {{String}}
```

## Properties
<a name="aws-properties-kinesisanalyticsv2-application-applicationmaintenanceconfiguration-properties"></a>

`ApplicationMaintenanceWindowStartTime`  <a name="cfn-kinesisanalyticsv2-application-applicationmaintenanceconfiguration-applicationmaintenancewindowstarttime"></a>
The UTC timestamp of a day from which the eight-hour maintenance window will begin every day of the week. Maintenance of the application happens only during this eight-hour window.
*Required*: Yes
*Type*: String
*Pattern*: `^([01][0-9]|2[0-3]):[0-5][0-9]$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
