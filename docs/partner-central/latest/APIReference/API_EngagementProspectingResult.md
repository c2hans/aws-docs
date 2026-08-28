---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_EngagementProspectingResult.html
---

# EngagementProspectingResult
<a name="API_EngagementProspectingResult"></a>

Contains the result of processing a single engagement within a prospecting task. Each engagement is processed independently, so individual engagements can succeed or fail regardless of other engagements in the same task.

## Contents
<a name="API_EngagementProspectingResult_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** EngagementIdentifier **   <a name="AWSPartnerCentral-Type-EngagementProspectingResult-EngagementIdentifier"></a>
The unique identifier of the engagement that was processed.
Type: String
Pattern: `eng-[0-9a-z]{14}`
Required: Yes

 ** Status **   <a name="AWSPartnerCentral-Type-EngagementProspectingResult-Status"></a>
The processing status of this specific engagement. Possible values are `PENDING`, `IN_PROGRESS`, `COMPLETED`, and `FAILED`.
Type: String
Valid Values: `PENDING | IN_PROGRESS | COMPLETED | FAILED`
Required: Yes

 ** EngagementContextId **   <a name="AWSPartnerCentral-Type-EngagementProspectingResult-EngagementContextId"></a>
The identifier of the prospecting context created for this engagement. This field is only populated when the engagement was processed successfully (status is `COMPLETED`). Use this identifier to reference the prospecting context in subsequent operations.
Type: String
Pattern: `ctx-[0-9a-z]{14}`
Required: No

 ** Message **   <a name="AWSPartnerCentral-Type-EngagementProspectingResult-Message"></a>
A human-readable description of the failure for this engagement, including suggested recovery steps. This field is only populated when `Status` is `FAILED`.
Type: String
Required: No

 ** ReasonCode **   <a name="AWSPartnerCentral-Type-EngagementProspectingResult-ReasonCode"></a>
An enumerated code indicating the reason this engagement failed to process. This field is only populated when `Status` is `FAILED`.
Type: String
Required: No

## See Also
<a name="API_EngagementProspectingResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/EngagementProspectingResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/EngagementProspectingResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/EngagementProspectingResult)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Partner Central. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query partner-central` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
