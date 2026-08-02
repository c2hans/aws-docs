---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sso-applicationprovider-displaydata.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SSO::ApplicationProvider DisplayData
<a name="aws-properties-sso-applicationprovider-displaydata"></a>

A structure that describes how the portal represents an application provider.

## Syntax
<a name="aws-properties-sso-applicationprovider-displaydata-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sso-applicationprovider-displaydata-syntax.json"></a>

```
{
  "[Description](#cfn-sso-applicationprovider-displaydata-description)" : {{String}},
  "[DisplayName](#cfn-sso-applicationprovider-displaydata-displayname)" : {{String}},
  "[IconUrl](#cfn-sso-applicationprovider-displaydata-iconurl)" : {{String}}
}
```

### YAML
<a name="aws-properties-sso-applicationprovider-displaydata-syntax.yaml"></a>

```
  [Description](#cfn-sso-applicationprovider-displaydata-description): {{String}}
  [DisplayName](#cfn-sso-applicationprovider-displaydata-displayname): {{String}}
  [IconUrl](#cfn-sso-applicationprovider-displaydata-iconurl): {{String}}
```

## Properties
<a name="aws-properties-sso-applicationprovider-displaydata-properties"></a>

`Description`  <a name="cfn-sso-applicationprovider-displaydata-description"></a>
The description of the application provider that appears in the portal.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DisplayName`  <a name="cfn-sso-applicationprovider-displaydata-displayname"></a>
The name of the application provider that appears in the portal.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IconUrl`  <a name="cfn-sso-applicationprovider-displaydata-iconurl"></a>
A URL that points to an icon that represents the application provider.
*Required*: No
*Type*: String
*Pattern*: `^(http|https):\/\/.*$`
*Minimum*: `1`
*Maximum*: `768`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
