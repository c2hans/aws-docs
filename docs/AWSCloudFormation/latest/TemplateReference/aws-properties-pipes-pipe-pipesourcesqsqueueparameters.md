---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-pipes-pipe-pipesourcesqsqueueparameters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Pipes::Pipe PipeSourceSqsQueueParameters
<a name="aws-properties-pipes-pipe-pipesourcesqsqueueparameters"></a>

The parameters for using a Amazon SQS stream as a source.

## Syntax
<a name="aws-properties-pipes-pipe-pipesourcesqsqueueparameters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-pipes-pipe-pipesourcesqsqueueparameters-syntax.json"></a>

```
{
  "[BatchSize](#cfn-pipes-pipe-pipesourcesqsqueueparameters-batchsize)" : {{Integer}},
  "[MaximumBatchingWindowInSeconds](#cfn-pipes-pipe-pipesourcesqsqueueparameters-maximumbatchingwindowinseconds)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-pipes-pipe-pipesourcesqsqueueparameters-syntax.yaml"></a>

```
  [BatchSize](#cfn-pipes-pipe-pipesourcesqsqueueparameters-batchsize): {{Integer}}
  [MaximumBatchingWindowInSeconds](#cfn-pipes-pipe-pipesourcesqsqueueparameters-maximumbatchingwindowinseconds): {{Integer}}
```

## Properties
<a name="aws-properties-pipes-pipe-pipesourcesqsqueueparameters-properties"></a>

`BatchSize`  <a name="cfn-pipes-pipe-pipesourcesqsqueueparameters-batchsize"></a>
The maximum number of records to include in each batch.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `10000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaximumBatchingWindowInSeconds`  <a name="cfn-pipes-pipe-pipesourcesqsqueueparameters-maximumbatchingwindowinseconds"></a>
The maximum length of a time to wait for events.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `300`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
