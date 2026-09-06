---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_ProjectDetails.html
---

# ProjectDetails
<a name="API_ProjectDetails"></a>

Contains details about the project associated with the Engagement Invitation, including the business problem and expected outcomes.

## Contents
<a name="API_ProjectDetails_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** BusinessProblem **   <a name="AWSPartnerCentral-Type-ProjectDetails-BusinessProblem"></a>
Describes the business problem that the project aims to solve. This information is crucial for understanding the project’s goals and objectives.
Type: String
Pattern: `(?s).{20,2000}`
Required: Yes

 ** ExpectedCustomerSpend **   <a name="AWSPartnerCentral-Type-ProjectDetails-ExpectedCustomerSpend"></a>
Contains revenue estimates for the partner related to the project. This field provides an idea of the financial potential of the opportunity for the partner.
Type: Array of [ExpectedCustomerSpend](API_ExpectedCustomerSpend.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: Yes

 ** TargetCompletionDate **   <a name="AWSPartnerCentral-Type-ProjectDetails-TargetCompletionDate"></a>
Specifies the estimated date of project completion. This field helps track the project timeline and manage expectations.
Type: String
Pattern: `[1-9][0-9]{3}-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])`
Required: Yes

 ** Title **   <a name="AWSPartnerCentral-Type-ProjectDetails-Title"></a>
Specifies the title of the project. This title helps partners quickly identify and understand the focus of the project.
Type: String
Pattern: `(?s).{1,255}`
Required: Yes

## See Also
<a name="API_ProjectDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/ProjectDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/ProjectDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/ProjectDetails)
