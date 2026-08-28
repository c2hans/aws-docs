---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-msk-replicator-kafkaclusteroauthiamjwtbearer.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MSK::Replicator KafkaClusterOAuthIamJwtBearer
<a name="aws-properties-msk-replicator-kafkaclusteroauthiamjwtbearer"></a>

<a name="aws-properties-msk-replicator-kafkaclusteroauthiamjwtbearer-description"></a>The `KafkaClusterOAuthIamJwtBearer` property type specifies Property description not available. for an [AWS::MSK::Replicator](aws-resource-msk-replicator.md).

## Syntax
<a name="aws-properties-msk-replicator-kafkaclusteroauthiamjwtbearer-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-msk-replicator-kafkaclusteroauthiamjwtbearer-syntax.json"></a>

```
{
  "[Audience](#cfn-msk-replicator-kafkaclusteroauthiamjwtbearer-audience)" : {{String}},
  "[SigningAlgorithm](#cfn-msk-replicator-kafkaclusteroauthiamjwtbearer-signingalgorithm)" : {{String}},
  "[TokenRequestSecretArn](#cfn-msk-replicator-kafkaclusteroauthiamjwtbearer-tokenrequestsecretarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-msk-replicator-kafkaclusteroauthiamjwtbearer-syntax.yaml"></a>

```
  [Audience](#cfn-msk-replicator-kafkaclusteroauthiamjwtbearer-audience): {{String}}
  [SigningAlgorithm](#cfn-msk-replicator-kafkaclusteroauthiamjwtbearer-signingalgorithm): {{String}}
  [TokenRequestSecretArn](#cfn-msk-replicator-kafkaclusteroauthiamjwtbearer-tokenrequestsecretarn): {{String}}
```

## Properties
<a name="aws-properties-msk-replicator-kafkaclusteroauthiamjwtbearer-properties"></a>

`Audience`  <a name="cfn-msk-replicator-kafkaclusteroauthiamjwtbearer-audience"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SigningAlgorithm`  <a name="cfn-msk-replicator-kafkaclusteroauthiamjwtbearer-signingalgorithm"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `RS256 | ES384`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TokenRequestSecretArn`  <a name="cfn-msk-replicator-kafkaclusteroauthiamjwtbearer-tokenrequestsecretarn"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
