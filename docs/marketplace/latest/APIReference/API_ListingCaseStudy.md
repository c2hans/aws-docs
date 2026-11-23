---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_ListingCaseStudy.html
---

# ListingCaseStudy

A recommended case study.

## Contents
<a name="API_ListingCaseStudy_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Id **   <a name="AWSMarketplaceService-Type-ListingCaseStudy-Id"></a>
The ID of the case study entity. Identify a case study by this ID and not by `Title`, which you can edit.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z0-9][.a-zA-Z0-9/-]+[a-zA-Z0-9]$`
Required: Yes

 ** Rationale **   <a name="AWSMarketplaceService-Type-ListingCaseStudy-Rationale"></a>
Why this case study was selected.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: Yes

 ** Title **   <a name="AWSMarketplaceService-Type-ListingCaseStudy-Title"></a>
The title of the case study.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Required: Yes

## See Also
<a name="API_ListingCaseStudy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-catalog-2018-09-17/ListingCaseStudy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-catalog-2018-09-17/ListingCaseStudy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-catalog-2018-09-17/ListingCaseStudy)
