---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ComputeNodeExecutionDetails.html
---

# ComputeNodeExecutionDetails
<a name="API_ComputeNodeExecutionDetails"></a>

Contains detailed execution information for a compute node within a pipeline execution.

## Contents
<a name="API_ComputeNodeExecutionDetails_Contents"></a>

 ** computeNodeName **   <a name="iotsitewise-Type-ComputeNodeExecutionDetails-computeNodeName"></a>
The name of the compute node.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** dependsOn **   <a name="iotsitewise-Type-ComputeNodeExecutionDetails-dependsOn"></a>
A list of compute node names that this node depends on.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** status **   <a name="iotsitewise-Type-ComputeNodeExecutionDetails-status"></a>
The current execution status of the compute node.
Type: [ComputeNodeExecutionStatus](API_ComputeNodeExecutionStatus.md) object
Required: Yes

 ** taskArn **   <a name="iotsitewise-Type-ComputeNodeExecutionDetails-taskArn"></a>
The ARN of the task.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:aws(-cn|-us-gov)?:[a-zA-Z0-9-:\/_\.]+$`
Required: Yes

 ** taskName **   <a name="iotsitewise-Type-ComputeNodeExecutionDetails-taskName"></a>
The name of the task executed for this compute node.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** taskVersion **   <a name="iotsitewise-Type-ComputeNodeExecutionDetails-taskVersion"></a>
The task version that executed for this compute node.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10.
Pattern: `^(0|([1-9]{1}\d*))$`
Required: Yes

 ** endTime **   <a name="iotsitewise-Type-ComputeNodeExecutionDetails-endTime"></a>
The time the compute node execution completed, in Unix epoch time.
Type: Timestamp
Required: No

 ** executionEnvironmentVariables **   <a name="iotsitewise-Type-ComputeNodeExecutionDetails-executionEnvironmentVariables"></a>
The fully resolved environment variables used for this compute node execution.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 255.
Value Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** startTime **   <a name="iotsitewise-Type-ComputeNodeExecutionDetails-startTime"></a>
The time the compute node execution started, in Unix epoch time.
Type: Timestamp
Required: No

## See Also
<a name="API_ComputeNodeExecutionDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/ComputeNodeExecutionDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/ComputeNodeExecutionDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/ComputeNodeExecutionDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
