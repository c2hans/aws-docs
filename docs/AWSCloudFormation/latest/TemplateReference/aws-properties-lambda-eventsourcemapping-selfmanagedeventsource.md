---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-eventsourcemapping-selfmanagedeventsource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::EventSourceMapping SelfManagedEventSource
<a name="aws-properties-lambda-eventsourcemapping-selfmanagedeventsource"></a>

The self-managed Apache Kafka cluster for your event source.

## Syntax
<a name="aws-properties-lambda-eventsourcemapping-selfmanagedeventsource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lambda-eventsourcemapping-selfmanagedeventsource-syntax.json"></a>

```
{
  "[Endpoints](#cfn-lambda-eventsourcemapping-selfmanagedeventsource-endpoints)" : {{Endpoints}}
}
```

### YAML
<a name="aws-properties-lambda-eventsourcemapping-selfmanagedeventsource-syntax.yaml"></a>

```
  [Endpoints](#cfn-lambda-eventsourcemapping-selfmanagedeventsource-endpoints): {{
    Endpoints}}
```

## Properties
<a name="aws-properties-lambda-eventsourcemapping-selfmanagedeventsource-properties"></a>

`Endpoints`  <a name="cfn-lambda-eventsourcemapping-selfmanagedeventsource-endpoints"></a>
The list of bootstrap servers for your Kafka brokers in the following format: `"KafkaBootstrapServers": ["abc.xyz.com:xxxx","abc2.xyz.com:xxxx"]`.
*Required*: No
*Type*: [Endpoints](aws-properties-lambda-eventsourcemapping-endpoints.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
