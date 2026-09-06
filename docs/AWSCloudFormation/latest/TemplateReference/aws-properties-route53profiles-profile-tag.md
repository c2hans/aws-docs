---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-route53profiles-profile-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Route53Profiles::Profile Tag
<a name="aws-properties-route53profiles-profile-tag"></a>

 Tag for the Profile.

## Syntax
<a name="aws-properties-route53profiles-profile-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-route53profiles-profile-tag-syntax.json"></a>

```
{
  "[Key](#cfn-route53profiles-profile-tag-key)" : {{String}},
  "[Value](#cfn-route53profiles-profile-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-route53profiles-profile-tag-syntax.yaml"></a>

```
  [Key](#cfn-route53profiles-profile-tag-key): {{String}}
  [Value](#cfn-route53profiles-profile-tag-value): {{String}}
```

## Properties
<a name="aws-properties-route53profiles-profile-tag-properties"></a>

`Key`  <a name="cfn-route53profiles-profile-tag-key"></a>
 Key associated with the `Tag`.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-route53profiles-profile-tag-value"></a>
 Value for the Tag.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
