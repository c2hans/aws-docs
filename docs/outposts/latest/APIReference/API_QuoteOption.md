---
source_url: https://docs.aws.amazon.com/outposts/latest/APIReference/API_QuoteOption.html
---

# QuoteOption
<a name="API_QuoteOption"></a>

A configuration and pricing option for a quote. Each option includes the capacity breakdown, physical specifications for the racks or servers, and pricing details.

## Contents
<a name="API_QuoteOption_Contents"></a>

 ** Capacities **   <a name="outposts-Type-QuoteOption-Capacities"></a>
The capacities included in this quote option.
Type: Array of [QuoteCapacity](API_QuoteCapacity.md) objects
Array Members: Maximum number of 2000 items.
Required: No

 ** CapacitySummary **   <a name="outposts-Type-QuoteOption-CapacitySummary"></a>
A summary of the existing, final, and changed capacity for this quote option.
Type: [CapacitySummary](API_CapacitySummary.md) object
Required: No

 ** PricingOptions **   <a name="outposts-Type-QuoteOption-PricingOptions"></a>
The pricing options for this quote option.
Type: Array of [PricingOption](API_PricingOption.md) objects
Array Members: Maximum number of 9 items.
Required: No

 ** QuoteOptionIdentifier **   <a name="outposts-Type-QuoteOption-QuoteOptionIdentifier"></a>
The ID of the quote option.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 21.
Pattern: `^oqo-[a-f0-9]{17}$`
Required: No

 ** Specifications **   <a name="outposts-Type-QuoteOption-Specifications"></a>
The physical specifications for the racks or servers in this quote option.
Type: Array of [QuoteSpecification](API_QuoteSpecification.md) objects
Array Members: Maximum number of 100 items.
Required: No

## See Also
<a name="API_QuoteOption_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/outposts-2019-12-03/QuoteOption)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/outposts-2019-12-03/QuoteOption)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/outposts-2019-12-03/QuoteOption)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Outposts. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query outposts` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
