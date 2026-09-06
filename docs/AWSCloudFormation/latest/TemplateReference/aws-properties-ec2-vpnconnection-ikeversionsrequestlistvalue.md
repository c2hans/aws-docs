---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-vpnconnection-ikeversionsrequestlistvalue.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::VPNConnection IKEVersionsRequestListValue
<a name="aws-properties-ec2-vpnconnection-ikeversionsrequestlistvalue"></a>

The IKE version that is permitted for the VPN tunnel.

## Syntax
<a name="aws-properties-ec2-vpnconnection-ikeversionsrequestlistvalue-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-vpnconnection-ikeversionsrequestlistvalue-syntax.json"></a>

```
{
  "[Value](#cfn-ec2-vpnconnection-ikeversionsrequestlistvalue-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-ec2-vpnconnection-ikeversionsrequestlistvalue-syntax.yaml"></a>

```
  [Value](#cfn-ec2-vpnconnection-ikeversionsrequestlistvalue-value): {{String}}
```

## Properties
<a name="aws-properties-ec2-vpnconnection-ikeversionsrequestlistvalue-properties"></a>

`Value`  <a name="cfn-ec2-vpnconnection-ikeversionsrequestlistvalue-value"></a>
The IKE version.
*Required*: No
*Type*: String
*Allowed values*: `ikev1 | ikev2`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
