---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-notifications-managednotificationaccountcontactassociation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Notifications::ManagedNotificationAccountContactAssociation
<a name="aws-resource-notifications-managednotificationaccountcontactassociation"></a>

Associates an Account Management Contact with a `ManagedNotificationConfiguration` for AWS User Notifications. For more information about AWS User Notifications, see the [AWS User Notifications User Guide](https://docs.aws.amazon.com/notifications/latest/userguide/what-is-service.html). For more information about Account Management Contacts, see the [AWS Account Management Reference Guide](https://docs.aws.amazon.com/accounts/latest/reference/API_AlternateContact.html).

## Syntax
<a name="aws-resource-notifications-managednotificationaccountcontactassociation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-notifications-managednotificationaccountcontactassociation-syntax.json"></a>

```
{
  "Type" : "AWS::Notifications::ManagedNotificationAccountContactAssociation",
  "Properties" : {
      "[ContactIdentifier](#cfn-notifications-managednotificationaccountcontactassociation-contactidentifier)" : {{String}},
      "[IsSensitiveEventsSubscribed](#cfn-notifications-managednotificationaccountcontactassociation-issensitiveeventssubscribed)" : {{Boolean}},
      "[ManagedNotificationConfigurationArn](#cfn-notifications-managednotificationaccountcontactassociation-managednotificationconfigurationarn)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-notifications-managednotificationaccountcontactassociation-syntax.yaml"></a>

```
Type: AWS::Notifications::ManagedNotificationAccountContactAssociation
Properties:
  [ContactIdentifier](#cfn-notifications-managednotificationaccountcontactassociation-contactidentifier): {{String}}
  [IsSensitiveEventsSubscribed](#cfn-notifications-managednotificationaccountcontactassociation-issensitiveeventssubscribed): {{Boolean}}
  [ManagedNotificationConfigurationArn](#cfn-notifications-managednotificationaccountcontactassociation-managednotificationconfigurationarn): {{String}}
```

## Properties
<a name="aws-resource-notifications-managednotificationaccountcontactassociation-properties"></a>

`ContactIdentifier`  <a name="cfn-notifications-managednotificationaccountcontactassociation-contactidentifier"></a>
The unique identifier of the notification contact associated with the AWS account. For more information about the contact types associated with an account, see the [AWS Account Management Reference Guide](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-update-contact-alternate.html#manage-acct-update-contact-alternate-orgs).
*Required*: Yes
*Type*: String
*Allowed values*: `ACCOUNT_PRIMARY | ACCOUNT_ALTERNATE_SECURITY | ACCOUNT_ALTERNATE_OPERATIONS | ACCOUNT_ALTERNATE_BILLING`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`IsSensitiveEventsSubscribed`  <a name="cfn-notifications-managednotificationaccountcontactassociation-issensitiveeventssubscribed"></a>
Property description not available.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ManagedNotificationConfigurationArn`  <a name="cfn-notifications-managednotificationaccountcontactassociation-managednotificationconfigurationarn"></a>
 The ARN of the `ManagedNotificationConfiguration` to be associated with the `Channel`.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:[a-z-]{3,10}:notifications::([0-9]{12}|):managed-notification-configuration/category/[a-zA-Z0-9\-]{3,64}/sub-category/[a-zA-Z0-9\-]{3,64}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-notifications-managednotificationaccountcontactassociation-return-values"></a>

### Ref
<a name="aws-resource-notifications-managednotificationaccountcontactassociation-return-values-ref"></a>

 When you pass the logical ID of this resource to the intrinsic Ref function, Ref returns the ARN of the configuration created.
