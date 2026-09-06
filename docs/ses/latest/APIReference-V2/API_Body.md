---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_Body.html
---

# Body
<a name="API_Body"></a>

Represents the body of the email message.

## Contents
<a name="API_Body_Contents"></a>

 ** Html **   <a name="SES-Type-Body-Html"></a>
An object that represents the version of the message that is displayed in email clients that support HTML. HTML messages can include formatted text, hyperlinks, images, and more.
Type: [Content](API_Content.md) object
Required: No

 ** Text **   <a name="SES-Type-Body-Text"></a>
An object that represents the version of the message that is displayed in email clients that don't support HTML, or clients where the recipient has disabled HTML rendering.
Type: [Content](API_Content.md) object
Required: No

## See Also
<a name="API_Body_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/Body)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/Body)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/Body)
