---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-sourceendpoint-publicsourceendpointnetworkingconfigurationallowrule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::SourceEndpoint PublicSourceEndpointNetworkingConfigurationAllowRule

A rule that allows a specific CIDR block to connect to the public source endpoint.

## Syntax
<a name="aws-properties-mediaconnect-sourceendpoint-publicsourceendpointnetworkingconfigurationallowrule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-sourceendpoint-publicsourceendpointnetworkingconfigurationallowrule-syntax.json"></a>

```json
{
  "[Cidr](#cfn-mediaconnect-sourceendpoint-publicsourceendpointnetworkingconfigurationallowrule-cidr)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediaconnect-sourceendpoint-publicsourceendpointnetworkingconfigurationallowrule-syntax.yaml"></a>

```yaml
  [Cidr](#cfn-mediaconnect-sourceendpoint-publicsourceendpointnetworkingconfigurationallowrule-cidr): {{String}}
```

## Properties
<a name="aws-properties-mediaconnect-sourceendpoint-publicsourceendpointnetworkingconfigurationallowrule-properties"></a>

`Cidr`  <a name="cfn-mediaconnect-sourceendpoint-publicsourceendpointnetworkingconfigurationallowrule-cidr"></a>
The CIDR block that is allowed to connect to the source endpoint, in CIDR notation.
*Required*: Yes
*Type*: String
*Pattern*: `^(?:[0-9]{1,3}\.){3}[0-9]{1,3}/([0-9]|[12][0-9]|3[0-2])$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
