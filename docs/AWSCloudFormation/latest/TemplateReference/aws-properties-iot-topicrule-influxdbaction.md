---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iot-topicrule-influxdbaction.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::TopicRule InfluxDBAction
<a name="aws-properties-iot-topicrule-influxdbaction"></a>

<a name="aws-properties-iot-topicrule-influxdbaction-description"></a>The `InfluxDBAction` property type specifies Property description not available. for an [AWS::IoT::TopicRule](aws-resource-iot-topicrule.md).

## Syntax
<a name="aws-properties-iot-topicrule-influxdbaction-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iot-topicrule-influxdbaction-syntax.json"></a>

```
{
  "[BatchConfig](#cfn-iot-topicrule-influxdbaction-batchconfig)" : {{InfluxDBBatchConfig}},
  "[DatabaseName](#cfn-iot-topicrule-influxdbaction-databasename)" : {{String}},
  "[DestinationArn](#cfn-iot-topicrule-influxdbaction-destinationarn)" : {{String}},
  "[Organization](#cfn-iot-topicrule-influxdbaction-organization)" : {{String}},
  "[RoleArn](#cfn-iot-topicrule-influxdbaction-rolearn)" : {{String}},
  "[TableName](#cfn-iot-topicrule-influxdbaction-tablename)" : {{String}},
  "[Tags](#cfn-iot-topicrule-influxdbaction-tags)" : {{{{{Key}}: {{Value}}, ...}}},
  "[TimestampUnit](#cfn-iot-topicrule-influxdbaction-timestampunit)" : {{String}}
}
```

### YAML
<a name="aws-properties-iot-topicrule-influxdbaction-syntax.yaml"></a>

```
  [BatchConfig](#cfn-iot-topicrule-influxdbaction-batchconfig): {{
    InfluxDBBatchConfig}}
  [DatabaseName](#cfn-iot-topicrule-influxdbaction-databasename): {{String}}
  [DestinationArn](#cfn-iot-topicrule-influxdbaction-destinationarn): {{String}}
  [Organization](#cfn-iot-topicrule-influxdbaction-organization): {{String}}
  [RoleArn](#cfn-iot-topicrule-influxdbaction-rolearn): {{String}}
  [TableName](#cfn-iot-topicrule-influxdbaction-tablename): {{String}}
  [Tags](#cfn-iot-topicrule-influxdbaction-tags): {{
    {{Key}}: {{Value}}}}
  [TimestampUnit](#cfn-iot-topicrule-influxdbaction-timestampunit): {{String}}
```

## Properties
<a name="aws-properties-iot-topicrule-influxdbaction-properties"></a>

`BatchConfig`  <a name="cfn-iot-topicrule-influxdbaction-batchconfig"></a>
Property description not available.
*Required*: No
*Type*: [InfluxDBBatchConfig](aws-properties-iot-topicrule-influxdbbatchconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DatabaseName`  <a name="cfn-iot-topicrule-influxdbaction-databasename"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DestinationArn`  <a name="cfn-iot-topicrule-influxdbaction-destinationarn"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Organization`  <a name="cfn-iot-topicrule-influxdbaction-organization"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleArn`  <a name="cfn-iot-topicrule-influxdbaction-rolearn"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TableName`  <a name="cfn-iot-topicrule-influxdbaction-tablename"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-iot-topicrule-influxdbaction-tags"></a>
Property description not available.
*Required*: No
*Type*: Object of String
*Pattern*: `.*`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TimestampUnit`  <a name="cfn-iot-topicrule-influxdbaction-timestampunit"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
