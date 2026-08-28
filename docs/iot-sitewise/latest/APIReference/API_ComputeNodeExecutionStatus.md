---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ComputeNodeExecutionStatus.html
---

# ComputeNodeExecutionStatus
<a name="API_ComputeNodeExecutionStatus"></a>

Current execution status of a compute node within a pipeline execution.

## Contents
<a name="API_ComputeNodeExecutionStatus_Contents"></a>

 ** state **   <a name="iotsitewise-Type-ComputeNodeExecutionStatus-state"></a>
Current state of the compute node execution.
Type: String
Valid Values: `NOT_STARTED | QUEUED | RUNNING | SUCCEEDED | FAILED`
Required: Yes

 ** stateDetails **   <a name="iotsitewise-Type-ComputeNodeExecutionStatus-stateDetails"></a>
Additional information about the compute node's failure. Populated when the compute node has failed.
Type: [ComputeNodeExecutionStateDetails](API_ComputeNodeExecutionStateDetails.md) object
Required: No

## See Also
<a name="API_ComputeNodeExecutionStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/ComputeNodeExecutionStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/ComputeNodeExecutionStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/ComputeNodeExecutionStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
