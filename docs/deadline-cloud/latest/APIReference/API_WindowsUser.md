---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_WindowsUser.html
---

# WindowsUser
<a name="API_WindowsUser"></a>

The Windows user details.

## Contents
<a name="API_WindowsUser_Contents"></a>

 ** passwordArn **   <a name="deadlinecloud-Type-WindowsUser-passwordArn"></a>
The password ARN for the Windows user.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:(aws[a-zA-Z-]*):secretsmanager:[a-z]{2}((-gov)|(-iso(b?)))?-[a-z]+-\d{1}:\d{12}:secret:[a-zA-Z0-9-/_+=.@]{1,2028}`
Required: Yes

 ** user **   <a name="deadlinecloud-Type-WindowsUser-user"></a>
The user.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 111.
Pattern: `[^"'/\[\]:;|=,+*?<>\s]*`
Required: Yes

## See Also
<a name="API_WindowsUser_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/WindowsUser)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/WindowsUser)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/WindowsUser)
