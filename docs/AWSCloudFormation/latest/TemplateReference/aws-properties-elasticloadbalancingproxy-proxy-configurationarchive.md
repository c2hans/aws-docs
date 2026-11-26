---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-elasticloadbalancingproxy-proxy-configurationarchive.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ElasticLoadBalancingProxy::Proxy ConfigurationArchive

The configuration archive for the proxy. The archive is a ZIP file of the supporting files that your configuration file references.

## Syntax
<a name="aws-properties-elasticloadbalancingproxy-proxy-configurationarchive-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-elasticloadbalancingproxy-proxy-configurationarchive-syntax.json"></a>

```json
{
  "[ConfigurationBytes](#cfn-elasticloadbalancingproxy-proxy-configurationarchive-configurationbytes)" : {{String}}
}
```

### YAML
<a name="aws-properties-elasticloadbalancingproxy-proxy-configurationarchive-syntax.yaml"></a>

```yaml
  [ConfigurationBytes](#cfn-elasticloadbalancingproxy-proxy-configurationarchive-configurationbytes): {{String}}
```

## Properties
<a name="aws-properties-elasticloadbalancingproxy-proxy-configurationarchive-properties"></a>

`ConfigurationBytes`  <a name="cfn-elasticloadbalancingproxy-proxy-configurationarchive-configurationbytes"></a>
The contents of the proxy configuration archive, as a base64-encoded string. The decoded contents must be a valid ZIP archive with at least one entry. The archive can be at most 10 MB (10,485,760 bytes), with at most 50 entries and at most 50 MB (52,428,800 bytes) of uncompressed content.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
