---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-msk-replicator-firehose.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MSK::Replicator Firehose
<a name="aws-properties-msk-replicator-firehose"></a>

Firehose details for ReplicatorLogDelivery.

## Syntax
<a name="aws-properties-msk-replicator-firehose-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-msk-replicator-firehose-syntax.json"></a>

```
{
  "[DeliveryStream](#cfn-msk-replicator-firehose-deliverystream)" : {{String}},
  "[Enabled](#cfn-msk-replicator-firehose-enabled)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-msk-replicator-firehose-syntax.yaml"></a>

```
  [DeliveryStream](#cfn-msk-replicator-firehose-deliverystream): {{String}}
  [Enabled](#cfn-msk-replicator-firehose-enabled): {{Boolean}}
```

## Properties
<a name="aws-properties-msk-replicator-firehose-properties"></a>

`DeliveryStream`  <a name="cfn-msk-replicator-firehose-deliverystream"></a>
The Firehose delivery stream that is the destination for log delivery.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Enabled`  <a name="cfn-msk-replicator-firehose-enabled"></a>
Whether log delivery to Firehose is enabled.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
