---
source_url: https://docs.aws.amazon.com/continuum/latest/APIReference/API_FindingSummary.html
---

# FindingSummary
<a name="API_FindingSummary"></a>

A summary of a finding returned in list responses. Shares FindingLifecycleFields with the read operations so the list and get projections cannot drift. Carries a lean content subset — fetch the finding for its full contents.

## Contents
<a name="API_FindingSummary_Contents"></a>

 ** createdAt **   <a name="continuum-Type-FindingSummary-createdAt"></a>
The timestamp when the resource was created.
Type: Timestamp
Required: Yes

 ** environmentId **   <a name="continuum-Type-FindingSummary-environmentId"></a>
The identifier of the environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9]+`
Required: Yes

 ** findingArn **   <a name="continuum-Type-FindingSummary-findingArn"></a>
The Amazon Resource Name (ARN) of the finding.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:[a-z0-9-]+:continuum:[a-z0-9-]+:[0-9]{12}:environments/[a-z0-9]+/code-findings/[a-z0-9]+`
Required: Yes

 ** findingId **   <a name="continuum-Type-FindingSummary-findingId"></a>
The identifier of the finding.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9]+`
Required: Yes

 ** reportedAt **   <a name="continuum-Type-FindingSummary-reportedAt"></a>
The reported At.
Type: Timestamp
Required: Yes

 ** severity **   <a name="continuum-Type-FindingSummary-severity"></a>
The severity.
Type: String
Valid Values: `UNKNOWN | INFORMATIONAL | LOW | MEDIUM | HIGH | CRITICAL | FATAL | OTHER`
Required: Yes

 ** source **   <a name="continuum-Type-FindingSummary-source"></a>
The source.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** sourceFindingId **   <a name="continuum-Type-FindingSummary-sourceFindingId"></a>
The identifier of the source Finding.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** status **   <a name="continuum-Type-FindingSummary-status"></a>
The lifecycle status of a finding as it moves through Continuum's processing pipeline. CONFIRMED and DISCARDED are terminal states — a CONFIRMED finding is promoted into a separate Issue (not yet implemented), which owns the subsequent remediation lifecycle; the finding's own status does not change after that.
Type: String
Valid Values: `SUBMITTED | VALIDATING | CONFIRMED | DISCARDED`
Required: Yes

 ** statusUpdatedAt **   <a name="continuum-Type-FindingSummary-statusUpdatedAt"></a>
The status Updated At.
Type: Timestamp
Required: Yes

 ** title **   <a name="continuum-Type-FindingSummary-title"></a>
The title.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** type **   <a name="continuum-Type-FindingSummary-type"></a>
What kind of finding this is, and who produced it.
Type: String
Valid Values: `CONTINUUM_CODE_VULN | CUSTOMER_CODE_VULN`
Required: Yes

 ** category **   <a name="continuum-Type-FindingSummary-category"></a>
The category.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** completedAt **   <a name="continuum-Type-FindingSummary-completedAt"></a>
The completed At.
Type: Timestamp
Required: No

 ** createdIssueId **   <a name="continuum-Type-FindingSummary-createdIssueId"></a>
The identifier of the created Issue.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9]+`
Required: No

 ** discardReason **   <a name="continuum-Type-FindingSummary-discardReason"></a>
Why a finding was not escalated into an issue. Present only when status is DISCARDED.
Type: String
Valid Values: `SCANNER_VALIDATED_FALSE_POSITIVE | SCANNER_NEEDS_REVIEW | FALSE_POSITIVE_VALIDATED_AGAINST_CONTEXT | DUPLICATE_OF_OPEN_ISSUE | DUPLICATE_OF_CLOSED_ISSUE | COMPENSATING_CONTROL_PRESENT | OUT_OF_SCOPE | INSUFFICIENT_EVIDENCE | PROCESSING_FAILED | SOURCE_REPO_NOT_FOUND`
Required: No

 ** discardReasoning **   <a name="continuum-Type-FindingSummary-discardReasoning"></a>
The discard Reasoning.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** duplicateOfIssueId **   <a name="continuum-Type-FindingSummary-duplicateOfIssueId"></a>
The identifier of the duplicate Of Issue.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9]+`
Required: No

 ** filePath **   <a name="continuum-Type-FindingSummary-filePath"></a>
The file Path.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

 ** scanRunId **   <a name="continuum-Type-FindingSummary-scanRunId"></a>
The identifier of the scan Run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9]+`
Required: No

 ** statusMessage **   <a name="continuum-Type-FindingSummary-statusMessage"></a>
The status Message.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## See Also
<a name="API_FindingSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/continuum-2022-07-26/FindingSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/continuum-2022-07-26/FindingSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/continuum-2022-07-26/FindingSummary)
