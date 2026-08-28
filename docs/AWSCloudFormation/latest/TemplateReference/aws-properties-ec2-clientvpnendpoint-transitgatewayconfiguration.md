---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-clientvpnendpoint-transitgatewayconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::ClientVpnEndpoint TransitGatewayConfiguration
<a name="aws-properties-ec2-clientvpnendpoint-transitgatewayconfiguration"></a>

<a name="aws-properties-ec2-clientvpnendpoint-transitgatewayconfiguration-description"></a>The `TransitGatewayConfiguration` property type specifies Property description not available. for an [AWS::EC2::ClientVpnEndpoint](aws-resource-ec2-clientvpnendpoint.md).

## Syntax
<a name="aws-properties-ec2-clientvpnendpoint-transitgatewayconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-clientvpnendpoint-transitgatewayconfiguration-syntax.json"></a>

```
{
  "[AvailabilityZoneIds](#cfn-ec2-clientvpnendpoint-transitgatewayconfiguration-availabilityzoneids)" : {{[ String, ... ]}},
  "[AvailabilityZones](#cfn-ec2-clientvpnendpoint-transitgatewayconfiguration-availabilityzones)" : {{[ String, ... ]}},
  "[TransitGatewayId](#cfn-ec2-clientvpnendpoint-transitgatewayconfiguration-transitgatewayid)" : {{String}}
}
```

### YAML
<a name="aws-properties-ec2-clientvpnendpoint-transitgatewayconfiguration-syntax.yaml"></a>

```
  [AvailabilityZoneIds](#cfn-ec2-clientvpnendpoint-transitgatewayconfiguration-availabilityzoneids): {{
    - String}}
  [AvailabilityZones](#cfn-ec2-clientvpnendpoint-transitgatewayconfiguration-availabilityzones): {{
    - String}}
  [TransitGatewayId](#cfn-ec2-clientvpnendpoint-transitgatewayconfiguration-transitgatewayid): {{String}}
```

## Properties
<a name="aws-properties-ec2-clientvpnendpoint-transitgatewayconfiguration-properties"></a>

`AvailabilityZoneIds`  <a name="cfn-ec2-clientvpnendpoint-transitgatewayconfiguration-availabilityzoneids"></a>
Property description not available.
*Required*: No
*Type*: Array of String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`AvailabilityZones`  <a name="cfn-ec2-clientvpnendpoint-transitgatewayconfiguration-availabilityzones"></a>
Property description not available.
*Required*: No
*Type*: Array of String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TransitGatewayId`  <a name="cfn-ec2-clientvpnendpoint-transitgatewayconfiguration-transitgatewayid"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
