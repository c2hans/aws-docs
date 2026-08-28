---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-msk-cluster-brokerlogs.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MSK::Cluster BrokerLogs
<a name="aws-properties-msk-cluster-brokerlogs"></a>

The broker logs configuration for this MSK cluster.

## Syntax
<a name="aws-properties-msk-cluster-brokerlogs-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-msk-cluster-brokerlogs-syntax.json"></a>

```
{
  "[CloudWatchLogs](#cfn-msk-cluster-brokerlogs-cloudwatchlogs)" : {{CloudWatchLogs}},
  "[Firehose](#cfn-msk-cluster-brokerlogs-firehose)" : {{Firehose}},
  "[S3](#cfn-msk-cluster-brokerlogs-s3)" : {{S3}}
}
```

### YAML
<a name="aws-properties-msk-cluster-brokerlogs-syntax.yaml"></a>

```
  [CloudWatchLogs](#cfn-msk-cluster-brokerlogs-cloudwatchlogs): {{
    CloudWatchLogs}}
  [Firehose](#cfn-msk-cluster-brokerlogs-firehose): {{
    Firehose}}
  [S3](#cfn-msk-cluster-brokerlogs-s3): {{
    S3}}
```

## Properties
<a name="aws-properties-msk-cluster-brokerlogs-properties"></a>

`CloudWatchLogs`  <a name="cfn-msk-cluster-brokerlogs-cloudwatchlogs"></a>
Property description not available.
*Required*: No
*Type*: [CloudWatchLogs](aws-properties-msk-cluster-cloudwatchlogs.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Firehose`  <a name="cfn-msk-cluster-brokerlogs-firehose"></a>
Details of the Kinesis Data Firehose delivery stream that is the destination for broker logs.
*Required*: No
*Type*: [Firehose](aws-properties-msk-cluster-firehose.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3`  <a name="cfn-msk-cluster-brokerlogs-s3"></a>
Details of the Amazon S3 destination for broker logs.
*Required*: No
*Type*: [S3](aws-properties-msk-cluster-s3.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
