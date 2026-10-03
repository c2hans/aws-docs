---
source_url: https://docs.aws.amazon.com/end-user-messaging/latest/APIReference/API_BrandProfileAttributeInput.html
---

# BrandProfileAttributeInput
<a name="API_BrandProfileAttributeInput"></a>

Specifies an attribute to create for a brand profile.

## Contents
<a name="API_BrandProfileAttributeInput_Contents"></a>

 ** attributeName **   <a name="endusermessaging-Type-BrandProfileAttributeInput-attributeName"></a>
The name of the brand profile attribute. The name is unique within a brand profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_ -]*[A-Za-z0-9_-][A-Za-z0-9_ -]*`
Required: Yes

 ** attributeType **   <a name="endusermessaging-Type-BrandProfileAttributeInput-attributeType"></a>
The type of the attribute. TEXT stores an inline value. IMAGE and DOCUMENT store binary media that you upload.
Type: String
Valid Values: `TEXT | IMAGE | DOCUMENT`
Required: Yes

 ** attachmentBody **   <a name="endusermessaging-Type-BrandProfileAttributeInput-attachmentBody"></a>
The binary content for an attribute of type IMAGE or DOCUMENT. The content is base64-encoded when it is sent over the wire.
Type: Base64-encoded binary data object
Length Constraints: Minimum length of 1. Maximum length of 5242880.
Required: No

 ** attributeValue **   <a name="endusermessaging-Type-BrandProfileAttributeInput-attributeValue"></a>
The text value for the attribute. This value applies to attributes of type TEXT. For attributes of type IMAGE or DOCUMENT, provide the media through the attachment body instead.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.
Required: No

 ** category **   <a name="endusermessaging-Type-BrandProfileAttributeInput-category"></a>
The category of the attribute.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** description **   <a name="endusermessaging-Type-BrandProfileAttributeInput-description"></a>
A description of the attribute.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

## See Also
<a name="API_BrandProfileAttributeInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/endusermessaging-2026-09-21/BrandProfileAttributeInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/endusermessaging-2026-09-21/BrandProfileAttributeInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/endusermessaging-2026-09-21/BrandProfileAttributeInput)
