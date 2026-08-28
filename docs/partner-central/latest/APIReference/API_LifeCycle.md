---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_LifeCycle.html
---

# LifeCycle
<a name="API_LifeCycle"></a>

An object that contains the `Opportunity` lifecycle's details.

## Contents
<a name="API_LifeCycle_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ClosedLostReason **   <a name="AWSPartnerCentral-Type-LifeCycle-ClosedLostReason"></a>
Specifies the reason code when an opportunity is marked as *Closed Lost*. When you select an appropriate reason code, you communicate the context for closing the `Opportunity`, and aid in accurate reports and analysis of opportunity outcomes. The possible values are:
+ Customer Deficiency: The customer lacked necessary resources or capabilities.
+ Delay/Cancellation of Project: The project was delayed or canceled.
+ Legal/Tax/Regulatory: Legal, tax, or regulatory issues prevented progress.
+ Lost to Competitor—Google: The opportunity was lost to Google.
+ Lost to Competitor—Microsoft: The opportunity was lost to Microsoft.
+ Lost to Competitor—SoftLayer: The opportunity was lost to SoftLayer.
+ Lost to Competitor—VMWare: The opportunity was lost to VMWare.
+ Lost to Competitor—Other: The opportunity was lost to a competitor not listed above.
+ No Opportunity: There was no opportunity to pursue.
+ On Premises Deployment: The customer chose an on-premises solution.
+ Partner Gap: The partner lacked necessary resources or capabilities.
+ Price: The price was not competitive or acceptable to the customer.
+ Security/Compliance: Security or compliance issues prevented progress.
+ Technical Limitations: Technical limitations prevented progress.
+ Customer Experience: Issues related to the customer's experience impacted the decision.
+ Other: Any reason not covered by the other values.
+ People/Relationship/Governance: Issues related to people, relationships, or governance.
+ Product/Technology: Issues related to the product or technology.
+ Financial/Commercial: Financial or commercial issues impacted the decision.
Type: String
Valid Values: `Customer Deficiency | Delay / Cancellation of Project | Legal / Tax / Regulatory | Lost to Competitor - Google | Lost to Competitor - Microsoft | Lost to Competitor - SoftLayer | Lost to Competitor - VMWare | Lost to Competitor - Other | No Opportunity | On Premises Deployment | Partner Gap | Price | Security / Compliance | Technical Limitations | Customer Experience | Other | People/Relationship/Governance | Product/Technology | Financial/Commercial`
Required: No

 ** NextSteps **   <a name="AWSPartnerCentral-Type-LifeCycle-NextSteps"></a>
Specifies the upcoming actions or tasks for the `Opportunity`. Use this field to communicate with AWS about the next actions required for the `Opportunity`.
Type: String
Pattern: `(?s).{0,255}`
Required: No

 ** NextStepsHistory **   <a name="AWSPartnerCentral-Type-LifeCycle-NextStepsHistory"></a>
Captures a chronological record of the next steps or actions planned or taken for the current opportunity, along with the timestamp.
Type: Array of [NextStepsHistory](API_NextStepsHistory.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** ReviewComments **   <a name="AWSPartnerCentral-Type-LifeCycle-ReviewComments"></a>
Contains detailed feedback from AWS when requesting additional information from partners. Provides specific guidance on what partners need to provide or clarify for opportunity validation, complementing the `ReviewStatusReason` field.
Type: String
Required: No

 ** ReviewStatus **   <a name="AWSPartnerCentral-Type-LifeCycle-ReviewStatus"></a>
Indicates the review status of an opportunity referred by a partner. This field is read-only and only applicable for partner referrals. The possible values are:
+ Pending Submission: Not submitted for validation (editable).
+ Submitted: Submitted for validation, and AWS hasn't reviewed it (read-only).
+ In Review: AWS is validating (read-only).
+ Action Required: Issues that AWS highlights need to be addressed. Partners should use the `UpdateOpportunity` API action to update the opportunity and helps to ensure that all required changes are made. Only the following fields are editable when the `Lifecycle.ReviewStatus` is `Action Required`:
  + Customer.Account.Address.City
  + Customer.Account.Address.CountryCode
  + Customer.Account.Address.PostalCode
  + Customer.Account.Address.StateOrRegion
  + Customer.Account.Address.StreetAddress
  + Customer.Account.WebsiteUrl
  + LifeCycle.TargetCloseDate
  + Project.ExpectedMonthlyAWSRevenue.Amount
  + Project.ExpectedMonthlyAWSRevenue.CurrencyCode
  + Project.CustomerBusinessProblem
  + PartnerOpportunityIdentifier

  After updates, the opportunity re-enters the validation phase. This process repeats until all issues are resolved, and the opportunity's `Lifecycle.ReviewStatus` is set to `Approved` or `Rejected`.
+ Approved: Validated and converted into the AWS seller's pipeline (editable).
+ Rejected: Disqualified (read-only).
Type: String
Valid Values: `Pending Submission | Submitted | In review | Approved | Rejected | Action Required`
Required: No

 ** ReviewStatusReason **   <a name="AWSPartnerCentral-Type-LifeCycle-ReviewStatusReason"></a>
Code indicating the validation decision during the AWS opportunity review. Applies when status is `Rejected` or `Action Required`. Used to document validation results for AWS Partner Referrals and indicate when additional information is needed from partners as part of the APN Customer Engagement (ACE) program.
Type: String
Required: No

 ** Stage **   <a name="AWSPartnerCentral-Type-LifeCycle-Stage"></a>
Specifies the current stage of the `Opportunity`'s lifecycle as it maps to AWS stages from the current stage in the partner CRM. This field provides a translated value of the stage, and offers insight into the `Opportunity`'s progression in the sales cycle, according to AWS definitions.
A lead and a prospect must be further matured to a `Qualified` opportunity before submission. Opportunities that were closed/lost before submission aren't suitable for submission.
The descriptions of each sales stage are:
+ Prospect: AWS identifies the opportunity. It can be active (Comes directly from the end customer through a lead) or latent (Your account team believes it exists based on research, account plans, sales plays).
+ Qualified: Your account team engaged with the customer to discuss viability and requirements. The customer agreed that the opportunity is real, of interest, and may solve business/technical needs.
+ Technical Validation: All parties understand the implementation plan.
+ Business Validation: Pricing was proposed, and all parties agree to the steps to close.
+ Committed: The customer signed the contract, but AWS hasn't started billing.
+ Launched: The workload is complete, and AWS has started billing.
+ Closed Lost: The opportunity is lost, and there are no steps to move forward.
Type: String
Valid Values: `Prospect | Qualified | Technical Validation | Business Validation | Committed | Launched | Closed Lost`
Required: No

 ** TargetCloseDate **   <a name="AWSPartnerCentral-Type-LifeCycle-TargetCloseDate"></a>
Specifies the date when AWS expects to start significant billing, when the project finishes, and when it moves into production. This field informs the AWS seller about when the opportunity launches and starts to incur AWS usage.
Ensure the `Target Close Date` isn't in the past.
Type: String
Pattern: `[1-9][0-9]{3}-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])`
Required: No

## See Also
<a name="API_LifeCycle_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/LifeCycle)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/LifeCycle)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/LifeCycle)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Partner Central. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query partner-central` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
