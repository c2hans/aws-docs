---
source_url: https://docs.aws.amazon.com/codepipeline/latest/userguide/pipelines-trigger-no-detection.html
---

# Add trigger to turn off change detection
<a name="pipelines-trigger-no-detection"></a>

Triggers allow you to configure your pipeline to start on a particular event type, such as a code push or pull request. Triggers are configurable for source actions with connections that use the `CodeStarSourceConnection` action in CodePipeline, such as GitHub, Bitbucket, and GitLab.

**Adding a trigger to turn off change detection (console)**

1. Sign in to the AWS Management Console and open the CodePipeline console at [http://console.aws.amazon.com/codesuite/codepipeline/home](http://console.aws.amazon.com/codesuite/codepipeline/home).

   The names and status of all pipelines associated with your AWS account are displayed.

1. In **Name**, choose the name of the pipeline you want to edit. Otherwise, use these steps on the pipeline creation wizard.

1. On the pipeline details page, choose **Edit**.

1. On the **Edit** page, choose the source action you want to edit. Choose **Edit triggers**. Choose to add a trigger.

1. In **Trigger type**, choose **Do not detect changes**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodePipeline. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codepipeline` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
