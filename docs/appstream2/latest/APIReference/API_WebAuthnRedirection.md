---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_WebAuthnRedirection.html
---

# WebAuthnRedirection

Describes the WebAuthn redirection configuration for a stack. With WebAuthn redirection, your users can complete passkey and security-key authentication from a streaming session by using an authenticator attached to their local device.

## Contents
<a name="API_WebAuthnRedirection_Contents"></a>

 ** Enabled **   <a name="WorkSpacesApplications-Type-WebAuthnRedirection-Enabled"></a>
Specifies whether WebAuthn redirection is enabled for the stack.
Type: Boolean
Required: Yes

 ** ProcessCompatibilityList **   <a name="WorkSpacesApplications-Type-WebAuthnRedirection-ProcessCompatibilityList"></a>
The list of process executable names for which you enable WebAuthn redirection. For example, chrome.exe.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 260.
Pattern: `^[\p{L}0-9_](?:[\p{L}0-9._ ()+-]*[\p{L}0-9._()+-])?(?<!\.[eE][xX][eE])\.[eE][xX][eE]$`
Required: No

## See Also
<a name="API_WebAuthnRedirection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/WebAuthnRedirection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/WebAuthnRedirection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/WebAuthnRedirection)
