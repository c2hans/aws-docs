---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_AwsOpportunityRelatedEntities.html
---

# AwsOpportunityRelatedEntities
<a name="API_AwsOpportunityRelatedEntities"></a>

Represents other entities related to the AWS opportunity, such as AWS products, partner solutions, and marketplace offers. These associations help build a complete picture of the solution being sold.

## Contents
<a name="API_AwsOpportunityRelatedEntities_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AwsProducts **   <a name="AWSPartnerCentral-Type-AwsOpportunityRelatedEntities-AwsProducts"></a>
Specifies the AWS products associated with the opportunity. This field helps track the specific products that are part of the proposed solution.
Type: Array of strings
Required: No

 ** Solutions **   <a name="AWSPartnerCentral-Type-AwsOpportunityRelatedEntities-Solutions"></a>
Specifies the partner solutions related to the opportunity. These solutions represent the partner's offerings that are being positioned as part of the overall AWS opportunity.
Type: Array of strings
Pattern: `S-[0-9]{1,19}`
Required: No

## See Also
<a name="API_AwsOpportunityRelatedEntities_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/AwsOpportunityRelatedEntities)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/AwsOpportunityRelatedEntities)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/AwsOpportunityRelatedEntities)
