---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iot-topicrule-kafkaactionheader.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::TopicRule KafkaActionHeader
<a name="aws-properties-iot-topicrule-kafkaactionheader"></a>

Specifies a Kafka header using key-value pairs when you create a Rule’s Kafka Action. You can use these headers to route data from IoT clients to downstream Kafka clusters without modifying your message payload.

## Syntax
<a name="aws-properties-iot-topicrule-kafkaactionheader-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iot-topicrule-kafkaactionheader-syntax.json"></a>

```
{
  "[Key](#cfn-iot-topicrule-kafkaactionheader-key)" : {{String}},
  "[Value](#cfn-iot-topicrule-kafkaactionheader-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-iot-topicrule-kafkaactionheader-syntax.yaml"></a>

```
  [Key](#cfn-iot-topicrule-kafkaactionheader-key): {{String}}
  [Value](#cfn-iot-topicrule-kafkaactionheader-value): {{String}}
```

## Properties
<a name="aws-properties-iot-topicrule-kafkaactionheader-properties"></a>

`Key`  <a name="cfn-iot-topicrule-kafkaactionheader-key"></a>
The key of the Kafka header.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-iot-topicrule-kafkaactionheader-value"></a>
The value of the Kafka header.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
