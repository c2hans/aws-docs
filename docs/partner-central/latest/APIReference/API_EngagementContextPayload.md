---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_EngagementContextPayload.html
---

# EngagementContextPayload
<a name="API_EngagementContextPayload"></a>

Represents the payload of an Engagement context. The structure of this payload varies based on the context type specified in the EngagementContextDetails.

## Contents
<a name="API_EngagementContextPayload_Contents"></a>

**Note**
In the following list, the required parameters are described first.

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** CustomerProject **   <a name="AWSPartnerCentral-Type-EngagementContextPayload-CustomerProject"></a>
Contains detailed information about a customer project when the context type is "CustomerProject". This field is present only when the Type in EngagementContextDetails is set to "CustomerProject".
Type: [CustomerProjectsContext](API_CustomerProjectsContext.md) object
Required: No

 ** Lead **   <a name="AWSPartnerCentral-Type-EngagementContextPayload-Lead"></a>
Contains detailed information about a lead when the context type is "Lead". This field is present only when the Type in EngagementContextDetails is set to "Lead".
Type: [LeadContext](API_LeadContext.md) object
Required: No

 ** ProspectingResult **   <a name="AWSPartnerCentral-Type-EngagementContextPayload-ProspectingResult"></a>
Contains prospecting result data with enriched insights. The system generates these insights when a partner runs an autonomous prospecting job on leads. This field appears only when the context type is "ProspectingResult".
Type: [ProspectingResult](API_ProspectingResult.md) object
Required: No

## See Also
<a name="API_EngagementContextPayload_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/EngagementContextPayload)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/EngagementContextPayload)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/EngagementContextPayload)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Partner Central. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query partner-central` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
