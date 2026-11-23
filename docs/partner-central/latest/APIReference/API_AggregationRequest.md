---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_AggregationRequest.html
---

# AggregationRequest

Groups customer accounts by the values of a field.

## Contents
<a name="API_AggregationRequest_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** GroupBy **   <a name="AWSPartnerCentral-Type-AggregationRequest-GroupBy"></a>
The field to group the customer accounts by. Specify one field.
Type: Array of strings
Array Members: Fixed number of 1 item.
Valid Values: `ENRICHMENT_STATUS | AWS_INDUSTRY | SEGMENT | REGION | SOLUTION_CATEGORY | ACCOUNT_PLANNING_QUALIFICATION | PROGRAM_ELIGIBILITY | MARKETPLACE_ENGAGEMENT_SCORE | GEO | COUNTRY | SOLUTION_SCORE`
Required: Yes

## See Also
<a name="API_AggregationRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/AggregationRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/AggregationRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/AggregationRequest)
