---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_OpportunityQuality.html
---

# OpportunityQuality
<a name="API_OpportunityQuality"></a>

Opportunity quality score and trend.

## Contents
<a name="API_OpportunityQuality_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Score **   <a name="AWSPartnerCentral-Type-OpportunityQuality-Score"></a>
Deal quality score based on opportunity content completeness and sales methodology criteria. Values range from 0 to 100.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** Trend **   <a name="AWSPartnerCentral-Type-OpportunityQuality-Trend"></a>
Direction of score change since last scoring iteration. Known values: `Improving`, `Declining`, `No Change`.
Type: String
Required: No

## See Also
<a name="API_OpportunityQuality_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/OpportunityQuality)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/OpportunityQuality)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/OpportunityQuality)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Partner Central. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query partner-central` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
