---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datasync-locationobjectstorage-googleoidcconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataSync::LocationObjectStorage GoogleOidcConfig
<a name="aws-properties-datasync-locationobjectstorage-googleoidcconfig"></a>

<a name="aws-properties-datasync-locationobjectstorage-googleoidcconfig-description"></a>The `GoogleOidcConfig` property type specifies Property description not available. for an [AWS::DataSync::LocationObjectStorage](aws-resource-datasync-locationobjectstorage.md).

## Syntax
<a name="aws-properties-datasync-locationobjectstorage-googleoidcconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datasync-locationobjectstorage-googleoidcconfig-syntax.json"></a>

```
{
  "[IdentityPoolName](#cfn-datasync-locationobjectstorage-googleoidcconfig-identitypoolname)" : {{String}},
  "[IdentityProviderName](#cfn-datasync-locationobjectstorage-googleoidcconfig-identityprovidername)" : {{String}},
  "[ProjectName](#cfn-datasync-locationobjectstorage-googleoidcconfig-projectname)" : {{String}},
  "[ProjectNumber](#cfn-datasync-locationobjectstorage-googleoidcconfig-projectnumber)" : {{String}}
}
```

### YAML
<a name="aws-properties-datasync-locationobjectstorage-googleoidcconfig-syntax.yaml"></a>

```
  [IdentityPoolName](#cfn-datasync-locationobjectstorage-googleoidcconfig-identitypoolname): {{String}}
  [IdentityProviderName](#cfn-datasync-locationobjectstorage-googleoidcconfig-identityprovidername): {{String}}
  [ProjectName](#cfn-datasync-locationobjectstorage-googleoidcconfig-projectname): {{String}}
  [ProjectNumber](#cfn-datasync-locationobjectstorage-googleoidcconfig-projectnumber): {{String}}
```

## Properties
<a name="aws-properties-datasync-locationobjectstorage-googleoidcconfig-properties"></a>

`IdentityPoolName`  <a name="cfn-datasync-locationobjectstorage-googleoidcconfig-identitypoolname"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^(?!gcp-)[a-z][a-z0-9-]{2,30}[a-z0-9]$`
*Minimum*: `4`
*Maximum*: `32`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IdentityProviderName`  <a name="cfn-datasync-locationobjectstorage-googleoidcconfig-identityprovidername"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^(?!gcp-)[a-z][a-z0-9-]{2,30}[a-z0-9]$`
*Minimum*: `4`
*Maximum*: `32`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProjectName`  <a name="cfn-datasync-locationobjectstorage-googleoidcconfig-projectname"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-z][a-z0-9-]{4,28}[a-z0-9]$`
*Minimum*: `6`
*Maximum*: `30`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProjectNumber`  <a name="cfn-datasync-locationobjectstorage-googleoidcconfig-projectnumber"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9]+$`
*Minimum*: `1`
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
