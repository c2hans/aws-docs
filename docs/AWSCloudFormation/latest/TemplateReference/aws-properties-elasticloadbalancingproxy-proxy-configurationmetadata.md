---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-elasticloadbalancingproxy-proxy-configurationmetadata.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ElasticLoadBalancingProxy::Proxy ConfigurationMetadata

Metadata that describes the proxy's stored configuration, including a hash and a timestamp for the configuration file and, when present, the configuration archive.

## Syntax
<a name="aws-properties-elasticloadbalancingproxy-proxy-configurationmetadata-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-elasticloadbalancingproxy-proxy-configurationmetadata-syntax.json"></a>

```json
{
  "[ConfigArchiveHash](#cfn-elasticloadbalancingproxy-proxy-configurationmetadata-configarchivehash)" : {{String}},
  "[ConfigArchiveLastUpdatedAt](#cfn-elasticloadbalancingproxy-proxy-configurationmetadata-configarchivelastupdatedat)" : {{String}},
  "[ConfigFileHash](#cfn-elasticloadbalancingproxy-proxy-configurationmetadata-configfilehash)" : {{String}},
  "[ConfigFileLastUpdatedAt](#cfn-elasticloadbalancingproxy-proxy-configurationmetadata-configfilelastupdatedat)" : {{String}}
}
```

### YAML
<a name="aws-properties-elasticloadbalancingproxy-proxy-configurationmetadata-syntax.yaml"></a>

```yaml
  [ConfigArchiveHash](#cfn-elasticloadbalancingproxy-proxy-configurationmetadata-configarchivehash): {{String}}
  [ConfigArchiveLastUpdatedAt](#cfn-elasticloadbalancingproxy-proxy-configurationmetadata-configarchivelastupdatedat): {{String}}
  [ConfigFileHash](#cfn-elasticloadbalancingproxy-proxy-configurationmetadata-configfilehash): {{String}}
  [ConfigFileLastUpdatedAt](#cfn-elasticloadbalancingproxy-proxy-configurationmetadata-configfilelastupdatedat): {{String}}
```

## Properties
<a name="aws-properties-elasticloadbalancingproxy-proxy-configurationmetadata-properties"></a>

`ConfigArchiveHash`  <a name="cfn-elasticloadbalancingproxy-proxy-configurationmetadata-configarchivehash"></a>
The SHA-256 hash of the configuration archive. This value is absent when the proxy has no configuration archive.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ConfigArchiveLastUpdatedAt`  <a name="cfn-elasticloadbalancingproxy-proxy-configurationmetadata-configarchivelastupdatedat"></a>
The date and time when the configuration archive was last updated.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ConfigFileHash`  <a name="cfn-elasticloadbalancingproxy-proxy-configurationmetadata-configfilehash"></a>
The SHA-256 hash of the configuration file.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ConfigFileLastUpdatedAt`  <a name="cfn-elasticloadbalancingproxy-proxy-configurationmetadata-configfilelastupdatedat"></a>
The date and time when the configuration file was last updated.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
