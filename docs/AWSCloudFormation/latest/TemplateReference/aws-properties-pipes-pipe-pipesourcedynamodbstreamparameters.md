---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-pipes-pipe-pipesourcedynamodbstreamparameters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Pipes::Pipe PipeSourceDynamoDBStreamParameters
<a name="aws-properties-pipes-pipe-pipesourcedynamodbstreamparameters"></a>

The parameters for using a DynamoDB stream as a source.

## Syntax
<a name="aws-properties-pipes-pipe-pipesourcedynamodbstreamparameters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-pipes-pipe-pipesourcedynamodbstreamparameters-syntax.json"></a>

```
{
  "[BatchSize](#cfn-pipes-pipe-pipesourcedynamodbstreamparameters-batchsize)" : {{Integer}},
  "[DeadLetterConfig](#cfn-pipes-pipe-pipesourcedynamodbstreamparameters-deadletterconfig)" : {{DeadLetterConfig}},
  "[MaximumBatchingWindowInSeconds](#cfn-pipes-pipe-pipesourcedynamodbstreamparameters-maximumbatchingwindowinseconds)" : {{Integer}},
  "[MaximumRecordAgeInSeconds](#cfn-pipes-pipe-pipesourcedynamodbstreamparameters-maximumrecordageinseconds)" : {{Integer}},
  "[MaximumRetryAttempts](#cfn-pipes-pipe-pipesourcedynamodbstreamparameters-maximumretryattempts)" : {{Integer}},
  "[OnPartialBatchItemFailure](#cfn-pipes-pipe-pipesourcedynamodbstreamparameters-onpartialbatchitemfailure)" : {{String}},
  "[ParallelizationFactor](#cfn-pipes-pipe-pipesourcedynamodbstreamparameters-parallelizationfactor)" : {{Integer}},
  "[StartingPosition](#cfn-pipes-pipe-pipesourcedynamodbstreamparameters-startingposition)" : {{String}}
}
```

### YAML
<a name="aws-properties-pipes-pipe-pipesourcedynamodbstreamparameters-syntax.yaml"></a>

```
  [BatchSize](#cfn-pipes-pipe-pipesourcedynamodbstreamparameters-batchsize): {{Integer}}
  [DeadLetterConfig](#cfn-pipes-pipe-pipesourcedynamodbstreamparameters-deadletterconfig): {{
    DeadLetterConfig}}
  [MaximumBatchingWindowInSeconds](#cfn-pipes-pipe-pipesourcedynamodbstreamparameters-maximumbatchingwindowinseconds): {{Integer}}
  [MaximumRecordAgeInSeconds](#cfn-pipes-pipe-pipesourcedynamodbstreamparameters-maximumrecordageinseconds): {{Integer}}
  [MaximumRetryAttempts](#cfn-pipes-pipe-pipesourcedynamodbstreamparameters-maximumretryattempts): {{Integer}}
  [OnPartialBatchItemFailure](#cfn-pipes-pipe-pipesourcedynamodbstreamparameters-onpartialbatchitemfailure): {{String}}
  [ParallelizationFactor](#cfn-pipes-pipe-pipesourcedynamodbstreamparameters-parallelizationfactor): {{Integer}}
  [StartingPosition](#cfn-pipes-pipe-pipesourcedynamodbstreamparameters-startingposition): {{String}}
```

## Properties
<a name="aws-properties-pipes-pipe-pipesourcedynamodbstreamparameters-properties"></a>

`BatchSize`  <a name="cfn-pipes-pipe-pipesourcedynamodbstreamparameters-batchsize"></a>
The maximum number of records to include in each batch.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `10000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DeadLetterConfig`  <a name="cfn-pipes-pipe-pipesourcedynamodbstreamparameters-deadletterconfig"></a>
Define the target queue to send dead-letter queue events to.
*Required*: No
*Type*: [DeadLetterConfig](aws-properties-pipes-pipe-deadletterconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaximumBatchingWindowInSeconds`  <a name="cfn-pipes-pipe-pipesourcedynamodbstreamparameters-maximumbatchingwindowinseconds"></a>
The maximum length of a time to wait for events.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `300`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaximumRecordAgeInSeconds`  <a name="cfn-pipes-pipe-pipesourcedynamodbstreamparameters-maximumrecordageinseconds"></a>
Discard records older than the specified age. The default value is -1, which sets the maximum age to infinite. When the value is set to infinite, EventBridge never discards old records.
*Required*: No
*Type*: Integer
*Minimum*: `-1`
*Maximum*: `604800`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaximumRetryAttempts`  <a name="cfn-pipes-pipe-pipesourcedynamodbstreamparameters-maximumretryattempts"></a>
Discard records after the specified number of retries. The default value is -1, which sets the maximum number of retries to infinite. When MaximumRetryAttempts is infinite, EventBridge retries failed records until the record expires in the event source.
*Required*: No
*Type*: Integer
*Minimum*: `-1`
*Maximum*: `10000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OnPartialBatchItemFailure`  <a name="cfn-pipes-pipe-pipesourcedynamodbstreamparameters-onpartialbatchitemfailure"></a>
Define how to handle item process failures. `AUTOMATIC_BISECT` halves each batch and retry each half until all the records are processed or there is one failed message left in the batch.
*Required*: No
*Type*: String
*Allowed values*: `AUTOMATIC_BISECT`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ParallelizationFactor`  <a name="cfn-pipes-pipe-pipesourcedynamodbstreamparameters-parallelizationfactor"></a>
The number of batches to process concurrently from each shard. The default value is 1.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StartingPosition`  <a name="cfn-pipes-pipe-pipesourcedynamodbstreamparameters-startingposition"></a>
(Streams only) The position in a stream from which to start reading.
*Valid values*: `TRIM_HORIZON | LATEST`
*Required*: Yes
*Type*: String
*Allowed values*: `TRIM_HORIZON | LATEST`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
