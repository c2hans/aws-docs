---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-transfer-webapp-webappcustomization.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Transfer::WebApp WebAppCustomization
<a name="aws-properties-transfer-webapp-webappcustomization"></a>

A structure that contains the customization fields for the web app. You can provide a title, logo, and icon to customize the appearance of your web app.

## Syntax
<a name="aws-properties-transfer-webapp-webappcustomization-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-transfer-webapp-webappcustomization-syntax.json"></a>

```
{
  "[FaviconFile](#cfn-transfer-webapp-webappcustomization-faviconfile)" : {{String}},
  "[LogoFile](#cfn-transfer-webapp-webappcustomization-logofile)" : {{String}},
  "[Title](#cfn-transfer-webapp-webappcustomization-title)" : {{String}}
}
```

### YAML
<a name="aws-properties-transfer-webapp-webappcustomization-syntax.yaml"></a>

```
  [FaviconFile](#cfn-transfer-webapp-webappcustomization-faviconfile): {{String}}
  [LogoFile](#cfn-transfer-webapp-webappcustomization-logofile): {{String}}
  [Title](#cfn-transfer-webapp-webappcustomization-title): {{String}}
```

## Properties
<a name="aws-properties-transfer-webapp-webappcustomization-properties"></a>

`FaviconFile`  <a name="cfn-transfer-webapp-webappcustomization-faviconfile"></a>
Returns an icon file data string (in base64 encoding).
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `20960`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LogoFile`  <a name="cfn-transfer-webapp-webappcustomization-logofile"></a>
Returns a logo file data string (in base64 encoding).
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `51200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Title`  <a name="cfn-transfer-webapp-webappcustomization-title"></a>
Returns the page title that you defined for your web app.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
