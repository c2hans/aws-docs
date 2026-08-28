---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-msk-replicator-kafkaclusterclientauthentication.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MSK::Replicator KafkaClusterClientAuthentication
<a name="aws-properties-msk-replicator-kafkaclusterclientauthentication"></a>

Details of the client authentication used by the Apache Kafka cluster.

## Syntax
<a name="aws-properties-msk-replicator-kafkaclusterclientauthentication-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-msk-replicator-kafkaclusterclientauthentication-syntax.json"></a>

```
{
  "[MTLS](#cfn-msk-replicator-kafkaclusterclientauthentication-mtls)" : {{KafkaClusterMtlsAuthentication}},
  "[SaslOAuthBearer](#cfn-msk-replicator-kafkaclusterclientauthentication-sasloauthbearer)" : {{KafkaClusterSaslOAuthBearerAuthentication}},
  "[SaslScram](#cfn-msk-replicator-kafkaclusterclientauthentication-saslscram)" : {{KafkaClusterSaslScramAuthentication}}
}
```

### YAML
<a name="aws-properties-msk-replicator-kafkaclusterclientauthentication-syntax.yaml"></a>

```
  [MTLS](#cfn-msk-replicator-kafkaclusterclientauthentication-mtls): {{
    KafkaClusterMtlsAuthentication}}
  [SaslOAuthBearer](#cfn-msk-replicator-kafkaclusterclientauthentication-sasloauthbearer): {{
    KafkaClusterSaslOAuthBearerAuthentication}}
  [SaslScram](#cfn-msk-replicator-kafkaclusterclientauthentication-saslscram): {{
    KafkaClusterSaslScramAuthentication}}
```

## Properties
<a name="aws-properties-msk-replicator-kafkaclusterclientauthentication-properties"></a>

`MTLS`  <a name="cfn-msk-replicator-kafkaclusterclientauthentication-mtls"></a>
Property description not available.
*Required*: No
*Type*: [KafkaClusterMtlsAuthentication](aws-properties-msk-replicator-kafkaclustermtlsauthentication.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SaslOAuthBearer`  <a name="cfn-msk-replicator-kafkaclusterclientauthentication-sasloauthbearer"></a>
Property description not available.
*Required*: No
*Type*: [KafkaClusterSaslOAuthBearerAuthentication](aws-properties-msk-replicator-kafkaclustersasloauthbearerauthentication.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SaslScram`  <a name="cfn-msk-replicator-kafkaclusterclientauthentication-saslscram"></a>
Details for SASL/SCRAM client authentication.
*Required*: No
*Type*: [KafkaClusterSaslScramAuthentication](aws-properties-msk-replicator-kafkaclustersaslscramauthentication.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
