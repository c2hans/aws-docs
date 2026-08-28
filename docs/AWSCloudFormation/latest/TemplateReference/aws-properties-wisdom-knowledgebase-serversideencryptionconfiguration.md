---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wisdom-knowledgebase-serversideencryptionconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Wisdom::KnowledgeBase ServerSideEncryptionConfiguration
<a name="aws-properties-wisdom-knowledgebase-serversideencryptionconfiguration"></a>

The configuration information for the customer managed key used for encryption.

## Syntax
<a name="aws-properties-wisdom-knowledgebase-serversideencryptionconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wisdom-knowledgebase-serversideencryptionconfiguration-syntax.json"></a>

```
{
  "[KmsKeyId](#cfn-wisdom-knowledgebase-serversideencryptionconfiguration-kmskeyid)" : {{String}}
}
```

### YAML
<a name="aws-properties-wisdom-knowledgebase-serversideencryptionconfiguration-syntax.yaml"></a>

```
  [KmsKeyId](#cfn-wisdom-knowledgebase-serversideencryptionconfiguration-kmskeyid): {{String}}
```

## Properties
<a name="aws-properties-wisdom-knowledgebase-serversideencryptionconfiguration-properties"></a>

`KmsKeyId`  <a name="cfn-wisdom-knowledgebase-serversideencryptionconfiguration-kmskeyid"></a>
The customer managed key used for encryption.
This customer managed key must have a policy that allows `kms:CreateGrant` and ` kms:DescribeKey` permissions to the IAM identity using the key to invoke Wisdom.
For more information about setting up a customer managed key for Wisdom, see [Enable Connect Customer Wisdom for your instance](https://docs.aws.amazon.com/connect/latest/adminguide/enable-wisdom.html). For information about valid ID values, see [Key identifiers (KeyId)](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id).
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `4096`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
