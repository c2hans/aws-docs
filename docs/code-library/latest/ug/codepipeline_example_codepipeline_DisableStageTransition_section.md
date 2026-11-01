---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/codepipeline_example_codepipeline_DisableStageTransition_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DisableStageTransition` with a CLI
<a name="codepipeline_example_codepipeline_DisableStageTransition_section"></a>

The following code examples show how to use `DisableStageTransition`.

------
#### [ CLI ]

**AWS CLI**
**To disable a transition to a stage in a pipeline**
The following `disable-stage-transition` example disables transitions into the Beta stage of the MyFirstPipeline pipeline in AWS CodePipeline.

```
aws codepipeline disable-stage-transition \
    --pipeline-name {{MyFirstPipeline}} \
    --stage-name {{Beta}}  \
    --transition-type {{Inbound}} \
    --reason {{"An example reason"}}
```
This command produces no output.
For more information, see [Working with stage transitions in CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/transitions.html) in the *AWS CodePipeline User Guide*.
+  For API details, see [DisableStageTransition](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/disable-stage-transition.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example disables the inbound transition for the specified stage in the specified pipeline.**

```
Disable-CPStageTransition -PipelineName CodePipelineDemo -Reason "Disabling temporarily." -StageName Beta -TransitionType Inbound
```
+  For API details, see [DisableStageTransition](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example disables the inbound transition for the specified stage in the specified pipeline.**

```
Disable-CPStageTransition -PipelineName CodePipelineDemo -Reason "Disabling temporarily." -StageName Beta -TransitionType Inbound
```
+  For API details, see [DisableStageTransition](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------
