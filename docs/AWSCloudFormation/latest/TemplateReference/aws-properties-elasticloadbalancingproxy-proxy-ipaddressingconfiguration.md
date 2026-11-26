---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-elasticloadbalancingproxy-proxy-ipaddressingconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ElasticLoadBalancingProxy::Proxy IpAddressingConfiguration

The IP addressing configuration of the proxy. You can't change this configuration after you create the proxy.

## Syntax
<a name="aws-properties-elasticloadbalancingproxy-proxy-ipaddressingconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-elasticloadbalancingproxy-proxy-ipaddressingconfiguration-syntax.json"></a>

```json
{
  "[Ipv4Addressability](#cfn-elasticloadbalancingproxy-proxy-ipaddressingconfiguration-ipv4addressability)" : {{String}},
  "[Ipv6Addressability](#cfn-elasticloadbalancingproxy-proxy-ipaddressingconfiguration-ipv6addressability)" : {{String}}
}
```

### YAML
<a name="aws-properties-elasticloadbalancingproxy-proxy-ipaddressingconfiguration-syntax.yaml"></a>

```yaml
  [Ipv4Addressability](#cfn-elasticloadbalancingproxy-proxy-ipaddressingconfiguration-ipv4addressability): {{String}}
  [Ipv6Addressability](#cfn-elasticloadbalancingproxy-proxy-ipaddressingconfiguration-ipv6addressability): {{String}}
```

## Properties
<a name="aws-properties-elasticloadbalancingproxy-proxy-ipaddressingconfiguration-properties"></a>

`Ipv4Addressability`  <a name="cfn-elasticloadbalancingproxy-proxy-ipaddressingconfiguration-ipv4addressability"></a>
The IPv4 addressability of the proxy. Valid values are the following:
+ `off` – The proxy isn't IPv4-addressable.
+ `internet-facing` – The proxy is IPv4-addressable for both internet-facing and internal clients.
+ `internal` – The proxy is IPv4-addressable for internal clients only.
*Required*: Yes
*Type*: String
*Allowed values*: `off | internet-facing | internal`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Ipv6Addressability`  <a name="cfn-elasticloadbalancingproxy-proxy-ipaddressingconfiguration-ipv6addressability"></a>
The IPv6 addressability of the proxy. Valid values are the following:
+ `off` – The proxy isn't IPv6-addressable.
+ `internet-facing` – The proxy is IPv6-addressable for both internet-facing and internal clients.
+ `internal` – The proxy is IPv6-addressable for internal clients only.
*Required*: Yes
*Type*: String
*Allowed values*: `off | internet-facing | internal`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
