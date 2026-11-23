---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_AdditionalResource.html
---

# AdditionalResource

An additional resource for a listing, with its type, display text, and URL.

## Contents
<a name="API_AdditionalResource_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Text **   <a name="AWSMarketplaceService-Type-AdditionalResource-Text"></a>
The text to display for the resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

 ** Type **   <a name="AWSMarketplaceService-Type-AdditionalResource-Type"></a>
The type of the resource. Currently, the only value that the service returns is `Link`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** Url **   <a name="AWSMarketplaceService-Type-AdditionalResource-Url"></a>
The URL of the resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

## See Also
<a name="API_AdditionalResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-catalog-2018-09-17/AdditionalResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-catalog-2018-09-17/AdditionalResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-catalog-2018-09-17/AdditionalResource)
