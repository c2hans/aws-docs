---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_Finding.html
---

# Finding
<a name="API_Finding"></a>

Represents a security finding discovered during a pentest job. A finding contains details about a vulnerability, including its risk level, confidence, and remediation status.

## Contents
<a name="API_Finding_Contents"></a>

 ** agentSpaceId **   <a name="securityagent-Type-Finding-agentSpaceId"></a>
The unique identifier of the agent space associated with the finding.
Type: String
Required: Yes

 ** findingId **   <a name="securityagent-Type-Finding-findingId"></a>
The unique identifier of the finding.
Type: String
Required: Yes

 ** alignmentRationale **   <a name="securityagent-Type-Finding-alignmentRationale"></a>
The rationale provided by the alignment agent explaining how the finding was adjusted based on customer preferences.
Type: String
Required: No

 ** attackScript **   <a name="securityagent-Type-Finding-attackScript"></a>
The attack script used to reproduce the finding.
Type: String
Required: No

 ** codeLocations **   <a name="securityagent-Type-Finding-codeLocations"></a>
The file locations involved in the vulnerability, as reported by the code scanner.
Type: Array of [CodeLocation](API_CodeLocation.md) objects
Required: No

 ** codeRemediationTask **   <a name="securityagent-Type-Finding-codeRemediationTask"></a>
The code remediation task associated with the finding, if code remediation was initiated.
Type: [CodeRemediationTask](API_CodeRemediationTask.md) object
Required: No

 ** codeReviewId **   <a name="securityagent-Type-Finding-codeReviewId"></a>
The unique identifier of the code review associated with the finding.
Type: String
Required: No

 ** codeReviewJobId **   <a name="securityagent-Type-Finding-codeReviewJobId"></a>
The unique identifier of the code review job that produced the finding.
Type: String
Required: No

 ** confidence **   <a name="securityagent-Type-Finding-confidence"></a>
The confidence level of the finding. Valid values include FALSE\_POSITIVE, UNCONFIRMED, LOW, MEDIUM, and HIGH.
Type: String
Valid Values: `FALSE_POSITIVE | UNCONFIRMED | LOW | MEDIUM | HIGH`
Required: No

 ** createdAt **   <a name="securityagent-Type-Finding-createdAt"></a>
The date and time the finding was created, in UTC format.
Type: Timestamp
Required: No

 ** customerNote **   <a name="securityagent-Type-Finding-customerNote"></a>
A customer-provided note on the finding.
Type: String
Required: No

 ** description **   <a name="securityagent-Type-Finding-description"></a>
A description of the finding.
Type: String
Required: No

 ** lastUpdatedBy **   <a name="securityagent-Type-Finding-lastUpdatedBy"></a>
The identifier of the entity that last updated the finding.
Type: String
Required: No

 ** name **   <a name="securityagent-Type-Finding-name"></a>
The name of the finding.
Type: String
Required: No

 ** originalFindingId **   <a name="securityagent-Type-Finding-originalFindingId"></a>
The identifier of the original finding that this revalidation finding was produced from.
Type: String
Required: No

 ** pentestId **   <a name="securityagent-Type-Finding-pentestId"></a>
The unique identifier of the pentest associated with the finding.
Type: String
Required: No

 ** pentestJobId **   <a name="securityagent-Type-Finding-pentestJobId"></a>
The unique identifier of the pentest job that produced the finding.
Type: String
Required: No

 ** reasoning **   <a name="securityagent-Type-Finding-reasoning"></a>
The reasoning behind the finding, explaining why it was identified as a vulnerability.
Type: String
Required: No

 ** revalidationJobIds **   <a name="securityagent-Type-Finding-revalidationJobIds"></a>
The list of pentest job identifiers for revalidation jobs that retested this finding.
Type: Array of strings
Required: No

 ** riskLevel **   <a name="securityagent-Type-Finding-riskLevel"></a>
The risk level of the finding. Valid values include UNKNOWN, INFORMATIONAL, LOW, MEDIUM, HIGH, and CRITICAL.
Type: String
Valid Values: `UNKNOWN | INFORMATIONAL | LOW | MEDIUM | HIGH | CRITICAL`
Required: No

 ** riskScore **   <a name="securityagent-Type-Finding-riskScore"></a>
The numerical risk score of the finding.
Type: String
Required: No

 ** riskType **   <a name="securityagent-Type-Finding-riskType"></a>
The type of security risk identified by the finding.
Type: String
Required: No

 ** status **   <a name="securityagent-Type-Finding-status"></a>
The current status of the finding. Valid values include ACTIVE, RESOLVED, ACCEPTED, and FALSE\_POSITIVE.
Type: String
Valid Values: `ACTIVE | RESOLVED | ACCEPTED | FALSE_POSITIVE`
Required: No

 ** taskId **   <a name="securityagent-Type-Finding-taskId"></a>
The unique identifier of the task that produced the finding.
Type: String
Required: No

 ** updatedAt **   <a name="securityagent-Type-Finding-updatedAt"></a>
The date and time the finding was last updated, in UTC format.
Type: Timestamp
Required: No

 ** validationStatus **   <a name="securityagent-Type-Finding-validationStatus"></a>
The simulated validation status of the finding. Valid values are NOT\_VALIDATED, VALIDATING, CONFIRMED, NOT\_REPRODUCED, and VALIDATION\_FAILED.
Type: String
Valid Values: `CONFIRMED | NOT_REPRODUCED | VALIDATION_FAILED | VALIDATING | NOT_VALIDATED`
Required: No

 ** verificationScript **   <a name="securityagent-Type-Finding-verificationScript"></a>
The verification script metadata for reproducing the finding, including download URL, instructions, and required environment variables.
Type: [VerificationScript](API_VerificationScript.md) object
Required: No

## See Also
<a name="API_Finding_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/Finding)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/Finding)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/Finding)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Agent. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityagent` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
