---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-fcapolicy-cidrmapping.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::FcaPolicy CidrMapping
<a name="aws-properties-ec2-fcapolicy-cidrmapping"></a>

<a name="aws-properties-ec2-fcapolicy-cidrmapping-description"></a>The `CidrMapping` property type specifies Property description not available. for an [AWS::EC2::FcaPolicy](aws-resource-ec2-fcapolicy.md).

## Syntax
<a name="aws-properties-ec2-fcapolicy-cidrmapping-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-fcapolicy-cidrmapping-syntax.json"></a>

```
{
  "[CidrLabel](#cfn-ec2-fcapolicy-cidrmapping-cidrlabel)" : {{String}},
  "[CidrRange](#cfn-ec2-fcapolicy-cidrmapping-cidrrange)" : {{String}}
}
```

### YAML
<a name="aws-properties-ec2-fcapolicy-cidrmapping-syntax.yaml"></a>

```
  [CidrLabel](#cfn-ec2-fcapolicy-cidrmapping-cidrlabel): {{String}}
  [CidrRange](#cfn-ec2-fcapolicy-cidrmapping-cidrrange): {{String}}
```

## Properties
<a name="aws-properties-ec2-fcapolicy-cidrmapping-properties"></a>

`CidrLabel`  <a name="cfn-ec2-fcapolicy-cidrmapping-cidrlabel"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9][a-zA-Z0-9_\-]{0,63}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CidrRange`  <a name="cfn-ec2-fcapolicy-cidrmapping-cidrrange"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `43`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
