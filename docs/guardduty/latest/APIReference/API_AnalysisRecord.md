---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_AnalysisRecord.html
---

# AnalysisRecord
<a name="API_AnalysisRecord"></a>

Contains an assessment that GuardDuty derived from the data during an investigation, such as a threat assessment, a comparison against normal behavior, or a process lineage. The record contains at most one of the payload members, the one that corresponds to `AnalysisType`. `Indicators` can accompany any analysis type.

## Contents
<a name="API_AnalysisRecord_Contents"></a>

 ** analysisType **   <a name="guardduty-Type-AnalysisRecord-analysisType"></a>
The kind of analysis. The value identifies the payload member that can be set: `REPUTATION`, `THREAT_ASSESSMENT`, and `RDS_THREAT_ASSESSMENT` (`ThreatAssessment`); `KUBERNETES_POLICY_VIOLATION` (`KubernetesPolicyViolation`); `S3_EXPOSURE`, `S3_ACTOR_CONTEXT`, and `S3_PEN_TEST` (`S3Analysis`); `PROCESS_LINEAGE` (`Processes`); and `TREND` and `BASELINE` (`AccountAnalysis`).
Type: String
Valid Values: `REPUTATION | THREAT_ASSESSMENT | RDS_THREAT_ASSESSMENT | KUBERNETES_POLICY_VIOLATION | S3_EXPOSURE | S3_ACTOR_CONTEXT | S3_PEN_TEST | PROCESS_LINEAGE | TREND | BASELINE`
Required: Yes

 ** accountAnalysis **   <a name="guardduty-Type-AnalysisRecord-accountAnalysis"></a>
An analysis of the findings in an account over time. Set when `AnalysisType` is `TREND` or `BASELINE`.
Type: [InvestigationAccountAnalysis](API_InvestigationAccountAnalysis.md) object
Required: No

 ** indicators **   <a name="guardduty-Type-AnalysisRecord-indicators"></a>
The threat indicators associated with the analysis, such as an IP address, a domain, or a file hash.
Type: Array of [InvestigationIndicator](API_InvestigationIndicator.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Required: No

 ** kubernetesPolicyViolation **   <a name="guardduty-Type-AnalysisRecord-kubernetesPolicyViolation"></a>
An assessment of a Kubernetes policy violation. Set when `AnalysisType` is `KUBERNETES_POLICY_VIOLATION`.
Type: [KubernetesPolicyViolation](API_KubernetesPolicyViolation.md) object
Required: No

 ** processes **   <a name="guardduty-Type-AnalysisRecord-processes"></a>
The processes in a process lineage. Set when `AnalysisType` is `PROCESS_LINEAGE`.
Type: Array of [Process](API_Process.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Required: No

 ** s3Analysis **   <a name="guardduty-Type-AnalysisRecord-s3Analysis"></a>
An analysis of Amazon S3 activity or exposure. Set when `AnalysisType` is `S3_EXPOSURE`, `S3_ACTOR_CONTEXT`, or `S3_PEN_TEST`.
Type: [S3Analysis](API_S3Analysis.md) object
Required: No

 ** threatAssessment **   <a name="guardduty-Type-AnalysisRecord-threatAssessment"></a>
A threat assessment. Set when `AnalysisType` is `REPUTATION`, `THREAT_ASSESSMENT`, or `RDS_THREAT_ASSESSMENT`.
Type: [InvestigationThreatAssessment](API_InvestigationThreatAssessment.md) object
Required: No

## See Also
<a name="API_AnalysisRecord_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/AnalysisRecord)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/AnalysisRecord)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/AnalysisRecord)
