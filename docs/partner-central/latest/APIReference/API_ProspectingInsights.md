---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_ProspectingInsights.html
---

# ProspectingInsights
<a name="API_ProspectingInsights"></a>

Contains insights that AI generates from the prospecting analysis. These insights include marketplace engagement scoring, solution fit assessments, and solution categorization for the prospected customer.

## Contents
<a name="API_ProspectingInsights_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** MarketplaceEngagementScore **   <a name="AWSPartnerCentral-Type-ProspectingInsights-MarketplaceEngagementScore"></a>
A score that indicates the prospected customer's level of engagement with AWS Marketplace. Valid values are `High`, `Medium`, and `Low`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Required: No

 ** SolutionCategory **   <a name="AWSPartnerCentral-Type-ProspectingInsights-SolutionCategory"></a>
The primary solution category classification for the prospected customer. This indicates the type of solution that best addresses their needs.
Type: String
Required: No

 ** SolutionScore **   <a name="AWSPartnerCentral-Type-ProspectingInsights-SolutionScore"></a>
A score that indicates how well the partner's solution fits the prospected customer's needs.
Type: String
Required: No

 ** SolutionSubCategory **   <a name="AWSPartnerCentral-Type-ProspectingInsights-SolutionSubCategory"></a>
The solution sub-category classification for the prospected customer. This provides more granular categorization of the recommended solution type.
Type: String
Required: No

## See Also
<a name="API_ProspectingInsights_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/ProspectingInsights)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/ProspectingInsights)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/ProspectingInsights)
