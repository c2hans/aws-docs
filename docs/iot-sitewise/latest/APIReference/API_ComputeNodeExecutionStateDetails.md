---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ComputeNodeExecutionStateDetails.html
---

# ComputeNodeExecutionStateDetails
<a name="API_ComputeNodeExecutionStateDetails"></a>

Additional information about a compute node that has failed.

## Contents
<a name="API_ComputeNodeExecutionStateDetails_Contents"></a>

 ** code **   <a name="iotsitewise-Type-ComputeNodeExecutionStateDetails-code"></a>
Classification of the failure.
Type: String
Valid Values: `VALIDATION_ERROR | INTERNAL_FAILURE | EXECUTION_ERROR | TIMED_OUT`
Required: Yes

 ** message **   <a name="iotsitewise-Type-ComputeNodeExecutionStateDetails-message"></a>
Human-readable description of why the compute node failed.
Type: String
Required: Yes

 ** details **   <a name="iotsitewise-Type-ComputeNodeExecutionStateDetails-details"></a>
Detailed error entries to help diagnose the failure.
Type: Array of [DetailedPipelineError](API_DetailedPipelineError.md) objects
Required: No

## See Also
<a name="API_ComputeNodeExecutionStateDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/ComputeNodeExecutionStateDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/ComputeNodeExecutionStateDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/ComputeNodeExecutionStateDetails)
