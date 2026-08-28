---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appstream-stack-usersetting.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppStream::Stack UserSetting
<a name="aws-properties-appstream-stack-usersetting"></a>

Specifies an action and whether the action is enabled or disabled for users during their streaming sessions.

## Syntax
<a name="aws-properties-appstream-stack-usersetting-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appstream-stack-usersetting-syntax.json"></a>

```
{
  "[Action](#cfn-appstream-stack-usersetting-action)" : {{String}},
  "[MaximumLength](#cfn-appstream-stack-usersetting-maximumlength)" : {{Integer}},
  "[Permission](#cfn-appstream-stack-usersetting-permission)" : {{String}}
}
```

### YAML
<a name="aws-properties-appstream-stack-usersetting-syntax.yaml"></a>

```
  [Action](#cfn-appstream-stack-usersetting-action): {{String}}
  [MaximumLength](#cfn-appstream-stack-usersetting-maximumlength): {{Integer}}
  [Permission](#cfn-appstream-stack-usersetting-permission): {{String}}
```

## Properties
<a name="aws-properties-appstream-stack-usersetting-properties"></a>

`Action`  <a name="cfn-appstream-stack-usersetting-action"></a>
The action that is enabled or disabled.
*Required*: Yes
*Type*: String
*Allowed values*: `CLIPBOARD_COPY_FROM_LOCAL_DEVICE | CLIPBOARD_COPY_TO_LOCAL_DEVICE | FILE_UPLOAD | FILE_DOWNLOAD | PRINTING_TO_LOCAL_DEVICE | DOMAIN_PASSWORD_SIGNIN | DOMAIN_SMART_CARD_SIGNIN | AUTO_TIME_ZONE_REDIRECTION`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaximumLength`  <a name="cfn-appstream-stack-usersetting-maximumlength"></a>
Specifies the number of characters that can be copied by end users from the local device to the remote session, and to the local device from the remote session.
This can be specified only for the `CLIPBOARD_COPY_FROM_LOCAL_DEVICE` and `CLIPBOARD_COPY_TO_LOCAL_DEVICE` actions.
This defaults to 20,971,520 (20 MB) when unspecified and the permission is `ENABLED`. This can't be specified when the permission is `DISABLED`.
The value can be between 1 and 20,971,520 (20 MB).
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Permission`  <a name="cfn-appstream-stack-usersetting-permission"></a>
Indicates whether the action is enabled or disabled.
*Required*: Yes
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
