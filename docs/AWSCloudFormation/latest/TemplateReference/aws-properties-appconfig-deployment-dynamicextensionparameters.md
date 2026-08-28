---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appconfig-deployment-dynamicextensionparameters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppConfig::Deployment DynamicExtensionParameters
<a name="aws-properties-appconfig-deployment-dynamicextensionparameters"></a>

A map of dynamic extension parameter names to values to pass to associated extensions with `PRE_START_DEPLOYMENT` actions.

## Syntax
<a name="aws-properties-appconfig-deployment-dynamicextensionparameters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appconfig-deployment-dynamicextensionparameters-syntax.json"></a>

```
{
  "[ExtensionReference](#cfn-appconfig-deployment-dynamicextensionparameters-extensionreference)" : {{String}},
  "[ParameterName](#cfn-appconfig-deployment-dynamicextensionparameters-parametername)" : {{String}},
  "[ParameterValue](#cfn-appconfig-deployment-dynamicextensionparameters-parametervalue)" : {{String}}
}
```

### YAML
<a name="aws-properties-appconfig-deployment-dynamicextensionparameters-syntax.yaml"></a>

```
  [ExtensionReference](#cfn-appconfig-deployment-dynamicextensionparameters-extensionreference): {{String}}
  [ParameterName](#cfn-appconfig-deployment-dynamicextensionparameters-parametername): {{String}}
  [ParameterValue](#cfn-appconfig-deployment-dynamicextensionparameters-parametervalue): {{String}}
```

## Properties
<a name="aws-properties-appconfig-deployment-dynamicextensionparameters-properties"></a>

`ExtensionReference`  <a name="cfn-appconfig-deployment-dynamicextensionparameters-extensionreference"></a>
The ARN or ID of the extension for which you are inserting a dynamic parameter.
*Required*: No
*Type*: String
*Pattern*: `arn:(aws[a-zA-Z-]*)?:[a-z]+:((eusc-)?[a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1})?:(\d{12})?:[a-zA-Z0-9-_/:.]+`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ParameterName`  <a name="cfn-appconfig-deployment-dynamicextensionparameters-parametername"></a>
The parameter name.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ParameterValue`  <a name="cfn-appconfig-deployment-dynamicextensionparameters-parametervalue"></a>
The parameter value.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
