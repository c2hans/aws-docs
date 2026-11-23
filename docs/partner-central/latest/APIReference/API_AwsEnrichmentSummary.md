---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_AwsEnrichmentSummary.html
---

# AwsEnrichmentSummary

The AWS enrichment information for an account in search results. It carries a reduced set of fields compared to the enrichment information that `GetCustomerAccount` returns. Present only when `EnrichmentStatus` is `ENRICHED`.

## Contents
<a name="API_AwsEnrichmentSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Customer **   <a name="AWSPartnerCentral-Type-AwsEnrichmentSummary-Customer"></a>
Information about the customer that AWS provides.
Type: [AwsEnrichmentCustomerSummary](API_AwsEnrichmentCustomerSummary.md) object
Required: No

 ** Insights **   <a name="AWSPartnerCentral-Type-AwsEnrichmentSummary-Insights"></a>
Insights that AWS computes for the customer.
Type: [AwsEnrichmentInsightsSummary](API_AwsEnrichmentInsightsSummary.md) object
Required: No

## See Also
<a name="API_AwsEnrichmentSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/AwsEnrichmentSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/AwsEnrichmentSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/AwsEnrichmentSummary)
