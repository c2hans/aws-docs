---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appconfig-extension-parameter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppConfig::Extension Parameter
<a name="aws-properties-appconfig-extension-parameter"></a>

A value such as an Amazon Resource Name (ARN) or an Amazon Simple Notification Service topic entered in an extension when invoked. Parameter values are specified in an extension association. For more information about extensions, see [Extending workflows](https://docs.aws.amazon.com/appconfig/latest/userguide/working-with-appconfig-extensions.html) in the *AWS AppConfig User Guide*.

## Syntax
<a name="aws-properties-appconfig-extension-parameter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appconfig-extension-parameter-syntax.json"></a>

```
{
  "[Description](#cfn-appconfig-extension-parameter-description)" : {{String}},
  "[Dynamic](#cfn-appconfig-extension-parameter-dynamic)" : {{Boolean}},
  "[Required](#cfn-appconfig-extension-parameter-required)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-appconfig-extension-parameter-syntax.yaml"></a>

```
  [Description](#cfn-appconfig-extension-parameter-description): {{String}}
  [Dynamic](#cfn-appconfig-extension-parameter-dynamic): {{Boolean}}
  [Required](#cfn-appconfig-extension-parameter-required): {{Boolean}}
```

## Properties
<a name="aws-properties-appconfig-extension-parameter-properties"></a>

`Description`  <a name="cfn-appconfig-extension-parameter-description"></a>
Information about the parameter.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Dynamic`  <a name="cfn-appconfig-extension-parameter-dynamic"></a>
Indicates whether this parameter's value can be supplied at the extension's action point instead of during extension association. Dynamic parameters can't be marked `Required`.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Required`  <a name="cfn-appconfig-extension-parameter-required"></a>
A parameter value must be specified in the extension association.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
