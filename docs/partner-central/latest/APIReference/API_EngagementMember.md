---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_EngagementMember.html
---

# EngagementMember
<a name="API_EngagementMember"></a>

Engagement members are the participants in an Engagement, which is likely a collaborative project or business opportunity within the AWS partner network. Members can be different partner organizations or AWS accounts that are working together on a specific engagement.

Each member is represented by their AWS Account ID, Company Name, and associated details. Members have a status within the Engagement (PENDING, ACCEPTED, REJECTED, or WITHDRAWN), indicating their current state of participation. Only existing members of an Engagement can view the list of other members. This implies a level of privacy and access control within the Engagement structure.

## Contents
<a name="API_EngagementMember_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AccountId **   <a name="AWSPartnerCentral-Type-EngagementMember-AccountId"></a>
This is the unique identifier for the AWS account associated with the member organization. It's used for AWS-related operations and identity verification.
Type: String
Pattern: `([0-9]{12}|\w{1,12})`
Required: No

 ** CompanyName **   <a name="AWSPartnerCentral-Type-EngagementMember-CompanyName"></a>
The official name of the member's company or organization.
Type: String
Pattern: `(?s).{1,120}`
Required: No

 ** WebsiteUrl **   <a name="AWSPartnerCentral-Type-EngagementMember-WebsiteUrl"></a>
The URL of the member company's website. This offers a way to find more information about the member organization and serves as an additional identifier.
Type: String
Required: No

## See Also
<a name="API_EngagementMember_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/EngagementMember)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/EngagementMember)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/EngagementMember)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Partner Central. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query partner-central` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
