---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_Payload.html
---

# Payload
<a name="API_Payload"></a>

Contains the data payload associated with the Engagement Invitation. This payload includes essential details related to the AWS opportunity and is used by partners to evaluate whether to accept or reject the engagement.

## Contents
<a name="API_Payload_Contents"></a>

**Note**
In the following list, the required parameters are described first.

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** LeadInvitation **   <a name="AWSPartnerCentral-Type-Payload-LeadInvitation"></a>
Specifies the details of the lead invitation within the Engagement Invitation payload. This data helps partners understand the lead context, customer information, and interaction history for the lead opportunity from AWS.
Type: [LeadInvitationPayload](API_LeadInvitationPayload.md) object
Required: No

 ** OpportunityInvitation **   <a name="AWSPartnerCentral-Type-Payload-OpportunityInvitation"></a>
Specifies the details of the opportunity invitation within the Engagement Invitation payload. This data helps partners understand the context, scope, and expected involvement for the opportunity from AWS.
Type: [OpportunityInvitationPayload](API_OpportunityInvitationPayload.md) object
Required: No

## See Also
<a name="API_Payload_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/Payload)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/Payload)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/Payload)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Partner Central. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query partner-central` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
