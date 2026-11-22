---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appstream-stack-usersetting.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppStream::Stack UserSetting

Specifies an action and whether the action is enabled or disabled for users during their streaming sessions.

## Syntax
<a name="aws-properties-appstream-stack-usersetting-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appstream-stack-usersetting-syntax.json"></a>

```json
{
  "[Action](#cfn-appstream-stack-usersetting-action)" : {{String}},
  "[MaximumLength](#cfn-appstream-stack-usersetting-maximumlength)" : {{Integer}},
  "[Permission](#cfn-appstream-stack-usersetting-permission)" : {{String}}
}
```

### YAML
<a name="aws-properties-appstream-stack-usersetting-syntax.yaml"></a>

```yaml
  [Action](#cfn-appstream-stack-usersetting-action): {{String}}
  [MaximumLength](#cfn-appstream-stack-usersetting-maximumlength): {{Integer}}
  [Permission](#cfn-appstream-stack-usersetting-permission): {{String}}
```

## Properties
<a name="aws-properties-appstream-stack-usersetting-properties"></a>

`Action`  <a name="cfn-appstream-stack-usersetting-action"></a>
The action you want to enable or disable. Choose from the following:
AUTO\_TIME\_ZONE\_REDIRECTION
Controls whether the streaming session's time zone matches the time zone of your local device.
CLIPBOARD\_COPY\_FROM\_LOCAL\_DEVICE
Controls whether you can copy data from your local device and paste it into the streaming session.
CLIPBOARD\_COPY\_TO\_LOCAL\_DEVICE
Controls whether you can copy data from the streaming session and paste it to your local device.
DOMAIN\_PASSWORD\_SIGNIN
Controls whether you can sign in to a domain-joined streaming session by using your password.
DOMAIN\_SMART\_CARD\_SIGNIN
Controls whether you can sign in to a domain-joined streaming session by using a smart card.
FILE\_DOWNLOAD
Controls whether you can download files from the streaming session to your local device.
FILE\_UPLOAD
Controls whether you can upload files from your local device to the streaming session.
PRINTING\_TO\_LOCAL\_DEVICE
Controls whether you can print from the streaming session to a printer on your local device.
SMART\_CARD\_REDIRECTION
Controls whether smart cards connected to your local device are redirected into the streaming session. Applications in the session can access the local smart card for use cases such as authentication, digital signing, and email encryption.
Smart card redirection was on by default for existing streaming sessions that use a Windows single-session fleet. To preserve that behavior, `SMART_CARD_REDIRECTION` is `ENABLED` by default on existing stacks associated with Windows single-session fleets. To turn it off, call `UpdateStack` with `SMART_CARD_REDIRECTION` set to `DISABLED`, and use an image that includes the latest WorkSpaces Applications agent version.
*Required*: Yes
*Type*: String
*Allowed values*: `CLIPBOARD_COPY_FROM_LOCAL_DEVICE | CLIPBOARD_COPY_TO_LOCAL_DEVICE | FILE_UPLOAD | FILE_DOWNLOAD | PRINTING_TO_LOCAL_DEVICE | DOMAIN_PASSWORD_SIGNIN | DOMAIN_SMART_CARD_SIGNIN | AUTO_TIME_ZONE_REDIRECTION | SMART_CARD_REDIRECTION`
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
Specifies whether to turn the action on or off.
*Required*: Yes
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
