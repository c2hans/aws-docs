---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_AwsOpportunityLifeCycle.html
---

# AwsOpportunityLifeCycle
<a name="API_AwsOpportunityLifeCycle"></a>

Tracks the lifecycle of the AWS opportunity, including stages such as qualification, validation, and closure. This field helps partners understand the current status and progression of the opportunity.

## Contents
<a name="API_AwsOpportunityLifeCycle_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ClosedLostReason **   <a name="AWSPartnerCentral-Type-AwsOpportunityLifeCycle-ClosedLostReason"></a>
Indicates the reason why an opportunity was marked as `Closed Lost`. This helps in understanding the context behind the lost opportunity and aids in refining future strategies.
Type: String
Valid Values: `Administrative | Business Associate Agreement | Company Acquired/Dissolved | Competitive Offering | Customer Data Requirement | Customer Deficiency | Customer Experience | Delay / Cancellation of Project | Duplicate | Duplicate Opportunity | Executive Blocker | Failed Vetting | Feature Limitation | Financial/Commercial | Insufficient Amazon Value | Insufficient AWS Value | International Constraints | Legal / Tax / Regulatory | Legal Terms and Conditions | Lost to Competitor | Lost to Competitor - Google | Lost to Competitor - Microsoft | Lost to Competitor - Other | Lost to Competitor - Rackspace | Lost to Competitor - SoftLayer | Lost to Competitor - VMWare | No Customer Reference | No Integration Resources | No Opportunity | No Perceived Value of MP | No Response | Not Committed to AWS | No Update | On Premises Deployment | Other | Other (Details in Description) | Partner Gap | Past Due | People/Relationship/Governance | Platform Technology Limitation | Preference for Competitor | Price | Product/Technology | Product Not on AWS | Security / Compliance | Self-Service | Technical Limitations | Term Sheet Impasse`
Required: No

 ** NextSteps **   <a name="AWSPartnerCentral-Type-AwsOpportunityLifeCycle-NextSteps"></a>
Specifies the immediate next steps required to progress the opportunity. These steps are based on AWS guidance and the current stage of the opportunity.
Type: String
Pattern: `(?s).{0,255}`
Required: No

 ** NextStepsHistory **   <a name="AWSPartnerCentral-Type-AwsOpportunityLifeCycle-NextStepsHistory"></a>
Provides a historical log of previous next steps that were taken to move the opportunity forward. This helps in tracking the decision-making process and identifying any delays or obstacles encountered.
Type: Array of [ProfileNextStepsHistory](API_ProfileNextStepsHistory.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** Stage **   <a name="AWSPartnerCentral-Type-AwsOpportunityLifeCycle-Stage"></a>
Represents the current stage of the opportunity in its lifecycle, such as `Qualification`, `Validation`, or `Closed Won`. This helps in understanding the opportunity's progress.
Type: String
Valid Values: `Not Started | In Progress | Prospect | Engaged | Identified | Qualify | Research | Seller Engaged | Evaluating | Seller Registered | Term Sheet Negotiation | Contract Negotiation | Onboarding | Building Integration | Qualified | On-hold | Technical Validation | Business Validation | Committed | Launched | Deferred to Partner | Closed Lost | Completed | Closed Incomplete`
Required: No

 ** TargetCloseDate **   <a name="AWSPartnerCentral-Type-AwsOpportunityLifeCycle-TargetCloseDate"></a>
Indicates the expected date by which the opportunity is projected to close. This field helps in planning resources and timelines for both the partner and AWS.
Type: String
Pattern: `[1-9][0-9]{3}-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])`
Required: No

## See Also
<a name="API_AwsOpportunityLifeCycle_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/AwsOpportunityLifeCycle)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/AwsOpportunityLifeCycle)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/AwsOpportunityLifeCycle)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Partner Central. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query partner-central` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
