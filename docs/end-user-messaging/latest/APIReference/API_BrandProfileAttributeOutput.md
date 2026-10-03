---
source_url: https://docs.aws.amazon.com/end-user-messaging/latest/APIReference/API_BrandProfileAttributeOutput.html
---

# BrandProfileAttributeOutput
<a name="API_BrandProfileAttributeOutput"></a>

Contains information about an attribute that was created for a brand profile.

## Contents
<a name="API_BrandProfileAttributeOutput_Contents"></a>

 ** attributeName **   <a name="endusermessaging-Type-BrandProfileAttributeOutput-attributeName"></a>
The name of the brand profile attribute. The name is unique within a brand profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_ -]*[A-Za-z0-9_-][A-Za-z0-9_ -]*`
Required: Yes

 ** attributeType **   <a name="endusermessaging-Type-BrandProfileAttributeOutput-attributeType"></a>
The type of the attribute. TEXT stores an inline value. IMAGE and DOCUMENT store binary media that you upload.
Type: String
Valid Values: `TEXT | IMAGE | DOCUMENT`
Required: Yes

 ** mediaDownloadUrl **   <a name="endusermessaging-Type-BrandProfileAttributeOutput-mediaDownloadUrl"></a>
A presigned Amazon S3 URL that you can use to download the attribute media. The URL is valid for one hour and is present only for attributes of type IMAGE or DOCUMENT.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

## See Also
<a name="API_BrandProfileAttributeOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/endusermessaging-2026-09-21/BrandProfileAttributeOutput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/endusermessaging-2026-09-21/BrandProfileAttributeOutput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/endusermessaging-2026-09-21/BrandProfileAttributeOutput)
