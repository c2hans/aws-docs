---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ses-mailmanageringresspoint-networkconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::MailManagerIngressPoint NetworkConfiguration
<a name="aws-properties-ses-mailmanageringresspoint-networkconfiguration"></a>

The network type (IPv4-only, Dual-Stack, PrivateLink) of the ingress endpoint resource.

## Syntax
<a name="aws-properties-ses-mailmanageringresspoint-networkconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ses-mailmanageringresspoint-networkconfiguration-syntax.json"></a>

```
{
  "[PrivateNetworkConfiguration](#cfn-ses-mailmanageringresspoint-networkconfiguration-privatenetworkconfiguration)" : {{PrivateNetworkConfiguration}},
  "[PublicNetworkConfiguration](#cfn-ses-mailmanageringresspoint-networkconfiguration-publicnetworkconfiguration)" : {{PublicNetworkConfiguration}}
}
```

### YAML
<a name="aws-properties-ses-mailmanageringresspoint-networkconfiguration-syntax.yaml"></a>

```
  [PrivateNetworkConfiguration](#cfn-ses-mailmanageringresspoint-networkconfiguration-privatenetworkconfiguration): {{
    PrivateNetworkConfiguration}}
  [PublicNetworkConfiguration](#cfn-ses-mailmanageringresspoint-networkconfiguration-publicnetworkconfiguration): {{
    PublicNetworkConfiguration}}
```

## Properties
<a name="aws-properties-ses-mailmanageringresspoint-networkconfiguration-properties"></a>

`PrivateNetworkConfiguration`  <a name="cfn-ses-mailmanageringresspoint-networkconfiguration-privatenetworkconfiguration"></a>
Specifies the network configuration for the private ingress point.
*Required*: No
*Type*: [PrivateNetworkConfiguration](aws-properties-ses-mailmanageringresspoint-privatenetworkconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PublicNetworkConfiguration`  <a name="cfn-ses-mailmanageringresspoint-networkconfiguration-publicnetworkconfiguration"></a>
Specifies the network configuration for the public ingress point.
*Required*: No
*Type*: [PublicNetworkConfiguration](aws-properties-ses-mailmanageringresspoint-publicnetworkconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
