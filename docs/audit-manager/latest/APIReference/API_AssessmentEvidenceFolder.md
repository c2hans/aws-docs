---
source_url: https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_AssessmentEvidenceFolder.html
---

# AssessmentEvidenceFolder
<a name="API_AssessmentEvidenceFolder"></a>

 The folder where AWS Audit Manager stores evidence for an assessment.

## Contents
<a name="API_AssessmentEvidenceFolder_Contents"></a>

 ** assessmentId **   <a name="auditmanager-Type-AssessmentEvidenceFolder-assessmentId"></a>
 The identifier for the assessment.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
Required: No

 ** assessmentReportSelectionCount **   <a name="auditmanager-Type-AssessmentEvidenceFolder-assessmentReportSelectionCount"></a>
 The total count of evidence that's included in the assessment report.
Type: Integer
Required: No

 ** author **   <a name="auditmanager-Type-AssessmentEvidenceFolder-author"></a>
 The name of the user who created the evidence folder.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `.*`
Required: No

 ** controlId **   <a name="auditmanager-Type-AssessmentEvidenceFolder-controlId"></a>
 The unique identifier for the control.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
Required: No

 ** controlName **   <a name="auditmanager-Type-AssessmentEvidenceFolder-controlName"></a>
 The name of the control.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Pattern: `^[^\\]*$`
Required: No

 ** controlSetId **   <a name="auditmanager-Type-AssessmentEvidenceFolder-controlSetId"></a>
 The identifier for the control set.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Pattern: `^[\w\W\s\S]*$`
Required: No

 ** dataSource **   <a name="auditmanager-Type-AssessmentEvidenceFolder-dataSource"></a>
 The AWS service that the evidence was collected from.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `.*`
Required: No

 ** date **   <a name="auditmanager-Type-AssessmentEvidenceFolder-date"></a>
 The date when the first evidence was added to the evidence folder.
Type: Timestamp
Required: No

 ** evidenceAwsServiceSourceCount **   <a name="auditmanager-Type-AssessmentEvidenceFolder-evidenceAwsServiceSourceCount"></a>
 The total number of AWS resources that were assessed to generate the evidence.
Type: Integer
Required: No

 ** evidenceByTypeComplianceCheckCount **   <a name="auditmanager-Type-AssessmentEvidenceFolder-evidenceByTypeComplianceCheckCount"></a>
 The number of evidence that falls under the compliance check category. This evidence is collected from AWS Config or AWS Security Hub CSPM.
Type: Integer
Required: No

 ** evidenceByTypeComplianceCheckIssuesCount **   <a name="auditmanager-Type-AssessmentEvidenceFolder-evidenceByTypeComplianceCheckIssuesCount"></a>
 The total number of issues that were reported directly from AWS Security Hub CSPM, AWS Config, or both.
Type: Integer
Required: No

 ** evidenceByTypeConfigurationDataCount **   <a name="auditmanager-Type-AssessmentEvidenceFolder-evidenceByTypeConfigurationDataCount"></a>
 The number of evidence that falls under the configuration data category. This evidence is collected from configuration snapshots of other AWS services such as Amazon EC2, Amazon S3, or IAM.
Type: Integer
Required: No

 ** evidenceByTypeManualCount **   <a name="auditmanager-Type-AssessmentEvidenceFolder-evidenceByTypeManualCount"></a>
 The number of evidence that falls under the manual category. This evidence is imported manually.
Type: Integer
Required: No

 ** evidenceByTypeUserActivityCount **   <a name="auditmanager-Type-AssessmentEvidenceFolder-evidenceByTypeUserActivityCount"></a>
 The number of evidence that falls under the user activity category. This evidence is collected from AWS CloudTrail logs.
Type: Integer
Required: No

 ** evidenceResourcesIncludedCount **   <a name="auditmanager-Type-AssessmentEvidenceFolder-evidenceResourcesIncludedCount"></a>
 The amount of evidence that's included in the evidence folder.
Type: Integer
Required: No

 ** id **   <a name="auditmanager-Type-AssessmentEvidenceFolder-id"></a>
 The identifier for the folder that the evidence is stored in.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
Required: No

 ** name **   <a name="auditmanager-Type-AssessmentEvidenceFolder-name"></a>
 The name of the evidence folder.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Pattern: `^[\w\W\s\S]*$`
Required: No

 ** totalEvidence **   <a name="auditmanager-Type-AssessmentEvidenceFolder-totalEvidence"></a>
 The total amount of evidence in the evidence folder.
Type: Integer
Required: No

## See Also
<a name="API_AssessmentEvidenceFolder_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/auditmanager-2017-07-25/AssessmentEvidenceFolder)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/auditmanager-2017-07-25/AssessmentEvidenceFolder)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/auditmanager-2017-07-25/AssessmentEvidenceFolder)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Audit Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query audit-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
