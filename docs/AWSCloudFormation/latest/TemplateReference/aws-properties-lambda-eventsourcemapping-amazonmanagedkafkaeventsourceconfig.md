---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-eventsourcemapping-amazonmanagedkafkaeventsourceconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::EventSourceMapping AmazonManagedKafkaEventSourceConfig
<a name="aws-properties-lambda-eventsourcemapping-amazonmanagedkafkaeventsourceconfig"></a>

Specific configuration settings for an Amazon Managed Streaming for Apache Kafka (Amazon MSK) event source.

## Syntax
<a name="aws-properties-lambda-eventsourcemapping-amazonmanagedkafkaeventsourceconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lambda-eventsourcemapping-amazonmanagedkafkaeventsourceconfig-syntax.json"></a>

```
{
  "[ConsumerGroupId](#cfn-lambda-eventsourcemapping-amazonmanagedkafkaeventsourceconfig-consumergroupid)" : {{String}},
  "[SchemaRegistryConfig](#cfn-lambda-eventsourcemapping-amazonmanagedkafkaeventsourceconfig-schemaregistryconfig)" : {{SchemaRegistryConfig}}
}
```

### YAML
<a name="aws-properties-lambda-eventsourcemapping-amazonmanagedkafkaeventsourceconfig-syntax.yaml"></a>

```
  [ConsumerGroupId](#cfn-lambda-eventsourcemapping-amazonmanagedkafkaeventsourceconfig-consumergroupid): {{String}}
  [SchemaRegistryConfig](#cfn-lambda-eventsourcemapping-amazonmanagedkafkaeventsourceconfig-schemaregistryconfig): {{
    SchemaRegistryConfig}}
```

## Properties
<a name="aws-properties-lambda-eventsourcemapping-amazonmanagedkafkaeventsourceconfig-properties"></a>

`ConsumerGroupId`  <a name="cfn-lambda-eventsourcemapping-amazonmanagedkafkaeventsourceconfig-consumergroupid"></a>
The identifier for the Kafka consumer group to join. The consumer group ID must be unique among all your Kafka event sources. After creating a Kafka event source mapping with the consumer group ID specified, you cannot update this value. For more information, see [Customizable consumer group ID](https://docs.aws.amazon.com/lambda/latest/dg/with-msk.html#services-msk-consumer-group-id).
*Required*: No
*Type*: String
*Pattern*: `[a-zA-Z0-9-\/*:_+=.@-]*`
*Minimum*: `1`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SchemaRegistryConfig`  <a name="cfn-lambda-eventsourcemapping-amazonmanagedkafkaeventsourceconfig-schemaregistryconfig"></a>
Specific configuration settings for a Kafka schema registry.
*Required*: No
*Type*: [SchemaRegistryConfig](aws-properties-lambda-eventsourcemapping-schemaregistryconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
