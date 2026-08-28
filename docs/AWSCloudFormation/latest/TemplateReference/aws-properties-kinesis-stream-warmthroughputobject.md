---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kinesis-stream-warmthroughputobject.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Kinesis::Stream WarmThroughputObject
<a name="aws-properties-kinesis-stream-warmthroughputobject"></a>

Represents the warm throughput configuration on the stream. This is only present for On-Demand Kinesis Data Streams in accounts that have `MinimumThroughputBillingCommitment` enabled.

## Syntax
<a name="aws-properties-kinesis-stream-warmthroughputobject-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kinesis-stream-warmthroughputobject-syntax.json"></a>

```
{
  "[CurrentMiBps](#cfn-kinesis-stream-warmthroughputobject-currentmibps)" : {{Integer}},
  "[TargetMiBps](#cfn-kinesis-stream-warmthroughputobject-targetmibps)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-kinesis-stream-warmthroughputobject-syntax.yaml"></a>

```
  [CurrentMiBps](#cfn-kinesis-stream-warmthroughputobject-currentmibps): {{Integer}}
  [TargetMiBps](#cfn-kinesis-stream-warmthroughputobject-targetmibps): {{Integer}}
```

## Properties
<a name="aws-properties-kinesis-stream-warmthroughputobject-properties"></a>

`CurrentMiBps`  <a name="cfn-kinesis-stream-warmthroughputobject-currentmibps"></a>
The current warm throughput value on the stream. This is the write throughput in MiBps that the stream is currently scaled to handle.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetMiBps`  <a name="cfn-kinesis-stream-warmthroughputobject-targetmibps"></a>
The target warm throughput value on the stream. This indicates that the stream is currently scaling towards this target value.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
