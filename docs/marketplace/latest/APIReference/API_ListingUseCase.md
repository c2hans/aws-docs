---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_ListingUseCase.html
---

# ListingUseCase

A use case from the AWS Marketplace use case taxonomy.

## Contents
<a name="API_ListingUseCase_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Group **   <a name="AWSMarketplaceService-Type-ListingUseCase-Group"></a>
The group of the use case in the taxonomy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** Id **   <a name="AWSMarketplaceService-Type-ListingUseCase-Id"></a>
The unique identifier of the use case.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** Name **   <a name="AWSMarketplaceService-Type-ListingUseCase-Name"></a>
The name of the use case.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** Rank **   <a name="AWSMarketplaceService-Type-ListingUseCase-Rank"></a>
The rank of the use case. A rank of 1 is the strongest match. Valid values range from 1 to 5.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 5.
Required: Yes

 ** Rationale **   <a name="AWSMarketplaceService-Type-ListingUseCase-Rationale"></a>
Why this use case is recommended.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: Yes

 ** Subgroup **   <a name="AWSMarketplaceService-Type-ListingUseCase-Subgroup"></a>
The subgroup of the use case in the taxonomy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** UseCaseDetails **   <a name="AWSMarketplaceService-Type-ListingUseCase-UseCaseDetails"></a>
How the solution serves the use case.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: No

## See Also
<a name="API_ListingUseCase_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-catalog-2018-09-17/ListingUseCase)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-catalog-2018-09-17/ListingUseCase)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-catalog-2018-09-17/ListingUseCase)
