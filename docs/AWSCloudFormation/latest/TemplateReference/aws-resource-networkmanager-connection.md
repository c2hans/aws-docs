---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-networkmanager-connection.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::NetworkManager::Connection

Describes a connection.

## Syntax
<a name="aws-resource-networkmanager-connection-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-networkmanager-connection-syntax.json"></a>

```json
{
  "Type" : "AWS::NetworkManager::Connection",
  "Properties" : {
      "[ConnectedDeviceId](#cfn-networkmanager-connection-connecteddeviceid)" : {{String}},
      "[ConnectedLinkId](#cfn-networkmanager-connection-connectedlinkid)" : {{String}},
      "[Description](#cfn-networkmanager-connection-description)" : {{String}},
      "[DeviceId](#cfn-networkmanager-connection-deviceid)" : {{String}},
      "[GlobalNetworkId](#cfn-networkmanager-connection-globalnetworkid)" : {{String}},
      "[LinkId](#cfn-networkmanager-connection-linkid)" : {{String}},
      "[Tags](#cfn-networkmanager-connection-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-networkmanager-connection-syntax.yaml"></a>

```yaml
Type: AWS::NetworkManager::Connection
Properties:
  [ConnectedDeviceId](#cfn-networkmanager-connection-connecteddeviceid): {{String}}
  [ConnectedLinkId](#cfn-networkmanager-connection-connectedlinkid): {{String}}
  [Description](#cfn-networkmanager-connection-description): {{String}}
  [DeviceId](#cfn-networkmanager-connection-deviceid): {{String}}
  [GlobalNetworkId](#cfn-networkmanager-connection-globalnetworkid): {{String}}
  [LinkId](#cfn-networkmanager-connection-linkid): {{String}}
  [Tags](#cfn-networkmanager-connection-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-networkmanager-connection-properties"></a>

`ConnectedDeviceId`  <a name="cfn-networkmanager-connection-connecteddeviceid"></a>
The ID of the second device in the connection.
*Required*: Yes
*Type*: String
*Pattern*: `^device-[a-z0-9-]*$`
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ConnectedLinkId`  <a name="cfn-networkmanager-connection-connectedlinkid"></a>
The ID of the link for the second device in the connection.
*Required*: No
*Type*: String
*Pattern*: `^link-[a-z0-9-]*$`
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-networkmanager-connection-description"></a>
The description of the connection.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DeviceId`  <a name="cfn-networkmanager-connection-deviceid"></a>
The ID of the first device in the connection.
*Required*: Yes
*Type*: String
*Pattern*: `^device-[a-z0-9-]*$`
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`GlobalNetworkId`  <a name="cfn-networkmanager-connection-globalnetworkid"></a>
The ID of the global network.
*Required*: Yes
*Type*: String
*Pattern*: `^global-network-[a-z0-9-]*$`
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`LinkId`  <a name="cfn-networkmanager-connection-linkid"></a>
The ID of the link for the first device in the connection.
*Required*: No
*Type*: String
*Pattern*: `^link-[a-z0-9-]*$`
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-networkmanager-connection-tags"></a>
The tags for the connection.
*Required*: No
*Type*: Array of [Tag](aws-properties-networkmanager-connection-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-networkmanager-connection-return-values"></a>

### Ref
<a name="aws-resource-networkmanager-connection-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-networkmanager-connection-return-values-fn--getatt"></a>

####
<a name="aws-resource-networkmanager-connection-return-values-fn--getatt-fn--getatt"></a>

`ConnectionArn`  <a name="ConnectionArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the connection.

`ConnectionId`  <a name="ConnectionId-fn::getatt"></a>
The ID of the connection.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The date and time that the connection was created.

`State`  <a name="State-fn::getatt"></a>
The state of the connection.
