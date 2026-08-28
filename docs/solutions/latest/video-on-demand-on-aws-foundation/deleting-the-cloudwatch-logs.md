---
source_url: https://docs.aws.amazon.com/solutions/latest/video-on-demand-on-aws-foundation/deleting-the-cloudwatch-logs.html
---

# Deleting the CloudWatch Logs
<a name="deleting-the-cloudwatch-logs"></a>

 To prevent accidental data loss, this solution retains the CloudWatch logs if you decide to delete the CloudFormation stack. After uninstalling the solution, you can manually delete the logs if you don't need to retain the data. Follow these steps to delete the CloudWatch logs.

1.  Sign in to the [Amazon CloudWatch console](https://console.aws.amazon.com/cloudwatch/home).

1.  Choose **Log Groups** from the left navigation pane.

1.  Locate the log groups created by the solution.

1.  Select one of the log groups.

1.  Choose **Actions** and then choose **Delete.**

 Repeat the steps until you have deleted all the solution log groups.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Video on Demand on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
