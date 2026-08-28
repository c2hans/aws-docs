---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-dynamodb-globaltable-replicassespecification.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DynamoDB::GlobalTable ReplicaSSESpecification
<a name="aws-properties-dynamodb-globaltable-replicassespecification"></a>

Allows you to specify a KMS key identifier to be used for server-side encryption. The key can be specified via ARN, key ID, or alias. The key must be created in the same region as the replica.

## Syntax
<a name="aws-properties-dynamodb-globaltable-replicassespecification-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-dynamodb-globaltable-replicassespecification-syntax.json"></a>

```
{
  "[KMSMasterKeyId](#cfn-dynamodb-globaltable-replicassespecification-kmsmasterkeyid)" : {{String}}
}
```

### YAML
<a name="aws-properties-dynamodb-globaltable-replicassespecification-syntax.yaml"></a>

```
  [KMSMasterKeyId](#cfn-dynamodb-globaltable-replicassespecification-kmsmasterkeyid): {{String}}
```

## Properties
<a name="aws-properties-dynamodb-globaltable-replicassespecification-properties"></a>

`KMSMasterKeyId`  <a name="cfn-dynamodb-globaltable-replicassespecification-kmsmasterkeyid"></a>
The AWS KMS key that should be used for the AWS KMS encryption. To specify a key, use its key ID, Amazon Resource Name (ARN), alias name, or alias ARN. Note that you should only provide this parameter if the key is different from the default DynamoDB key `alias/aws/dynamodb`.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
