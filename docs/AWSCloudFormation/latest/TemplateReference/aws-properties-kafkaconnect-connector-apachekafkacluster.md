---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kafkaconnect-connector-apachekafkacluster.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KafkaConnect::Connector ApacheKafkaCluster
<a name="aws-properties-kafkaconnect-connector-apachekafkacluster"></a>

The details of the Apache Kafka cluster to which the connector is connected.

## Syntax
<a name="aws-properties-kafkaconnect-connector-apachekafkacluster-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kafkaconnect-connector-apachekafkacluster-syntax.json"></a>

```
{
  "[BootstrapServers](#cfn-kafkaconnect-connector-apachekafkacluster-bootstrapservers)" : {{String}},
  "[Vpc](#cfn-kafkaconnect-connector-apachekafkacluster-vpc)" : {{Vpc}}
}
```

### YAML
<a name="aws-properties-kafkaconnect-connector-apachekafkacluster-syntax.yaml"></a>

```
  [BootstrapServers](#cfn-kafkaconnect-connector-apachekafkacluster-bootstrapservers): {{String}}
  [Vpc](#cfn-kafkaconnect-connector-apachekafkacluster-vpc): {{
    Vpc}}
```

## Properties
<a name="aws-properties-kafkaconnect-connector-apachekafkacluster-properties"></a>

`BootstrapServers`  <a name="cfn-kafkaconnect-connector-apachekafkacluster-bootstrapservers"></a>
The bootstrap servers of the cluster.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Vpc`  <a name="cfn-kafkaconnect-connector-apachekafkacluster-vpc"></a>
Details of an Amazon VPC which has network connectivity to the Apache Kafka cluster.
*Required*: Yes
*Type*: [Vpc](aws-properties-kafkaconnect-connector-vpc.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
