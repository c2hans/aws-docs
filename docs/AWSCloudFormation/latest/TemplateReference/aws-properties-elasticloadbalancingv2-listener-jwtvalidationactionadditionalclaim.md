---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-elasticloadbalancingv2-listener-jwtvalidationactionadditionalclaim.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ElasticLoadBalancingV2::Listener JwtValidationActionAdditionalClaim
<a name="aws-properties-elasticloadbalancingv2-listener-jwtvalidationactionadditionalclaim"></a>

Information about an additional claim to validate.

## Syntax
<a name="aws-properties-elasticloadbalancingv2-listener-jwtvalidationactionadditionalclaim-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-elasticloadbalancingv2-listener-jwtvalidationactionadditionalclaim-syntax.json"></a>

```
{
  "[Format](#cfn-elasticloadbalancingv2-listener-jwtvalidationactionadditionalclaim-format)" : {{String}},
  "[Name](#cfn-elasticloadbalancingv2-listener-jwtvalidationactionadditionalclaim-name)" : {{String}},
  "[Values](#cfn-elasticloadbalancingv2-listener-jwtvalidationactionadditionalclaim-values)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-elasticloadbalancingv2-listener-jwtvalidationactionadditionalclaim-syntax.yaml"></a>

```
  [Format](#cfn-elasticloadbalancingv2-listener-jwtvalidationactionadditionalclaim-format): {{String}}
  [Name](#cfn-elasticloadbalancingv2-listener-jwtvalidationactionadditionalclaim-name): {{String}}
  [Values](#cfn-elasticloadbalancingv2-listener-jwtvalidationactionadditionalclaim-values): {{
    - String}}
```

## Properties
<a name="aws-properties-elasticloadbalancingv2-listener-jwtvalidationactionadditionalclaim-properties"></a>

`Format`  <a name="cfn-elasticloadbalancingv2-listener-jwtvalidationactionadditionalclaim-format"></a>
The format of the claim value.
*Required*: Yes
*Type*: String
*Allowed values*: `single-string | string-array | space-separated-values`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-elasticloadbalancingv2-listener-jwtvalidationactionadditionalclaim-name"></a>
The name of the claim. You can't specify `exp`, `iss`, `nbf`, or `iat` because we validate them by default.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Values`  <a name="cfn-elasticloadbalancingv2-listener-jwtvalidationactionadditionalclaim-values"></a>
The claim value. The maximum size of the list is 10. Each value can be up to 256 characters in length. If the format is `space-separated-values`, the values can't include spaces.
*Required*: Yes
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
