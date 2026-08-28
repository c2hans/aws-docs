---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_OpportunitySummary.html
---

# OpportunitySummary
<a name="API_OpportunitySummary"></a>

An object that contains an `Opportunity`'s subset of fields.

## Contents
<a name="API_OpportunitySummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Catalog **   <a name="AWSPartnerCentral-Type-OpportunitySummary-Catalog"></a>
Specifies the catalog associated with the opportunity, either `AWS` or `Sandbox`. This indicates the environment in which the opportunity is managed.
Type: String
Pattern: `[a-zA-Z]+`
Required: Yes

 ** Arn **   <a name="AWSPartnerCentral-Type-OpportunitySummary-Arn"></a>
 The Amazon Resource Name (ARN) for the opportunity. This globally unique identifier can be used for IAM policies and cross-service references.
Type: String
Pattern: `arn:.*`
Required: No

 ** CreatedDate **   <a name="AWSPartnerCentral-Type-OpportunitySummary-CreatedDate"></a>
 `DateTime` when the `Opportunity` was last created.
Type: Timestamp
Required: No

 ** Customer **   <a name="AWSPartnerCentral-Type-OpportunitySummary-Customer"></a>
An object that contains the `Opportunity`'s customer details.
Type: [CustomerSummary](API_CustomerSummary.md) object
Required: No

 ** Id **   <a name="AWSPartnerCentral-Type-OpportunitySummary-Id"></a>
Read-only, system-generated `Opportunity` unique identifier.
Type: String
Pattern: `O[0-9]{1,19}`
Required: No

 ** LastModifiedDate **   <a name="AWSPartnerCentral-Type-OpportunitySummary-LastModifiedDate"></a>
 `DateTime` when the `Opportunity` was last modified.
Type: Timestamp
Required: No

 ** LifeCycle **   <a name="AWSPartnerCentral-Type-OpportunitySummary-LifeCycle"></a>
An object that contains the `Opportunity`'s lifecycle details.
Type: [LifeCycleSummary](API_LifeCycleSummary.md) object
Required: No

 ** OpportunityType **   <a name="AWSPartnerCentral-Type-OpportunitySummary-OpportunityType"></a>
Specifies opportunity type as a renewal, new, or expansion.
Opportunity types:
+ New Opportunity: Represents a new business opportunity with a potential customer that's not previously engaged with your solutions or services.
+ Renewal Opportunity: Represents an opportunity to renew an existing contract or subscription with a current customer, ensuring continuity of service.
+ Expansion Opportunity: Represents an opportunity to expand the scope of an existing contract or subscription, either by adding new services or increasing the volume of existing services for a current customer.
Type: String
Valid Values: `Net New Business | Flat Renewal | Expansion`
Required: No

 ** PartnerOpportunityIdentifier **   <a name="AWSPartnerCentral-Type-OpportunitySummary-PartnerOpportunityIdentifier"></a>
Specifies the `Opportunity`'s unique identifier in the partner's CRM system. This value is essential to track and reconcile because it's included in the outbound payload sent back to the partner. It allows partners to link an opportunity to their CRM.
Type: String
Required: No

 ** Project **   <a name="AWSPartnerCentral-Type-OpportunitySummary-Project"></a>
An object that contains the `Opportunity`'s project details summary.
Type: [ProjectSummary](API_ProjectSummary.md) object
Required: No

## See Also
<a name="API_OpportunitySummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/OpportunitySummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/OpportunitySummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/OpportunitySummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Partner Central. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query partner-central` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
