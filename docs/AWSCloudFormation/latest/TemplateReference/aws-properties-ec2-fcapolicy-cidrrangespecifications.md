---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-fcapolicy-cidrrangespecifications.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::FcaPolicy CidrRangeSpecifications
<a name="aws-properties-ec2-fcapolicy-cidrrangespecifications"></a>

<a name="aws-properties-ec2-fcapolicy-cidrrangespecifications-description"></a>The `CidrRangeSpecifications` property type specifies Property description not available. for an [AWS::EC2::FcaPolicy](aws-resource-ec2-fcapolicy.md).

## Syntax
<a name="aws-properties-ec2-fcapolicy-cidrrangespecifications-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-fcapolicy-cidrrangespecifications-syntax.json"></a>

```
{
  "[Prefixes](#cfn-ec2-fcapolicy-cidrrangespecifications-prefixes)" : {{[ CidrMapping, ... ]}},
  "[PrefixesType](#cfn-ec2-fcapolicy-cidrrangespecifications-prefixestype)" : {{String}}
}
```

### YAML
<a name="aws-properties-ec2-fcapolicy-cidrrangespecifications-syntax.yaml"></a>

```
  [Prefixes](#cfn-ec2-fcapolicy-cidrrangespecifications-prefixes): {{
    - CidrMapping}}
  [PrefixesType](#cfn-ec2-fcapolicy-cidrrangespecifications-prefixestype): {{String}}
```

## Properties
<a name="aws-properties-ec2-fcapolicy-cidrrangespecifications-properties"></a>

`Prefixes`  <a name="cfn-ec2-fcapolicy-cidrrangespecifications-prefixes"></a>
Property description not available.
*Required*: Yes
*Type*: Array of [CidrMapping](aws-properties-ec2-fcapolicy-cidrmapping.md)
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PrefixesType`  <a name="cfn-ec2-fcapolicy-cidrrangespecifications-prefixestype"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
