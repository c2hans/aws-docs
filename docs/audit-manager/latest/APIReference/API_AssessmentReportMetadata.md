---
source_url: https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_AssessmentReportMetadata.html
---

# AssessmentReportMetadata
<a name="API_AssessmentReportMetadata"></a>

 The metadata objects that are associated with the specified assessment report.

## Contents
<a name="API_AssessmentReportMetadata_Contents"></a>

 ** assessmentId **   <a name="auditmanager-Type-AssessmentReportMetadata-assessmentId"></a>
 The unique identifier for the associated assessment.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
Required: No

 ** assessmentName **   <a name="auditmanager-Type-AssessmentReportMetadata-assessmentName"></a>
The name of the associated assessment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Pattern: `^[^\\]*$`
Required: No

 ** author **   <a name="auditmanager-Type-AssessmentReportMetadata-author"></a>
 The name of the user who created the assessment report.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[a-zA-Z0-9-_()\s\+=,.@]+$`
Required: No

 ** creationTime **   <a name="auditmanager-Type-AssessmentReportMetadata-creationTime"></a>
 Specifies when the assessment report was created.
Type: Timestamp
Required: No

 ** description **   <a name="auditmanager-Type-AssessmentReportMetadata-description"></a>
 The description of the assessment report.
Type: String
Length Constraints: Maximum length of 1000.
Pattern: `^[\w\W\s\S]*$`
Required: No

 ** id **   <a name="auditmanager-Type-AssessmentReportMetadata-id"></a>
 The unique identifier for the assessment report.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
Required: No

 ** name **   <a name="auditmanager-Type-AssessmentReportMetadata-name"></a>
 The name of the assessment report.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Pattern: `^[a-zA-Z0-9-_\.]+$`
Required: No

 ** status **   <a name="auditmanager-Type-AssessmentReportMetadata-status"></a>
 The current status of the assessment report.
Type: String
Valid Values: `COMPLETE | IN_PROGRESS | FAILED`
Required: No

## See Also
<a name="API_AssessmentReportMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/auditmanager-2017-07-25/AssessmentReportMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/auditmanager-2017-07-25/AssessmentReportMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/auditmanager-2017-07-25/AssessmentReportMetadata)
