---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kendra-index-serversideencryptionconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Kendra::Index ServerSideEncryptionConfiguration
<a name="aws-properties-kendra-index-serversideencryptionconfiguration"></a>

Provides the identifier of the AWS KMS customer master key (CMK) used to encrypt data indexed by Amazon Kendra. We suggest that you use a CMK from your account to help secure your index. Amazon Kendra doesn't support asymmetric CMKs.

## Syntax
<a name="aws-properties-kendra-index-serversideencryptionconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kendra-index-serversideencryptionconfiguration-syntax.json"></a>

```
{
  "[KmsKeyId](#cfn-kendra-index-serversideencryptionconfiguration-kmskeyid)" : {{String}}
}
```

### YAML
<a name="aws-properties-kendra-index-serversideencryptionconfiguration-syntax.yaml"></a>

```
  [KmsKeyId](#cfn-kendra-index-serversideencryptionconfiguration-kmskeyid): {{String}}
```

## Properties
<a name="aws-properties-kendra-index-serversideencryptionconfiguration-properties"></a>

`KmsKeyId`  <a name="cfn-kendra-index-serversideencryptionconfiguration-kmskeyid"></a>
The identifier of the AWS KMS key. Amazon Kendra doesn't support asymmetric keys.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
