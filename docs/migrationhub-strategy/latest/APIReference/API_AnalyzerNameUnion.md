---
source_url: https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_AnalyzerNameUnion.html
---

# AnalyzerNameUnion
<a name="API_AnalyzerNameUnion"></a>

The combination of the existing analyzers.

## Contents
<a name="API_AnalyzerNameUnion_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** binaryAnalyzerName **   <a name="migrationhubstrategy-Type-AnalyzerNameUnion-binaryAnalyzerName"></a>
The binary analyzer names.
Type: String
Valid Values: `DLL_ANALYZER | BYTECODE_ANALYZER`
Required: No

 ** runTimeAnalyzerName **   <a name="migrationhubstrategy-Type-AnalyzerNameUnion-runTimeAnalyzerName"></a>
The assessment analyzer names.
Type: String
Valid Values: `A2C_ANALYZER | REHOST_ANALYZER | EMP_PA_ANALYZER | DATABASE_ANALYZER | SCT_ANALYZER`
Required: No

 ** sourceCodeAnalyzerName **   <a name="migrationhubstrategy-Type-AnalyzerNameUnion-sourceCodeAnalyzerName"></a>
The source code analyzer names.
Type: String
Valid Values: `CSHARP_ANALYZER | JAVA_ANALYZER | BYTECODE_ANALYZER | PORTING_ASSISTANT`
Required: No

## See Also
<a name="API_AnalyzerNameUnion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migrationhubstrategy-2020-02-19/AnalyzerNameUnion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migrationhubstrategy-2020-02-19/AnalyzerNameUnion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migrationhubstrategy-2020-02-19/AnalyzerNameUnion)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Migration Hub Strategy Recommendations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query migrationhub-strategy` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
