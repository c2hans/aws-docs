---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/codepipeline_example_codepipeline_DeletePipeline_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DeletePipeline` with a CLI
<a name="codepipeline_example_codepipeline_DeletePipeline_section"></a>

The following code examples show how to use `DeletePipeline`.

------
#### [ CLI ]

**AWS CLI**
**To delete a pipeline**
This example deletes a pipeline named MySecondPipeline from AWS CodePipeline. Use the list-pipelines command to view a list of pipelines associated with your AWS account.
Command:

```
aws codepipeline delete-pipeline --name {{MySecondPipeline}}
```
Output:

```
None.
```
+  For API details, see [DeletePipeline](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/delete-pipeline.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example deletes the specified pipeline. The command will prompt for confirmation before proceeding. Add the -Force parameter to delete the pipeline without a prompt.**

```
Remove-CPPipeline -Name CodePipelineDemo
```
+  For API details, see [DeletePipeline](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example deletes the specified pipeline. The command will prompt for confirmation before proceeding. Add the -Force parameter to delete the pipeline without a prompt.**

```
Remove-CPPipeline -Name CodePipelineDemo
```
+  For API details, see [DeletePipeline](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------
