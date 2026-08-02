---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-qbusiness-webexperience-customizationconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QBusiness::WebExperience CustomizationConfiguration
<a name="aws-properties-qbusiness-webexperience-customizationconfiguration"></a>

Contains the configuration information to customize the logo, font, and color of an Amazon Q Business web experience with individual files for each property or a CSS file for them all.

## Syntax
<a name="aws-properties-qbusiness-webexperience-customizationconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-qbusiness-webexperience-customizationconfiguration-syntax.json"></a>

```
{
  "[CustomCSSUrl](#cfn-qbusiness-webexperience-customizationconfiguration-customcssurl)" : {{String}},
  "[FaviconUrl](#cfn-qbusiness-webexperience-customizationconfiguration-faviconurl)" : {{String}},
  "[FontUrl](#cfn-qbusiness-webexperience-customizationconfiguration-fonturl)" : {{String}},
  "[LogoUrl](#cfn-qbusiness-webexperience-customizationconfiguration-logourl)" : {{String}}
}
```

### YAML
<a name="aws-properties-qbusiness-webexperience-customizationconfiguration-syntax.yaml"></a>

```
  [CustomCSSUrl](#cfn-qbusiness-webexperience-customizationconfiguration-customcssurl): {{String}}
  [FaviconUrl](#cfn-qbusiness-webexperience-customizationconfiguration-faviconurl): {{String}}
  [FontUrl](#cfn-qbusiness-webexperience-customizationconfiguration-fonturl): {{String}}
  [LogoUrl](#cfn-qbusiness-webexperience-customizationconfiguration-logourl): {{String}}
```

## Properties
<a name="aws-properties-qbusiness-webexperience-customizationconfiguration-properties"></a>

`CustomCSSUrl`  <a name="cfn-qbusiness-webexperience-customizationconfiguration-customcssurl"></a>
Provides the URL where the custom CSS file is hosted for an Amazon Q web experience.
*Required*: No
*Type*: String
*Pattern*: `^(https?://[a-zA-Z0-9-_.+%/]+\.css)?$`
*Minimum*: `0`
*Maximum*: `1284`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FaviconUrl`  <a name="cfn-qbusiness-webexperience-customizationconfiguration-faviconurl"></a>
Provides the URL where the custom favicon file is hosted for an Amazon Q web experience.
*Required*: No
*Type*: String
*Pattern*: `^(https?://[a-zA-Z0-9-_.+%/]+\.(svg|ico))?$`
*Minimum*: `0`
*Maximum*: `1284`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FontUrl`  <a name="cfn-qbusiness-webexperience-customizationconfiguration-fonturl"></a>
Provides the URL where the custom font file is hosted for an Amazon Q web experience.
*Required*: No
*Type*: String
*Pattern*: `^(https?://[a-zA-Z0-9-_.+%/]+\.(ttf|woff|woff2|otf))?$`
*Minimum*: `0`
*Maximum*: `1284`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LogoUrl`  <a name="cfn-qbusiness-webexperience-customizationconfiguration-logourl"></a>
Provides the URL where the custom logo file is hosted for an Amazon Q web experience.
*Required*: No
*Type*: String
*Pattern*: `^(https?://[a-zA-Z0-9-_.+%/]+\.(svg|png))?$`
*Minimum*: `0`
*Maximum*: `1284`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
