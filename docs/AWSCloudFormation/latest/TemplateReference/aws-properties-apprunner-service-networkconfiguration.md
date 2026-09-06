---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-apprunner-service-networkconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppRunner::Service NetworkConfiguration
<a name="aws-properties-apprunner-service-networkconfiguration"></a>

Describes configuration settings related to network traffic of an AWS App Runner service. Consists of embedded objects for each configurable network feature.

## Syntax
<a name="aws-properties-apprunner-service-networkconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-apprunner-service-networkconfiguration-syntax.json"></a>

```
{
  "[EgressConfiguration](#cfn-apprunner-service-networkconfiguration-egressconfiguration)" : {{EgressConfiguration}},
  "[IngressConfiguration](#cfn-apprunner-service-networkconfiguration-ingressconfiguration)" : {{IngressConfiguration}},
  "[IpAddressType](#cfn-apprunner-service-networkconfiguration-ipaddresstype)" : {{String}}
}
```

### YAML
<a name="aws-properties-apprunner-service-networkconfiguration-syntax.yaml"></a>

```
  [EgressConfiguration](#cfn-apprunner-service-networkconfiguration-egressconfiguration): {{
    EgressConfiguration}}
  [IngressConfiguration](#cfn-apprunner-service-networkconfiguration-ingressconfiguration): {{
    IngressConfiguration}}
  [IpAddressType](#cfn-apprunner-service-networkconfiguration-ipaddresstype): {{String}}
```

## Properties
<a name="aws-properties-apprunner-service-networkconfiguration-properties"></a>

`EgressConfiguration`  <a name="cfn-apprunner-service-networkconfiguration-egressconfiguration"></a>
Network configuration settings for outbound message traffic.
*Required*: No
*Type*: [EgressConfiguration](aws-properties-apprunner-service-egressconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IngressConfiguration`  <a name="cfn-apprunner-service-networkconfiguration-ingressconfiguration"></a>
Network configuration settings for inbound message traffic.
*Required*: No
*Type*: [IngressConfiguration](aws-properties-apprunner-service-ingressconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IpAddressType`  <a name="cfn-apprunner-service-networkconfiguration-ipaddresstype"></a>
App Runner provides you with the option to choose between *IPv4* and *dual stack* (IPv4 and IPv6) for your incoming public network configuration. This is an optional parameter. If you do not specify an `IpAddressType`, it defaults to select IPv4.
*Required*: No
*Type*: String
*Allowed values*: `IPV4 | DUAL_STACK`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
