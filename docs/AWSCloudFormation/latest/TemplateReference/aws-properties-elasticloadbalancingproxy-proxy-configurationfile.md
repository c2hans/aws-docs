---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-elasticloadbalancingproxy-proxy-configurationfile.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ElasticLoadBalancingProxy::Proxy ConfigurationFile

The configuration file for the proxy. The configuration file is your Envoy bootstrap configuration, in YAML format.

## Syntax
<a name="aws-properties-elasticloadbalancingproxy-proxy-configurationfile-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-elasticloadbalancingproxy-proxy-configurationfile-syntax.json"></a>

```json
{
  "[ConfigurationBytes](#cfn-elasticloadbalancingproxy-proxy-configurationfile-configurationbytes)" : {{String}}
}
```

### YAML
<a name="aws-properties-elasticloadbalancingproxy-proxy-configurationfile-syntax.yaml"></a>

```yaml
  [ConfigurationBytes](#cfn-elasticloadbalancingproxy-proxy-configurationfile-configurationbytes): {{String}}
```

## Properties
<a name="aws-properties-elasticloadbalancingproxy-proxy-configurationfile-properties"></a>

`ConfigurationBytes`  <a name="cfn-elasticloadbalancingproxy-proxy-configurationfile-configurationbytes"></a>
The contents of the proxy configuration file, as a base64-encoded string. The decoded contents must be a valid Envoy bootstrap configuration for the proxy version and can be at most 128 KB (131,072 bytes).
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
