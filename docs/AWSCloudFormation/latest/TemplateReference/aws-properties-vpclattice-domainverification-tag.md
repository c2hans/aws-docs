---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-vpclattice-domainverification-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::VpcLattice::DomainVerification Tag
<a name="aws-properties-vpclattice-domainverification-tag"></a>

Specifies a tag for a domain verification.

## Syntax
<a name="aws-properties-vpclattice-domainverification-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-vpclattice-domainverification-tag-syntax.json"></a>

```
{
  "[Key](#cfn-vpclattice-domainverification-tag-key)" : {{String}},
  "[Value](#cfn-vpclattice-domainverification-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-vpclattice-domainverification-tag-syntax.yaml"></a>

```
  [Key](#cfn-vpclattice-domainverification-tag-key): {{String}}
  [Value](#cfn-vpclattice-domainverification-tag-value): {{String}}
```

## Properties
<a name="aws-properties-vpclattice-domainverification-tag-properties"></a>

`Key`  <a name="cfn-vpclattice-domainverification-tag-key"></a>
The tag key.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-vpclattice-domainverification-tag-value"></a>
The tag value.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
