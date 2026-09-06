---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-rum-appmonitor-deobfuscationconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RUM::AppMonitor DeobfuscationConfiguration
<a name="aws-properties-rum-appmonitor-deobfuscationconfiguration"></a>

 A structure that contains the configuration for how an app monitor can deobfuscate stack traces.

## Syntax
<a name="aws-properties-rum-appmonitor-deobfuscationconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-rum-appmonitor-deobfuscationconfiguration-syntax.json"></a>

```
{
  "[JavaScriptSourceMaps](#cfn-rum-appmonitor-deobfuscationconfiguration-javascriptsourcemaps)" : {{JavaScriptSourceMaps}}
}
```

### YAML
<a name="aws-properties-rum-appmonitor-deobfuscationconfiguration-syntax.yaml"></a>

```
  [JavaScriptSourceMaps](#cfn-rum-appmonitor-deobfuscationconfiguration-javascriptsourcemaps): {{
    JavaScriptSourceMaps}}
```

## Properties
<a name="aws-properties-rum-appmonitor-deobfuscationconfiguration-properties"></a>

`JavaScriptSourceMaps`  <a name="cfn-rum-appmonitor-deobfuscationconfiguration-javascriptsourcemaps"></a>
 A structure that contains the configuration for how an app monitor can unminify JavaScript error stack traces using source maps.
*Required*: No
*Type*: [JavaScriptSourceMaps](aws-properties-rum-appmonitor-javascriptsourcemaps.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
