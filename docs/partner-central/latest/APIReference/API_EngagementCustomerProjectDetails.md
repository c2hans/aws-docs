---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_EngagementCustomerProjectDetails.html
---

# EngagementCustomerProjectDetails
<a name="API_EngagementCustomerProjectDetails"></a>

Provides comprehensive details about a customer project associated with an Engagement. This may include information such as project goals, timelines, and specific customer requirements.

## Contents
<a name="API_EngagementCustomerProjectDetails_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** BusinessProblem **   <a name="AWSPartnerCentral-Type-EngagementCustomerProjectDetails-BusinessProblem"></a>
A description of the business problem the project aims to solve.
Type: String
Pattern: `(?s).{20,2000}`
Required: Yes

 ** TargetCompletionDate **   <a name="AWSPartnerCentral-Type-EngagementCustomerProjectDetails-TargetCompletionDate"></a>
The target completion date for the customer's project.
Type: String
Pattern: `[1-9][0-9]{3}-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])`
Required: Yes

 ** Title **   <a name="AWSPartnerCentral-Type-EngagementCustomerProjectDetails-Title"></a>
The title of the project.
Type: String
Pattern: `(?s).{1,255}`
Required: Yes

## See Also
<a name="API_EngagementCustomerProjectDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/EngagementCustomerProjectDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/EngagementCustomerProjectDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/EngagementCustomerProjectDetails)
