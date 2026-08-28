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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
