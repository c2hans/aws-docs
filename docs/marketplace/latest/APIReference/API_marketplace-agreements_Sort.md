---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_Sort.html
---

# Sort
<a name="API_marketplace-agreements_Sort"></a>

An object that contains the `SortBy` and `SortOrder` attributes.

## Contents
<a name="API_marketplace-agreements_Sort_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** sortBy **   <a name="AWSMarketplaceService-Type-marketplace-agreements_Sort-sortBy"></a>
The attribute on which the data is grouped, which can be `EndTime`, `StartTime`, or `LastUpdateTime`. `StartTime` and `LastUpdateTime` are supported only when `PartyType` is `Proposer`. The default value is `EndTime`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[A-Za-z_]+`
Required: No

 ** sortOrder **   <a name="AWSMarketplaceService-Type-marketplace-agreements_Sort-sortOrder"></a>
The sorting order, which can be `ASCENDING` or `DESCENDING`. The default value is `ASCENDING`.
Type: String
Valid Values: `ASCENDING | DESCENDING`
Required: No

## See Also
<a name="API_marketplace-agreements_Sort_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-agreement-2020-03-01/Sort)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/Sort)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-agreement-2020-03-01/Sort)
