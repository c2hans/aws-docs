---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_EngagementSummary.html
---

# EngagementSummary
<a name="API_EngagementSummary"></a>

An object that contains an `Engagement`'s subset of fields.

## Contents
<a name="API_EngagementSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Arn **   <a name="AWSPartnerCentral-Type-EngagementSummary-Arn"></a>
The Amazon Resource Name (ARN) of the created Engagement.
Type: String
Pattern: `arn:.*`
Required: No

 ** ContextTypes **   <a name="AWSPartnerCentral-Type-EngagementSummary-ContextTypes"></a>
An array of context types associated with the engagement, such as "CustomerProject" or "Lead". This provides a quick overview of the types of contexts included in the engagement.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Valid Values: `CustomerProject | Lead | ProspectingResult`
Required: No

 ** CreatedAt **   <a name="AWSPartnerCentral-Type-EngagementSummary-CreatedAt"></a>
The date and time when the Engagement was created.
Type: Timestamp
Required: No

 ** CreatedBy **   <a name="AWSPartnerCentral-Type-EngagementSummary-CreatedBy"></a>
The AWS Account ID of the Engagement creator.
Type: String
Pattern: `([0-9]{12}|\w{1,12})`
Required: No

 ** Id **   <a name="AWSPartnerCentral-Type-EngagementSummary-Id"></a>
The unique identifier for the Engagement.
Type: String
Pattern: `eng-[0-9a-z]{14}`
Required: No

 ** MemberCount **   <a name="AWSPartnerCentral-Type-EngagementSummary-MemberCount"></a>
The number of members in the Engagement.
Type: Integer
Required: No

 ** ModifiedAt **   <a name="AWSPartnerCentral-Type-EngagementSummary-ModifiedAt"></a>
The timestamp indicating when the engagement was last modified, in ISO 8601 format (UTC). Example: "2023-05-01T20:37:46Z".
Type: Timestamp
Required: No

 ** ModifiedBy **   <a name="AWSPartnerCentral-Type-EngagementSummary-ModifiedBy"></a>
The AWS account ID of the user who last modified the engagement. This field helps track who made the most recent changes to the engagement.
Type: String
Pattern: `([0-9]{12}|\w{1,12})`
Required: No

 ** Title **   <a name="AWSPartnerCentral-Type-EngagementSummary-Title"></a>
The title of the Engagement.
Type: String
Pattern: `(?s).{0,40}`
Required: No

## See Also
<a name="API_EngagementSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/EngagementSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/EngagementSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/EngagementSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Partner Central. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query partner-central` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
