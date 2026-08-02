---
source_url: https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_ApplicationComponentStatusSummary.html
---

# ApplicationComponentStatusSummary
<a name="API_ApplicationComponentStatusSummary"></a>

Summary of the analysis status of the application component.

## Contents
<a name="API_ApplicationComponentStatusSummary_Contents"></a>

 ** count **   <a name="migrationhubstrategy-Type-ApplicationComponentStatusSummary-count"></a>
The number of application components successfully analyzed, partially successful or failed analysis.
Type: Integer
Required: No

 ** srcCodeOrDbAnalysisStatus **   <a name="migrationhubstrategy-Type-ApplicationComponentStatusSummary-srcCodeOrDbAnalysisStatus"></a>
The status of database analysis.
Type: String
Valid Values: `ANALYSIS_TO_BE_SCHEDULED | ANALYSIS_STARTED | ANALYSIS_SUCCESS | ANALYSIS_FAILED | ANALYSIS_PARTIAL_SUCCESS | UNCONFIGURED | CONFIGURED`
Required: No

## See Also
<a name="API_ApplicationComponentStatusSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migrationhubstrategy-2020-02-19/ApplicationComponentStatusSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migrationhubstrategy-2020-02-19/ApplicationComponentStatusSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migrationhubstrategy-2020-02-19/ApplicationComponentStatusSummary)
