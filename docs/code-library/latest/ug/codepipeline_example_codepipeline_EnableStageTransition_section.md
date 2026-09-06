---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/codepipeline_example_codepipeline_EnableStageTransition_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `EnableStageTransition` with a CLI
<a name="codepipeline_example_codepipeline_EnableStageTransition_section"></a>

The following code examples show how to use `EnableStageTransition`.

------
#### [ CLI ]

**AWS CLI**
**To enable a transition to a stage in a pipeline**
This example enables transitions into the Beta stage of the MyFirstPipeline pipeline in AWS CodePipeline.
Command:

```
aws codepipeline enable-stage-transition --pipeline-name {{MyFirstPipeline}} --stage-name {{Beta}}  --transition-type {{Inbound}}
```
Output:

```
None.
```
+  For API details, see [EnableStageTransition](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/enable-stage-transition.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example enables the inbound transition for the specified stage in the specified pipeline.**

```
Enable-CPStageTransition -PipelineName CodePipelineDemo -StageName Beta -TransitionType Inbound
```
+  For API details, see [EnableStageTransition](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example enables the inbound transition for the specified stage in the specified pipeline.**

```
Enable-CPStageTransition -PipelineName CodePipelineDemo -StageName Beta -TransitionType Inbound
```
+  For API details, see [EnableStageTransition](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------
