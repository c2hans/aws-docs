---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_AwsOpportunitySummaryFullView.html
---

# AwsOpportunitySummaryFullView
<a name="API_AwsOpportunitySummaryFullView"></a>

Provides a comprehensive view of AwsOpportunitySummaryFullView template.

## Contents
<a name="API_AwsOpportunitySummaryFullView_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** CosellMotion **   <a name="AWSPartnerCentral-Type-AwsOpportunitySummaryFullView-CosellMotion"></a>
Engagement classification for this opportunity. Read-only. Null before scoring. Known values: `AWS Field-engaged`, `Agent-engaged`, `Partner-led`.
Type: String
Required: No

 ** Customer **   <a name="AWSPartnerCentral-Type-AwsOpportunitySummaryFullView-Customer"></a>
Represents the customer associated with the AWS opportunity. This field captures key details about the customer that are necessary for managing the opportunity.
Type: [AwsOpportunityCustomer](API_AwsOpportunityCustomer.md) object
Required: No

 ** Insights **   <a name="AWSPartnerCentral-Type-AwsOpportunitySummaryFullView-Insights"></a>
Contains insights provided by AWS for the opportunity, offering recommendations and analysis that can help the partner optimize their engagement and strategy.
Type: [AwsOpportunityInsights](API_AwsOpportunityInsights.md) object
Required: No

 ** InvolvementType **   <a name="AWSPartnerCentral-Type-AwsOpportunitySummaryFullView-InvolvementType"></a>
Type of AWS involvement in the opportunity.
Type: String
Valid Values: `For Visibility Only | Co-Sell`
Required: No

 ** InvolvementTypeChangeReason **   <a name="AWSPartnerCentral-Type-AwsOpportunitySummaryFullView-InvolvementTypeChangeReason"></a>
Reason for changes in AWS involvement type for the opportunity.
Type: String
Valid Values: `Expansion Opportunity | Change in Deal Information | Customer Requested | Technical Complexity | Risk Mitigation`
Required: No

 ** LifeCycle **   <a name="AWSPartnerCentral-Type-AwsOpportunitySummaryFullView-LifeCycle"></a>
Tracks the lifecycle of the AWS opportunity, including stages such as qualification, validation, and closure. This field helps partners understand the current status and progression of the opportunity.
Type: [AwsOpportunityLifeCycle](API_AwsOpportunityLifeCycle.md) object
Required: No

 ** OpportunityTeam **   <a name="AWSPartnerCentral-Type-AwsOpportunitySummaryFullView-OpportunityTeam"></a>
AWS team members involved in the opportunity.
Type: Array of [AwsTeamMember](API_AwsTeamMember.md) objects
Required: No

 ** Origin **   <a name="AWSPartnerCentral-Type-AwsOpportunitySummaryFullView-Origin"></a>
Source origin of the AWS opportunity.
Type: String
Valid Values: `AWS Referral | Partner Referral`
Required: No

 ** Project **   <a name="AWSPartnerCentral-Type-AwsOpportunitySummaryFullView-Project"></a>
Captures details about the project associated with the opportunity, including objectives, scope, and customer requirements.
Type: [AwsOpportunityProject](API_AwsOpportunityProject.md) object
Required: No

 ** RelatedEntityIds **   <a name="AWSPartnerCentral-Type-AwsOpportunitySummaryFullView-RelatedEntityIds"></a>
Represents other entities related to the AWS opportunity, such as AWS products, partner solutions, and marketplace offers. These associations help build a complete picture of the solution being sold.
Type: [AwsOpportunityRelatedEntities](API_AwsOpportunityRelatedEntities.md) object
Required: No

 ** RelatedOpportunityId **   <a name="AWSPartnerCentral-Type-AwsOpportunitySummaryFullView-RelatedOpportunityId"></a>
Identifier of the related partner opportunity.
Type: String
Pattern: `O[0-9]{1,19}`
Required: No

 ** Visibility **   <a name="AWSPartnerCentral-Type-AwsOpportunitySummaryFullView-Visibility"></a>
Visibility level for the AWS opportunity.
Type: String
Valid Values: `Full | Limited`
Required: No

## See Also
<a name="API_AwsOpportunitySummaryFullView_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/AwsOpportunitySummaryFullView)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/AwsOpportunitySummaryFullView)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/AwsOpportunitySummaryFullView)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Partner Central. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query partner-central` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
