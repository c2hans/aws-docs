---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_FindingSummary.html
---

# FindingSummary
<a name="API_FindingSummary"></a>

Contains summary information about a security finding.

## Contents
<a name="API_FindingSummary_Contents"></a>

 ** agentSpaceId **   <a name="securityagent-Type-FindingSummary-agentSpaceId"></a>
The unique identifier of the agent space associated with the finding.
Type: String
Required: Yes

 ** findingId **   <a name="securityagent-Type-FindingSummary-findingId"></a>
The unique identifier of the finding.
Type: String
Required: Yes

 ** codeReviewId **   <a name="securityagent-Type-FindingSummary-codeReviewId"></a>
The unique identifier of the code review associated with the finding.
Type: String
Required: No

 ** codeReviewJobId **   <a name="securityagent-Type-FindingSummary-codeReviewJobId"></a>
The unique identifier of the code review job that produced the finding.
Type: String
Required: No

 ** confidence **   <a name="securityagent-Type-FindingSummary-confidence"></a>
The confidence level of the finding.
Type: String
Valid Values: `FALSE_POSITIVE | UNCONFIRMED | LOW | MEDIUM | HIGH`
Required: No

 ** createdAt **   <a name="securityagent-Type-FindingSummary-createdAt"></a>
The date and time the finding was created, in UTC format.
Type: Timestamp
Required: No

 ** name **   <a name="securityagent-Type-FindingSummary-name"></a>
The name of the finding.
Type: String
Required: No

 ** pentestId **   <a name="securityagent-Type-FindingSummary-pentestId"></a>
The unique identifier of the pentest associated with the finding.
Type: String
Required: No

 ** pentestJobId **   <a name="securityagent-Type-FindingSummary-pentestJobId"></a>
The unique identifier of the pentest job that produced the finding.
Type: String
Required: No

 ** riskLevel **   <a name="securityagent-Type-FindingSummary-riskLevel"></a>
The risk level of the finding.
Type: String
Valid Values: `UNKNOWN | INFORMATIONAL | LOW | MEDIUM | HIGH | CRITICAL`
Required: No

 ** riskType **   <a name="securityagent-Type-FindingSummary-riskType"></a>
The type of security risk identified by the finding.
Type: String
Required: No

 ** status **   <a name="securityagent-Type-FindingSummary-status"></a>
The current status of the finding.
Type: String
Valid Values: `ACTIVE | RESOLVED | ACCEPTED | FALSE_POSITIVE`
Required: No

 ** updatedAt **   <a name="securityagent-Type-FindingSummary-updatedAt"></a>
The date and time the finding was last updated, in UTC format.
Type: Timestamp
Required: No

 ** validationStatus **   <a name="securityagent-Type-FindingSummary-validationStatus"></a>
The simulated validation status of the finding.
Type: String
Valid Values: `CONFIRMED | NOT_REPRODUCED | VALIDATION_FAILED | VALIDATING | NOT_VALIDATED`
Required: No

## See Also
<a name="API_FindingSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/FindingSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/FindingSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/FindingSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Agent. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityagent` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
