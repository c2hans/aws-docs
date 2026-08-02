---
source_url: https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_AssessmentReportEvidenceError.html
---

# AssessmentReportEvidenceError
<a name="API_AssessmentReportEvidenceError"></a>

 An error entity for assessment report evidence errors. This is used to provide more meaningful errors than a simple string message.

## Contents
<a name="API_AssessmentReportEvidenceError_Contents"></a>

 ** errorCode **   <a name="auditmanager-Type-AssessmentReportEvidenceError-errorCode"></a>
 The error code that was returned.
Type: String
Length Constraints: Fixed length of 3.
Pattern: `[0-9]{3}`
Required: No

 ** errorMessage **   <a name="auditmanager-Type-AssessmentReportEvidenceError-errorMessage"></a>
 The error message that was returned.
Type: String
Length Constraints: Maximum length of 300.
Pattern: `^[\w\W\s\S]*$`
Required: No

 ** evidenceId **   <a name="auditmanager-Type-AssessmentReportEvidenceError-evidenceId"></a>
 The identifier for the evidence.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
Required: No

## See Also
<a name="API_AssessmentReportEvidenceError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/auditmanager-2017-07-25/AssessmentReportEvidenceError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/auditmanager-2017-07-25/AssessmentReportEvidenceError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/auditmanager-2017-07-25/AssessmentReportEvidenceError)
