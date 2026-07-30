---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-codeartifact-domain-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CodeArtifact::Domain Tag
<a name="aws-properties-codeartifact-domain-tag"></a>

A tag is a key-value pair that can be used to manage, search for, or filter resources in AWS CodeArtifact.

## Syntax
<a name="aws-properties-codeartifact-domain-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-codeartifact-domain-tag-syntax.json"></a>

```
{
  "[Key](#cfn-codeartifact-domain-tag-key)" : {{String}},
  "[Value](#cfn-codeartifact-domain-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-codeartifact-domain-tag-syntax.yaml"></a>

```
  [Key](#cfn-codeartifact-domain-tag-key): {{String}}
  [Value](#cfn-codeartifact-domain-tag-value): {{String}}
```

## Properties
<a name="aws-properties-codeartifact-domain-tag-properties"></a>

`Key`  <a name="cfn-codeartifact-domain-tag-key"></a>
The tag key.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-codeartifact-domain-tag-value"></a>
The tag value.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
