---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-signer-signingprofile-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Signer::SigningProfile Tag
<a name="aws-properties-signer-signingprofile-tag"></a>

<a name="aws-properties-signer-signingprofile-tag-description"></a>The `Tag` property type specifies Property description not available. for an [AWS::Signer::SigningProfile](aws-resource-signer-signingprofile.md).

## Syntax
<a name="aws-properties-signer-signingprofile-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-signer-signingprofile-tag-syntax.json"></a>

```
{
  "[Key](#cfn-signer-signingprofile-tag-key)" : {{String}},
  "[Value](#cfn-signer-signingprofile-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-signer-signingprofile-tag-syntax.yaml"></a>

```
  [Key](#cfn-signer-signingprofile-tag-key): {{String}}
  [Value](#cfn-signer-signingprofile-tag-value): {{String}}
```

## Properties
<a name="aws-properties-signer-signingprofile-tag-properties"></a>

`Key`  <a name="cfn-signer-signingprofile-tag-key"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^(?!aws:)[a-zA-Z+-=._:/]+$`
*Minimum*: `1`
*Maximum*: `127`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-signer-signingprofile-tag-value"></a>
Property description not available.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
