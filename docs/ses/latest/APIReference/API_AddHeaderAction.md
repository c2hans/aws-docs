---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference/API_AddHeaderAction.html
---

# AddHeaderAction
<a name="API_AddHeaderAction"></a>

When included in a receipt rule, this action adds a header to the received email.

For information about adding a header using a receipt rule, see the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/dg/receiving-email-action-add-header.html).

## Contents
<a name="API_AddHeaderAction_Contents"></a>

 ** HeaderName **
The name of the header to add to the incoming message. The name must contain at least one character, and can contain up to 50 characters. It consists of alphanumeric (a–z, A–Z, 0–9) characters and dashes.
Type: String
Required: Yes

 ** HeaderValue **
The content to include in the header. This value can contain up to 2048 characters. It can't contain newline (`\n`) or carriage return (`\r`) characters.
Type: String
Required: Yes

## See Also
<a name="API_AddHeaderAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/email-2010-12-01/AddHeaderAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/email-2010-12-01/AddHeaderAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/email-2010-12-01/AddHeaderAction)
