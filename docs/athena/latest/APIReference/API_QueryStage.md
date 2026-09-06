---
source_url: https://docs.aws.amazon.com/athena/latest/APIReference/API_QueryStage.html
---

# QueryStage
<a name="API_QueryStage"></a>

Stage statistics such as input and output rows and bytes, execution time and stage state. This information also includes substages and the query stage plan.

## Contents
<a name="API_QueryStage_Contents"></a>

 ** ExecutionTime **   <a name="athena-Type-QueryStage-ExecutionTime"></a>
Time taken to execute this stage.
Type: Long
Required: No

 ** InputBytes **   <a name="athena-Type-QueryStage-InputBytes"></a>
The number of bytes input into the stage for execution.
Type: Long
Required: No

 ** InputRows **   <a name="athena-Type-QueryStage-InputRows"></a>
The number of rows input into the stage for execution.
Type: Long
Required: No

 ** OutputBytes **   <a name="athena-Type-QueryStage-OutputBytes"></a>
The number of bytes output from the stage after execution.
Type: Long
Required: No

 ** OutputRows **   <a name="athena-Type-QueryStage-OutputRows"></a>
The number of rows output from the stage after execution.
Type: Long
Required: No

 ** QueryStagePlan **   <a name="athena-Type-QueryStage-QueryStagePlan"></a>
Stage plan information such as name, identifier, sub plans, and source stages.
Type: [QueryStagePlanNode](API_QueryStagePlanNode.md) object
Required: No

 ** StageId **   <a name="athena-Type-QueryStage-StageId"></a>
The identifier for a stage.
Type: Long
Required: No

 ** State **   <a name="athena-Type-QueryStage-State"></a>
State of the stage after query execution.
Type: String
Required: No

 ** SubStages **   <a name="athena-Type-QueryStage-SubStages"></a>
List of sub query stages that form this stage execution plan.
Type: Array of [QueryStage](#API_QueryStage) objects
Required: No

## See Also
<a name="API_QueryStage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/athena-2017-05-18/QueryStage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/athena-2017-05-18/QueryStage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/athena-2017-05-18/QueryStage)
