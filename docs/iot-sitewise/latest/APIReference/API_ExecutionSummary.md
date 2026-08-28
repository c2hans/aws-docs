---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ExecutionSummary.html
---

# ExecutionSummary
<a name="API_ExecutionSummary"></a>

Contains the execution summary of the computation model.

## Contents
<a name="API_ExecutionSummary_Contents"></a>

 ** executionId **   <a name="iotsitewise-Type-ExecutionSummary-executionId"></a>
The ID of the execution.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: Yes

 ** executionStartTime **   <a name="iotsitewise-Type-ExecutionSummary-executionStartTime"></a>
The time the process started.
Type: Timestamp
Required: Yes

 ** executionStatus **   <a name="iotsitewise-Type-ExecutionSummary-executionStatus"></a>
The status of the execution process.
Type: [ExecutionStatus](API_ExecutionStatus.md) object
Required: Yes

 ** targetResource **   <a name="iotsitewise-Type-ExecutionSummary-targetResource"></a>
The resource the action will be taken on. This can include asset-based resources and computation model resources.
Type: [TargetResource](API_TargetResource.md) object
Required: Yes

 ** targetResourceVersion **   <a name="iotsitewise-Type-ExecutionSummary-targetResourceVersion"></a>
The version of the target resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10.
Pattern: `^(0|([1-9]{1}\d*))$`
Required: Yes

 ** actionType **   <a name="iotsitewise-Type-ExecutionSummary-actionType"></a>
The type of action exectued.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: No

 ** executionEndTime **   <a name="iotsitewise-Type-ExecutionSummary-executionEndTime"></a>
The time the process ended.
Type: Timestamp
Required: No

 ** executionEntityVersion **   <a name="iotsitewise-Type-ExecutionSummary-executionEntityVersion"></a>
The execution entity version associated with the summary.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10.
Pattern: `^(0|([1-9]{1}\d*))$`
Required: No

 ** resolveTo **   <a name="iotsitewise-Type-ExecutionSummary-resolveTo"></a>
The detailed resource this execution resolves to.
Type: [ResolveTo](API_ResolveTo.md) object
Required: No

## See Also
<a name="API_ExecutionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/ExecutionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/ExecutionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/ExecutionSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
