---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-elasticloadbalancingproxy-proxy-subnetandzone.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ElasticLoadBalancingProxy::Proxy SubnetAndZone

A subnet that the proxy is deployed into, together with the Availability Zone that contains it.

## Syntax
<a name="aws-properties-elasticloadbalancingproxy-proxy-subnetandzone-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-elasticloadbalancingproxy-proxy-subnetandzone-syntax.json"></a>

```json
{
  "[SubnetId](#cfn-elasticloadbalancingproxy-proxy-subnetandzone-subnetid)" : {{String}},
  "[ZoneId](#cfn-elasticloadbalancingproxy-proxy-subnetandzone-zoneid)" : {{String}},
  "[ZoneName](#cfn-elasticloadbalancingproxy-proxy-subnetandzone-zonename)" : {{String}}
}
```

### YAML
<a name="aws-properties-elasticloadbalancingproxy-proxy-subnetandzone-syntax.yaml"></a>

```yaml
  [SubnetId](#cfn-elasticloadbalancingproxy-proxy-subnetandzone-subnetid): {{String}}
  [ZoneId](#cfn-elasticloadbalancingproxy-proxy-subnetandzone-zoneid): {{String}}
  [ZoneName](#cfn-elasticloadbalancingproxy-proxy-subnetandzone-zonename): {{String}}
```

## Properties
<a name="aws-properties-elasticloadbalancingproxy-proxy-subnetandzone-properties"></a>

`SubnetId`  <a name="cfn-elasticloadbalancingproxy-proxy-subnetandzone-subnetid"></a>
The ID of the subnet.
*Required*: Yes
*Type*: String
*Pattern*: `^subnet-.+$`
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ZoneId`  <a name="cfn-elasticloadbalancingproxy-proxy-subnetandzone-zoneid"></a>
The ID of the Availability Zone that contains the subnet.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ZoneName`  <a name="cfn-elasticloadbalancingproxy-proxy-subnetandzone-zonename"></a>
The name of the Availability Zone that contains the subnet (for example, `us-east-1a`).
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
