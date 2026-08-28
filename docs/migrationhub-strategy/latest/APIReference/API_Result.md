---
source_url: https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_Result.html
---

# Result
<a name="API_Result"></a>

The error in server analysis.

## Contents
<a name="API_Result_Contents"></a>

 ** analysisStatus **   <a name="migrationhubstrategy-Type-Result-analysisStatus"></a>
The error in server analysis.
Type: [AnalysisStatusUnion](API_AnalysisStatusUnion.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** analysisType **   <a name="migrationhubstrategy-Type-Result-analysisType"></a>
The error in server analysis.
Type: String
Valid Values: `SOURCE_CODE_ANALYSIS | DATABASE_ANALYSIS | RUNTIME_ANALYSIS | BINARY_ANALYSIS`
Required: No

 ** antipatternReportResultList **   <a name="migrationhubstrategy-Type-Result-antipatternReportResultList"></a>
The error in server analysis.
Type: Array of [AntipatternReportResult](API_AntipatternReportResult.md) objects
Required: No

 ** statusMessage **   <a name="migrationhubstrategy-Type-Result-statusMessage"></a>
The error in server analysis.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_Result_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migrationhubstrategy-2020-02-19/Result)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migrationhubstrategy-2020-02-19/Result)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migrationhubstrategy-2020-02-19/Result)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Migration Hub Strategy Recommendations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query migrationhub-strategy` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
