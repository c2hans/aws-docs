---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-msk-replicator-kafkaclustersaslscramauthentication.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MSK::Replicator KafkaClusterSaslScramAuthentication
<a name="aws-properties-msk-replicator-kafkaclustersaslscramauthentication"></a>

Details for SASL/SCRAM client authentication.

## Syntax
<a name="aws-properties-msk-replicator-kafkaclustersaslscramauthentication-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-msk-replicator-kafkaclustersaslscramauthentication-syntax.json"></a>

```
{
  "[Mechanism](#cfn-msk-replicator-kafkaclustersaslscramauthentication-mechanism)" : {{String}},
  "[SecretArn](#cfn-msk-replicator-kafkaclustersaslscramauthentication-secretarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-msk-replicator-kafkaclustersaslscramauthentication-syntax.yaml"></a>

```
  [Mechanism](#cfn-msk-replicator-kafkaclustersaslscramauthentication-mechanism): {{String}}
  [SecretArn](#cfn-msk-replicator-kafkaclustersaslscramauthentication-secretarn): {{String}}
```

## Properties
<a name="aws-properties-msk-replicator-kafkaclustersaslscramauthentication-properties"></a>

`Mechanism`  <a name="cfn-msk-replicator-kafkaclustersaslscramauthentication-mechanism"></a>
The SCRAM mechanism to use for authentication.
*Required*: Yes
*Type*: String
*Allowed values*: `SHA256 | SHA512`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SecretArn`  <a name="cfn-msk-replicator-kafkaclustersaslscramauthentication-secretarn"></a>
Amazon Resource Name (ARN) of the Secrets Manager secret containing the username and password.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
