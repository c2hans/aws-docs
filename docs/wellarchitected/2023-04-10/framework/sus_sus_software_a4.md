---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/sus_sus_software_a4.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# SUS03-BP03 Optimize areas of code that consume the most time or resources
<a name="sus_sus_software_a4"></a>

|  |
| --- |
| This best practice was updated with new guidance on July 13th, 2023. |

Optimize your code that runs within different components of your architecture to minimize resource usage while maximizing performance.

 **Common anti-patterns:**
+  You ignore optimizing your code for resource usage.
+  You usually respond to performance issues by increasing the resources.
+  Your code review and development process does not track performance changes.

 **Benefits of establishing this best practice:** Using efficient code minimizes resource usage and improves performance.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>

 It is crucial to examine every functional area, including the code for a cloud architected application, to optimize its resource usage and performance. Continually monitor your workload’s performance in build environments and production and identify opportunities to improve code snippets that have particularly high resource usage. Adopt a regular review process to identify bugs or anti-patterns within your code that use resources inefficiently. Leverage simple and efficient algorithms that produce the same results for your use case.

## Implementation steps
<a name="implementation-steps"></a>
+  While developing your workloads, adopt an automated code review process to improve quality and identify bugs and anti-patterns.
  + [ Automate code reviews with Amazon CodeGuru Reviewer ](https://aws.amazon.com/blogs/devops/automate-code-reviews-with-amazon-codeguru-reviewer/)
  + [ Detecting concurrency bugs with Amazon CodeGuru ](https://aws.amazon.com/blogs/devops/detecting-concurrency-bugs-with-amazon-codeguru/)
  + [ Raising code quality for Python applications using Amazon CodeGuru ](https://aws.amazon.com/blogs/devops/raising-code-quality-for-python-applications-using-amazon-codeguru/)
+  As you run your workloads, monitor resources to identify components with high resource requirements per unit of work as targets for code reviews.
+  For code reviews, use a code profiler to identify the areas of code that use the most time or resources as targets for optimization.
  + [ Reducing your organization's carbon footprint with Amazon CodeGuru Profiler ](https://aws.amazon.com/blogs/devops/reducing-your-organizations-carbon-footprint-with-codeguru-profiler/)
  + [ Understanding memory usage in your Java application with Amazon CodeGuru Profiler ](https://aws.amazon.com/blogs/devops/understanding-memory-usage-in-your-java-application-with-amazon-codeguru-profiler/)
  + [ Improving customer experience and reducing cost with Amazon CodeGuru Profiler ](https://aws.amazon.com/blogs/devops/improving-customer-experience-and-reducing-cost-with-codeguru-profiler/)
+  Use the most efficient operating system and programming language for the workload. For details on energy efficient programming languages (including Rust), see [Sustainability with Rust](https://aws.amazon.com/blogs/opensource/sustainability-with-rust/).
+  Replace computationally intensive algorithms with simpler and more efficient version that produce the same result.
+  Remove unnecessary code such as sorting and formatting.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [What is Amazon CodeGuru Profiler?](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/what-is-codeguru-profiler.html)
+  [FPGA instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/fpga-getting-started.html)
+  [The AWS SDKs on Tools to Build on AWS](https://aws.amazon.com/tools/)

 **Related videos:**
+ [ Improve Code Efficiency Using Amazon CodeGuru Profiler ](https://www.youtube.com/watch?v=1pU4VddsBRw)
+ [ Automate Code Reviews and Application Performance Recommendations with Amazon CodeGuru ](https://www.youtube.com/watch?v=OD8H63C0E0I)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
