---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-workspaces-directory-storageconnector.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WorkSpaces::Directory StorageConnector
<a name="aws-properties-workspaces-directory-storageconnector"></a>

Describes the storage connector.

## Syntax
<a name="aws-properties-workspaces-directory-storageconnector-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-workspaces-directory-storageconnector-syntax.json"></a>

```
{
  "[ConnectorType](#cfn-workspaces-directory-storageconnector-connectortype)" : {{String}},
  "[Status](#cfn-workspaces-directory-storageconnector-status)" : {{String}}
}
```

### YAML
<a name="aws-properties-workspaces-directory-storageconnector-syntax.yaml"></a>

```
  [ConnectorType](#cfn-workspaces-directory-storageconnector-connectortype): {{String}}
  [Status](#cfn-workspaces-directory-storageconnector-status): {{String}}
```

## Properties
<a name="aws-properties-workspaces-directory-storageconnector-properties"></a>

`ConnectorType`  <a name="cfn-workspaces-directory-storageconnector-connectortype"></a>
The type of connector used to save user files.
*Required*: Yes
*Type*: String
*Allowed values*: `HOME_FOLDER`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Status`  <a name="cfn-workspaces-directory-storageconnector-status"></a>
Indicates if the storage connetor is enabled or disabled.
*Required*: Yes
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
