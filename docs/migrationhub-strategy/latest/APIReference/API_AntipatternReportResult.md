---
source_url: https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_AntipatternReportResult.html
---

# AntipatternReportResult
<a name="API_AntipatternReportResult"></a>

The anti-pattern report result.

## Contents
<a name="API_AntipatternReportResult_Contents"></a>

 ** analyzerName **   <a name="migrationhubstrategy-Type-AntipatternReportResult-analyzerName"></a>
The analyzer name.
Type: [AnalyzerNameUnion](API_AnalyzerNameUnion.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** antiPatternReportS3Object **   <a name="migrationhubstrategy-Type-AntipatternReportResult-antiPatternReportS3Object"></a>
 Contains the S3 bucket name and the Amazon S3 key name.
Type: [S3Object](API_S3Object.md) object
Required: No

 ** antipatternReportStatus **   <a name="migrationhubstrategy-Type-AntipatternReportResult-antipatternReportStatus"></a>
The status of the anti-pattern report generation.
Type: String
Valid Values: `FAILED | IN_PROGRESS | SUCCESS`
Required: No

 ** antipatternReportStatusMessage **   <a name="migrationhubstrategy-Type-AntipatternReportResult-antipatternReportStatusMessage"></a>
The status message for the anti-pattern.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AntipatternReportResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migrationhubstrategy-2020-02-19/AntipatternReportResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migrationhubstrategy-2020-02-19/AntipatternReportResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migrationhubstrategy-2020-02-19/AntipatternReportResult)
