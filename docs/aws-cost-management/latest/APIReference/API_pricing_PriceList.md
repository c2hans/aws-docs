---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_pricing_PriceList.html
---

# PriceList
<a name="API_pricing_PriceList"></a>

This is the type of price list references that match your request.

## Contents
<a name="API_pricing_PriceList_Contents"></a>

 ** CurrencyCode **   <a name="awscostmanagement-Type-pricing_PriceList-CurrencyCode"></a>
The three alphabetical character ISO-4217 currency code the Price List files are denominated in.
Type: String
Pattern: `[A-Z]{3}`
Required: No

 ** FileFormats **   <a name="awscostmanagement-Type-pricing_PriceList-FileFormats"></a>
The format you want to retrieve your Price List files. The `FileFormat` can be obtained from the [`ListPriceList`](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_pricing_ListPriceLists.html) response.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** PriceListArn **   <a name="awscostmanagement-Type-pricing_PriceList-PriceListArn"></a>
The unique identifier that maps to where your Price List files are located. `PriceListArn` can be obtained from the [`ListPriceList`](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_pricing_ListPriceLists.html) response.
Type: String
Length Constraints: Minimum length of 18. Maximum length of 2048.
Pattern: `arn:[A-Za-z0-9][-.A-Za-z0-9]{0,62}:pricing:::price-list/[A-Za-z0-9+_/.-]{1,1023}`
Required: No

 ** RegionCode **   <a name="awscostmanagement-Type-pricing_PriceList-RegionCode"></a>
This is used to filter the Price List by AWS Region. For example, to get the price list only for the `US East (N. Virginia)` Region, use `us-east-1`. If nothing is specified, you retrieve price lists for all applicable Regions. The available `RegionCode` list can be retrieved from [`GetAttributeValues`](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_pricing_GetAttributeValues.html) API.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

## See Also
<a name="API_pricing_PriceList_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pricing-2017-10-15/PriceList)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pricing-2017-10-15/PriceList)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pricing-2017-10-15/PriceList)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
