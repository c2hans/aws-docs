---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-msk-replicator-kafkacluster.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MSK::Replicator KafkaCluster
<a name="aws-properties-msk-replicator-kafkacluster"></a>

Information about Kafka Cluster to be used as source / target for replication.

## Syntax
<a name="aws-properties-msk-replicator-kafkacluster-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-msk-replicator-kafkacluster-syntax.json"></a>

```
{
  "[AmazonMskCluster](#cfn-msk-replicator-kafkacluster-amazonmskcluster)" : {{AmazonMskCluster}},
  "[ApacheKafkaCluster](#cfn-msk-replicator-kafkacluster-apachekafkacluster)" : {{ApacheKafkaCluster}},
  "[ClientAuthentication](#cfn-msk-replicator-kafkacluster-clientauthentication)" : {{KafkaClusterClientAuthentication}},
  "[EncryptionInTransit](#cfn-msk-replicator-kafkacluster-encryptionintransit)" : {{KafkaClusterEncryptionInTransit}},
  "[VpcConfig](#cfn-msk-replicator-kafkacluster-vpcconfig)" : {{KafkaClusterClientVpcConfig}}
}
```

### YAML
<a name="aws-properties-msk-replicator-kafkacluster-syntax.yaml"></a>

```
  [AmazonMskCluster](#cfn-msk-replicator-kafkacluster-amazonmskcluster): {{
    AmazonMskCluster}}
  [ApacheKafkaCluster](#cfn-msk-replicator-kafkacluster-apachekafkacluster): {{
    ApacheKafkaCluster}}
  [ClientAuthentication](#cfn-msk-replicator-kafkacluster-clientauthentication): {{
    KafkaClusterClientAuthentication}}
  [EncryptionInTransit](#cfn-msk-replicator-kafkacluster-encryptionintransit): {{
    KafkaClusterEncryptionInTransit}}
  [VpcConfig](#cfn-msk-replicator-kafkacluster-vpcconfig): {{
    KafkaClusterClientVpcConfig}}
```

## Properties
<a name="aws-properties-msk-replicator-kafkacluster-properties"></a>

`AmazonMskCluster`  <a name="cfn-msk-replicator-kafkacluster-amazonmskcluster"></a>
Details of an Amazon MSK Cluster.
*Required*: No
*Type*: [AmazonMskCluster](aws-properties-msk-replicator-amazonmskcluster.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ApacheKafkaCluster`  <a name="cfn-msk-replicator-kafkacluster-apachekafkacluster"></a>
Details of an Apache Kafka cluster. Exactly one of amazonMskCluster and apacheKafkaCluster is required.
*Required*: No
*Type*: [ApacheKafkaCluster](aws-properties-msk-replicator-apachekafkacluster.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ClientAuthentication`  <a name="cfn-msk-replicator-kafkacluster-clientauthentication"></a>
Details of the client authentication used by the Apache Kafka cluster.
*Required*: No
*Type*: [KafkaClusterClientAuthentication](aws-properties-msk-replicator-kafkaclusterclientauthentication.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EncryptionInTransit`  <a name="cfn-msk-replicator-kafkacluster-encryptionintransit"></a>
Details of encryption in transit to the Apache Kafka cluster.
*Required*: No
*Type*: [KafkaClusterEncryptionInTransit](aws-properties-msk-replicator-kafkaclusterencryptionintransit.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VpcConfig`  <a name="cfn-msk-replicator-kafkacluster-vpcconfig"></a>
Details of an Amazon VPC which has network connectivity to the Apache Kafka cluster.
*Required*: No
*Type*: [KafkaClusterClientVpcConfig](aws-properties-msk-replicator-kafkaclusterclientvpcconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
