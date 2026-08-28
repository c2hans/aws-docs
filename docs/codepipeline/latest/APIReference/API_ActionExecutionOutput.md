---
source_url: https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_ActionExecutionOutput.html
---

# ActionExecutionOutput
<a name="API_ActionExecutionOutput"></a>

Output details listed for an action execution, such as the action execution result.

## Contents
<a name="API_ActionExecutionOutput_Contents"></a>

 ** executionResult **   <a name="CodePipeline-Type-ActionExecutionOutput-executionResult"></a>
Execution result information listed in the output details for an action execution.
Type: [ActionExecutionResult](API_ActionExecutionResult.md) object
Required: No

 ** outputArtifacts **   <a name="CodePipeline-Type-ActionExecutionOutput-outputArtifacts"></a>
Details of output artifacts of the action that correspond to the action execution.
Type: Array of [ArtifactDetail](API_ArtifactDetail.md) objects
Required: No

 ** outputVariables **   <a name="CodePipeline-Type-ActionExecutionOutput-outputVariables"></a>
The outputVariables field shows the key-value pairs that were output as part of that execution.
Type: String to string map
Key Pattern: `[A-Za-z0-9@\-_]+`
Required: No

## See Also
<a name="API_ActionExecutionOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/ActionExecutionOutput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/ActionExecutionOutput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/ActionExecutionOutput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for CodePipeline. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codepipeline` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
