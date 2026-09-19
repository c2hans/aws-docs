---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datasync-locationazureblob-azureoidcconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataSync::LocationAzureBlob AzureOidcConfig
<a name="aws-properties-datasync-locationazureblob-azureoidcconfig"></a>

<a name="aws-properties-datasync-locationazureblob-azureoidcconfig-description"></a>The `AzureOidcConfig` property type specifies Property description not available. for an [AWS::DataSync::LocationAzureBlob](aws-resource-datasync-locationazureblob.md).

## Syntax
<a name="aws-properties-datasync-locationazureblob-azureoidcconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datasync-locationazureblob-azureoidcconfig-syntax.json"></a>

```
{
  "[ClientId](#cfn-datasync-locationazureblob-azureoidcconfig-clientid)" : {{String}},
  "[TenantId](#cfn-datasync-locationazureblob-azureoidcconfig-tenantid)" : {{String}}
}
```

### YAML
<a name="aws-properties-datasync-locationazureblob-azureoidcconfig-syntax.yaml"></a>

```
  [ClientId](#cfn-datasync-locationazureblob-azureoidcconfig-clientid): {{String}}
  [TenantId](#cfn-datasync-locationazureblob-azureoidcconfig-tenantid): {{String}}
```

## Properties
<a name="aws-properties-datasync-locationazureblob-azureoidcconfig-properties"></a>

`ClientId`  <a name="cfn-datasync-locationazureblob-azureoidcconfig-clientid"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$`
*Minimum*: `36`
*Maximum*: `36`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TenantId`  <a name="cfn-datasync-locationazureblob-azureoidcconfig-tenantid"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$`
*Minimum*: `36`
*Maximum*: `36`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
