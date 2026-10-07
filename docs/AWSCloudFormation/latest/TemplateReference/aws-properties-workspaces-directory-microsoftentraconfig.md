---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-workspaces-directory-microsoftentraconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WorkSpaces::Directory MicrosoftEntraConfig
<a name="aws-properties-workspaces-directory-microsoftentraconfig"></a>

Specifies the configurations of the Microsoft Entra.

## Syntax
<a name="aws-properties-workspaces-directory-microsoftentraconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-workspaces-directory-microsoftentraconfig-syntax.json"></a>

```
{
  "[ApplicationConfigSecretArn](#cfn-workspaces-directory-microsoftentraconfig-applicationconfigsecretarn)" : {{String}},
  "[TenantId](#cfn-workspaces-directory-microsoftentraconfig-tenantid)" : {{String}}
}
```

### YAML
<a name="aws-properties-workspaces-directory-microsoftentraconfig-syntax.yaml"></a>

```
  [ApplicationConfigSecretArn](#cfn-workspaces-directory-microsoftentraconfig-applicationconfigsecretarn): {{String}}
  [TenantId](#cfn-workspaces-directory-microsoftentraconfig-tenantid): {{String}}
```

## Properties
<a name="aws-properties-workspaces-directory-microsoftentraconfig-properties"></a>

`ApplicationConfigSecretArn`  <a name="cfn-workspaces-directory-microsoftentraconfig-applicationconfigsecretarn"></a>
The Amazon Resource Name (ARN) of the application config.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws[a-z-]{0,7}:secretsmanager:[A-za-z0-9_/.-]{0,63}:[A-za-z0-9_/.-]{0,63}:secret:[A-Za-z0-9][A-za-z0-9_/.-]{8,519}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TenantId`  <a name="cfn-workspaces-directory-microsoftentraconfig-tenantid"></a>
The identifier of the tenant.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9-]{1,100}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
