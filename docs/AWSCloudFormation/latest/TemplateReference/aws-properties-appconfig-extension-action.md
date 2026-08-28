---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appconfig-extension-action.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppConfig::Extension Action
<a name="aws-properties-appconfig-extension-action"></a>

The actions defined in the extension.

## Syntax
<a name="aws-properties-appconfig-extension-action-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appconfig-extension-action-syntax.json"></a>

```
{
  "[Description](#cfn-appconfig-extension-action-description)" : {{String}},
  "[Name](#cfn-appconfig-extension-action-name)" : {{String}},
  "[RoleArn](#cfn-appconfig-extension-action-rolearn)" : {{String}},
  "[Uri](#cfn-appconfig-extension-action-uri)" : {{String}}
}
```

### YAML
<a name="aws-properties-appconfig-extension-action-syntax.yaml"></a>

```
  [Description](#cfn-appconfig-extension-action-description): {{String}}
  [Name](#cfn-appconfig-extension-action-name): {{String}}
  [RoleArn](#cfn-appconfig-extension-action-rolearn): {{String}}
  [Uri](#cfn-appconfig-extension-action-uri): {{String}}
```

## Properties
<a name="aws-properties-appconfig-extension-action-properties"></a>

`Description`  <a name="cfn-appconfig-extension-action-description"></a>
Information about actions defined in the extension.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-appconfig-extension-action-name"></a>
The extension name.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleArn`  <a name="cfn-appconfig-extension-action-rolearn"></a>
An Amazon Resource Name (ARN) for an AWS Identity and Access Management assume role.
*Required*: No
*Type*: String
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Uri`  <a name="cfn-appconfig-extension-action-uri"></a>
The extension URI associated to the action point in the extension definition. The URI can be an Amazon Resource Name (ARN) for one of the following: an AWS Lambda function, an Amazon Simple Queue Service queue, an Amazon Simple Notification Service topic, or the Amazon EventBridge default event bus.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
