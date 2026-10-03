---
source_url: https://docs.aws.amazon.com/end-user-messaging/latest/APIReference/API_BrandProfileAttributeSummary.html
---

# BrandProfileAttributeSummary
<a name="API_BrandProfileAttributeSummary"></a>

Contains summary information about a brand profile attribute in a list response.

## Contents
<a name="API_BrandProfileAttributeSummary_Contents"></a>

 ** attributeName **   <a name="endusermessaging-Type-BrandProfileAttributeSummary-attributeName"></a>
The name of the brand profile attribute. The name is unique within a brand profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_ -]*[A-Za-z0-9_-][A-Za-z0-9_ -]*`
Required: Yes

 ** attributeType **   <a name="endusermessaging-Type-BrandProfileAttributeSummary-attributeType"></a>
The type of the attribute. TEXT stores an inline value. IMAGE and DOCUMENT store binary media that you upload.
Type: String
Valid Values: `TEXT | IMAGE | DOCUMENT`
Required: Yes

 ** createdAt **   <a name="endusermessaging-Type-BrandProfileAttributeSummary-createdAt"></a>
The time when the resource was created, in Unix epoch time.
Type: Timestamp
Required: Yes

 ** updatedAt **   <a name="endusermessaging-Type-BrandProfileAttributeSummary-updatedAt"></a>
The time when the resource was last updated, in Unix epoch time.
Type: Timestamp
Required: Yes

 ** category **   <a name="endusermessaging-Type-BrandProfileAttributeSummary-category"></a>
The category of the attribute.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** description **   <a name="endusermessaging-Type-BrandProfileAttributeSummary-description"></a>
A description of the attribute.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

## See Also
<a name="API_BrandProfileAttributeSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/endusermessaging-2026-09-21/BrandProfileAttributeSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/endusermessaging-2026-09-21/BrandProfileAttributeSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/endusermessaging-2026-09-21/BrandProfileAttributeSummary)
