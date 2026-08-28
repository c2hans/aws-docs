---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-athena-workgroup-customercontentencryptionconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Athena::WorkGroup CustomerContentEncryptionConfiguration
<a name="aws-properties-athena-workgroup-customercontentencryptionconfiguration"></a>

Specifies the customer managed KMS key that is used to encrypt the user's data stores in Athena. When an AWS managed key is used, this value is null. This setting does not apply to Athena SQL workgroups.

## Syntax
<a name="aws-properties-athena-workgroup-customercontentencryptionconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-athena-workgroup-customercontentencryptionconfiguration-syntax.json"></a>

```
{
  "[KmsKey](#cfn-athena-workgroup-customercontentencryptionconfiguration-kmskey)" : {{String}}
}
```

### YAML
<a name="aws-properties-athena-workgroup-customercontentencryptionconfiguration-syntax.yaml"></a>

```
  [KmsKey](#cfn-athena-workgroup-customercontentencryptionconfiguration-kmskey): {{String}}
```

## Properties
<a name="aws-properties-athena-workgroup-customercontentencryptionconfiguration-properties"></a>

`KmsKey`  <a name="cfn-athena-workgroup-customercontentencryptionconfiguration-kmskey"></a>
The customer managed KMS key that is used to encrypt the user's data stores in Athena.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws[a-z\-]*:kms:([a-z0-9\-]+):\d{12}:key/?[a-zA-Z_0-9+=,.@\-_/]+$|^arn:aws[a-z\-]*:kms:([a-z0-9\-]+):\d{12}:alias/?[a-zA-Z_0-9+=,.@\-_/]+$|^alias/[a-zA-Z0-9/_-]+$|[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
