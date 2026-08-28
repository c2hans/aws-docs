---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cognito-userpool-admincreateuserconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Cognito::UserPool AdminCreateUserConfig
<a name="aws-properties-cognito-userpool-admincreateuserconfig"></a>

The settings for administrator creation of users in a user pool. Contains settings for allowing user sign-up, customizing invitation messages to new users, and the amount of time before temporary passwords expire.

## Syntax
<a name="aws-properties-cognito-userpool-admincreateuserconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cognito-userpool-admincreateuserconfig-syntax.json"></a>

```
{
  "[AllowAdminCreateUserOnly](#cfn-cognito-userpool-admincreateuserconfig-allowadmincreateuseronly)" : {{Boolean}},
  "[InviteMessageTemplate](#cfn-cognito-userpool-admincreateuserconfig-invitemessagetemplate)" : {{InviteMessageTemplate}},
  "[UnusedAccountValidityDays](#cfn-cognito-userpool-admincreateuserconfig-unusedaccountvaliditydays)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-cognito-userpool-admincreateuserconfig-syntax.yaml"></a>

```
  [AllowAdminCreateUserOnly](#cfn-cognito-userpool-admincreateuserconfig-allowadmincreateuseronly): {{Boolean}}
  [InviteMessageTemplate](#cfn-cognito-userpool-admincreateuserconfig-invitemessagetemplate): {{
    InviteMessageTemplate}}
  [UnusedAccountValidityDays](#cfn-cognito-userpool-admincreateuserconfig-unusedaccountvaliditydays): {{Integer}}
```

## Properties
<a name="aws-properties-cognito-userpool-admincreateuserconfig-properties"></a>

`AllowAdminCreateUserOnly`  <a name="cfn-cognito-userpool-admincreateuserconfig-allowadmincreateuseronly"></a>
The setting for allowing self-service sign-up. When `true`, only administrators can create new user profiles. When `false`, users can register themselves and create a new user profile with the `SignUp` operation.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InviteMessageTemplate`  <a name="cfn-cognito-userpool-admincreateuserconfig-invitemessagetemplate"></a>
The template for the welcome message to new users. This template must include the `{####}` temporary password placeholder if you are creating users with passwords. If your users don't have passwords, you can omit the placeholder.
See also [Customizing User Invitation Messages](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-settings-message-customizations.html#cognito-user-pool-settings-user-invitation-message-customization).
*Required*: No
*Type*: [InviteMessageTemplate](aws-properties-cognito-userpool-invitemessagetemplate.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UnusedAccountValidityDays`  <a name="cfn-cognito-userpool-admincreateuserconfig-unusedaccountvaliditydays"></a>
This parameter is no longer in use.
The password expiration limit in days for administrator-created users. When this time expires, the user can't sign in with their temporary password. To reset the account after that time limit, you must call `AdminCreateUser` again, specifying `RESEND` for the `MessageAction` parameter.
The default value for this parameter is 7.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `365`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
