---
source_url: https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_AssessmentSummary.html
---

# AssessmentSummary
<a name="API_AssessmentSummary"></a>

 Contains the summary of the assessment results.

## Contents
<a name="API_AssessmentSummary_Contents"></a>

 ** antipatternReportS3Object **   <a name="migrationhubstrategy-Type-AssessmentSummary-antipatternReportS3Object"></a>
 The Amazon S3 object containing the anti-pattern report.
Type: [S3Object](API_S3Object.md) object
Required: No

 ** antipatternReportStatus **   <a name="migrationhubstrategy-Type-AssessmentSummary-antipatternReportStatus"></a>
 The status of the anti-pattern report.
Type: String
Valid Values: `FAILED | IN_PROGRESS | SUCCESS`
Required: No

 ** antipatternReportStatusMessage **   <a name="migrationhubstrategy-Type-AssessmentSummary-antipatternReportStatusMessage"></a>
 The status message of the anti-pattern report.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*\S.*`
Required: No

 ** lastAnalyzedTimestamp **   <a name="migrationhubstrategy-Type-AssessmentSummary-lastAnalyzedTimestamp"></a>
 The time the assessment was performed.
Type: Timestamp
Required: No

 ** listAntipatternSeveritySummary **   <a name="migrationhubstrategy-Type-AssessmentSummary-listAntipatternSeveritySummary"></a>
 List of AntipatternSeveritySummary.
Type: Array of [AntipatternSeveritySummary](API_AntipatternSeveritySummary.md) objects
Required: No

 ** listApplicationComponentStatusSummary **   <a name="migrationhubstrategy-Type-AssessmentSummary-listApplicationComponentStatusSummary"></a>
List of status summaries of the analyzed application components.
Type: Array of [ApplicationComponentStatusSummary](API_ApplicationComponentStatusSummary.md) objects
Required: No

 ** listApplicationComponentStrategySummary **   <a name="migrationhubstrategy-Type-AssessmentSummary-listApplicationComponentStrategySummary"></a>
 List of ApplicationComponentStrategySummary.
Type: Array of [StrategySummary](API_StrategySummary.md) objects
Required: No

 ** listApplicationComponentSummary **   <a name="migrationhubstrategy-Type-AssessmentSummary-listApplicationComponentSummary"></a>
 List of ApplicationComponentSummary.
Type: Array of [ApplicationComponentSummary](API_ApplicationComponentSummary.md) objects
Required: No

 ** listServerStatusSummary **   <a name="migrationhubstrategy-Type-AssessmentSummary-listServerStatusSummary"></a>
List of status summaries of the analyzed servers.
Type: Array of [ServerStatusSummary](API_ServerStatusSummary.md) objects
Required: No

 ** listServerStrategySummary **   <a name="migrationhubstrategy-Type-AssessmentSummary-listServerStrategySummary"></a>
 List of ServerStrategySummary.
Type: Array of [StrategySummary](API_StrategySummary.md) objects
Required: No

 ** listServerSummary **   <a name="migrationhubstrategy-Type-AssessmentSummary-listServerSummary"></a>
 List of ServerSummary.
Type: Array of [ServerSummary](API_ServerSummary.md) objects
Required: No

## See Also
<a name="API_AssessmentSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migrationhubstrategy-2020-02-19/AssessmentSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migrationhubstrategy-2020-02-19/AssessmentSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migrationhubstrategy-2020-02-19/AssessmentSummary)
