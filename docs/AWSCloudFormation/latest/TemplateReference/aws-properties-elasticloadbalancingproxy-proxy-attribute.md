---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-elasticloadbalancingproxy-proxy-attribute.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ElasticLoadBalancingProxy::Proxy Attribute

A key-value attribute for a proxy. Attributes are optional settings that control secondary proxy behavior.

## Syntax
<a name="aws-properties-elasticloadbalancingproxy-proxy-attribute-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-elasticloadbalancingproxy-proxy-attribute-syntax.json"></a>

```json
{
  "[Key](#cfn-elasticloadbalancingproxy-proxy-attribute-key)" : {{String}},
  "[Value](#cfn-elasticloadbalancingproxy-proxy-attribute-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-elasticloadbalancingproxy-proxy-attribute-syntax.yaml"></a>

```yaml
  [Key](#cfn-elasticloadbalancingproxy-proxy-attribute-key): {{String}}
  [Value](#cfn-elasticloadbalancingproxy-proxy-attribute-value): {{String}}
```

## Properties
<a name="aws-properties-elasticloadbalancingproxy-proxy-attribute-properties"></a>

`Key`  <a name="cfn-elasticloadbalancingproxy-proxy-attribute-key"></a>
The key of the attribute. For the supported keys, see the `Attributes` property.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-elasticloadbalancingproxy-proxy-attribute-value"></a>
The value of the attribute. For boolean attributes, specify the string `true` or `false`.
*Required*: Yes
*Type*: String
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
