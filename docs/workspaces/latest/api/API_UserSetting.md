---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_UserSetting.html
---

# UserSetting
<a name="API_UserSetting"></a>

Information about the user's permission settings.

## Contents
<a name="API_UserSetting_Contents"></a>

 ** Action **   <a name="WorkSpaces-Type-UserSetting-Action"></a>
Indicates the type of action.
Type: String
Valid Values: `CLIPBOARD_COPY_FROM_LOCAL_DEVICE | CLIPBOARD_COPY_TO_LOCAL_DEVICE | PRINTING_TO_LOCAL_DEVICE | SMART_CARD`
Required: Yes

 ** Permission **   <a name="WorkSpaces-Type-UserSetting-Permission"></a>
Indicates if the setting is enabled or disabled.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: Yes

 ** MaximumLength **   <a name="WorkSpaces-Type-UserSetting-MaximumLength"></a>
Indicates the maximum character length for the specified user setting.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_UserSetting_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/UserSetting)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/UserSetting)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/UserSetting)
