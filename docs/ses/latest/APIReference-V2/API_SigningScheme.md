---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_SigningScheme.html
---

# SigningScheme
<a name="API_SigningScheme"></a>

Specifies the signing scheme to apply to messages sent with a configuration set. This is a union type, so you specify exactly one of its members.

## Contents
<a name="API_SigningScheme_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** DefaultScheme **   <a name="SES-Type-SigningScheme-DefaultScheme"></a>
Use the default signing behavior. When you select this option, Amazon SES API v2 doesn't add an S/MIME signature to messages sent with the configuration set.
Type: [DefaultSigningScheme](API_DefaultSigningScheme.md) object
Required: No

 ** SmimeScheme **   <a name="SES-Type-SigningScheme-SmimeScheme"></a>
Sign messages sent with the configuration set using S/MIME. For signing to apply, the email identity used to send a message must have an active S/MIME certificate association.
Type: [SmimeSigningScheme](API_SmimeSigningScheme.md) object
Required: No

## See Also
<a name="API_SigningScheme_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/SigningScheme)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/SigningScheme)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/SigningScheme)
