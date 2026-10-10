---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-clientvpnendpoint-devicepostureoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::ClientVpnEndpoint DevicePostureOptions
<a name="aws-properties-ec2-clientvpnendpoint-devicepostureoptions"></a>

Describes the device posture options for a Client VPN endpoint. Device posture options specify the device trust providers that the endpoint uses to evaluate the security posture of connecting devices.

## Syntax
<a name="aws-properties-ec2-clientvpnendpoint-devicepostureoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-clientvpnendpoint-devicepostureoptions-syntax.json"></a>

```
{
  "[Enabled](#cfn-ec2-clientvpnendpoint-devicepostureoptions-enabled)" : {{Boolean}},
  "[TrustProviders](#cfn-ec2-clientvpnendpoint-devicepostureoptions-trustproviders)" : {{[ DevicePostureTrustProvider, ... ]}}
}
```

### YAML
<a name="aws-properties-ec2-clientvpnendpoint-devicepostureoptions-syntax.yaml"></a>

```
  [Enabled](#cfn-ec2-clientvpnendpoint-devicepostureoptions-enabled): {{Boolean}}
  [TrustProviders](#cfn-ec2-clientvpnendpoint-devicepostureoptions-trustproviders): {{
    - DevicePostureTrustProvider}}
```

## Properties
<a name="aws-properties-ec2-clientvpnendpoint-devicepostureoptions-properties"></a>

`Enabled`  <a name="cfn-ec2-clientvpnendpoint-devicepostureoptions-enabled"></a>
Indicates whether device posture evaluation is enabled for the Client VPN endpoint. Specify `false` to disable device posture, which clears the configured device trust providers.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TrustProviders`  <a name="cfn-ec2-clientvpnendpoint-devicepostureoptions-trustproviders"></a>
The device trust providers to configure for the Client VPN endpoint.
*Required*: Yes
*Type*: Array of [DevicePostureTrustProvider](aws-properties-ec2-clientvpnendpoint-deviceposturetrustprovider.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
