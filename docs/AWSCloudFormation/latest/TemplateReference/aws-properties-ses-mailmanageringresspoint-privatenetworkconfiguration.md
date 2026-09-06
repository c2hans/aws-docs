---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ses-mailmanageringresspoint-privatenetworkconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::MailManagerIngressPoint PrivateNetworkConfiguration
<a name="aws-properties-ses-mailmanageringresspoint-privatenetworkconfiguration"></a>

Specifies the network configuration for the private ingress point.

## Syntax
<a name="aws-properties-ses-mailmanageringresspoint-privatenetworkconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ses-mailmanageringresspoint-privatenetworkconfiguration-syntax.json"></a>

```
{
  "[VpcEndpointId](#cfn-ses-mailmanageringresspoint-privatenetworkconfiguration-vpcendpointid)" : {{String}}
}
```

### YAML
<a name="aws-properties-ses-mailmanageringresspoint-privatenetworkconfiguration-syntax.yaml"></a>

```
  [VpcEndpointId](#cfn-ses-mailmanageringresspoint-privatenetworkconfiguration-vpcendpointid): {{String}}
```

## Properties
<a name="aws-properties-ses-mailmanageringresspoint-privatenetworkconfiguration-properties"></a>

`VpcEndpointId`  <a name="cfn-ses-mailmanageringresspoint-privatenetworkconfiguration-vpcendpointid"></a>
The identifier of the VPC endpoint to associate with this private ingress point.
*Required*: Yes
*Type*: String
*Pattern*: `^vpce-[a-zA-Z0-9]{17}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
