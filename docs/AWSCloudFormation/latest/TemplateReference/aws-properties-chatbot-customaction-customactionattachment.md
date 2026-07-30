---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-chatbot-customaction-customactionattachment.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Chatbot::CustomAction CustomActionAttachment
<a name="aws-properties-chatbot-customaction-customactionattachment"></a>

**Note**
AWS Chatbot is now Amazon Q Developer. [Learn more](https://docs.aws.amazon.com//chatbot/latest/adminguide/service-rename.html)
`Type` attribute values remain unchanged.

Defines when a custom action button should be attached to a notification.

## Syntax
<a name="aws-properties-chatbot-customaction-customactionattachment-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-chatbot-customaction-customactionattachment-syntax.json"></a>

```
{
  "[ButtonText](#cfn-chatbot-customaction-customactionattachment-buttontext)" : {{String}},
  "[Criteria](#cfn-chatbot-customaction-customactionattachment-criteria)" : {{[ CustomActionAttachmentCriteria, ... ]}},
  "[NotificationType](#cfn-chatbot-customaction-customactionattachment-notificationtype)" : {{String}},
  "[Variables](#cfn-chatbot-customaction-customactionattachment-variables)" : {{{{{Key}}: {{Value}}, ...}}}
}
```

### YAML
<a name="aws-properties-chatbot-customaction-customactionattachment-syntax.yaml"></a>

```
  [ButtonText](#cfn-chatbot-customaction-customactionattachment-buttontext): {{String}}
  [Criteria](#cfn-chatbot-customaction-customactionattachment-criteria): {{
    - CustomActionAttachmentCriteria}}
  [NotificationType](#cfn-chatbot-customaction-customactionattachment-notificationtype): {{String}}
  [Variables](#cfn-chatbot-customaction-customactionattachment-variables): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-properties-chatbot-customaction-customactionattachment-properties"></a>

`ButtonText`  <a name="cfn-chatbot-customaction-customactionattachment-buttontext"></a>
The text of the button that appears on the notification.
*Required*: No
*Type*: String
*Pattern*: `^[\S\s]+$`
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Criteria`  <a name="cfn-chatbot-customaction-customactionattachment-criteria"></a>
The criteria for when a button should be shown based on values in the notification.
*Required*: No
*Type*: Array of [CustomActionAttachmentCriteria](aws-properties-chatbot-customaction-customactionattachmentcriteria.md)
*Minimum*: `1`
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NotificationType`  <a name="cfn-chatbot-customaction-customactionattachment-notificationtype"></a>
The type of notification that the custom action should be attached to.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9-]+$`
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Variables`  <a name="cfn-chatbot-customaction-customactionattachment-variables"></a>
The variables to extract from the notification.
*Required*: No
*Type*: Object of String
*Pattern*: `.+`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
