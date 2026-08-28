---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-elasticache-replicationgroup-logdeliveryconfigurationrequest.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ElastiCache::ReplicationGroup LogDeliveryConfigurationRequest
<a name="aws-properties-elasticache-replicationgroup-logdeliveryconfigurationrequest"></a>

Specifies the destination, format and type of the logs.

## Syntax
<a name="aws-properties-elasticache-replicationgroup-logdeliveryconfigurationrequest-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-elasticache-replicationgroup-logdeliveryconfigurationrequest-syntax.json"></a>

```
{
  "[DestinationDetails](#cfn-elasticache-replicationgroup-logdeliveryconfigurationrequest-destinationdetails)" : {{DestinationDetails}},
  "[DestinationType](#cfn-elasticache-replicationgroup-logdeliveryconfigurationrequest-destinationtype)" : {{String}},
  "[LogFormat](#cfn-elasticache-replicationgroup-logdeliveryconfigurationrequest-logformat)" : {{String}},
  "[LogType](#cfn-elasticache-replicationgroup-logdeliveryconfigurationrequest-logtype)" : {{String}}
}
```

### YAML
<a name="aws-properties-elasticache-replicationgroup-logdeliveryconfigurationrequest-syntax.yaml"></a>

```
  [DestinationDetails](#cfn-elasticache-replicationgroup-logdeliveryconfigurationrequest-destinationdetails): {{
    DestinationDetails}}
  [DestinationType](#cfn-elasticache-replicationgroup-logdeliveryconfigurationrequest-destinationtype): {{String}}
  [LogFormat](#cfn-elasticache-replicationgroup-logdeliveryconfigurationrequest-logformat): {{String}}
  [LogType](#cfn-elasticache-replicationgroup-logdeliveryconfigurationrequest-logtype): {{String}}
```

## Properties
<a name="aws-properties-elasticache-replicationgroup-logdeliveryconfigurationrequest-properties"></a>

`DestinationDetails`  <a name="cfn-elasticache-replicationgroup-logdeliveryconfigurationrequest-destinationdetails"></a>
Configuration details of either a CloudWatch Logs destination or Kinesis Data Firehose destination.
*Required*: Yes
*Type*: [DestinationDetails](aws-properties-elasticache-replicationgroup-destinationdetails.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DestinationType`  <a name="cfn-elasticache-replicationgroup-logdeliveryconfigurationrequest-destinationtype"></a>
Specify either CloudWatch Logs or Kinesis Data Firehose as the destination type. Valid values are either `cloudwatch-logs` or `kinesis-firehose`.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LogFormat`  <a name="cfn-elasticache-replicationgroup-logdeliveryconfigurationrequest-logformat"></a>
Valid values are either `json` or `text`.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LogType`  <a name="cfn-elasticache-replicationgroup-logdeliveryconfigurationrequest-logtype"></a>
Valid value is either `slow-log`, which refers to [slow-log](https://redis.io/commands/slowlog) or `engine-log`.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
