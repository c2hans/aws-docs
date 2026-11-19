---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_UserSetting.html
---

# UserSetting

Describes an action and whether the action is enabled or disabled for users during their streaming sessions.

## Contents
<a name="API_UserSetting_Contents"></a>

 ** Action **   <a name="WorkSpacesApplications-Type-UserSetting-Action"></a>
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
Type: String
Valid Values: `CLIPBOARD_COPY_FROM_LOCAL_DEVICE | CLIPBOARD_COPY_TO_LOCAL_DEVICE | FILE_UPLOAD | FILE_DOWNLOAD | PRINTING_TO_LOCAL_DEVICE | DOMAIN_PASSWORD_SIGNIN | DOMAIN_SMART_CARD_SIGNIN | AUTO_TIME_ZONE_REDIRECTION | SMART_CARD_REDIRECTION`
Required: Yes

 ** Permission **   <a name="WorkSpacesApplications-Type-UserSetting-Permission"></a>
Specifies whether to turn the action on or off.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: Yes

 ** MaximumLength **   <a name="WorkSpacesApplications-Type-UserSetting-MaximumLength"></a>
Specifies the number of characters that can be copied by end users from the local device to the remote session, and to the local device from the remote session.
This can be specified only for the `CLIPBOARD_COPY_FROM_LOCAL_DEVICE` and `CLIPBOARD_COPY_TO_LOCAL_DEVICE` actions.
This defaults to 20,971,520 (20 MB) when unspecified and the permission is `ENABLED`. This can't be specified when the permission is `DISABLED`.
The value can be between 1 and 20,971,520 (20 MB).
Type: Integer
Required: No

## See Also
<a name="API_UserSetting_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/UserSetting)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/UserSetting)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/UserSetting)
