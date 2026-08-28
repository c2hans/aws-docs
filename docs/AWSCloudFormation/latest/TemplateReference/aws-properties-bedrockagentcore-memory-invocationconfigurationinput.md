---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-memory-invocationconfigurationinput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Memory InvocationConfigurationInput
<a name="aws-properties-bedrockagentcore-memory-invocationconfigurationinput"></a>

The memory invocation configuration input.

## Syntax
<a name="aws-properties-bedrockagentcore-memory-invocationconfigurationinput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-memory-invocationconfigurationinput-syntax.json"></a>

```
{
  "[PayloadDeliveryBucketName](#cfn-bedrockagentcore-memory-invocationconfigurationinput-payloaddeliverybucketname)" : {{String}},
  "[TopicArn](#cfn-bedrockagentcore-memory-invocationconfigurationinput-topicarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-memory-invocationconfigurationinput-syntax.yaml"></a>

```
  [PayloadDeliveryBucketName](#cfn-bedrockagentcore-memory-invocationconfigurationinput-payloaddeliverybucketname): {{String}}
  [TopicArn](#cfn-bedrockagentcore-memory-invocationconfigurationinput-topicarn): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-memory-invocationconfigurationinput-properties"></a>

`PayloadDeliveryBucketName`  <a name="cfn-bedrockagentcore-memory-invocationconfigurationinput-payloaddeliverybucketname"></a>
The message invocation configuration information for the bucket name.
*Required*: No
*Type*: String
*Pattern*: `^[a-z0-9][a-z0-9.-]{1,61}[a-z0-9]$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TopicArn`  <a name="cfn-bedrockagentcore-memory-invocationconfigurationinput-topicarn"></a>
The memory trigger condition topic Amazon Resource Name (ARN).
*Required*: No
*Type*: String
*Pattern*: `^arn:(aws(?:-cn|-us-gov|-iso(?:-[bef])?)?):[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
