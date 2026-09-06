---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-appstream-user.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppStream::User
<a name="aws-resource-appstream-user"></a>

The `AWS::AppStream::User` resource creates a new user in the WorkSpaces Applications user pool.

## Syntax
<a name="aws-resource-appstream-user-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-appstream-user-syntax.json"></a>

```
{
  "Type" : "AWS::AppStream::User",
  "Properties" : {
      "[AuthenticationType](#cfn-appstream-user-authenticationtype)" : {{String}},
      "[FirstName](#cfn-appstream-user-firstname)" : {{String}},
      "[LastName](#cfn-appstream-user-lastname)" : {{String}},
      "[MessageAction](#cfn-appstream-user-messageaction)" : {{String}},
      "[UserName](#cfn-appstream-user-username)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-appstream-user-syntax.yaml"></a>

```
Type: AWS::AppStream::User
Properties:
  [AuthenticationType](#cfn-appstream-user-authenticationtype): {{String}}
  [FirstName](#cfn-appstream-user-firstname): {{String}}
  [LastName](#cfn-appstream-user-lastname): {{String}}
  [MessageAction](#cfn-appstream-user-messageaction): {{String}}
  [UserName](#cfn-appstream-user-username): {{String}}
```

## Properties
<a name="aws-resource-appstream-user-properties"></a>

`AuthenticationType`  <a name="cfn-appstream-user-authenticationtype"></a>
The authentication type for the user. You must specify USERPOOL.
*Required*: Yes
*Type*: String
*Allowed values*: `API | SAML | USERPOOL | AWS_AD`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`FirstName`  <a name="cfn-appstream-user-firstname"></a>
The first name, or given name, of the user.
*Required*: No
*Type*: String
*Pattern*: `^[A-Za-z0-9_\-\s]+$`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`LastName`  <a name="cfn-appstream-user-lastname"></a>
The last name, or surname, of the user.
*Required*: No
*Type*: String
*Pattern*: `^[A-Za-z0-9_\-\s]+$`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MessageAction`  <a name="cfn-appstream-user-messageaction"></a>
The action to take for the welcome email that is sent to a user after the user is created in the user pool. If you specify SUPPRESS, no email is sent. If you specify RESEND, do not specify the first name or last name of the user. If the value is null, the email is sent.
The temporary password in the welcome email is valid for only 7 days. If users don’t set their passwords within 7 days, you must send them a new welcome email.
*Required*: No
*Type*: String
*Allowed values*: `SUPPRESS | RESEND`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`UserName`  <a name="cfn-appstream-user-username"></a>
The email address of the user.
Users' email addresses are case-sensitive. During login, if they specify an email address that doesn't use the same capitalization as the email address specified when their user pool account was created, a "user does not exist" error message displays.
*Required*: Yes
*Type*: String
*Pattern*: `[\p{L}\p{M}\p{S}\p{N}\p{P}]+`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also
<a name="aws-resource-appstream-user--seealso"></a>
+ [CreateUser](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_CreateUser.html) in the *Amazon WorkSpaces Applications API Reference*
