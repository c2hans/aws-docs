---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_FilterCondition.html
---

# FilterCondition

A single comparison in a filter. It names the field to compare and the value to compare it against.

## Contents
<a name="API_FilterCondition_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Key **   <a name="AWSPartnerCentral-Type-FilterCondition-Key"></a>
The field that the condition applies to.
Type: String
Valid Values: `ENRICHMENT_STATUS | COMPANY_NAME | AWS_INDUSTRY | ACCOUNT_PLANNING_QUALIFICATION | PROGRAM_ELIGIBILITY | IMPORT_ID | CREATED_DATE | LAST_MODIFIED_DATE | GEO | COUNTRY | SEGMENT | SOLUTION_CATEGORY | MARKETPLACE_ENGAGEMENT_SCORE | SOLUTION_SCORE`
Required: Yes

 ** Value **   <a name="AWSPartnerCentral-Type-FilterCondition-Value"></a>
The value that the condition compares the field against.
Type: [FilterValue](API_FilterValue.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

## See Also
<a name="API_FilterCondition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/FilterCondition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/FilterCondition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/FilterCondition)
