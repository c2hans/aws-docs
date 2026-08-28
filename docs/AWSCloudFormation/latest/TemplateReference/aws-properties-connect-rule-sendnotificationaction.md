---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-rule-sendnotificationaction.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::Rule SendNotificationAction
<a name="aws-properties-connect-rule-sendnotificationaction"></a>

Information about the send notification action.

## Syntax
<a name="aws-properties-connect-rule-sendnotificationaction-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-rule-sendnotificationaction-syntax.json"></a>

```
{
  "[Content](#cfn-connect-rule-sendnotificationaction-content)" : {{String}},
  "[ContentType](#cfn-connect-rule-sendnotificationaction-contenttype)" : {{String}},
  "[DeliveryMethod](#cfn-connect-rule-sendnotificationaction-deliverymethod)" : {{String}},
  "[Exclusion](#cfn-connect-rule-sendnotificationaction-exclusion)" : {{NotificationRecipientType}},
  "[Recipient](#cfn-connect-rule-sendnotificationaction-recipient)" : {{NotificationRecipientType}},
  "[Subject](#cfn-connect-rule-sendnotificationaction-subject)" : {{String}}
}
```

### YAML
<a name="aws-properties-connect-rule-sendnotificationaction-syntax.yaml"></a>

```
  [Content](#cfn-connect-rule-sendnotificationaction-content): {{String}}
  [ContentType](#cfn-connect-rule-sendnotificationaction-contenttype): {{String}}
  [DeliveryMethod](#cfn-connect-rule-sendnotificationaction-deliverymethod): {{String}}
  [Exclusion](#cfn-connect-rule-sendnotificationaction-exclusion): {{
    NotificationRecipientType}}
  [Recipient](#cfn-connect-rule-sendnotificationaction-recipient): {{
    NotificationRecipientType}}
  [Subject](#cfn-connect-rule-sendnotificationaction-subject): {{String}}
```

## Properties
<a name="aws-properties-connect-rule-sendnotificationaction-properties"></a>

`Content`  <a name="cfn-connect-rule-sendnotificationaction-content"></a>
Notification content. Supports variable injection. For more information, see [JSONPath reference](https://docs.aws.amazon.com/connect/latest/adminguide/contact-lens-variable-injection.html) in the *Connect Customer Administrators Guide*.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ContentType`  <a name="cfn-connect-rule-sendnotificationaction-contenttype"></a>
Content type format.
*Allowed value*: `PLAIN_TEXT`
*Required*: Yes
*Type*: String
*Allowed values*: `PLAIN_TEXT`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DeliveryMethod`  <a name="cfn-connect-rule-sendnotificationaction-deliverymethod"></a>
Notification delivery method.
*Allowed value*: `EMAIL`
*Required*: Yes
*Type*: String
*Allowed values*: `EMAIL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Exclusion`  <a name="cfn-connect-rule-sendnotificationaction-exclusion"></a>
Property description not available.
*Required*: No
*Type*: [NotificationRecipientType](aws-properties-connect-rule-notificationrecipienttype.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Recipient`  <a name="cfn-connect-rule-sendnotificationaction-recipient"></a>
Notification recipient.
*Required*: Yes
*Type*: [NotificationRecipientType](aws-properties-connect-rule-notificationrecipienttype.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Subject`  <a name="cfn-connect-rule-sendnotificationaction-subject"></a>
The subject of the email if the delivery method is `EMAIL`. Supports variable injection. For more information, see [JSONPath reference](https://docs.aws.amazon.com/connect/latest/adminguide/contact-lens-variable-injection.html) in the *Connect Customer Administrators Guide*.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
