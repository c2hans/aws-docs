---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-notificationscontacts-emailcontact.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::NotificationsContacts::EmailContact
<a name="aws-resource-notificationscontacts-emailcontact"></a>

Configures email contacts for AWS User Notifications.

## Syntax
<a name="aws-resource-notificationscontacts-emailcontact-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-notificationscontacts-emailcontact-syntax.json"></a>

```
{
  "Type" : "AWS::NotificationsContacts::EmailContact",
  "Properties" : {
      "[EmailAddress](#cfn-notificationscontacts-emailcontact-emailaddress)" : {{String}},
      "[Name](#cfn-notificationscontacts-emailcontact-name)" : {{String}},
      "[Tags](#cfn-notificationscontacts-emailcontact-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-notificationscontacts-emailcontact-syntax.yaml"></a>

```
Type: AWS::NotificationsContacts::EmailContact
Properties:
  [EmailAddress](#cfn-notificationscontacts-emailcontact-emailaddress): {{String}}
  [Name](#cfn-notificationscontacts-emailcontact-name): {{String}}
  [Tags](#cfn-notificationscontacts-emailcontact-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-notificationscontacts-emailcontact-properties"></a>

`EmailAddress`  <a name="cfn-notificationscontacts-emailcontact-emailaddress"></a>
The email address of the contact. The activation and notification emails are sent here.
*Required*: Yes
*Type*: String
*Pattern*: `^(.+)@(.+)$`
*Minimum*: `6`
*Maximum*: `254`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-notificationscontacts-emailcontact-name"></a>
The name of the contact.
*Required*: Yes
*Type*: String
*Pattern*: `[\w-.~]+`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-notificationscontacts-emailcontact-tags"></a>
A list of tags to apply to the email contact.
*Required*: No
*Type*: Array of [Tag](aws-properties-notificationscontacts-emailcontact-tag.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-notificationscontacts-emailcontact-return-values"></a>

### Ref
<a name="aws-resource-notificationscontacts-emailcontact-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic Ref function, Ref returns the Amazon Resource Name (ARN) of the configuration created.

### Fn::GetAtt
<a name="aws-resource-notificationscontacts-emailcontact-return-values-fn--getatt"></a>

####
<a name="aws-resource-notificationscontacts-emailcontact-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Returns the ARN of the contact.

`EmailContact.Address`  <a name="EmailContact.Address-fn::getatt"></a>
Returns the email address that the contact points to.

`EmailContact.Arn`  <a name="EmailContact.Arn-fn::getatt"></a>
Returns the ARN of the contact.

`EmailContact.CreationTime`  <a name="EmailContact.CreationTime-fn::getatt"></a>
Returns the creation time of the resource.

`EmailContact.Name`  <a name="EmailContact.Name-fn::getatt"></a>
Returns the name of the contact.

`EmailContact.Status`  <a name="EmailContact.Status-fn::getatt"></a>
Returns the status of the contact.

`EmailContact.UpdateTime`  <a name="EmailContact.UpdateTime-fn::getatt"></a>
Returns the time the resource was last updated.
