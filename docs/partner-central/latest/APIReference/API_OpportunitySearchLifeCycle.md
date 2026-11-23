---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_OpportunitySearchLifeCycle.html
---

# OpportunitySearchLifeCycle

Contains the lifecycle fields (review status, stage, next steps, and target close date) returned for an opportunity in search results.

## Contents
<a name="API_OpportunitySearchLifeCycle_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** NextSteps **   <a name="AWSPartnerCentral-Type-OpportunitySearchLifeCycle-NextSteps"></a>
The next steps for the opportunity. Mandatory for co-sell opportunities.
Type: String
Pattern: `(?s).{0,255}`
Required: No

 ** ReviewStatus **   <a name="AWSPartnerCentral-Type-OpportunitySearchLifeCycle-ReviewStatus"></a>
The approval status of the opportunity.
Type: String
Valid Values: `Pending Submission | Submitted | In review | Approved | Rejected | Action Required`
Required: No

 ** Stage **   <a name="AWSPartnerCentral-Type-OpportunitySearchLifeCycle-Stage"></a>
The stage of the opportunity.
Type: String
Valid Values: `Prospect | Qualified | Technical Validation | Business Validation | Committed | Launched | Closed Lost`
Required: No

 ** TargetCloseDate **   <a name="AWSPartnerCentral-Type-OpportunitySearchLifeCycle-TargetCloseDate"></a>
The projected launch date of the opportunity, in ISO 8601 (YYYY-MM-DD) format.
Type: String
Pattern: `[1-9][0-9]{3}-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])`
Required: No

## See Also
<a name="API_OpportunitySearchLifeCycle_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/OpportunitySearchLifeCycle)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/OpportunitySearchLifeCycle)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/OpportunitySearchLifeCycle)
