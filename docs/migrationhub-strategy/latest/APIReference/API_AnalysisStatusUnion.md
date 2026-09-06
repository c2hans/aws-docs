---
source_url: https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_AnalysisStatusUnion.html
---

# AnalysisStatusUnion
<a name="API_AnalysisStatusUnion"></a>

A combination of existing analysis statuses.

## Contents
<a name="API_AnalysisStatusUnion_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** runtimeAnalysisStatus **   <a name="migrationhubstrategy-Type-AnalysisStatusUnion-runtimeAnalysisStatus"></a>
The status of the analysis.
Type: String
Valid Values: `ANALYSIS_TO_BE_SCHEDULED | ANALYSIS_STARTED | ANALYSIS_SUCCESS | ANALYSIS_FAILED`
Required: No

 ** srcCodeOrDbAnalysisStatus **   <a name="migrationhubstrategy-Type-AnalysisStatusUnion-srcCodeOrDbAnalysisStatus"></a>
The status of the source code or database analysis.
Type: String
Valid Values: `ANALYSIS_TO_BE_SCHEDULED | ANALYSIS_STARTED | ANALYSIS_SUCCESS | ANALYSIS_FAILED | ANALYSIS_PARTIAL_SUCCESS | UNCONFIGURED | CONFIGURED`
Required: No

## See Also
<a name="API_AnalysisStatusUnion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migrationhubstrategy-2020-02-19/AnalysisStatusUnion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migrationhubstrategy-2020-02-19/AnalysisStatusUnion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migrationhubstrategy-2020-02-19/AnalysisStatusUnion)
