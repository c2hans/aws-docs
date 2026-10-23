---
source_url: https://docs.aws.amazon.com/continuum/latest/APIReference/API_IssueSummary.html
---

# IssueSummary
<a name="API_IssueSummary"></a>

A summary of an issue returned in list responses.

## Contents
<a name="API_IssueSummary_Contents"></a>

 ** createdAt **   <a name="continuum-Type-IssueSummary-createdAt"></a>
The timestamp when the resource was created.
Type: Timestamp
Required: Yes

 ** issueArn **   <a name="continuum-Type-IssueSummary-issueArn"></a>
The Amazon Resource Name (ARN) of the issue.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:[a-z0-9-]+:continuum:[a-z0-9-]+:[0-9]{12}:environments/[a-z0-9]+/code-issues/[a-z0-9]+`
Required: Yes

 ** issueId **   <a name="continuum-Type-IssueSummary-issueId"></a>
The identifier of the issue.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9]+`
Required: Yes

 ** name **   <a name="continuum-Type-IssueSummary-name"></a>
The name of the resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** status **   <a name="continuum-Type-IssueSummary-status"></a>
The current status of the resource.
Type: String
Valid Values: `CREATED | IN_PROGRESS | COMPLETED | FAILED`
Required: Yes

 ** statusUpdatedAt **   <a name="continuum-Type-IssueSummary-statusUpdatedAt"></a>
The status Updated At.
Type: Timestamp
Required: Yes

 ** confidence **   <a name="continuum-Type-IssueSummary-confidence"></a>
The confidence.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** phase **   <a name="continuum-Type-IssueSummary-phase"></a>
The phase.
Type: String
Valid Values: `VALIDATION | PRIORITIZATION | REMEDIATION`
Required: No

 ** severity **   <a name="continuum-Type-IssueSummary-severity"></a>
The severity.
Type: String
Valid Values: `LOW | MEDIUM | HIGH | CRITICAL`
Required: No

 ** statusMessage **   <a name="continuum-Type-IssueSummary-statusMessage"></a>
The status Message.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** statusReason **   <a name="continuum-Type-IssueSummary-statusReason"></a>
The status Reason.
Type: String
Valid Values: `INTERNAL_ERROR | REMEDIATION_FAILED`
Required: No

 ** updatedAt **   <a name="continuum-Type-IssueSummary-updatedAt"></a>
The timestamp when the resource was last updated.
Type: Timestamp
Required: No

## See Also
<a name="API_IssueSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/continuum-2022-07-26/IssueSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/continuum-2022-07-26/IssueSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/continuum-2022-07-26/IssueSummary)
