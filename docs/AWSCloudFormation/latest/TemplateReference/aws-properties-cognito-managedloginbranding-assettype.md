---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cognito-managedloginbranding-assettype.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Cognito::ManagedLoginBranding AssetType
<a name="aws-properties-cognito-managedloginbranding-assettype"></a>

An image file from a managed login branding style in a user pool.

## Syntax
<a name="aws-properties-cognito-managedloginbranding-assettype-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cognito-managedloginbranding-assettype-syntax.json"></a>

```
{
  "[Bytes](#cfn-cognito-managedloginbranding-assettype-bytes)" : {{String}},
  "[Category](#cfn-cognito-managedloginbranding-assettype-category)" : {{String}},
  "[ColorMode](#cfn-cognito-managedloginbranding-assettype-colormode)" : {{String}},
  "[Extension](#cfn-cognito-managedloginbranding-assettype-extension)" : {{String}},
  "[ResourceId](#cfn-cognito-managedloginbranding-assettype-resourceid)" : {{String}}
}
```

### YAML
<a name="aws-properties-cognito-managedloginbranding-assettype-syntax.yaml"></a>

```
  [Bytes](#cfn-cognito-managedloginbranding-assettype-bytes): {{String}}
  [Category](#cfn-cognito-managedloginbranding-assettype-category): {{String}}
  [ColorMode](#cfn-cognito-managedloginbranding-assettype-colormode): {{String}}
  [Extension](#cfn-cognito-managedloginbranding-assettype-extension): {{String}}
  [ResourceId](#cfn-cognito-managedloginbranding-assettype-resourceid): {{String}}
```

## Properties
<a name="aws-properties-cognito-managedloginbranding-assettype-properties"></a>

`Bytes`  <a name="cfn-cognito-managedloginbranding-assettype-bytes"></a>
The image file, in Base64-encoded binary.
*Required*: No
*Type*: String
*Maximum*: `1000000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Category`  <a name="cfn-cognito-managedloginbranding-assettype-category"></a>
The category that the image corresponds to in your managed login configuration. Managed login has asset categories for different types of logos, backgrounds, and icons.
*Required*: Yes
*Type*: String
*Allowed values*: `FAVICON_ICO | FAVICON_SVG | EMAIL_GRAPHIC | SMS_GRAPHIC | AUTH_APP_GRAPHIC | PASSWORD_GRAPHIC | PASSKEY_GRAPHIC | PAGE_HEADER_LOGO | PAGE_HEADER_BACKGROUND | PAGE_FOOTER_LOGO | PAGE_FOOTER_BACKGROUND | PAGE_BACKGROUND | FORM_BACKGROUND | FORM_LOGO | IDP_BUTTON_ICON`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ColorMode`  <a name="cfn-cognito-managedloginbranding-assettype-colormode"></a>
The display-mode target of the asset: light, dark, or browser-adaptive. For example, Amazon Cognito displays a dark-mode image only when the browser or application is in dark mode, but displays a browser-adaptive file in all contexts.
*Required*: Yes
*Type*: String
*Allowed values*: `LIGHT | DARK | DYNAMIC`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Extension`  <a name="cfn-cognito-managedloginbranding-assettype-extension"></a>
The file type of the image file.
*Required*: Yes
*Type*: String
*Allowed values*: `ICO | JPEG | PNG | SVG | WEBP`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceId`  <a name="cfn-cognito-managedloginbranding-assettype-resourceid"></a>
The ID of the asset.
*Required*: No
*Type*: String
*Pattern*: `^[\w\- ]+$`
*Minimum*: `1`
*Maximum*: `40`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
