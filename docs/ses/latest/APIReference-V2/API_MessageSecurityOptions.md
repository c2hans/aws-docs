---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_MessageSecurityOptions.html
---

# MessageSecurityOptions
<a name="API_MessageSecurityOptions"></a>

An object that defines the message-level security options that apply to messages that you send using the configuration set. Currently, these options determine whether Amazon SES API v2 adds an S/MIME signature to your messages and, if so, the format of that signature.

## Contents
<a name="API_MessageSecurityOptions_Contents"></a>

 ** SigningScheme **   <a name="SES-Type-MessageSecurityOptions-SigningScheme"></a>
The signing scheme that Amazon SES API v2 applies to messages sent with the configuration set.
Type: [SigningScheme](API_SigningScheme.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## See Also
<a name="API_MessageSecurityOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/MessageSecurityOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/MessageSecurityOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/MessageSecurityOptions)
