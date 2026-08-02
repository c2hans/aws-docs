---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-route53-cidrcollection-location.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Route53::CidrCollection Location
<a name="aws-properties-route53-cidrcollection-location"></a>

Specifies the list of CIDR blocks for a CIDR location.

## Syntax
<a name="aws-properties-route53-cidrcollection-location-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-route53-cidrcollection-location-syntax.json"></a>

```
{
  "[CidrList](#cfn-route53-cidrcollection-location-cidrlist)" : {{[ String, ... ]}},
  "[LocationName](#cfn-route53-cidrcollection-location-locationname)" : {{String}}
}
```

### YAML
<a name="aws-properties-route53-cidrcollection-location-syntax.yaml"></a>

```
  [CidrList](#cfn-route53-cidrcollection-location-cidrlist): {{
    - String}}
  [LocationName](#cfn-route53-cidrcollection-location-locationname): {{String}}
```

## Properties
<a name="aws-properties-route53-cidrcollection-location-properties"></a>

`CidrList`  <a name="cfn-route53-cidrcollection-location-cidrlist"></a>
List of CIDR blocks.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LocationName`  <a name="cfn-route53-cidrcollection-location-locationname"></a>
The CIDR collection location name.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `16`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-route53-cidrcollection-location--seealso"></a>
+ [LocationSummary](https://docs.aws.amazon.com/Route53/latest/APIReference/API_LocationSummary.html) in the *Amazon Route 53 API Reference*
