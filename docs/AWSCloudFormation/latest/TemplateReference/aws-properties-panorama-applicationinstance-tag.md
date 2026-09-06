---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-panorama-applicationinstance-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Panorama::ApplicationInstance Tag
<a name="aws-properties-panorama-applicationinstance-tag"></a>

<a name="aws-properties-panorama-applicationinstance-tag-description"></a>The `Tag` property type specifies Property description not available. for an [AWS::Panorama::ApplicationInstance](aws-resource-panorama-applicationinstance.md).

## Syntax
<a name="aws-properties-panorama-applicationinstance-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-panorama-applicationinstance-tag-syntax.json"></a>

```
{
  "[Key](#cfn-panorama-applicationinstance-tag-key)" : {{String}},
  "[Value](#cfn-panorama-applicationinstance-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-panorama-applicationinstance-tag-syntax.yaml"></a>

```
  [Key](#cfn-panorama-applicationinstance-tag-key): {{String}}
  [Value](#cfn-panorama-applicationinstance-tag-value): {{String}}
```

## Properties
<a name="aws-properties-panorama-applicationinstance-tag-properties"></a>

`Key`  <a name="cfn-panorama-applicationinstance-tag-key"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^.+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-panorama-applicationinstance-tag-value"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^.+$`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
