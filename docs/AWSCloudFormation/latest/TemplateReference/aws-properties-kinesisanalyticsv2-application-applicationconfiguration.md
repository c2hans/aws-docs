---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kinesisanalyticsv2-application-applicationconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KinesisAnalyticsV2::Application ApplicationConfiguration
<a name="aws-properties-kinesisanalyticsv2-application-applicationconfiguration"></a>

Specifies the creation parameters for a Managed Service for Apache Flink application.

## Syntax
<a name="aws-properties-kinesisanalyticsv2-application-applicationconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kinesisanalyticsv2-application-applicationconfiguration-syntax.json"></a>

```
{
  "[ApplicationCodeConfiguration](#cfn-kinesisanalyticsv2-application-applicationconfiguration-applicationcodeconfiguration)" : {{ApplicationCodeConfiguration}},
  "[ApplicationEncryptionConfiguration](#cfn-kinesisanalyticsv2-application-applicationconfiguration-applicationencryptionconfiguration)" : {{ApplicationEncryptionConfiguration}},
  "[ApplicationSnapshotConfiguration](#cfn-kinesisanalyticsv2-application-applicationconfiguration-applicationsnapshotconfiguration)" : {{ApplicationSnapshotConfiguration}},
  "[ApplicationSystemRollbackConfiguration](#cfn-kinesisanalyticsv2-application-applicationconfiguration-applicationsystemrollbackconfiguration)" : {{ApplicationSystemRollbackConfiguration}},
  "[EnvironmentProperties](#cfn-kinesisanalyticsv2-application-applicationconfiguration-environmentproperties)" : {{EnvironmentProperties}},
  "[FlinkApplicationConfiguration](#cfn-kinesisanalyticsv2-application-applicationconfiguration-flinkapplicationconfiguration)" : {{FlinkApplicationConfiguration}},
  "[SqlApplicationConfiguration](#cfn-kinesisanalyticsv2-application-applicationconfiguration-sqlapplicationconfiguration)" : {{SqlApplicationConfiguration}},
  "[VpcConfigurations](#cfn-kinesisanalyticsv2-application-applicationconfiguration-vpcconfigurations)" : {{[ VpcConfiguration, ... ]}},
  "[ZeppelinApplicationConfiguration](#cfn-kinesisanalyticsv2-application-applicationconfiguration-zeppelinapplicationconfiguration)" : {{ZeppelinApplicationConfiguration}}
}
```

### YAML
<a name="aws-properties-kinesisanalyticsv2-application-applicationconfiguration-syntax.yaml"></a>

```
  [ApplicationCodeConfiguration](#cfn-kinesisanalyticsv2-application-applicationconfiguration-applicationcodeconfiguration): {{
    ApplicationCodeConfiguration}}
  [ApplicationEncryptionConfiguration](#cfn-kinesisanalyticsv2-application-applicationconfiguration-applicationencryptionconfiguration): {{
    ApplicationEncryptionConfiguration}}
  [ApplicationSnapshotConfiguration](#cfn-kinesisanalyticsv2-application-applicationconfiguration-applicationsnapshotconfiguration): {{
    ApplicationSnapshotConfiguration}}
  [ApplicationSystemRollbackConfiguration](#cfn-kinesisanalyticsv2-application-applicationconfiguration-applicationsystemrollbackconfiguration): {{
    ApplicationSystemRollbackConfiguration}}
  [EnvironmentProperties](#cfn-kinesisanalyticsv2-application-applicationconfiguration-environmentproperties): {{
    EnvironmentProperties}}
  [FlinkApplicationConfiguration](#cfn-kinesisanalyticsv2-application-applicationconfiguration-flinkapplicationconfiguration): {{
    FlinkApplicationConfiguration}}
  [SqlApplicationConfiguration](#cfn-kinesisanalyticsv2-application-applicationconfiguration-sqlapplicationconfiguration): {{
    SqlApplicationConfiguration}}
  [VpcConfigurations](#cfn-kinesisanalyticsv2-application-applicationconfiguration-vpcconfigurations): {{
    - VpcConfiguration}}
  [ZeppelinApplicationConfiguration](#cfn-kinesisanalyticsv2-application-applicationconfiguration-zeppelinapplicationconfiguration): {{
    ZeppelinApplicationConfiguration}}
```

