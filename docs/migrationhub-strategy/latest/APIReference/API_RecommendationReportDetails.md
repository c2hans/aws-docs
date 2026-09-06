---
source_url: https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_RecommendationReportDetails.html
---

# RecommendationReportDetails
<a name="API_RecommendationReportDetails"></a>

 Contains detailed information about a recommendation report.

## Contents
<a name="API_RecommendationReportDetails_Contents"></a>

 ** completionTime **   <a name="migrationhubstrategy-Type-RecommendationReportDetails-completionTime"></a>
 The time that the recommendation report generation task completes.
Type: Timestamp
Required: No

 ** s3Bucket **   <a name="migrationhubstrategy-Type-RecommendationReportDetails-s3Bucket"></a>
 The S3 bucket where the report file is located.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*\S.*`
Required: No

 ** s3Keys **   <a name="migrationhubstrategy-Type-RecommendationReportDetails-s3Keys"></a>
 The Amazon S3 key name of the report file.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*\S.*`
Required: No

 ** startTime **   <a name="migrationhubstrategy-Type-RecommendationReportDetails-startTime"></a>
 The time that the recommendation report generation task starts.
Type: Timestamp
Required: No

 ** status **   <a name="migrationhubstrategy-Type-RecommendationReportDetails-status"></a>
 The status of the recommendation report generation task.
Type: String
Valid Values: `FAILED | IN_PROGRESS | SUCCESS`
Required: No

 ** statusMessage **   <a name="migrationhubstrategy-Type-RecommendationReportDetails-statusMessage"></a>
 The status message for recommendation report generation.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 512.
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_RecommendationReportDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migrationhubstrategy-2020-02-19/RecommendationReportDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migrationhubstrategy-2020-02-19/RecommendationReportDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migrationhubstrategy-2020-02-19/RecommendationReportDetails)
