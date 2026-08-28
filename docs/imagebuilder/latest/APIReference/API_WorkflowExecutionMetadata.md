---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_WorkflowExecutionMetadata.html
---

# WorkflowExecutionMetadata
<a name="API_WorkflowExecutionMetadata"></a>

Metadata that includes details and status from this runtime instance of the workflow.

## Contents
<a name="API_WorkflowExecutionMetadata_Contents"></a>

 ** endTime **   <a name="imagebuilder-Type-WorkflowExecutionMetadata-endTime"></a>
The timestamp when this runtime instance of the workflow finished.
Type: String
Required: No

 ** message **   <a name="imagebuilder-Type-WorkflowExecutionMetadata-message"></a>
The runtime output message from the workflow, if applicable.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Required: No

 ** parallelGroup **   <a name="imagebuilder-Type-WorkflowExecutionMetadata-parallelGroup"></a>
The name of the test group that included the test workflow resource at runtime.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[A-Za-z0-9][A-Za-z0-9-_+#]{0,99}$`
Required: No

 ** retried **   <a name="imagebuilder-Type-WorkflowExecutionMetadata-retried"></a>
Indicates retry status for this runtime instance of the workflow.
Type: Boolean
Required: No

 ** startTime **   <a name="imagebuilder-Type-WorkflowExecutionMetadata-startTime"></a>
The timestamp when the runtime instance of this workflow started.
Type: String
Required: No

 ** status **   <a name="imagebuilder-Type-WorkflowExecutionMetadata-status"></a>
The current runtime status for this workflow.
Type: String
Valid Values: `PENDING | SKIPPED | RUNNING | COMPLETED | FAILED | ROLLBACK_IN_PROGRESS | ROLLBACK_COMPLETED | CANCELLED`
Required: No

 ** totalStepCount **   <a name="imagebuilder-Type-WorkflowExecutionMetadata-totalStepCount"></a>
The total number of steps in the workflow. This should equal the sum of the step counts for steps that succeeded, were skipped, and failed.
Type: Integer
Required: No

 ** totalStepsFailed **   <a name="imagebuilder-Type-WorkflowExecutionMetadata-totalStepsFailed"></a>
A runtime count for the number of steps in the workflow that failed.
Type: Integer
Required: No

 ** totalStepsSkipped **   <a name="imagebuilder-Type-WorkflowExecutionMetadata-totalStepsSkipped"></a>
A runtime count for the number of steps in the workflow that were skipped.
Type: Integer
Required: No

 ** totalStepsSucceeded **   <a name="imagebuilder-Type-WorkflowExecutionMetadata-totalStepsSucceeded"></a>
A runtime count for the number of steps in the workflow that ran successfully.
Type: Integer
Required: No

 ** type **   <a name="imagebuilder-Type-WorkflowExecutionMetadata-type"></a>
Indicates what type of workflow that Image Builder ran for this runtime instance of the workflow.
Type: String
Valid Values: `BUILD | TEST | DISTRIBUTION`
Required: No

 ** workflowBuildVersionArn **   <a name="imagebuilder-Type-WorkflowExecutionMetadata-workflowBuildVersionArn"></a>
The Amazon Resource Name (ARN) of the workflow resource build version that ran.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `^arn:aws(?:-[a-z]+)*:imagebuilder:[a-z]{2,}(?:-[a-z]+)+-[0-9]+:(?:[0-9]{12}|aws(?:-[a-z-]+)?):workflow/(build|test|distribution)/[a-z0-9-_]+/[0-9]+\.[0-9]+\.[0-9]+/[0-9]+$`
Required: No

 ** workflowExecutionId **   <a name="imagebuilder-Type-WorkflowExecutionMetadata-workflowExecutionId"></a>
Unique identifier that Image Builder assigns to keep track of runtime resources each time it runs a workflow.
Type: String
Pattern: `^wf-[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$`
Required: No

## See Also
<a name="API_WorkflowExecutionMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/WorkflowExecutionMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/WorkflowExecutionMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/WorkflowExecutionMetadata)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for EC2 Image Builder. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query imagebuilder` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
