---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_OpportunitySearchProject.html
---

# OpportunitySearchProject

Contains the project fields (title, AWS Partner Network (APN) programs, and expected customer spend) returned for an opportunity in search results.

## Contents
<a name="API_OpportunitySearchProject_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ApnPrograms **   <a name="AWSPartnerCentral-Type-OpportunitySearchProject-ApnPrograms"></a>
The AWS Partner Network (APN) programs associated with the opportunity's products or services.
Type: Array of strings
Required: No

 ** ExpectedCustomerSpend **   <a name="AWSPartnerCentral-Type-OpportunitySearchProject-ExpectedCustomerSpend"></a>
The estimated AWS monthly recurring revenue (MRR): amount and currency only.
Type: Array of [OpportunitySearchExpectedCustomerSpend](API_OpportunitySearchExpectedCustomerSpend.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** Title **   <a name="AWSPartnerCentral-Type-OpportunitySearchProject-Title"></a>
The partner opportunity name.
Type: String
Pattern: `(?s).{0,255}`
Required: No

## See Also
<a name="API_OpportunitySearchProject_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/OpportunitySearchProject)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/OpportunitySearchProject)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/OpportunitySearchProject)
