---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/sus_sus_dev_a2.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# SUS06-BP01 Adopt methods that can rapidly introduce sustainability improvements
<a name="sus_sus_dev_a2"></a>

Adopt methods and processes to validate potential improvements, minimize testing costs, and deliver small improvements.

 **Common anti-patterns:**
+  Reviewing your application for sustainability is a task done only once at the beginning of a project.
+  Your workload has become stale, as the release process is too cumbersome to introduce minor changes for resource efficiency.
+  You do not have mechanisms to improve your workload for sustainability.

 **Benefits of establishing this best practice:** By establishing a process to introduce and track sustainability improvements, you will be able to continually adopt new features and capabilities, remove issues, and improve workload efficiency.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>

 Test and validate potential sustainability improvements before deploying them to production. Account for the cost of testing when calculating potential future benefit of an improvement. Develop low cost testing methods to deliver small improvements.

 **Implementation steps**
+  Add requirements for sustainability improvement to your development backlog.
+  Use an iterative [improvement process](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/improvement-process.html) to identify, evaluate, prioritize, test, and deploy these improvements.
+  Continually improve and streamline your development processes. As an example, [Automate your software delivery process using continuous integration and delivery (CI/CD) pipelines](https://aws.amazon.com/getting-started/hands-on/set-up-ci-cd-pipeline/) to test and deploy potential improvements to reduce the level of effort and limit errors caused by manual processes.
+  Develop and test potential improvements using the minimum viable representative components to reduce the cost of testing.
+  Continually assess the impact of improvements and make adjustment as needed.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [AWS enables sustainability solutions](https://aws.amazon.com/sustainability/)
+ [ Scalable agile development practices based on AWS CodeCommit](https://aws.amazon.com/blogs/devops/scalable-agile-development-practices-based-on-aws-codecommit/)

 **Related videos:**
+ [ Delivering sustainable, high-performing architectures ](https://www.youtube.com/watch?v=FBc9hXQfat0)

 **Related examples:**
+  [Well-Architected Lab - Turning cost & usage reports into efficiency reports](https://www.wellarchitectedlabs.com/sustainability/300_labs/300_cur_reports_as_efficiency_reports/)
