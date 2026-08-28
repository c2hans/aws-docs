---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-notificationscontacts-emailcontact-emailcontact.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::NotificationsContacts::EmailContact EmailContact
<a name="aws-properties-notificationscontacts-emailcontact-emailcontact"></a>

Configures email contacts for AWS User Notifications. You must activate the email contact using the activation token that you will receive when the email contact is set up.

## Syntax
<a name="aws-properties-notificationscontacts-emailcontact-emailcontact-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-notificationscontacts-emailcontact-emailcontact-syntax.json"></a>

```
{
  "[Address](#cfn-notificationscontacts-emailcontact-emailcontact-address)" : {{String}},
  "[Arn](#cfn-notificationscontacts-emailcontact-emailcontact-arn)" : {{String}},
  "[CreationTime](#cfn-notificationscontacts-emailcontact-emailcontact-creationtime)" : {{String}},
  "[Name](#cfn-notificationscontacts-emailcontact-emailcontact-name)" : {{String}},
  "[Status](#cfn-notificationscontacts-emailcontact-emailcontact-status)" : {{String}},
  "[UpdateTime](#cfn-notificationscontacts-emailcontact-emailcontact-updatetime)" : {{String}}
}
```

### YAML
<a name="aws-properties-notificationscontacts-emailcontact-emailcontact-syntax.yaml"></a>

```
  [Address](#cfn-notificationscontacts-emailcontact-emailcontact-address): {{String}}
  [Arn](#cfn-notificationscontacts-emailcontact-emailcontact-arn): {{String}}
  [CreationTime](#cfn-notificationscontacts-emailcontact-emailcontact-creationtime): {{String}}
  [Name](#cfn-notificationscontacts-emailcontact-emailcontact-name): {{String}}
  [Status](#cfn-notificationscontacts-emailcontact-emailcontact-status): {{String}}
  [UpdateTime](#cfn-notificationscontacts-emailcontact-emailcontact-updatetime): {{String}}
```

## Properties
<a name="aws-properties-notificationscontacts-emailcontact-emailcontact-properties"></a>

`Address`  <a name="cfn-notificationscontacts-emailcontact-emailcontact-address"></a>
The email address of the contact.
*Required*: Yes
*Type*: String
*Pattern*: `^(.+)@(.+)$`
*Minimum*: `6`
*Maximum*: `254`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Arn`  <a name="cfn-notificationscontacts-emailcontact-emailcontact-arn"></a>
The Amazon Resource Name (ARN) of the contact.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws:notifications-contacts::[0-9]{12}:emailcontact/[a-z0-9]{27}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreationTime`  <a name="cfn-notificationscontacts-emailcontact-emailcontact-creationtime"></a>
The creation time of the `EmailContact`.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-notificationscontacts-emailcontact-emailcontact-name"></a>
The name of the contact.
*Required*: Yes
*Type*: String
*Pattern*: `[\w-.~]+`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Status`  <a name="cfn-notificationscontacts-emailcontact-emailcontact-status"></a>
The status of the contact. Only activated contacts receive emails.
*Required*: Yes
*Type*: String
*Allowed values*: `inactive | active`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UpdateTime`  <a name="cfn-notificationscontacts-emailcontact-emailcontact-updatetime"></a>
The time the `EmailContact` was last updated.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
