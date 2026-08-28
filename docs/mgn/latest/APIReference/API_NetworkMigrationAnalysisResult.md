---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_NetworkMigrationAnalysisResult.html
---

# NetworkMigrationAnalysisResult
<a name="API_NetworkMigrationAnalysisResult"></a>

The result of a network migration analysis operation.

## Contents
<a name="API_NetworkMigrationAnalysisResult_Contents"></a>

 ** analysisResult **   <a name="mgn-Type-NetworkMigrationAnalysisResult-analysisResult"></a>
The detailed analysis findings and recommendations.
Type: String
Required: No

 ** analyzerType **   <a name="mgn-Type-NetworkMigrationAnalysisResult-analyzerType"></a>
The type of analyzer that generated this result.
Type: String
Valid Values: `REACHABILITY_ANALYZER`
Required: No

 ** jobID **   <a name="mgn-Type-NetworkMigrationAnalysisResult-jobID"></a>
The unique identifier of the analysis job that generated this result.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

 ** networkMigrationDefinitionID **   <a name="mgn-Type-NetworkMigrationAnalysisResult-networkMigrationDefinitionID"></a>
The unique identifier of the network migration definition.
Type: String
Length Constraints: Fixed length of 21.
Pattern: `nmd-[0-9a-zA-Z]{17}`
Required: No

 ** networkMigrationExecutionID **   <a name="mgn-Type-NetworkMigrationAnalysisResult-networkMigrationExecutionID"></a>
The unique identifier of the network migration execution.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

 ** source **   <a name="mgn-Type-NetworkMigrationAnalysisResult-source"></a>
The source resource that was analyzed.
Type: [NetworkMigrationAnalysisResultSource](API_NetworkMigrationAnalysisResultSource.md) object
Required: No

 ** status **   <a name="mgn-Type-NetworkMigrationAnalysisResult-status"></a>
The status of the analysis result.
Type: String
Valid Values: `PENDING | STARTED | SUCCEEDED | FAILED`
Required: No

 ** target **   <a name="mgn-Type-NetworkMigrationAnalysisResult-target"></a>
The target resource in the analysis.
Type: [NetworkMigrationAnalysisResultTarget](API_NetworkMigrationAnalysisResultTarget.md) object
Required: No

## See Also
<a name="API_NetworkMigrationAnalysisResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/NetworkMigrationAnalysisResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/NetworkMigrationAnalysisResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/NetworkMigrationAnalysisResult)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for ApplicationMigrationService. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mgn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
