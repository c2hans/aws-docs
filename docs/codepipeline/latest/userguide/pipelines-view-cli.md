---
source_url: https://docs.aws.amazon.com/codepipeline/latest/userguide/pipelines-view-cli.html
---

# View pipeline details and history (CLI)
<a name="pipelines-view-cli"></a>

You can run the following commands to view details about your pipelines and pipeline executions:
+  **list-pipelines** command to view a summary of all of the pipelines associated with your AWS account.
+ **get-pipeline** command to review details of a single pipeline.
+ **list-pipeline-executions** to view summaries of the most recent executions for a pipeline.
+ **get-pipeline-execution** to view information about an execution of a pipeline, including details about artifacts, the pipeline execution ID, and the name, version, and status of the pipeline.
+ **get-pipeline-state** command to view pipeline, stage, and action status.
+ **list-action-executions** to view action execution details for a pipeline.

**Topics**

1. Open a terminal (Linux, macOS, or Unix) or command prompt (Windows) and use the AWS CLI to run the **[list-pipelines](http://docs.aws.amazon.com/cli/latest/reference/codepipeline/list-pipelines.html)** command:

   ```
   aws codepipeline list-pipelines
   ```

   This command returns a list of all of the pipelines associated with your AWS account.

1. To view details about a pipeline, run the **[get-pipeline](http://docs.aws.amazon.com/cli/latest/reference/codepipeline/get-pipeline.html)** command, specifying the unique name of the pipeline. For example, to view details about a pipeline named {{MyFirstPipeline}}, enter the following:

   ```
   aws codepipeline get-pipeline --name {{MyFirstPipeline}}
   ```

   This command returns the structure of the pipeline.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodePipeline. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codepipeline` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
