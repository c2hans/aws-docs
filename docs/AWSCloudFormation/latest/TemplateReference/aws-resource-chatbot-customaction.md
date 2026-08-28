---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-chatbot-customaction.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Chatbot::CustomAction
<a name="aws-resource-chatbot-customaction"></a>

**Note**
AWS Chatbot is now Amazon Q Developer. [Learn more](https://docs.aws.amazon.com/chatbot/latest/adminguide/service-rename.html)
`Type` attribute values remain unchanged.

## Syntax
<a name="aws-resource-chatbot-customaction-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-chatbot-customaction-syntax.json"></a>

```
{
  "Type" : "AWS::Chatbot::CustomAction",
  "Properties" : {
      "[ActionName](#cfn-chatbot-customaction-actionname)" : {{String}},
      "[AliasName](#cfn-chatbot-customaction-aliasname)" : {{String}},
      "[Attachments](#cfn-chatbot-customaction-attachments)" : {{[ CustomActionAttachment, ... ]}},
      "[Definition](#cfn-chatbot-customaction-definition)" : {{CustomActionDefinition}},
      "[Tags](#cfn-chatbot-customaction-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-chatbot-customaction-syntax.yaml"></a>

```
Type: AWS::Chatbot::CustomAction
Properties:
  [ActionName](#cfn-chatbot-customaction-actionname): {{String}}
  [AliasName](#cfn-chatbot-customaction-aliasname): {{String}}
  [Attachments](#cfn-chatbot-customaction-attachments): {{
    - CustomActionAttachment}}
  [Definition](#cfn-chatbot-customaction-definition): {{
    CustomActionDefinition}}
  [Tags](#cfn-chatbot-customaction-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-chatbot-customaction-properties"></a>

`ActionName`  <a name="cfn-chatbot-customaction-actionname"></a>
The name of the custom action. This name is included in the Amazon Resource Name (ARN).
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_-]{1,64}$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`AliasName`  <a name="cfn-chatbot-customaction-aliasname"></a>
The name used to invoke this action in a chat channel. For example, `@Amazon Q run my-alias`.
*Required*: No
*Type*: String
*Pattern*: `^[A-Za-z0-9-_]+$`
*Minimum*: `1`
*Maximum*: `30`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Attachments`  <a name="cfn-chatbot-customaction-attachments"></a>
Defines when this custom action button should be attached to a notification.
*Required*: No
*Type*: Array of [CustomActionAttachment](aws-properties-chatbot-customaction-customactionattachment.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Definition`  <a name="cfn-chatbot-customaction-definition"></a>
The definition of the command to run when invoked as an alias or as an action button.
*Required*: Yes
*Type*: [CustomActionDefinition](aws-properties-chatbot-customaction-customactiondefinition.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-chatbot-customaction-tags"></a>
The tags to add to the configuration.
*Required*: No
*Type*: Array of [Tag](aws-properties-chatbot-customaction-tag.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-chatbot-customaction-return-values"></a>

### Ref
<a name="aws-resource-chatbot-customaction-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic Ref function, Ref returns the ARN of the configuration created.

### Fn::GetAtt
<a name="aws-resource-chatbot-customaction-return-values-fn--getatt"></a>

####
<a name="aws-resource-chatbot-customaction-return-values-fn--getatt-fn--getatt"></a>

`CustomActionArn`  <a name="CustomActionArn-fn::getatt"></a>
The fully defined ARN of the custom action.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
