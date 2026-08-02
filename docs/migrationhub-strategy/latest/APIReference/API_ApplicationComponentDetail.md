---
source_url: https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_ApplicationComponentDetail.html
---

# ApplicationComponentDetail
<a name="API_ApplicationComponentDetail"></a>

 Contains detailed information about an application component.

## Contents
<a name="API_ApplicationComponentDetail_Contents"></a>

 ** analysisStatus **   <a name="migrationhubstrategy-Type-ApplicationComponentDetail-analysisStatus"></a>
 The status of analysis, if the application component has source code or an associated database.
Type: String
Valid Values: `ANALYSIS_TO_BE_SCHEDULED | ANALYSIS_STARTED | ANALYSIS_SUCCESS | ANALYSIS_FAILED | ANALYSIS_PARTIAL_SUCCESS | UNCONFIGURED | CONFIGURED`
Required: No

 ** antipatternReportS3Object **   <a name="migrationhubstrategy-Type-ApplicationComponentDetail-antipatternReportS3Object"></a>
 The S3 bucket name and the Amazon S3 key name for the anti-pattern report.
Type: [S3Object](API_S3Object.md) object
Required: No

 ** antipatternReportStatus **   <a name="migrationhubstrategy-Type-ApplicationComponentDetail-antipatternReportStatus"></a>
 The status of the anti-pattern report generation.
Type: String
Valid Values: `FAILED | IN_PROGRESS | SUCCESS`
Required: No

 ** antipatternReportStatusMessage **   <a name="migrationhubstrategy-Type-ApplicationComponentDetail-antipatternReportStatusMessage"></a>
 The status message for the anti-pattern.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*\S.*`
Required: No

 ** appType **   <a name="migrationhubstrategy-Type-ApplicationComponentDetail-appType"></a>
 The type of application component.
Type: String
Valid Values: `DotNetFramework | Java | SQLServer | IIS | Oracle | Other | Tomcat | JBoss | Spring | Mongo DB | DB2 | Maria DB | MySQL | Sybase | PostgreSQLServer | Cassandra | IBM WebSphere | Oracle WebLogic | Visual Basic | Unknown | DotnetCore | Dotnet`
Required: No

 ** appUnitError **   <a name="migrationhubstrategy-Type-ApplicationComponentDetail-appUnitError"></a>
The error in the analysis of the source code or database.
Type: [AppUnitError](API_AppUnitError.md) object
Required: No

 ** associatedServerId **   <a name="migrationhubstrategy-Type-ApplicationComponentDetail-associatedServerId"></a>
 The ID of the server that the application component is running on.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 27.
Pattern: `.*\S.*`
Required: No

 ** databaseConfigDetail **   <a name="migrationhubstrategy-Type-ApplicationComponentDetail-databaseConfigDetail"></a>
 Configuration details for the database associated with the application component.
Type: [DatabaseConfigDetail](API_DatabaseConfigDetail.md) object
Required: No

 ** id **   <a name="migrationhubstrategy-Type-ApplicationComponentDetail-id"></a>
 The ID of the application component.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 44.
Pattern: `[0-9a-b]+.*`
Required: No

 ** inclusionStatus **   <a name="migrationhubstrategy-Type-ApplicationComponentDetail-inclusionStatus"></a>
 Indicates whether the application component has been included for server recommendation or not.
Type: String
Valid Values: `excludeFromAssessment | includeInAssessment`
Required: No

 ** lastAnalyzedTimestamp **   <a name="migrationhubstrategy-Type-ApplicationComponentDetail-lastAnalyzedTimestamp"></a>
 The timestamp of when the application component was assessed.
Type: Timestamp
Required: No

 ** listAntipatternSeveritySummary **   <a name="migrationhubstrategy-Type-ApplicationComponentDetail-listAntipatternSeveritySummary"></a>
 A list of anti-pattern severity summaries.
Type: Array of [AntipatternSeveritySummary](API_AntipatternSeveritySummary.md) objects
Required: No

 ** moreServerAssociationExists **   <a name="migrationhubstrategy-Type-ApplicationComponentDetail-moreServerAssociationExists"></a>
 Set to true if the application component is running on multiple servers.
Type: Boolean
Required: No

 ** name **   <a name="migrationhubstrategy-Type-ApplicationComponentDetail-name"></a>
 The name of application component.
Type: String
Required: No

 ** osDriver **   <a name="migrationhubstrategy-Type-ApplicationComponentDetail-osDriver"></a>
 OS driver.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*\S.*`
Required: No

 ** osVersion **   <a name="migrationhubstrategy-Type-ApplicationComponentDetail-osVersion"></a>
 OS version.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*\S.*`
Required: No

 ** recommendationSet **   <a name="migrationhubstrategy-Type-ApplicationComponentDetail-recommendationSet"></a>
 The top recommendation set for the application component.
Type: [RecommendationSet](API_RecommendationSet.md) object
Required: No

 ** resourceSubType **   <a name="migrationhubstrategy-Type-ApplicationComponentDetail-resourceSubType"></a>
 The application component subtype.
Type: String
Valid Values: `Database | Process | DatabaseProcess`
Required: No

 ** resultList **   <a name="migrationhubstrategy-Type-ApplicationComponentDetail-resultList"></a>
A list of the analysis results.
Type: Array of [Result](API_Result.md) objects
Required: No

 ** runtimeStatus **   <a name="migrationhubstrategy-Type-ApplicationComponentDetail-runtimeStatus"></a>
The status of the application unit.
Type: String
Valid Values: `ANALYSIS_TO_BE_SCHEDULED | ANALYSIS_STARTED | ANALYSIS_SUCCESS | ANALYSIS_FAILED`
Required: No

 ** runtimeStatusMessage **   <a name="migrationhubstrategy-Type-ApplicationComponentDetail-runtimeStatusMessage"></a>
The status message for the application unit.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*\S.*`
Required: No

 ** sourceCodeRepositories **   <a name="migrationhubstrategy-Type-ApplicationComponentDetail-sourceCodeRepositories"></a>
 Details about the source code repository associated with the application component.
Type: Array of [SourceCodeRepository](API_SourceCodeRepository.md) objects
Required: No

 ** statusMessage **   <a name="migrationhubstrategy-Type-ApplicationComponentDetail-statusMessage"></a>
 A detailed description of the analysis status and any failure message.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_ApplicationComponentDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migrationhubstrategy-2020-02-19/ApplicationComponentDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migrationhubstrategy-2020-02-19/ApplicationComponentDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migrationhubstrategy-2020-02-19/ApplicationComponentDetail)
