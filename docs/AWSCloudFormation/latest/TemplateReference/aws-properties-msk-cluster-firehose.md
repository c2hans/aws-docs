---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-msk-cluster-firehose.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MSK::Cluster Firehose
<a name="aws-properties-msk-cluster-firehose"></a>

Firehose details for BrokerLogs.

## Syntax
<a name="aws-properties-msk-cluster-firehose-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-msk-cluster-firehose-syntax.json"></a>

```
{
  "[DeliveryStream](#cfn-msk-cluster-firehose-deliverystream)" : {{String}},
  "[Enabled](#cfn-msk-cluster-firehose-enabled)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-msk-cluster-firehose-syntax.yaml"></a>

```
  [DeliveryStream](#cfn-msk-cluster-firehose-deliverystream): {{String}}
  [Enabled](#cfn-msk-cluster-firehose-enabled): {{Boolean}}
```

## Properties
<a name="aws-properties-msk-cluster-firehose-properties"></a>

`DeliveryStream`  <a name="cfn-msk-cluster-firehose-deliverystream"></a>
The Kinesis Data Firehose delivery stream that is the destination for broker logs.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Enabled`  <a name="cfn-msk-cluster-firehose-enabled"></a>
Specifies whether broker logs get send to the specified Kinesis Data Firehose delivery stream.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
