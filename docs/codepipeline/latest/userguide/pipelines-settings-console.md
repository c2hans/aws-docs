---
source_url: https://docs.aws.amazon.com/codepipeline/latest/userguide/pipelines-settings-console.html
---

# View the pipeline ARN and service role ARN (console)
<a name="pipelines-settings-console"></a>

You can use the console to view pipeline settings, such as the pipeline ARN, the service role ARN, and the pipeline artifact store.

1. Sign in to the AWS Management Console and open the CodePipeline console at [http://console.aws.amazon.com/codesuite/codepipeline/home](http://console.aws.amazon.com/codesuite/codepipeline/home).

   The names of all pipelines associated with your AWS account will be displayed.

1. Choose the name of your pipeline, and then choose **Settings** in the left-hand navigation pane. The page shows the following:
   + The pipeline name
   + The pipeline Amazon Resource Name (ARN)

     The pipeline ARN is constructed in this format:

     arn:aws:codepipeline:{{region}}:{{account}}:{{pipeline-name}}

     Sample pipeline ARN:

     `arn:aws:codepipeline:us-east-2:80398EXAMPLE:MyFirstPipeline`
   + The CodePipeline service role ARN for your pipeline
   + The pipeline version
   + The name and location of the artifact store for the pipeline

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodePipeline. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codepipeline` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
