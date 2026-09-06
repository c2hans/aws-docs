---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_PipelineExecutionStatus.html
---

# PipelineExecutionStatus
<a name="API_PipelineExecutionStatus"></a>

Current execution status of a pipeline.

## Contents
<a name="API_PipelineExecutionStatus_Contents"></a>

 ** state **   <a name="iotsitewise-Type-PipelineExecutionStatus-state"></a>
Current state of the pipeline execution.
Type: String
Valid Values: `NOT_STARTED | RUNNING | SUCCEEDED | FAILED | CANCELLING | CANCELLED`
Required: Yes

 ** stateDetails **   <a name="iotsitewise-Type-PipelineExecutionStatus-stateDetails"></a>
Additional information about the execution outcome. Populated when the execution has terminated (failed or cancelled).
Type: [PipelineExecutionStateDetails](API_PipelineExecutionStateDetails.md) object
Required: No

## See Also
<a name="API_PipelineExecutionStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/PipelineExecutionStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/PipelineExecutionStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/PipelineExecutionStatus)
