---
source_url: https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_InsightsByAssessment.html
---

# InsightsByAssessment
<a name="API_InsightsByAssessment"></a>

A summary of the latest analytics data for a specific active assessment.

This summary is a snapshot of the data that was collected on the `lastUpdated` date. It’s important to understand that the totals in `InsightsByAssessment` are daily counts based on this date — they aren’t a total sum to date.

The `InsightsByAssessment` data is eventually consistent. This means that when you read data from `InsightsByAssessment`, the response might not instantly reflect the results of a recently completed write or update operation. If you repeat your read request after a few hours, the response returns the latest data.

**Note**
If you delete an assessment or change its status to inactive, `InsightsByAssessment` includes data for that assessment as follows.
 **Inactive assessments** - If Audit Manager collected evidence for your assessment before you changed it inactive, that evidence is included in the `InsightsByAssessment` counts for that day.
 **Deleted assessments** - If Audit Manager collected evidence for your assessment before you deleted it, that evidence isn't included in the `InsightsByAssessment` counts for that day.

## Contents
<a name="API_InsightsByAssessment_Contents"></a>

 ** assessmentControlsCountByNoncompliantEvidence **   <a name="auditmanager-Type-InsightsByAssessment-assessmentControlsCountByNoncompliantEvidence"></a>
The number of assessment controls that collected non-compliant evidence on the `lastUpdated` date.
Type: Integer
Required: No

 ** compliantEvidenceCount **   <a name="auditmanager-Type-InsightsByAssessment-compliantEvidenceCount"></a>
The number of compliance check evidence that Audit Manager classified as compliant. This includes evidence that was collected from AWS Security Hub CSPM with a *Pass* ruling, or collected from AWS Config with a *Compliant* ruling.
Type: Integer
Required: No

 ** inconclusiveEvidenceCount **   <a name="auditmanager-Type-InsightsByAssessment-inconclusiveEvidenceCount"></a>
The amount of evidence without a compliance check ruling. Evidence is inconclusive if the associated control uses AWS Security Hub CSPM or AWS Config as a data source and you didn't enable those services. This is also the case if a control uses a data source that doesn’t support compliance checks (for example, manual evidence, API calls, or AWS CloudTrail).
If evidence has a compliance check status of *not applicable*, it's classified as *inconclusive* in `InsightsByAssessment` data.
Type: Integer
Required: No

 ** lastUpdated **   <a name="auditmanager-Type-InsightsByAssessment-lastUpdated"></a>
The time when the assessment insights were last updated.
Type: Timestamp
Required: No

 ** noncompliantEvidenceCount **   <a name="auditmanager-Type-InsightsByAssessment-noncompliantEvidenceCount"></a>
The number of compliance check evidence that Audit Manager classified as non-compliant. This includes evidence that was collected from AWS Security Hub CSPM with a *Fail* ruling, or collected from AWS Config with a *Non-compliant* ruling.
Type: Integer
Required: No

 ** totalAssessmentControlsCount **   <a name="auditmanager-Type-InsightsByAssessment-totalAssessmentControlsCount"></a>
The total number of controls in the assessment.
Type: Integer
Required: No

## See Also
<a name="API_InsightsByAssessment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/auditmanager-2017-07-25/InsightsByAssessment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/auditmanager-2017-07-25/InsightsByAssessment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/auditmanager-2017-07-25/InsightsByAssessment)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Audit Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query audit-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
