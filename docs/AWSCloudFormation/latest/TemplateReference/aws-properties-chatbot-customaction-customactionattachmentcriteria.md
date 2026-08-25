---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-chatbot-customaction-customactionattachmentcriteria.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Chatbot::CustomAction CustomActionAttachmentCriteria
<a name="aws-properties-chatbot-customaction-customactionattachmentcriteria"></a>

**Note**
AWS Chatbot is now Amazon Q Developer. [Learn more](https://docs.aws.amazon.com/chatbot/latest/adminguide/service-rename.html)
`Type` attribute values remain unchanged.

A criteria for when a button should be shown based on values in the notification.

## Syntax
<a name="aws-properties-chatbot-customaction-customactionattachmentcriteria-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-chatbot-customaction-customactionattachmentcriteria-syntax.json"></a>

```
{
  "[Operator](#cfn-chatbot-customaction-customactionattachmentcriteria-operator)" : {{String}},
  "[Value](#cfn-chatbot-customaction-customactionattachmentcriteria-value)" : {{String}},
  "[VariableName](#cfn-chatbot-customaction-customactionattachmentcriteria-variablename)" : {{String}}
}
```

### YAML
<a name="aws-properties-chatbot-customaction-customactionattachmentcriteria-syntax.yaml"></a>

```
  [Operator](#cfn-chatbot-customaction-customactionattachmentcriteria-operator): {{String}}
  [Value](#cfn-chatbot-customaction-customactionattachmentcriteria-value): {{String}}
  [VariableName](#cfn-chatbot-customaction-customactionattachmentcriteria-variablename): {{String}}
```

## Properties
<a name="aws-properties-chatbot-customaction-customactionattachmentcriteria-properties"></a>

`Operator`  <a name="cfn-chatbot-customaction-customactionattachmentcriteria-operator"></a>
The operation to perform on the named variable.
*Required*: Yes
*Type*: String
*Allowed values*: `HAS_VALUE | EQUALS`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-chatbot-customaction-customactionattachmentcriteria-value"></a>
A value that is compared with the actual value of the variable based on the behavior of the operator.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VariableName`  <a name="cfn-chatbot-customaction-customactionattachmentcriteria-variablename"></a>
The name of the variable to operate on.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
