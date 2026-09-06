---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-pipes-pipe-pipesourcerabbitmqbrokerparameters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Pipes::Pipe PipeSourceRabbitMQBrokerParameters
<a name="aws-properties-pipes-pipe-pipesourcerabbitmqbrokerparameters"></a>

The parameters for using a Rabbit MQ broker as a source.

## Syntax
<a name="aws-properties-pipes-pipe-pipesourcerabbitmqbrokerparameters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-pipes-pipe-pipesourcerabbitmqbrokerparameters-syntax.json"></a>

```
{
  "[BatchSize](#cfn-pipes-pipe-pipesourcerabbitmqbrokerparameters-batchsize)" : {{Integer}},
  "[Credentials](#cfn-pipes-pipe-pipesourcerabbitmqbrokerparameters-credentials)" : {{MQBrokerAccessCredentials}},
  "[MaximumBatchingWindowInSeconds](#cfn-pipes-pipe-pipesourcerabbitmqbrokerparameters-maximumbatchingwindowinseconds)" : {{Integer}},
  "[QueueName](#cfn-pipes-pipe-pipesourcerabbitmqbrokerparameters-queuename)" : {{String}},
  "[VirtualHost](#cfn-pipes-pipe-pipesourcerabbitmqbrokerparameters-virtualhost)" : {{String}}
}
```

### YAML
<a name="aws-properties-pipes-pipe-pipesourcerabbitmqbrokerparameters-syntax.yaml"></a>

```
  [BatchSize](#cfn-pipes-pipe-pipesourcerabbitmqbrokerparameters-batchsize): {{Integer}}
  [Credentials](#cfn-pipes-pipe-pipesourcerabbitmqbrokerparameters-credentials): {{
    MQBrokerAccessCredentials}}
  [MaximumBatchingWindowInSeconds](#cfn-pipes-pipe-pipesourcerabbitmqbrokerparameters-maximumbatchingwindowinseconds): {{Integer}}
  [QueueName](#cfn-pipes-pipe-pipesourcerabbitmqbrokerparameters-queuename): {{String}}
  [VirtualHost](#cfn-pipes-pipe-pipesourcerabbitmqbrokerparameters-virtualhost): {{String}}
```

## Properties
<a name="aws-properties-pipes-pipe-pipesourcerabbitmqbrokerparameters-properties"></a>

`BatchSize`  <a name="cfn-pipes-pipe-pipesourcerabbitmqbrokerparameters-batchsize"></a>
The maximum number of records to include in each batch.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `10000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Credentials`  <a name="cfn-pipes-pipe-pipesourcerabbitmqbrokerparameters-credentials"></a>
The credentials needed to access the resource.
*Required*: Yes
*Type*: [MQBrokerAccessCredentials](aws-properties-pipes-pipe-mqbrokeraccesscredentials.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaximumBatchingWindowInSeconds`  <a name="cfn-pipes-pipe-pipesourcerabbitmqbrokerparameters-maximumbatchingwindowinseconds"></a>
The maximum length of a time to wait for events.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `300`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`QueueName`  <a name="cfn-pipes-pipe-pipesourcerabbitmqbrokerparameters-queuename"></a>
The name of the destination queue to consume.
*Required*: Yes
*Type*: String
*Pattern*: `^[\s\S]*$`
*Minimum*: `1`
*Maximum*: `1000`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VirtualHost`  <a name="cfn-pipes-pipe-pipesourcerabbitmqbrokerparameters-virtualhost"></a>
The name of the virtual host associated with the source broker.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9-\/*:_+=.@-]*$`
*Minimum*: `1`
*Maximum*: `200`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
