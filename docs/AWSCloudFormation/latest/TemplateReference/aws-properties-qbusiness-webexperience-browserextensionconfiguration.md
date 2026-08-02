---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-qbusiness-webexperience-browserextensionconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QBusiness::WebExperience BrowserExtensionConfiguration
<a name="aws-properties-qbusiness-webexperience-browserextensionconfiguration"></a>

The container for browser extension configuration for an Amazon Q Business web experience.

## Syntax
<a name="aws-properties-qbusiness-webexperience-browserextensionconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-qbusiness-webexperience-browserextensionconfiguration-syntax.json"></a>

```
{
  "[EnabledBrowserExtensions](#cfn-qbusiness-webexperience-browserextensionconfiguration-enabledbrowserextensions)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-qbusiness-webexperience-browserextensionconfiguration-syntax.yaml"></a>

```
  [EnabledBrowserExtensions](#cfn-qbusiness-webexperience-browserextensionconfiguration-enabledbrowserextensions): {{
    - String}}
```

## Properties
<a name="aws-properties-qbusiness-webexperience-browserextensionconfiguration-properties"></a>

`EnabledBrowserExtensions`  <a name="cfn-qbusiness-webexperience-browserextensionconfiguration-enabledbrowserextensions"></a>
Specify the browser extensions allowed for your Amazon Q web experience.
+ `CHROME` — Enables the extension for Chromium-based browsers (Google Chrome, Microsoft Edge, Opera, etc.).
+ `FIREFOX` — Enables the extension for Mozilla Firefox.
+ `CHROME` and `FIREFOX` — Enable the extension for Chromium-based browsers and Mozilla Firefox.
*Required*: Yes
*Type*: Array of String
*Minimum*: `0`
*Maximum*: `2`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