## Properties
<a name="aws-properties-kinesisanalyticsv2-application-applicationconfiguration-properties"></a>

`ApplicationCodeConfiguration`  <a name="cfn-kinesisanalyticsv2-application-applicationconfiguration-applicationcodeconfiguration"></a>
The code location and type parameters for a Managed Service for Apache Flink application.
*Required*: Conditional
*Type*: [ApplicationCodeConfiguration](aws-properties-kinesisanalyticsv2-application-applicationcodeconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ApplicationEncryptionConfiguration`  <a name="cfn-kinesisanalyticsv2-application-applicationconfiguration-applicationencryptionconfiguration"></a>
The configuration to manage encryption at rest.
*Required*: No
*Type*: [ApplicationEncryptionConfiguration](aws-properties-kinesisanalyticsv2-application-applicationencryptionconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ApplicationSnapshotConfiguration`  <a name="cfn-kinesisanalyticsv2-application-applicationconfiguration-applicationsnapshotconfiguration"></a>
Describes whether snapshots are enabled for a Managed Service for Apache Flink application.
*Required*: No
*Type*: [ApplicationSnapshotConfiguration](aws-properties-kinesisanalyticsv2-application-applicationsnapshotconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ApplicationSystemRollbackConfiguration`  <a name="cfn-kinesisanalyticsv2-application-applicationconfiguration-applicationsystemrollbackconfiguration"></a>
Describes whether system rollbacks are enabled for a Managed Service for Apache Flink application.
*Required*: No
*Type*: [ApplicationSystemRollbackConfiguration](aws-properties-kinesisanalyticsv2-application-applicationsystemrollbackconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EnvironmentProperties`  <a name="cfn-kinesisanalyticsv2-application-applicationconfiguration-environmentproperties"></a>
Describes execution properties for a Managed Service for Apache Flink application.
*Required*: No
*Type*: [EnvironmentProperties](aws-properties-kinesisanalyticsv2-application-environmentproperties.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FlinkApplicationConfiguration`  <a name="cfn-kinesisanalyticsv2-application-applicationconfiguration-flinkapplicationconfiguration"></a>
The creation and update parameters for a Managed Service for Apache Flink application.
*Required*: No
*Type*: [FlinkApplicationConfiguration](aws-properties-kinesisanalyticsv2-application-flinkapplicationconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SqlApplicationConfiguration`  <a name="cfn-kinesisanalyticsv2-application-applicationconfiguration-sqlapplicationconfiguration"></a>
The creation and update parameters for a SQL-based Kinesis Data Analytics application.
*Required*: No
*Type*: [SqlApplicationConfiguration](aws-properties-kinesisanalyticsv2-application-sqlapplicationconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VpcConfigurations`  <a name="cfn-kinesisanalyticsv2-application-applicationconfiguration-vpcconfigurations"></a>
The array of descriptions of VPC configurations available to the application.
*Required*: No
*Type*: Array of [VpcConfiguration](aws-properties-kinesisanalyticsv2-application-vpcconfiguration.md)
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ZeppelinApplicationConfiguration`  <a name="cfn-kinesisanalyticsv2-application-applicationconfiguration-zeppelinapplicationconfiguration"></a>
The configuration parameters for a Kinesis Data Analytics Studio notebook.
*Required*: No
*Type*: [ZeppelinApplicationConfiguration](aws-properties-kinesisanalyticsv2-application-zeppelinapplicationconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-kinesisanalyticsv2-application-applicationconfiguration--seealso"></a>
+ [ApplicationConfiguration](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_ApplicationConfiguration.html) in the *Amazon Kinesis Data Analytics API Reference*
