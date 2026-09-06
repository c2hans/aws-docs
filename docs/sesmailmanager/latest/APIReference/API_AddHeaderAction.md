---
source_url: https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_AddHeaderAction.html
---

# AddHeaderAction
<a name="API_AddHeaderAction"></a>

The action to add a header to a message. When executed, this action will add the given header to the message.

## Contents
<a name="API_AddHeaderAction_Contents"></a>

 ** HeaderName **   <a name="sesmailmanager-Type-AddHeaderAction-HeaderName"></a>
The name of the header to add to an email. The header must be prefixed with "X-". Headers are added regardless of whether the header name pre-existed in the email.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[xX]\-[a-zA-Z0-9\-]+`
Required: Yes

 ** HeaderValue **   <a name="sesmailmanager-Type-AddHeaderAction-HeaderValue"></a>
The value of the header to add to the email.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

## See Also
<a name="API_AddHeaderAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mailmanager-2023-10-17/AddHeaderAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mailmanager-2023-10-17/AddHeaderAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mailmanager-2023-10-17/AddHeaderAction)
