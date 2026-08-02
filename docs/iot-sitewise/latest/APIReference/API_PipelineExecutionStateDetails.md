---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_PipelineExecutionStateDetails.html
---

# PipelineExecutionStateDetails
<a name="API_PipelineExecutionStateDetails"></a>

Additional information about the current execution status. Populated when the execution has terminated.

## Contents
<a name="API_PipelineExecutionStateDetails_Contents"></a>

 ** message **   <a name="iotsitewise-Type-PipelineExecutionStateDetails-message"></a>
Human-readable description of the outcome. For a failed execution, this describes why it failed; for a cancelled execution, this is the reason you supplied when calling CancelPipelineExecution.
Type: String
Required: Yes

 ** code **   <a name="iotsitewise-Type-PipelineExecutionStateDetails-code"></a>
Classification of the failure. Present when the execution failed.
Type: String
Valid Values: `VALIDATION_ERROR | INTERNAL_FAILURE | EXECUTION_ERROR | TIMED_OUT`
Required: No

 ** details **   <a name="iotsitewise-Type-PipelineExecutionStateDetails-details"></a>
Per-step error entries to help diagnose a failed execution. Present when the execution failed.
Type: Array of [DetailedPipelineError](API_DetailedPipelineError.md) objects
Required: No

## See Also
<a name="API_PipelineExecutionStateDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/PipelineExecutionStateDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/PipelineExecutionStateDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/PipelineExecutionStateDetails)
