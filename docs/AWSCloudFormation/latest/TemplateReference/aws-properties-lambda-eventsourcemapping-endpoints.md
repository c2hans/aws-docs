---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-eventsourcemapping-endpoints.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::EventSourceMapping Endpoints
<a name="aws-properties-lambda-eventsourcemapping-endpoints"></a>

The list of bootstrap servers for your Kafka brokers in the following format: `"KafkaBootstrapServers": ["abc.xyz.com:xxxx","abc2.xyz.com:xxxx"]`.

## Syntax
<a name="aws-properties-lambda-eventsourcemapping-endpoints-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lambda-eventsourcemapping-endpoints-syntax.json"></a>

```
{
  "[KafkaBootstrapServers](#cfn-lambda-eventsourcemapping-endpoints-kafkabootstrapservers)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-lambda-eventsourcemapping-endpoints-syntax.yaml"></a>

```
  [KafkaBootstrapServers](#cfn-lambda-eventsourcemapping-endpoints-kafkabootstrapservers): {{
    - String}}
```

## Properties
<a name="aws-properties-lambda-eventsourcemapping-endpoints-properties"></a>

`KafkaBootstrapServers`  <a name="cfn-lambda-eventsourcemapping-endpoints-kafkabootstrapservers"></a>
The list of bootstrap servers for your Kafka brokers in the following format: `"KafkaBootstrapServers": ["abc.xyz.com:xxxx","abc2.xyz.com:xxxx"]`.
*Required*: No
*Type*: Array of String
*Minimum*: `1 | 1`
*Maximum*: `300 | 10`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
