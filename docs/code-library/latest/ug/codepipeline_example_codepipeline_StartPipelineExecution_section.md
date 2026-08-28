---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/codepipeline_example_codepipeline_StartPipelineExecution_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `StartPipelineExecution` with a CLI
<a name="codepipeline_example_codepipeline_StartPipelineExecution_section"></a>

The following code examples show how to use `StartPipelineExecution`.

------
#### [ CLI ]

**AWS CLI**
**To run the latest revision through a pipeline**
This example runs the latest revision present in the source stage of a pipeline through the pipeline named "MyFirstPipeline".
Command:

```
aws codepipeline start-pipeline-execution --name {{MyFirstPipeline}}
```
Output:

```
{
  "pipelineExecutionId": "3137f7cb-7cf7-EXAMPLE"
}
```
+  For API details, see [StartPipelineExecution](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/start-pipeline-execution.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example starts running the specified pipeline.**

```
Start-CPPipelineExecution -Name CodePipelineDemo
```
+  For API details, see [StartPipelineExecution](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example starts running the specified pipeline.**

```
Start-CPPipelineExecution -Name CodePipelineDemo
```
+  For API details, see [StartPipelineExecution](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
