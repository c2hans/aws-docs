---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kinesisanalyticsv2-application-applicationsystemrollbackconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KinesisAnalyticsV2::Application ApplicationSystemRollbackConfiguration
<a name="aws-properties-kinesisanalyticsv2-application-applicationsystemrollbackconfiguration"></a>

Describes the system rollback configuration for a Managed Service for Apache Flink application.

## Syntax
<a name="aws-properties-kinesisanalyticsv2-application-applicationsystemrollbackconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kinesisanalyticsv2-application-applicationsystemrollbackconfiguration-syntax.json"></a>

```
{
  "[RollbackEnabled](#cfn-kinesisanalyticsv2-application-applicationsystemrollbackconfiguration-rollbackenabled)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-kinesisanalyticsv2-application-applicationsystemrollbackconfiguration-syntax.yaml"></a>

```
  [RollbackEnabled](#cfn-kinesisanalyticsv2-application-applicationsystemrollbackconfiguration-rollbackenabled): {{Boolean}}
```

## Properties
<a name="aws-properties-kinesisanalyticsv2-application-applicationsystemrollbackconfiguration-properties"></a>

`RollbackEnabled`  <a name="cfn-kinesisanalyticsv2-application-applicationsystemrollbackconfiguration-rollbackenabled"></a>
Describes whether system rollbacks are enabled for a Managed Service for Apache Flink application.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
