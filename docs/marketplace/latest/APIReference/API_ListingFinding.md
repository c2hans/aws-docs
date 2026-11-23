---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_ListingFinding.html
---

# ListingFinding

One row of the checklist of criteria for a listing field. A row is either a criterion that the field already meets or advice for a criterion that it doesn't.

## Contents
<a name="API_ListingFinding_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Action **   <a name="AWSMarketplaceService-Type-ListingFinding-Action"></a>
What you should do to meet the criterion.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: Yes

 ** Description **   <a name="AWSMarketplaceService-Type-ListingFinding-Description"></a>
What the criterion asks for. The text is the same for every listing. The reasoning for a specific listing is in the rationale of the alternatives.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

 ** Severity **   <a name="AWSMarketplaceService-Type-ListingFinding-Severity"></a>
How much the criterion blocks the listing. It is set on every row. For a row with a status of `PASS`, it is the weight of a criterion that is already met. Valid values are `BLOCKING` and `ADVISORY`.
Type: String
Valid Values: `BLOCKING | ADVISORY`
Required: Yes

 ** Status **   <a name="AWSMarketplaceService-Type-ListingFinding-Status"></a>
The result for the criterion. Valid values are:
+  `PASS` - The criterion is met and no action is needed.
+  `FAIL` - The criterion isn't met or wasn't scored.
This value is different from the status of the content recommendation.
Type: String
Valid Values: `PASS | FAIL`
Required: Yes

## See Also
<a name="API_ListingFinding_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-catalog-2018-09-17/ListingFinding)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-catalog-2018-09-17/ListingFinding)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-catalog-2018-09-17/ListingFinding)
