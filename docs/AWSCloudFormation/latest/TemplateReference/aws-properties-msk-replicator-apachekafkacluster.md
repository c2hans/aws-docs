---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-msk-replicator-apachekafkacluster.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MSK::Replicator ApacheKafkaCluster
<a name="aws-properties-msk-replicator-apachekafkacluster"></a>

Details of an Apache Kafka cluster.

## Syntax
<a name="aws-properties-msk-replicator-apachekafkacluster-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-msk-replicator-apachekafkacluster-syntax.json"></a>

```
{
  "[ApacheKafkaClusterId](#cfn-msk-replicator-apachekafkacluster-apachekafkaclusterid)" : {{String}},
  "[BootstrapBrokerString](#cfn-msk-replicator-apachekafkacluster-bootstrapbrokerstring)" : {{String}}
}
```

### YAML
<a name="aws-properties-msk-replicator-apachekafkacluster-syntax.yaml"></a>

```
  [ApacheKafkaClusterId](#cfn-msk-replicator-apachekafkacluster-apachekafkaclusterid): {{String}}
  [BootstrapBrokerString](#cfn-msk-replicator-apachekafkacluster-bootstrapbrokerstring): {{
    String}}
```

## Properties
<a name="aws-properties-msk-replicator-apachekafkacluster-properties"></a>

`ApacheKafkaClusterId`  <a name="cfn-msk-replicator-apachekafkacluster-apachekafkaclusterid"></a>
The globally unique cluster ID of the Apache Kafka cluster. For information on how to retrieve the cluster ID, see https://github.com/apache/kafka/blob/trunk/bin/kafka-cluster.sh
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`BootstrapBrokerString`  <a name="cfn-msk-replicator-apachekafkacluster-bootstrapbrokerstring"></a>
The bootstrap broker string of the Apache Kafka cluster.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
