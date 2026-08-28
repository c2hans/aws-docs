---
source_url: https://docs.aws.amazon.com/codebuild/latest/userguide/monitoring-builds.html
---

# Monitor CodeBuild builds with CloudWatch
<a name="monitoring-builds"></a>

You can use Amazon CloudWatch to watch your builds, report when something is wrong, and take automatic actions when appropriate. You can monitor your builds at two levels:

Project level
These metrics are for all builds in the specified project. To see metrics for a project, specify `ProjectName` for the dimension in CloudWatch.

AWS account level
These metrics are for all builds in an account. To see metrics at the AWS account level, do not enter a dimension in CloudWatch. Build resource utilization metrics are not available at the AWS account level.

CloudWatch metrics show the behavior of your builds over time. For example, you can monitor:
+  How many builds were attempted in a build project or an AWS account over time.
+  How many builds were successful in a build project or an AWS account over time.
+  How many builds failed in a build project or an AWS account over time.
+  How much time CodeBuild spent running builds in a build project or an AWS account over time.
+ Build resource utilization for a build or an entire build project. Build resource utilization metrics include metrics such as CPU, memory, and storage utilization.

 For more information, see [View CodeBuild metrics](monitoring-metrics.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeBuild. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codebuild` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
