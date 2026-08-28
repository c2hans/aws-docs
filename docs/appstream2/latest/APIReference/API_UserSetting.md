---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_UserSetting.html
---

# UserSetting
<a name="API_UserSetting"></a>

Describes an action and whether the action is enabled or disabled for users during their streaming sessions.

## Contents
<a name="API_UserSetting_Contents"></a>

 ** Action **   <a name="WorkSpacesApplications-Type-UserSetting-Action"></a>
The action that is enabled or disabled.
Type: String
Valid Values: `CLIPBOARD_COPY_FROM_LOCAL_DEVICE | CLIPBOARD_COPY_TO_LOCAL_DEVICE | FILE_UPLOAD | FILE_DOWNLOAD | PRINTING_TO_LOCAL_DEVICE | DOMAIN_PASSWORD_SIGNIN | DOMAIN_SMART_CARD_SIGNIN | AUTO_TIME_ZONE_REDIRECTION`
Required: Yes

 ** Permission **   <a name="WorkSpacesApplications-Type-UserSetting-Permission"></a>
Indicates whether the action is enabled or disabled.
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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
