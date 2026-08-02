---
source_url: https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_AssessmentReport.html
---

# AssessmentReport
<a name="API_AssessmentReport"></a>

 A finalized document that's generated from an Audit Manager assessment. These reports summarize the relevant evidence that was collected for your audit, and link to the relevant evidence folders. These evidence folders are named and organized according to the controls that are specified in your assessment.

## Contents
<a name="API_AssessmentReport_Contents"></a>

 ** assessmentId **   <a name="auditmanager-Type-AssessmentReport-assessmentId"></a>
 The identifier for the specified assessment.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
Required: No

 ** assessmentName **   <a name="auditmanager-Type-AssessmentReport-assessmentName"></a>
 The name of the associated assessment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Pattern: `^[^\\]*$`
Required: No

 ** author **   <a name="auditmanager-Type-AssessmentReport-author"></a>
 The name of the user who created the assessment report.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[a-zA-Z0-9-_()\s\+=,.@]+$`
Required: No

 ** awsAccountId **   <a name="auditmanager-Type-AssessmentReport-awsAccountId"></a>
 The identifier for the specified AWS account.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `^[0-9]{12}$`
Required: No

 ** creationTime **   <a name="auditmanager-Type-AssessmentReport-creationTime"></a>
 Specifies when the assessment report was created.
Type: Timestamp
Required: No

 ** description **   <a name="auditmanager-Type-AssessmentReport-description"></a>
 The description of the specified assessment report.
Type: String
Length Constraints: Maximum length of 1000.
Pattern: `^[\w\W\s\S]*$`
Required: No

 ** id **   <a name="auditmanager-Type-AssessmentReport-id"></a>
 The unique identifier for the assessment report.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
Required: No

 ** name **   <a name="auditmanager-Type-AssessmentReport-name"></a>
 The name that's given to the assessment report.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Pattern: `^[a-zA-Z0-9-_\.]+$`
Required: No

 ** status **   <a name="auditmanager-Type-AssessmentReport-status"></a>
 The current status of the specified assessment report.
Type: String
Valid Values: `COMPLETE | IN_PROGRESS | FAILED`
Required: No

## See Also
<a name="API_AssessmentReport_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/auditmanager-2017-07-25/AssessmentReport)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/auditmanager-2017-07-25/AssessmentReport)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/auditmanager-2017-07-25/AssessmentReport)
