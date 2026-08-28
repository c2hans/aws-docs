---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kinesisanalyticsv2-application-zeppelinapplicationconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KinesisAnalyticsV2::Application ZeppelinApplicationConfiguration
<a name="aws-properties-kinesisanalyticsv2-application-zeppelinapplicationconfiguration"></a>

The configuration of a Kinesis Data Analytics Studio notebook.

## Syntax
<a name="aws-properties-kinesisanalyticsv2-application-zeppelinapplicationconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kinesisanalyticsv2-application-zeppelinapplicationconfiguration-syntax.json"></a>

```
{
  "[CatalogConfiguration](#cfn-kinesisanalyticsv2-application-zeppelinapplicationconfiguration-catalogconfiguration)" : {{CatalogConfiguration}},
  "[CustomArtifactsConfiguration](#cfn-kinesisanalyticsv2-application-zeppelinapplicationconfiguration-customartifactsconfiguration)" : {{[ CustomArtifactConfiguration, ... ]}},
  "[DeployAsApplicationConfiguration](#cfn-kinesisanalyticsv2-application-zeppelinapplicationconfiguration-deployasapplicationconfiguration)" : {{DeployAsApplicationConfiguration}},
  "[MonitoringConfiguration](#cfn-kinesisanalyticsv2-application-zeppelinapplicationconfiguration-monitoringconfiguration)" : {{ZeppelinMonitoringConfiguration}}
}
```

### YAML
<a name="aws-properties-kinesisanalyticsv2-application-zeppelinapplicationconfiguration-syntax.yaml"></a>

```
  [CatalogConfiguration](#cfn-kinesisanalyticsv2-application-zeppelinapplicationconfiguration-catalogconfiguration): {{
    CatalogConfiguration}}
  [CustomArtifactsConfiguration](#cfn-kinesisanalyticsv2-application-zeppelinapplicationconfiguration-customartifactsconfiguration): {{
    - CustomArtifactConfiguration}}
  [DeployAsApplicationConfiguration](#cfn-kinesisanalyticsv2-application-zeppelinapplicationconfiguration-deployasapplicationconfiguration): {{
    DeployAsApplicationConfiguration}}
  [MonitoringConfiguration](#cfn-kinesisanalyticsv2-application-zeppelinapplicationconfiguration-monitoringconfiguration): {{
    ZeppelinMonitoringConfiguration}}
```

## Properties
<a name="aws-properties-kinesisanalyticsv2-application-zeppelinapplicationconfiguration-properties"></a>

`CatalogConfiguration`  <a name="cfn-kinesisanalyticsv2-application-zeppelinapplicationconfiguration-catalogconfiguration"></a>
The Amazon Glue Data Catalog that you use in queries in a Kinesis Data Analytics Studio notebook.
*Required*: No
*Type*: [CatalogConfiguration](aws-properties-kinesisanalyticsv2-application-catalogconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CustomArtifactsConfiguration`  <a name="cfn-kinesisanalyticsv2-application-zeppelinapplicationconfiguration-customartifactsconfiguration"></a>
A list of `CustomArtifactConfiguration` objects.
*Required*: No
*Type*: Array of [CustomArtifactConfiguration](aws-properties-kinesisanalyticsv2-application-customartifactconfiguration.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DeployAsApplicationConfiguration`  <a name="cfn-kinesisanalyticsv2-application-zeppelinapplicationconfiguration-deployasapplicationconfiguration"></a>
The information required to deploy a Kinesis Data Analytics Studio notebook as an application with durable state.
*Required*: No
*Type*: [DeployAsApplicationConfiguration](aws-properties-kinesisanalyticsv2-application-deployasapplicationconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MonitoringConfiguration`  <a name="cfn-kinesisanalyticsv2-application-zeppelinapplicationconfiguration-monitoringconfiguration"></a>
The monitoring configuration of a Kinesis Data Analytics Studio notebook.
*Required*: No
*Type*: [ZeppelinMonitoringConfiguration](aws-properties-kinesisanalyticsv2-application-zeppelinmonitoringconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
