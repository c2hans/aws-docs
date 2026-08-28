---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-pipes-pipe-pipesourceactivemqbrokerparameters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Pipes::Pipe PipeSourceActiveMQBrokerParameters
<a name="aws-properties-pipes-pipe-pipesourceactivemqbrokerparameters"></a>

The parameters for using an Active MQ broker as a source.

## Syntax
<a name="aws-properties-pipes-pipe-pipesourceactivemqbrokerparameters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-pipes-pipe-pipesourceactivemqbrokerparameters-syntax.json"></a>

```
{
  "[BatchSize](#cfn-pipes-pipe-pipesourceactivemqbrokerparameters-batchsize)" : {{Integer}},
  "[Credentials](#cfn-pipes-pipe-pipesourceactivemqbrokerparameters-credentials)" : {{MQBrokerAccessCredentials}},
  "[MaximumBatchingWindowInSeconds](#cfn-pipes-pipe-pipesourceactivemqbrokerparameters-maximumbatchingwindowinseconds)" : {{Integer}},
  "[QueueName](#cfn-pipes-pipe-pipesourceactivemqbrokerparameters-queuename)" : {{String}}
}
```

### YAML
<a name="aws-properties-pipes-pipe-pipesourceactivemqbrokerparameters-syntax.yaml"></a>

```
  [BatchSize](#cfn-pipes-pipe-pipesourceactivemqbrokerparameters-batchsize): {{Integer}}
  [Credentials](#cfn-pipes-pipe-pipesourceactivemqbrokerparameters-credentials): {{
    MQBrokerAccessCredentials}}
  [MaximumBatchingWindowInSeconds](#cfn-pipes-pipe-pipesourceactivemqbrokerparameters-maximumbatchingwindowinseconds): {{Integer}}
  [QueueName](#cfn-pipes-pipe-pipesourceactivemqbrokerparameters-queuename): {{String}}
```

## Properties
<a name="aws-properties-pipes-pipe-pipesourceactivemqbrokerparameters-properties"></a>

`BatchSize`  <a name="cfn-pipes-pipe-pipesourceactivemqbrokerparameters-batchsize"></a>
The maximum number of records to include in each batch.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `10000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Credentials`  <a name="cfn-pipes-pipe-pipesourceactivemqbrokerparameters-credentials"></a>
The credentials needed to access the resource.
*Required*: Yes
*Type*: [MQBrokerAccessCredentials](aws-properties-pipes-pipe-mqbrokeraccesscredentials.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaximumBatchingWindowInSeconds`  <a name="cfn-pipes-pipe-pipesourceactivemqbrokerparameters-maximumbatchingwindowinseconds"></a>
The maximum length of a time to wait for events.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `300`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`QueueName`  <a name="cfn-pipes-pipe-pipesourceactivemqbrokerparameters-queuename"></a>
The name of the destination queue to consume.
*Required*: Yes
*Type*: String
*Pattern*: `^[\s\S]*$`
*Minimum*: `1`
*Maximum*: `1000`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
