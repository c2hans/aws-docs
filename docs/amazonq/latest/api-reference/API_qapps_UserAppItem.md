---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_UserAppItem.html
---

# UserAppItem
<a name="API_qapps_UserAppItem"></a>

An Amazon Q App associated with a user, either owned by the user or favorited.

## Contents
<a name="API_qapps_UserAppItem_Contents"></a>

 ** appArn **   <a name="qbusiness-Type-qapps_UserAppItem-appArn"></a>
The Amazon Resource Name (ARN) of the Q App.
Type: String
Required: Yes

 ** appId **   <a name="qbusiness-Type-qapps_UserAppItem-appId"></a>
The unique identifier of the Q App.
Type: String
Pattern: `[\da-f]{8}-[\da-f]{4}-[45][\da-f]{3}-[89ABab][\da-f]{3}-[\da-f]{12}`
Required: Yes

 ** createdAt **   <a name="qbusiness-Type-qapps_UserAppItem-createdAt"></a>
The date and time the user's association with the Q App was created.
Type: Timestamp
Required: Yes

 ** title **   <a name="qbusiness-Type-qapps_UserAppItem-title"></a>
The title of the Q App.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Pattern: `[^{}\\"<>]+`
Required: Yes

 ** canEdit **   <a name="qbusiness-Type-qapps_UserAppItem-canEdit"></a>
A flag indicating whether the user can edit the Q App.
Type: Boolean
Required: No

 ** description **   <a name="qbusiness-Type-qapps_UserAppItem-description"></a>
The description of the Q App.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Required: No

 ** isVerified **   <a name="qbusiness-Type-qapps_UserAppItem-isVerified"></a>
Indicates whether the Q App has been verified.
Type: Boolean
Required: No

 ** status **   <a name="qbusiness-Type-qapps_UserAppItem-status"></a>
The status of the user's association with the Q App.
Type: String
Required: No

## See Also
<a name="API_qapps_UserAppItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qapps-2023-11-27/UserAppItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qapps-2023-11-27/UserAppItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qapps-2023-11-27/UserAppItem)
