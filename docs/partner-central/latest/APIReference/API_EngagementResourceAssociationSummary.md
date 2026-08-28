---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_EngagementResourceAssociationSummary.html
---

# EngagementResourceAssociationSummary
<a name="API_EngagementResourceAssociationSummary"></a>

 This provide a streamlined view of the relationships between engagements and resources. These summaries offer a crucial link between collaborative engagements and the specific resources involved, such as opportunities.These summaries are particularly valuable for partners navigating complex engagements with multiple resources. They enable quick insights into resource distribution across engagements, support efficient resource management, and help maintain a clear overview of collaborative activities.

## Contents
<a name="API_EngagementResourceAssociationSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Catalog **   <a name="AWSPartnerCentral-Type-EngagementResourceAssociationSummary-Catalog"></a>
 Indicates the environment in which the resource and engagement exist.
Type: String
Pattern: `[a-zA-Z]+`
Required: Yes

 ** CreatedBy **   <a name="AWSPartnerCentral-Type-EngagementResourceAssociationSummary-CreatedBy"></a>
The AWS account ID of the entity that owns the resource. Identifies the account responsible for or having primary control over the resource.
Type: String
Pattern: `([0-9]{12}|\w{1,12})`
Required: No

 ** EngagementId **   <a name="AWSPartnerCentral-Type-EngagementResourceAssociationSummary-EngagementId"></a>
 A unique identifier for the engagement associated with the resource.
Type: String
Pattern: `eng-[0-9a-z]{14}`
Required: No

 ** ResourceId **   <a name="AWSPartnerCentral-Type-EngagementResourceAssociationSummary-ResourceId"></a>
 A unique identifier for the specific resource. Varies depending on the resource type.
Type: String
Pattern: `O[0-9]{1,19}`
Required: No

 ** ResourceType **   <a name="AWSPartnerCentral-Type-EngagementResourceAssociationSummary-ResourceType"></a>
 Categorizes the type of resource associated with the engagement.
Type: String
Valid Values: `Opportunity`
Required: No

## See Also
<a name="API_EngagementResourceAssociationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/EngagementResourceAssociationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/EngagementResourceAssociationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/EngagementResourceAssociationSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Partner Central. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query partner-central` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
