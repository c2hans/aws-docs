---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kafkaconnect-connector-logdelivery.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KafkaConnect::Connector LogDelivery
<a name="aws-properties-kafkaconnect-connector-logdelivery"></a>

Details about log delivery.

## Syntax
<a name="aws-properties-kafkaconnect-connector-logdelivery-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kafkaconnect-connector-logdelivery-syntax.json"></a>

```
{
  "[WorkerLogDelivery](#cfn-kafkaconnect-connector-logdelivery-workerlogdelivery)" : {{WorkerLogDelivery}}
}
```

### YAML
<a name="aws-properties-kafkaconnect-connector-logdelivery-syntax.yaml"></a>

```
  [WorkerLogDelivery](#cfn-kafkaconnect-connector-logdelivery-workerlogdelivery): {{
    WorkerLogDelivery}}
```

## Properties
<a name="aws-properties-kafkaconnect-connector-logdelivery-properties"></a>

`WorkerLogDelivery`  <a name="cfn-kafkaconnect-connector-logdelivery-workerlogdelivery"></a>
The workers can send worker logs to different destination types. This configuration specifies the details of these destinations.
*Required*: Yes
*Type*: [WorkerLogDelivery](aws-properties-kafkaconnect-connector-workerlogdelivery.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
