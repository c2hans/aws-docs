---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-fcapolicy-cidrrangespecifications.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::FcaPolicy CidrRangeSpecifications

Maps CIDR ranges to labels for cost reporting. Specify this property when the reporting granularity is `cidr`.

## Syntax
<a name="aws-properties-ec2-fcapolicy-cidrrangespecifications-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-fcapolicy-cidrrangespecifications-syntax.json"></a>

```json
{
  "[Prefixes](#cfn-ec2-fcapolicy-cidrrangespecifications-prefixes)" : {{[ CidrMapping, ... ]}},
  "[PrefixesType](#cfn-ec2-fcapolicy-cidrrangespecifications-prefixestype)" : {{String}}
}
```

### YAML
<a name="aws-properties-ec2-fcapolicy-cidrrangespecifications-syntax.yaml"></a>

```yaml
  [Prefixes](#cfn-ec2-fcapolicy-cidrrangespecifications-prefixes): {{
    - CidrMapping}}
  [PrefixesType](#cfn-ec2-fcapolicy-cidrrangespecifications-prefixestype): {{String}}
```

## Properties
<a name="aws-properties-ec2-fcapolicy-cidrrangespecifications-properties"></a>

`Prefixes`  <a name="cfn-ec2-fcapolicy-cidrrangespecifications-prefixes"></a>
The CIDR range to label mappings.
You can specify from 1 to 100 mappings.
*Required*: Yes
*Type*: Array of [CidrMapping](aws-properties-ec2-fcapolicy-cidrmapping.md)
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PrefixesType`  <a name="cfn-ec2-fcapolicy-cidrrangespecifications-prefixestype"></a>
The type of prefixes that the mappings apply to.
Valid values: `source-prefixes` \| `destination-prefixes`
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
