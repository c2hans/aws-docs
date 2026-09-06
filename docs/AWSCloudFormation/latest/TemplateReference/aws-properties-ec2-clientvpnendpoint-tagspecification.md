---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-clientvpnendpoint-tagspecification.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::ClientVpnEndpoint TagSpecification
<a name="aws-properties-ec2-clientvpnendpoint-tagspecification"></a>

Specifies the tags to apply to the Client VPN endpoint.

## Syntax
<a name="aws-properties-ec2-clientvpnendpoint-tagspecification-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-clientvpnendpoint-tagspecification-syntax.json"></a>

```
{
  "[ResourceType](#cfn-ec2-clientvpnendpoint-tagspecification-resourcetype)" : {{String}},
  "[Tags](#cfn-ec2-clientvpnendpoint-tagspecification-tags)" : {{[ Tag, ... ]}}
}
```

### YAML
<a name="aws-properties-ec2-clientvpnendpoint-tagspecification-syntax.yaml"></a>

```
  [ResourceType](#cfn-ec2-clientvpnendpoint-tagspecification-resourcetype): {{String}}
  [Tags](#cfn-ec2-clientvpnendpoint-tagspecification-tags): {{
    - Tag}}
```

## Properties
<a name="aws-properties-ec2-clientvpnendpoint-tagspecification-properties"></a>

`ResourceType`  <a name="cfn-ec2-clientvpnendpoint-tagspecification-resourcetype"></a>
The type of resource to tag. To tag a Client VPN endpoint, `ResourceType` must be `client-vpn-endpoint`.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-ec2-clientvpnendpoint-tagspecification-tags"></a>
The tags to apply to the resource.
*Required*: Yes
*Type*: Array of [Tag](aws-properties-ec2-clientvpnendpoint-tag.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
