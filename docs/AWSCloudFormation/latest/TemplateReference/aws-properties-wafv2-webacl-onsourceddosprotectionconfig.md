---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wafv2-webacl-onsourceddosprotectionconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WAFv2::WebACL OnSourceDDoSProtectionConfig
<a name="aws-properties-wafv2-webacl-onsourceddosprotectionconfig"></a>

Configures the level of DDoS protection that applies to web ACLs associated with Application Load Balancers.

## Syntax
<a name="aws-properties-wafv2-webacl-onsourceddosprotectionconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wafv2-webacl-onsourceddosprotectionconfig-syntax.json"></a>

```
{
  "[ALBLowReputationMode](#cfn-wafv2-webacl-onsourceddosprotectionconfig-alblowreputationmode)" : {{String}}
}
```

### YAML
<a name="aws-properties-wafv2-webacl-onsourceddosprotectionconfig-syntax.yaml"></a>

```
  [ALBLowReputationMode](#cfn-wafv2-webacl-onsourceddosprotectionconfig-alblowreputationmode): {{String}}
```

## Properties
<a name="aws-properties-wafv2-webacl-onsourceddosprotectionconfig-properties"></a>

`ALBLowReputationMode`  <a name="cfn-wafv2-webacl-onsourceddosprotectionconfig-alblowreputationmode"></a>
The level of DDoS protection that applies to web ACLs associated with Application Load Balancers. `ACTIVE_UNDER_DDOS` protection is enabled by default whenever a web ACL is associated with an Application Load Balancer. In the event that an Application Load Balancer experiences high-load conditions or suspected DDoS attacks, the `ACTIVE_UNDER_DDOS` protection automatically rate limits traffic from known low reputation sources without disrupting Application Load Balancer availability. `ALWAYS_ON` protection provides constant, always-on monitoring of known low reputation sources for suspected DDoS attacks. While this provides a higher level of protection, there may be potential impacts on legitimate traffic.
*Required*: Yes
*Type*: String
*Allowed values*: `ACTIVE_UNDER_DDOS | ALWAYS_ON`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
