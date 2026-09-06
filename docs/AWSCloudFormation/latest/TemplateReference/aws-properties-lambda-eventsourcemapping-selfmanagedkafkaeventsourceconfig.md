---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-eventsourcemapping-selfmanagedkafkaeventsourceconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::EventSourceMapping SelfManagedKafkaEventSourceConfig
<a name="aws-properties-lambda-eventsourcemapping-selfmanagedkafkaeventsourceconfig"></a>

Specific configuration settings for a self-managed Apache Kafka event source.

## Syntax
<a name="aws-properties-lambda-eventsourcemapping-selfmanagedkafkaeventsourceconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lambda-eventsourcemapping-selfmanagedkafkaeventsourceconfig-syntax.json"></a>

```
{
  "[ConsumerGroupId](#cfn-lambda-eventsourcemapping-selfmanagedkafkaeventsourceconfig-consumergroupid)" : {{String}},
  "[SchemaRegistryConfig](#cfn-lambda-eventsourcemapping-selfmanagedkafkaeventsourceconfig-schemaregistryconfig)" : {{SchemaRegistryConfig}}
}
```

### YAML
<a name="aws-properties-lambda-eventsourcemapping-selfmanagedkafkaeventsourceconfig-syntax.yaml"></a>

```
  [ConsumerGroupId](#cfn-lambda-eventsourcemapping-selfmanagedkafkaeventsourceconfig-consumergroupid): {{String}}
  [SchemaRegistryConfig](#cfn-lambda-eventsourcemapping-selfmanagedkafkaeventsourceconfig-schemaregistryconfig): {{
    SchemaRegistryConfig}}
```

## Properties
<a name="aws-properties-lambda-eventsourcemapping-selfmanagedkafkaeventsourceconfig-properties"></a>

`ConsumerGroupId`  <a name="cfn-lambda-eventsourcemapping-selfmanagedkafkaeventsourceconfig-consumergroupid"></a>
 The identifier for the Kafka consumer group to join. The consumer group ID must be unique among all your Kafka event sources. After creating a Kafka event source mapping with the consumer group ID specified, you cannot update this value. For more information, see [Customizable consumer group ID](https://docs.aws.amazon.com/lambda/latest/dg/with-kafka-process.html#services-smaa-topic-add).
*Required*: No
*Type*: String
*Pattern*: `[a-zA-Z0-9-\/*:_+=.@-]*`
*Minimum*: `1`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SchemaRegistryConfig`  <a name="cfn-lambda-eventsourcemapping-selfmanagedkafkaeventsourceconfig-schemaregistryconfig"></a>
Specific configuration settings for a Kafka schema registry.
*Required*: No
*Type*: [SchemaRegistryConfig](aws-properties-lambda-eventsourcemapping-schemaregistryconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
