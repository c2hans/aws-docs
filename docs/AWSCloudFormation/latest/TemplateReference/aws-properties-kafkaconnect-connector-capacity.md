---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kafkaconnect-connector-capacity.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KafkaConnect::Connector Capacity
<a name="aws-properties-kafkaconnect-connector-capacity"></a>

Information about the capacity of the connector, whether it is auto scaled or provisioned.

## Syntax
<a name="aws-properties-kafkaconnect-connector-capacity-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kafkaconnect-connector-capacity-syntax.json"></a>

```
{
  "[AutoScaling](#cfn-kafkaconnect-connector-capacity-autoscaling)" : {{AutoScaling}},
  "[ProvisionedCapacity](#cfn-kafkaconnect-connector-capacity-provisionedcapacity)" : {{ProvisionedCapacity}}
}
```

### YAML
<a name="aws-properties-kafkaconnect-connector-capacity-syntax.yaml"></a>

```
  [AutoScaling](#cfn-kafkaconnect-connector-capacity-autoscaling): {{
    AutoScaling}}
  [ProvisionedCapacity](#cfn-kafkaconnect-connector-capacity-provisionedcapacity): {{
    ProvisionedCapacity}}
```

## Properties
<a name="aws-properties-kafkaconnect-connector-capacity-properties"></a>

`AutoScaling`  <a name="cfn-kafkaconnect-connector-capacity-autoscaling"></a>
Information about the auto scaling parameters for the connector.
*Required*: No
*Type*: [AutoScaling](aws-properties-kafkaconnect-connector-autoscaling.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProvisionedCapacity`  <a name="cfn-kafkaconnect-connector-capacity-provisionedcapacity"></a>
Details about a fixed capacity allocated to a connector.
*Required*: No
*Type*: [ProvisionedCapacity](aws-properties-kafkaconnect-connector-provisionedcapacity.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
