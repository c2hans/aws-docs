---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-elasticloadbalancingv2-listenerrule-jwtvalidationconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ElasticLoadBalancingV2::ListenerRule JwtValidationConfig
<a name="aws-properties-elasticloadbalancingv2-listenerrule-jwtvalidationconfig"></a>

<a name="aws-properties-elasticloadbalancingv2-listenerrule-jwtvalidationconfig-description"></a>The `JwtValidationConfig` property type specifies Property description not available. for an [AWS::ElasticLoadBalancingV2::ListenerRule](aws-resource-elasticloadbalancingv2-listenerrule.md).

## Syntax
<a name="aws-properties-elasticloadbalancingv2-listenerrule-jwtvalidationconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-elasticloadbalancingv2-listenerrule-jwtvalidationconfig-syntax.json"></a>

```
{
  "[AdditionalClaims](#cfn-elasticloadbalancingv2-listenerrule-jwtvalidationconfig-additionalclaims)" : {{[ JwtValidationActionAdditionalClaim, ... ]}},
  "[Issuer](#cfn-elasticloadbalancingv2-listenerrule-jwtvalidationconfig-issuer)" : {{String}},
  "[JwksEndpoint](#cfn-elasticloadbalancingv2-listenerrule-jwtvalidationconfig-jwksendpoint)" : {{String}}
}
```

### YAML
<a name="aws-properties-elasticloadbalancingv2-listenerrule-jwtvalidationconfig-syntax.yaml"></a>

```
  [AdditionalClaims](#cfn-elasticloadbalancingv2-listenerrule-jwtvalidationconfig-additionalclaims): {{
    - JwtValidationActionAdditionalClaim}}
  [Issuer](#cfn-elasticloadbalancingv2-listenerrule-jwtvalidationconfig-issuer): {{String}}
  [JwksEndpoint](#cfn-elasticloadbalancingv2-listenerrule-jwtvalidationconfig-jwksendpoint): {{String}}
```

## Properties
<a name="aws-properties-elasticloadbalancingv2-listenerrule-jwtvalidationconfig-properties"></a>

`AdditionalClaims`  <a name="cfn-elasticloadbalancingv2-listenerrule-jwtvalidationconfig-additionalclaims"></a>
Property description not available.
*Required*: No
*Type*: Array of [JwtValidationActionAdditionalClaim](aws-properties-elasticloadbalancingv2-listenerrule-jwtvalidationactionadditionalclaim.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Issuer`  <a name="cfn-elasticloadbalancingv2-listenerrule-jwtvalidationconfig-issuer"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`JwksEndpoint`  <a name="cfn-elasticloadbalancingv2-listenerrule-jwtvalidationconfig-jwksendpoint"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
