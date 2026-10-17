---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-rule-sendinappnotificationaction.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::Rule SendInAppNotificationAction
<a name="aws-properties-connect-rule-sendinappnotificationaction"></a>

<a name="aws-properties-connect-rule-sendinappnotificationaction-description"></a>The `SendInAppNotificationAction` property type specifies Property description not available. for an [AWS::Connect::Rule](aws-resource-connect-rule.md).

## Syntax
<a name="aws-properties-connect-rule-sendinappnotificationaction-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-rule-sendinappnotificationaction-syntax.json"></a>

```
{
  "[Content](#cfn-connect-rule-sendinappnotificationaction-content)" : {{NotificationContent}},
  "[Exclusion](#cfn-connect-rule-sendinappnotificationaction-exclusion)" : {{InAppNotificationRecipientType}},
  "[Priority](#cfn-connect-rule-sendinappnotificationaction-priority)" : {{String}},
  "[Recipient](#cfn-connect-rule-sendinappnotificationaction-recipient)" : {{InAppNotificationRecipientType}}
}
```

### YAML
<a name="aws-properties-connect-rule-sendinappnotificationaction-syntax.yaml"></a>

```
  [Content](#cfn-connect-rule-sendinappnotificationaction-content): {{
    NotificationContent}}
  [Exclusion](#cfn-connect-rule-sendinappnotificationaction-exclusion): {{
    InAppNotificationRecipientType}}
  [Priority](#cfn-connect-rule-sendinappnotificationaction-priority): {{String}}
  [Recipient](#cfn-connect-rule-sendinappnotificationaction-recipient): {{
    InAppNotificationRecipientType}}
```

## Properties
<a name="aws-properties-connect-rule-sendinappnotificationaction-properties"></a>

`Content`  <a name="cfn-connect-rule-sendinappnotificationaction-content"></a>
Property description not available.
*Required*: Yes
*Type*: [NotificationContent](aws-properties-connect-rule-notificationcontent.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Exclusion`  <a name="cfn-connect-rule-sendinappnotificationaction-exclusion"></a>
Property description not available.
*Required*: No
*Type*: [InAppNotificationRecipientType](aws-properties-connect-rule-inappnotificationrecipienttype.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Priority`  <a name="cfn-connect-rule-sendinappnotificationaction-priority"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `HIGH | LOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Recipient`  <a name="cfn-connect-rule-sendinappnotificationaction-recipient"></a>
Property description not available.
*Required*: Yes
*Type*: [InAppNotificationRecipientType](aws-properties-connect-rule-inappnotificationrecipienttype.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
