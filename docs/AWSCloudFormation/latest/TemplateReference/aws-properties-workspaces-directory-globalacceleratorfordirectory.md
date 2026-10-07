---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-workspaces-directory-globalacceleratorfordirectory.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WorkSpaces::Directory GlobalAcceleratorForDirectory
<a name="aws-properties-workspaces-directory-globalacceleratorfordirectory"></a>

Describes the Global Accelerator for directory

## Syntax
<a name="aws-properties-workspaces-directory-globalacceleratorfordirectory-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-workspaces-directory-globalacceleratorfordirectory-syntax.json"></a>

```
{
  "[Mode](#cfn-workspaces-directory-globalacceleratorfordirectory-mode)" : {{String}},
  "[PreferredProtocol](#cfn-workspaces-directory-globalacceleratorfordirectory-preferredprotocol)" : {{String}}
}
```

### YAML
<a name="aws-properties-workspaces-directory-globalacceleratorfordirectory-syntax.yaml"></a>

```
  [Mode](#cfn-workspaces-directory-globalacceleratorfordirectory-mode): {{String}}
  [PreferredProtocol](#cfn-workspaces-directory-globalacceleratorfordirectory-preferredprotocol): {{String}}
```

## Properties
<a name="aws-properties-workspaces-directory-globalacceleratorfordirectory-properties"></a>

`Mode`  <a name="cfn-workspaces-directory-globalacceleratorfordirectory-mode"></a>
Indicates if Global Accelerator for directory is enabled or disabled.
*Required*: Yes
*Type*: String
*Allowed values*: `ENABLED_AUTO | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PreferredProtocol`  <a name="cfn-workspaces-directory-globalacceleratorfordirectory-preferredprotocol"></a>
Indicates the preferred protocol for Global Accelerator.
*Required*: No
*Type*: String
*Allowed values*: `TCP | NONE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
