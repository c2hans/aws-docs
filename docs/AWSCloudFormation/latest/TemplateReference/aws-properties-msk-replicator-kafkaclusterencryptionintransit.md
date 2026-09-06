---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-msk-replicator-kafkaclusterencryptionintransit.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MSK::Replicator KafkaClusterEncryptionInTransit
<a name="aws-properties-msk-replicator-kafkaclusterencryptionintransit"></a>

Details of encryption in transit to the Apache Kafka cluster.

## Syntax
<a name="aws-properties-msk-replicator-kafkaclusterencryptionintransit-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-msk-replicator-kafkaclusterencryptionintransit-syntax.json"></a>

```
{
  "[EncryptionType](#cfn-msk-replicator-kafkaclusterencryptionintransit-encryptiontype)" : {{String}},
  "[RootCaCertificate](#cfn-msk-replicator-kafkaclusterencryptionintransit-rootcacertificate)" : {{String}}
}
```

### YAML
<a name="aws-properties-msk-replicator-kafkaclusterencryptionintransit-syntax.yaml"></a>

```
  [EncryptionType](#cfn-msk-replicator-kafkaclusterencryptionintransit-encryptiontype): {{String}}
  [RootCaCertificate](#cfn-msk-replicator-kafkaclusterencryptionintransit-rootcacertificate): {{String}}
```

## Properties
<a name="aws-properties-msk-replicator-kafkaclusterencryptionintransit-properties"></a>

`EncryptionType`  <a name="cfn-msk-replicator-kafkaclusterencryptionintransit-encryptiontype"></a>
The type of encryption in transit to the Apache Kafka cluster.
*Required*: Yes
*Type*: String
*Allowed values*: `TLS`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RootCaCertificate`  <a name="cfn-msk-replicator-kafkaclusterencryptionintransit-rootcacertificate"></a>
Amazon Resource Name (ARN) of the Secrets Manager secret containing the root CA certificate for TLS encryption.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
