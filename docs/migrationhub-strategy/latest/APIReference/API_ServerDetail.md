---
source_url: https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_ServerDetail.html
---

# ServerDetail
<a name="API_ServerDetail"></a>

 Detailed information about a server.

## Contents
<a name="API_ServerDetail_Contents"></a>

 ** antipatternReportS3Object **   <a name="migrationhubstrategy-Type-ServerDetail-antipatternReportS3Object"></a>
 The S3 bucket name and Amazon S3 key name for anti-pattern report.
Type: [S3Object](API_S3Object.md) object
Required: No

 ** antipatternReportStatus **   <a name="migrationhubstrategy-Type-ServerDetail-antipatternReportStatus"></a>
 The status of the anti-pattern report generation.
Type: String
Valid Values: `FAILED | IN_PROGRESS | SUCCESS`
Required: No

 ** antipatternReportStatusMessage **   <a name="migrationhubstrategy-Type-ServerDetail-antipatternReportStatusMessage"></a>
 A message about the status of the anti-pattern report generation.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*\S.*`
Required: No

 ** applicationComponentStrategySummary **   <a name="migrationhubstrategy-Type-ServerDetail-applicationComponentStrategySummary"></a>
 A list of strategy summaries.
Type: Array of [StrategySummary](API_StrategySummary.md) objects
Required: No

 ** dataCollectionStatus **   <a name="migrationhubstrategy-Type-ServerDetail-dataCollectionStatus"></a>
 The status of assessment for the server.
Type: String
Valid Values: `dataCollectionTaskToBeScheduled | dataCollectionTaskScheduled | dataCollectionTaskStarted | dataCollectionTaskStopped | dataCollectionTaskSuccess | dataCollectionTaskFailed | dataCollectionTaskPartialSuccess`
Required: No

 ** id **   <a name="migrationhubstrategy-Type-ServerDetail-id"></a>
 The server ID.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 44.
Pattern: `[0-9a-b]+.*`
Required: No

 ** lastAnalyzedTimestamp **   <a name="migrationhubstrategy-Type-ServerDetail-lastAnalyzedTimestamp"></a>
 The timestamp of when the server was assessed.
Type: Timestamp
Required: No

 ** listAntipatternSeveritySummary **   <a name="migrationhubstrategy-Type-ServerDetail-listAntipatternSeveritySummary"></a>
 A list of anti-pattern severity summaries.
Type: Array of [AntipatternSeveritySummary](API_AntipatternSeveritySummary.md) objects
Required: No

 ** name **   <a name="migrationhubstrategy-Type-ServerDetail-name"></a>
 The name of the server.
Type: String
Required: No

 ** recommendationSet **   <a name="migrationhubstrategy-Type-ServerDetail-recommendationSet"></a>
 A set of recommendations.
Type: [RecommendationSet](API_RecommendationSet.md) object
Required: No

 ** serverError **   <a name="migrationhubstrategy-Type-ServerDetail-serverError"></a>
The error in server analysis.
Type: [ServerError](API_ServerError.md) object
Required: No

 ** serverType **   <a name="migrationhubstrategy-Type-ServerDetail-serverType"></a>
 The type of server.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*\S.*`
Required: No

 ** statusMessage **   <a name="migrationhubstrategy-Type-ServerDetail-statusMessage"></a>
 A message about the status of data collection, which contains detailed descriptions of any error messages.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*\S.*`
Required: No

 ** systemInfo **   <a name="migrationhubstrategy-Type-ServerDetail-systemInfo"></a>
 System information about the server.
Type: [SystemInfo](API_SystemInfo.md) object
Required: No

## See Also
<a name="API_ServerDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migrationhubstrategy-2020-02-19/ServerDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migrationhubstrategy-2020-02-19/ServerDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migrationhubstrategy-2020-02-19/ServerDetail)
