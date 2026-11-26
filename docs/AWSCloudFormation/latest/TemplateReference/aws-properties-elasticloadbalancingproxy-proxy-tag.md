---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-elasticloadbalancingproxy-proxy-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ElasticLoadBalancingProxy::Proxy Tag

A key-value pair to associate with the proxy.

## Syntax
<a name="aws-properties-elasticloadbalancingproxy-proxy-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-elasticloadbalancingproxy-proxy-tag-syntax.json"></a>

```json
{
  "[Key](#cfn-elasticloadbalancingproxy-proxy-tag-key)" : {{String}},
  "[Value](#cfn-elasticloadbalancingproxy-proxy-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-elasticloadbalancingproxy-proxy-tag-syntax.yaml"></a>

```yaml
  [Key](#cfn-elasticloadbalancingproxy-proxy-tag-key): {{String}}
  [Value](#cfn-elasticloadbalancingproxy-proxy-tag-value): {{String}}
```

## Properties
<a name="aws-properties-elasticloadbalancingproxy-proxy-tag-properties"></a>

`Key`  <a name="cfn-elasticloadbalancingproxy-proxy-tag-key"></a>
The key of the tag. You can specify a value that's 1 to 128 Unicode characters in length and can't be prefixed with `aws:`. The key is case-sensitive.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-elasticloadbalancingproxy-proxy-tag-value"></a>
The value of the tag. You can specify a value that's 0 to 256 Unicode characters in length. The value is case-sensitive.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
