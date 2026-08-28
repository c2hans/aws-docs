---
source_url: https://docs.aws.amazon.com/codebuild/latest/userguide/how-to-tag-report-group.html
---

# Tag a report group in AWS CodeBuild
<a name="how-to-tag-report-group"></a>

A *tag* is a custom attribute label that you or AWS assigns to an AWS resource. Each AWS tag has two parts:
+ A *tag key* (for example, `CostCenter`, `Environment`, `Project`, or `Secret`). Tag keys are case sensitive.
+ An optional field known as a *tag value* (for example, `111122223333`, `Production`, or a team name). Omitting the tag value is the same as using an empty string. Like tag keys, tag values are case sensitive.

Together these are known as key-value pairs. For limits on the number of tags you can have on a report group and restrictions on tag keys and values, see [Tags](limits.md#tag-limits).

Tags help you identify and organize your AWS resources. Many AWS services support tagging, so you can assign the same tag to resources from different services to indicate that the resources are related. For example, you can assign the same tag to a CodeBuild report group that you assign to an Amazon S3 bucket. For more information about using tags, see the [Tagging best practices](https://d1.awsstatic.com/whitepapers/aws-tagging-best-practices.pdf) whitepaper.

In CodeBuild, the primary resources are the report group and the project. You can use the CodeBuild console, the AWS CLI, CodeBuild APIs, or AWS SDKs to add, manage, and remove tags for a report group. In addition to identifying, organizing, and tracking your report group with tags, you can use tags in IAM policies to help control who can view and interact with your report group. For examples of tag-based access policies, see [Using tags to control access to AWS CodeBuild resources](auth-and-access-control-using-tags.md).

**Topics**
+ [Add tags to a report group](how-to-tag-report-group-add.md)
+ [View tags for a report group](how-to-tag-report-group-list.md)
+ [Edit tags for a report group](how-to-tag-report-group-update.md)
+ [Remove tags from a report group](how-to-tag-report-group-delete.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeBuild. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codebuild` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
