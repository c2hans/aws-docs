---
source_url: https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_BatchImportEvidenceToAssessmentControlError.html
---

# BatchImportEvidenceToAssessmentControlError
<a name="API_BatchImportEvidenceToAssessmentControlError"></a>

 An error entity for the `BatchImportEvidenceToAssessmentControl` API. This is used to provide more meaningful errors than a simple string message.

## Contents
<a name="API_BatchImportEvidenceToAssessmentControlError_Contents"></a>

 ** errorCode **   <a name="auditmanager-Type-BatchImportEvidenceToAssessmentControlError-errorCode"></a>
 The error code that the `BatchImportEvidenceToAssessmentControl` API returned.
Type: String
Length Constraints: Fixed length of 3.
Pattern: `[0-9]{3}`
Required: No

 ** errorMessage **   <a name="auditmanager-Type-BatchImportEvidenceToAssessmentControlError-errorMessage"></a>
 The error message that the `BatchImportEvidenceToAssessmentControl` API returned.
Type: String
Length Constraints: Maximum length of 300.
Pattern: `^[\w\W\s\S]*$`
Required: No

 ** manualEvidence **   <a name="auditmanager-Type-BatchImportEvidenceToAssessmentControlError-manualEvidence"></a>
 Manual evidence that can't be collected automatically by Audit Manager.
Type: [ManualEvidence](API_ManualEvidence.md) object
Required: No

## See Also
<a name="API_BatchImportEvidenceToAssessmentControlError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/auditmanager-2017-07-25/BatchImportEvidenceToAssessmentControlError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/auditmanager-2017-07-25/BatchImportEvidenceToAssessmentControlError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/auditmanager-2017-07-25/BatchImportEvidenceToAssessmentControlError)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Audit Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query audit-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
