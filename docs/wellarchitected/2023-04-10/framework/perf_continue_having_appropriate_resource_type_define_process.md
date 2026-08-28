---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/perf_continue_having_appropriate_resource_type_define_process.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# PERF06-BP02 Define a process to improve workload performance
<a name="perf_continue_having_appropriate_resource_type_define_process"></a>

 Define a process to evaluate new services, design patterns, resource types, and configurations as they become available. For example, run existing performance tests on new instance offerings to determine their potential to improve your workload.

 Your workload's performance has a few key constraints. Document these so that you know what kinds of innovation might improve the performance of your workload. Use this information when learning about new services or technology as it becomes available to identify ways to alleviate constraints or bottlenecks.

 **Common anti-patterns:**
+  You assume your current architecture will become static and never update over time.
+  You introduce architecture changes over time with no metric justification.

 **Benefits of establishing this best practice:** By defining your process for making architectural changes, you allow gathered data to influence your workload design over time.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>

 Identify the key performance constraints for your workload: Document your workload’s performance constraints so that you know what kinds of innovation might improve the performance of your workload.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [AWS Blog](https://aws.amazon.com/blogs/)
+  [What's New with AWS](https://aws.amazon.com/new/?ref=wellarchitected)

 **Related videos:**
+  [AWS Events YouTube Channel](https://www.youtube.com/channel/UCdoadna9HFHsxXWhafhNvKw)
+  [AWS Online Tech Talks YouTube Channel](https://www.youtube.com/user/AWSwebinars)
+  [Amazon Web Services YouTube Channel](https://www.youtube.com/channel/UCd6MoB9NC6uYN2grvUNT-Zg)

 **Related examples:**
+  [AWS Github](https://github.com/aws)
+  [AWS Skill Builder](https://explore.skillbuilder.aws/learn)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
