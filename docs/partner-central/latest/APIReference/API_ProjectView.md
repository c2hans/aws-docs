---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_ProjectView.html
---

# ProjectView
<a name="API_ProjectView"></a>

 Provides the project view of an opportunity resource shared through a snapshot.

## Contents
<a name="API_ProjectView_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** CustomerUseCase **   <a name="AWSPartnerCentral-Type-ProjectView-CustomerUseCase"></a>
 Specifies the proposed solution focus or type of workload for the project.
Type: String
Required: No

 ** DeliveryModels **   <a name="AWSPartnerCentral-Type-ProjectView-DeliveryModels"></a>
 Describes the deployment or consumption model for the partner solution or offering. This field indicates how the project's solution will be delivered or implemented for the customer.
Type: Array of strings
Valid Values: `SaaS or PaaS | BYOL or AMI | Managed Services | Professional Services | Resell | Other`
Required: No

 ** ExpectedContractDuration **   <a name="AWSPartnerCentral-Type-ProjectView-ExpectedContractDuration"></a>
Optional. The expected contract duration for this opportunity, representing the anticipated length of the contract in the unit specified by `Term`.
Type: [ExpectedContractDuration](API_ExpectedContractDuration.md) object
Required: No

 ** ExpectedCustomerSpend **   <a name="AWSPartnerCentral-Type-ProjectView-ExpectedCustomerSpend"></a>
 Provides information about the anticipated customer spend related to this project. This may include details such as amount, frequency, and currency of expected expenditure.
Type: Array of [ExpectedCustomerSpend](API_ExpectedCustomerSpend.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** OtherSolutionDescription **   <a name="AWSPartnerCentral-Type-ProjectView-OtherSolutionDescription"></a>
 Offers a description of other solutions if the standard solutions do not adequately cover the project's scope.
Type: String
Pattern: `(?s).{0,255}`
Required: No

 ** SalesActivities **   <a name="AWSPartnerCentral-Type-ProjectView-SalesActivities"></a>
 Lists the pre-sales activities that have occurred with the end-customer related to the opportunity. This field is conditionally mandatory when the project is qualified for Co-Sell and helps drive assignment priority on the AWS side. It provides insight into the engagement level with the customer.
Type: Array of strings
Valid Values: `Initialized discussions with customer | Customer has shown interest in solution | Conducted POC / Demo | In evaluation / planning stage | Agreed on solution to Business Problem | Completed Action Plan | Finalized Deployment Need | SOW Signed`
Required: No

## See Also
<a name="API_ProjectView_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/ProjectView)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/ProjectView)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/ProjectView)
