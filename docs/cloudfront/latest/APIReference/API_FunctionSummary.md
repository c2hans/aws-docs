---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_FunctionSummary.html
---

# FunctionSummary
<a name="API_FunctionSummary"></a>

Contains configuration information and metadata about a CloudFront function.

## Contents
<a name="API_FunctionSummary_Contents"></a>

 ** FunctionConfig **   <a name="cloudfront-Type-FunctionSummary-FunctionConfig"></a>
Contains configuration information about a CloudFront function.
Type: [FunctionConfig](API_FunctionConfig.md) object
Required: Yes

 ** FunctionMetadata **   <a name="cloudfront-Type-FunctionSummary-FunctionMetadata"></a>
Contains metadata about a CloudFront function.
Type: [FunctionMetadata](API_FunctionMetadata.md) object
Required: Yes

 ** Name **   <a name="cloudfront-Type-FunctionSummary-Name"></a>
The name of the CloudFront function.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-_]{1,64}`
Required: Yes

 ** Status **   <a name="cloudfront-Type-FunctionSummary-Status"></a>
The status of the CloudFront function.
Type: String
Required: No

## See Also
<a name="API_FunctionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/FunctionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/FunctionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/FunctionSummary)
