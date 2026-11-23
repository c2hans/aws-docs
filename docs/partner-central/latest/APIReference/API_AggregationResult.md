---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_AggregationResult.html
---

# AggregationResult

The result of an aggregation. It includes the grouped field, the number of customer accounts for each value, and the number of accounts with other values.

## Contents
<a name="API_AggregationResult_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Buckets **   <a name="AWSPartnerCentral-Type-AggregationResult-Buckets"></a>
The groups of customer accounts, one for each value of the field, with the number of accounts in each group.
Type: Array of [Bucket](API_Bucket.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Required: Yes

 ** GroupBy **   <a name="AWSPartnerCentral-Type-AggregationResult-GroupBy"></a>
The field that the customer accounts are grouped by.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Valid Values: `ENRICHMENT_STATUS | AWS_INDUSTRY | SEGMENT | REGION | SOLUTION_CATEGORY | ACCOUNT_PLANNING_QUALIFICATION | PROGRAM_ELIGIBILITY | MARKETPLACE_ENGAGEMENT_SCORE | GEO | COUNTRY | SOLUTION_SCORE`
Required: Yes

 ** OtherCount **   <a name="AWSPartnerCentral-Type-AggregationResult-OtherCount"></a>
The number of customer accounts that have a value not included in `Buckets`.
Type: Integer
Required: Yes

## See Also
<a name="API_AggregationResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/AggregationResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/AggregationResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/AggregationResult)
