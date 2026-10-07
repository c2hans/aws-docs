---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-workspaces-directory-workspaceaccessproperties.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WorkSpaces::Directory WorkspaceAccessProperties
<a name="aws-properties-workspaces-directory-workspaceaccessproperties"></a>

The device types and operating systems that can be used to access a WorkSpace. For more information, see [Amazon WorkSpaces Client Network Requirements](https://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-network-requirements.html).

## Syntax
<a name="aws-properties-workspaces-directory-workspaceaccessproperties-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-workspaces-directory-workspaceaccessproperties-syntax.json"></a>

```
{
  "[AccessEndpointConfig](#cfn-workspaces-directory-workspaceaccessproperties-accessendpointconfig)" : {{AccessEndpointConfig}},
  "[DeviceTypeAndroid](#cfn-workspaces-directory-workspaceaccessproperties-devicetypeandroid)" : {{String}},
  "[DeviceTypeChromeOs](#cfn-workspaces-directory-workspaceaccessproperties-devicetypechromeos)" : {{String}},
  "[DeviceTypeIos](#cfn-workspaces-directory-workspaceaccessproperties-devicetypeios)" : {{String}},
  "[DeviceTypeLinux](#cfn-workspaces-directory-workspaceaccessproperties-devicetypelinux)" : {{String}},
  "[DeviceTypeOsx](#cfn-workspaces-directory-workspaceaccessproperties-devicetypeosx)" : {{String}},
  "[DeviceTypeWeb](#cfn-workspaces-directory-workspaceaccessproperties-devicetypeweb)" : {{String}},
  "[DeviceTypeWindows](#cfn-workspaces-directory-workspaceaccessproperties-devicetypewindows)" : {{String}},
  "[DeviceTypeWorkSpacesThinClient](#cfn-workspaces-directory-workspaceaccessproperties-devicetypeworkspacesthinclient)" : {{String}},
  "[DeviceTypeZeroClient](#cfn-workspaces-directory-workspaceaccessproperties-devicetypezeroclient)" : {{String}}
}
```

### YAML
<a name="aws-properties-workspaces-directory-workspaceaccessproperties-syntax.yaml"></a>

```
  [AccessEndpointConfig](#cfn-workspaces-directory-workspaceaccessproperties-accessendpointconfig): {{
    AccessEndpointConfig}}
  [DeviceTypeAndroid](#cfn-workspaces-directory-workspaceaccessproperties-devicetypeandroid): {{String}}
  [DeviceTypeChromeOs](#cfn-workspaces-directory-workspaceaccessproperties-devicetypechromeos): {{String}}
  [DeviceTypeIos](#cfn-workspaces-directory-workspaceaccessproperties-devicetypeios): {{String}}
  [DeviceTypeLinux](#cfn-workspaces-directory-workspaceaccessproperties-devicetypelinux): {{String}}
  [DeviceTypeOsx](#cfn-workspaces-directory-workspaceaccessproperties-devicetypeosx): {{String}}
  [DeviceTypeWeb](#cfn-workspaces-directory-workspaceaccessproperties-devicetypeweb): {{String}}
  [DeviceTypeWindows](#cfn-workspaces-directory-workspaceaccessproperties-devicetypewindows): {{String}}
  [DeviceTypeWorkSpacesThinClient](#cfn-workspaces-directory-workspaceaccessproperties-devicetypeworkspacesthinclient): {{String}}
  [DeviceTypeZeroClient](#cfn-workspaces-directory-workspaceaccessproperties-devicetypezeroclient): {{String}}
```

## Properties
<a name="aws-properties-workspaces-directory-workspaceaccessproperties-properties"></a>

`AccessEndpointConfig`  <a name="cfn-workspaces-directory-workspaceaccessproperties-accessendpointconfig"></a>
Specifies the configuration for accessing the WorkSpace.
*Required*: No
*Type*: [AccessEndpointConfig](aws-properties-workspaces-directory-accessendpointconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DeviceTypeAndroid`  <a name="cfn-workspaces-directory-workspaceaccessproperties-devicetypeandroid"></a>
Indicates whether users can use Android and Android-compatible Chrome OS devices to access their WorkSpaces.
*Required*: No
*Type*: String
*Allowed values*: `ALLOW | DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DeviceTypeChromeOs`  <a name="cfn-workspaces-directory-workspaceaccessproperties-devicetypechromeos"></a>
Indicates whether users can use Chromebooks to access their WorkSpaces.
*Required*: No
*Type*: String
*Allowed values*: `ALLOW | DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DeviceTypeIos`  <a name="cfn-workspaces-directory-workspaceaccessproperties-devicetypeios"></a>
Indicates whether users can use iOS devices to access their WorkSpaces.
*Required*: No
*Type*: String
*Allowed values*: `ALLOW | DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DeviceTypeLinux`  <a name="cfn-workspaces-directory-workspaceaccessproperties-devicetypelinux"></a>
Indicates whether users can use Linux clients to access their WorkSpaces.
*Required*: No
*Type*: String
*Allowed values*: `ALLOW | DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DeviceTypeOsx`  <a name="cfn-workspaces-directory-workspaceaccessproperties-devicetypeosx"></a>
Indicates whether users can use macOS clients to access their WorkSpaces.
*Required*: No
*Type*: String
*Allowed values*: `ALLOW | DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DeviceTypeWeb`  <a name="cfn-workspaces-directory-workspaceaccessproperties-devicetypeweb"></a>
Indicates whether users can access their WorkSpaces through a web browser.
*Required*: No
*Type*: String
*Allowed values*: `ALLOW | DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DeviceTypeWindows`  <a name="cfn-workspaces-directory-workspaceaccessproperties-devicetypewindows"></a>
Indicates whether users can use Windows clients to access their WorkSpaces.
*Required*: No
*Type*: String
*Allowed values*: `ALLOW | DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DeviceTypeWorkSpacesThinClient`  <a name="cfn-workspaces-directory-workspaceaccessproperties-devicetypeworkspacesthinclient"></a>
Indicates whether users can access their WorkSpaces through a WorkSpaces Thin Client.
*Required*: No
*Type*: String
*Allowed values*: `ALLOW | DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DeviceTypeZeroClient`  <a name="cfn-workspaces-directory-workspaceaccessproperties-devicetypezeroclient"></a>
Indicates whether users can use zero client devices to access their WorkSpaces.
*Required*: No
*Type*: String
*Allowed values*: `ALLOW | DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
