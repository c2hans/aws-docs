---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_LifeCycleSummary.html
---

# LifeCycleSummary
<a name="API_LifeCycleSummary"></a>

An object that contains a `LifeCycle` object's subset of fields.

## Contents
<a name="API_LifeCycleSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ClosedLostReason **   <a name="AWSPartnerCentral-Type-LifeCycleSummary-ClosedLostReason"></a>
Specifies the reason code when an opportunity is marked as *Closed Lost*. When you select an appropriate reason code, you communicate the context for closing the `Opportunity`, and aid in accurate reports and analysis of opportunity outcomes.
Type: String
Valid Values: `Customer Deficiency | Delay / Cancellation of Project | Legal / Tax / Regulatory | Lost to Competitor - Google | Lost to Competitor - Microsoft | Lost to Competitor - SoftLayer | Lost to Competitor - VMWare | Lost to Competitor - Other | No Opportunity | On Premises Deployment | Partner Gap | Price | Security / Compliance | Technical Limitations | Customer Experience | Other | People/Relationship/Governance | Product/Technology | Financial/Commercial`
Required: No

 ** NextSteps **   <a name="AWSPartnerCentral-Type-LifeCycleSummary-NextSteps"></a>
Specifies the upcoming actions or tasks for the `Opportunity`. This field is utilized to communicate to AWS the next actions required for the `Opportunity`.
Type: String
Pattern: `(?s).{0,255}`
Required: No

 ** ReviewComments **   <a name="AWSPartnerCentral-Type-LifeCycleSummary-ReviewComments"></a>
Indicates why an opportunity was sent back for further details. Partners must take corrective action based on the `ReviewComments`.
Type: String
Required: No

 ** ReviewStatus **   <a name="AWSPartnerCentral-Type-LifeCycleSummary-ReviewStatus"></a>
Indicates the review status of a partner referred opportunity. This field is read-only and only applicable for partner referrals. Valid values:
+ Pending Submission: Not submitted for validation (editable).
+ Submitted: Submitted for validation and not yet AWS reviewed (read-only).
+ In Review: Undergoing AWS validation (read-only).
+ Action Required: Address any issues AWS highlights. Use the `UpdateOpportunity` API action to update the opportunity, and ensure you make all required changes. Only these fields are editable when the `Lifecycle.ReviewStatus` is `Action Required`:
  + Customer.Account.Address.City
  + Customer.Account.Address.CountryCode
  + Customer.Account.Address.PostalCode
  + Customer.Account.Address.StateOrRegion
  + Customer.Account.Address.StreetAddress
  + Customer.Account.WebsiteUrl
  + LifeCycle.TargetCloseDate
  + Project.ExpectedCustomerSpend.Amount
  + Project.ExpectedCustomerSpend.CurrencyCode
  + Project.CustomerBusinessProblem
  + PartnerOpportunityIdentifier

  After updates, the opportunity re-enters the validation phase. This process repeats until all issues are resolved, and the opportunity's `Lifecycle.ReviewStatus` is set to `Approved` or `Rejected`.
+ Approved: Validated and converted into the AWS seller's pipeline (editable).
+ Rejected: Disqualified (read-only).
Type: String
Valid Values: `Pending Submission | Submitted | In review | Approved | Rejected | Action Required`
Required: No

 ** ReviewStatusReason **   <a name="AWSPartnerCentral-Type-LifeCycleSummary-ReviewStatusReason"></a>
Indicates the reason a specific decision was taken during the opportunity review process. This field combines the reasons for both disqualified and action required statuses, and provides clarity for why an opportunity was disqualified or required further action.
Type: String
Required: No

 ** Stage **   <a name="AWSPartnerCentral-Type-LifeCycleSummary-Stage"></a>
Specifies the current stage of the `Opportunity`'s lifecycle as it maps to AWS stages from the current stage in the partner CRM. This field provides a translated value of the stage, and offers insight into the `Opportunity`'s progression in the sales cycle, according to AWS definitions.
A lead and a prospect must be further matured to a `Qualified` opportunity before submission. Opportunities that were closed/lost before submission aren't suitable for submission.
The descriptions of each sales stage are:
+ Prospect: AWS identifies the opportunity. It can be active (Comes directly from the end customer through a lead) or latent (Your account team believes it exists based on research, account plans, sales plays).
+ Qualified: Your account team engaged with the customer to discuss viability and understand requirements. The customer agreed that the opportunity is real, of interest, and may solve business/technical needs.
+ Technical Validation: All parties understand the implementation plan.
+ Business Validation: Pricing was proposed, and all parties agree to the steps to close.
+ Committed: The customer signed the contract, but AWS hasn't started billing.
+ Launched: The workload is complete, and AWS has started billing.
+ Closed Lost: The opportunity is lost, and there are no steps to move forward.
Type: String
Valid Values: `Prospect | Qualified | Technical Validation | Business Validation | Committed | Launched | Closed Lost`
Required: No

 ** TargetCloseDate **   <a name="AWSPartnerCentral-Type-LifeCycleSummary-TargetCloseDate"></a>
Specifies the date when AWS expects to start significant billing, when the project finishes, and when it moves into production. This field informs the AWS seller about when the opportunity launches and starts to incur AWS usage.
Ensure the `Target Close Date` isn't in the past.
Type: String
Pattern: `[1-9][0-9]{3}-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])`
Required: No

## See Also
<a name="API_LifeCycleSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/LifeCycleSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/LifeCycleSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/LifeCycleSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Partner Central. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query partner-central` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
