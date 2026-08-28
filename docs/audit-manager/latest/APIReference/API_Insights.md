---
source_url: https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_Insights.html
---

# Insights
<a name="API_Insights"></a>

A summary of the latest analytics data for all your active assessments.

This summary is a snapshot of the data that your active assessments collected on the `lastUpdated` date. It’s important to understand that the following totals are daily counts based on this date — they aren’t a total sum to date.

The `Insights` data is eventually consistent. This means that, when you read data from `Insights`, the response might not instantly reflect the results of a recently completed write or update operation. If you repeat your read request after a few hours, the response should return the latest data.

**Note**
If you delete an assessment or change its status to inactive, `InsightsByAssessment` includes data for that assessment as follows.
 **Inactive assessments** - If Audit Manager collected evidence for your assessment before you changed it inactive, that evidence is included in the `InsightsByAssessment` counts for that day.
 **Deleted assessments** - If Audit Manager collected evidence for your assessment before you deleted it, that evidence isn't included in the `InsightsByAssessment` counts for that day.

## Contents
<a name="API_Insights_Contents"></a>

 ** activeAssessmentsCount **   <a name="auditmanager-Type-Insights-activeAssessmentsCount"></a>
The number of active assessments in Audit Manager.
Type: Integer
Required: No

 ** assessmentControlsCountByNoncompliantEvidence **   <a name="auditmanager-Type-Insights-assessmentControlsCountByNoncompliantEvidence"></a>
The number of assessment controls that collected non-compliant evidence on the `lastUpdated` date.
Type: Integer
Required: No

 ** compliantEvidenceCount **   <a name="auditmanager-Type-Insights-compliantEvidenceCount"></a>
The number of compliance check evidence that Audit Manager classified as compliant on the `lastUpdated` date. This includes evidence that was collected from AWS Security Hub CSPM with a *Pass* ruling, or collected from AWS Config with a *Compliant* ruling.
Type: Integer
Required: No

 ** inconclusiveEvidenceCount **   <a name="auditmanager-Type-Insights-inconclusiveEvidenceCount"></a>
The number of evidence without a compliance check ruling. Evidence is inconclusive when the associated control uses AWS Security Hub CSPM or AWS Config as a data source but you didn't enable those services. This is also the case when a control uses a data source that doesn’t support compliance checks (for example: manual evidence, API calls, or AWS CloudTrail).
If evidence has a compliance check status of *not applicable*, it's classed as *inconclusive* in `Insights` data.
Type: Integer
Required: No

 ** lastUpdated **   <a name="auditmanager-Type-Insights-lastUpdated"></a>
The time when the cross-assessment insights were last updated.
Type: Timestamp
Required: No

 ** noncompliantEvidenceCount **   <a name="auditmanager-Type-Insights-noncompliantEvidenceCount"></a>
The number of compliance check evidence that Audit Manager classified as non-compliant on the `lastUpdated` date. This includes evidence that was collected from AWS Security Hub CSPM with a *Fail* ruling, or collected from AWS Config with a *Non-compliant* ruling.
Type: Integer
Required: No

 ** totalAssessmentControlsCount **   <a name="auditmanager-Type-Insights-totalAssessmentControlsCount"></a>
The total number of controls across all active assessments.
Type: Integer
Required: No

## See Also
<a name="API_Insights_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/auditmanager-2017-07-25/Insights)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/auditmanager-2017-07-25/Insights)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/auditmanager-2017-07-25/Insights)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Audit Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query audit-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
