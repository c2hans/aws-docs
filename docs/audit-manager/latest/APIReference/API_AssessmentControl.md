---
source_url: https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_AssessmentControl.html
---

# AssessmentControl
<a name="API_AssessmentControl"></a>

 The control entity that represents a standard control or a custom control in an Audit Manager assessment.

## Contents
<a name="API_AssessmentControl_Contents"></a>

 ** assessmentReportEvidenceCount **   <a name="auditmanager-Type-AssessmentControl-assessmentReportEvidenceCount"></a>
 The amount of evidence in the assessment report.
Type: Integer
Required: No

 ** comments **   <a name="auditmanager-Type-AssessmentControl-comments"></a>
 The list of comments that's attached to the control.
Type: Array of [ControlComment](API_ControlComment.md) objects
Required: No

 ** description **   <a name="auditmanager-Type-AssessmentControl-description"></a>
 *This member has been deprecated.*
 The description of the control.
Type: String
Length Constraints: Maximum length of 1000.
Pattern: `^[\w\W\s\S]*$`
Required: No

 ** evidenceCount **   <a name="auditmanager-Type-AssessmentControl-evidenceCount"></a>
 The amount of evidence that's collected for the control.
Type: Integer
Required: No

 ** evidenceSources **   <a name="auditmanager-Type-AssessmentControl-evidenceSources"></a>
 The list of data sources for the evidence.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `.*\S.*`
Required: No

 ** id **   <a name="auditmanager-Type-AssessmentControl-id"></a>
 The identifier for the control.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
Required: No

 ** name **   <a name="auditmanager-Type-AssessmentControl-name"></a>
 The name of the control.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Pattern: `^[^\\]*$`
Required: No

 ** response **   <a name="auditmanager-Type-AssessmentControl-response"></a>
 The response of the control.
Type: String
Valid Values: `MANUAL | AUTOMATE | DEFER | IGNORE`
Required: No

 ** status **   <a name="auditmanager-Type-AssessmentControl-status"></a>
 The status of the control.
Type: String
Valid Values: `UNDER_REVIEW | REVIEWED | INACTIVE`
Required: No

## See Also
<a name="API_AssessmentControl_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/auditmanager-2017-07-25/AssessmentControl)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/auditmanager-2017-07-25/AssessmentControl)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/auditmanager-2017-07-25/AssessmentControl)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Audit Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query audit-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
