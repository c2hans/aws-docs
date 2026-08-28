---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kafkaconnect-connector-kafkaclusterencryptionintransit.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KafkaConnect::Connector KafkaClusterEncryptionInTransit
<a name="aws-properties-kafkaconnect-connector-kafkaclusterencryptionintransit"></a>

Details of encryption in transit to the Apache Kafka cluster.

## Syntax
<a name="aws-properties-kafkaconnect-connector-kafkaclusterencryptionintransit-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kafkaconnect-connector-kafkaclusterencryptionintransit-syntax.json"></a>

```
{
  "[EncryptionType](#cfn-kafkaconnect-connector-kafkaclusterencryptionintransit-encryptiontype)" : {{String}}
}
```

### YAML
<a name="aws-properties-kafkaconnect-connector-kafkaclusterencryptionintransit-syntax.yaml"></a>

```
  [EncryptionType](#cfn-kafkaconnect-connector-kafkaclusterencryptionintransit-encryptiontype): {{String}}
```

## Properties
<a name="aws-properties-kafkaconnect-connector-kafkaclusterencryptionintransit-properties"></a>

`EncryptionType`  <a name="cfn-kafkaconnect-connector-kafkaclusterencryptionintransit-encryptiontype"></a>
The type of encryption in transit to the Apache Kafka cluster.
*Required*: Yes
*Type*: String
*Allowed values*: `PLAINTEXT | TLS`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
