---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_PipelineExecutionSummary.html
---

# PipelineExecutionSummary
<a name="API_PipelineExecutionSummary"></a>

Contains summary information about a pipeline execution.

## Contents
<a name="API_PipelineExecutionSummary_Contents"></a>

 ** pipelineExecutionId **   <a name="iotsitewise-Type-PipelineExecutionSummary-pipelineExecutionId"></a>
The unique identifier of the pipeline execution.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: Yes

 ** pipelineVersion **   <a name="iotsitewise-Type-PipelineExecutionSummary-pipelineVersion"></a>
The pipeline version this execution ran against.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10.
Pattern: `^(0|([1-9]{1}\d*))$`
Required: Yes

 ** status **   <a name="iotsitewise-Type-PipelineExecutionSummary-status"></a>
The current execution status of the pipeline.
Type: [PipelineExecutionStatus](API_PipelineExecutionStatus.md) object
Required: Yes

 ** endTime **   <a name="iotsitewise-Type-PipelineExecutionSummary-endTime"></a>
The time the pipeline execution completed, in Unix epoch time.
Type: Timestamp
Required: No

 ** executionPriority **   <a name="iotsitewise-Type-PipelineExecutionSummary-executionPriority"></a>
Scheduling priority for the execution. When not specified, defaults to lowest priority.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 2.
Required: No

 ** startTime **   <a name="iotsitewise-Type-PipelineExecutionSummary-startTime"></a>
The time the pipeline execution started, in Unix epoch time.
Type: Timestamp
Required: No

## See Also
<a name="API_PipelineExecutionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/PipelineExecutionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/PipelineExecutionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/PipelineExecutionSummary)
