---
source_url: https://docs.aws.amazon.com/codepipeline/latest/userguide/pipelines-sources.html
---

# Connect to first-party source providers using source actions
<a name="pipelines-sources"></a>

You can use the AWS CodePipeline console or the AWS CLI to connect to source action providers, such as CodeCommit or S3.

**Note**
When you use the console to create or edit a pipeline, the change detection resources are created for you. If you use the AWS CLI to create the pipeline, you must create the additional resources yourself. For more information, see [CodeCommit source actions and EventBridge](triggering.md).

**Topics**
+ [Amazon ECR source actions and EventBridge resources](create-cwe-ecr-source.md)
+ [Connecting to Amazon S3 source actions with a source enabled for events](create-S3-source-events.md)
+ [Connecting to Amazon S3 source actions that use EventBridge and AWS CloudTrail](create-cloudtrail-S3-source.md)
+ [CodeCommit source actions and EventBridge](triggering.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodePipeline. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codepipeline` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
