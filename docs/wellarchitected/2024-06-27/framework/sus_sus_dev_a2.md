---
source_url: https://docs.aws.amazon.com/wellarchitected/2024-06-27/framework/sus_sus_dev_a2.html
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
+  **Understand and communicate your organizational sustainability goals:** Understand your organizational sustainability goals, such carbon reduction or water stewardship. Translate these goals into sustainability requirements for your cloud workloads. Communicate these requirements to key stakeholders.
+  **Add sustainability requirements to your backlog:** Add requirements for sustainability improvement to your development backlog.
+  **Iterate and improve:** Use an [iterative improvement process](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/improvement-process.html) to identify, evaluate, prioritize, test, and deploy these improvements.
+  **Test using minimum viable product (MVP):** Develop and test potential improvements using the minimum viable representative components to reduce the cost and environmental impact of testing.
+  **Streamline the process:** Continually improve and streamline your development processes. As an example, Automate your software delivery process using continuous integration and delivery (CI/CD) pipelines to test and deploy potential improvements to reduce the level of effort and limit errors caused by manual processes.
+  **Training and awareness:** Run training programs for your team members to educate them about sustainability and how their activities impact your organizational sustainability goals.
+  **Assess and adjust:** Continually assess the impact of improvements and make adjustments as needed.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [AWS enables sustainability solutions](https://aws.amazon.com/sustainability/)
+ [ Scalable agile development practices based on AWS CodeCommit](https://aws.amazon.com/blogs/devops/scalable-agile-development-practices-based-on-aws-codecommit/)

 **Related videos:**
+  [AWS re:Invent 2023 - Sustainable architecture: Past, present, and future](https://www.youtube.com/watch?v=2xpUQ-Q4QcM)
+  [AWS re:Invent 2022 - Delivering sustainable, high-performing architectures](https://www.youtube.com/watch?v=FBc9hXQfat0)
+  [AWS re:Invent 2022 - Architecting sustainably and reducing your AWS carbon footprint](https://www.youtube.com/watch?v=jsbamOLpCr8)
+  [AWS re:Invent 2022 - Sustainability in AWS global infrastructure](https://www.youtube.com/watch?v=NgMa8R9-Ywk)
+  [AWS re:Invent 2023 - What’s new with AWS observability and operations](https://www.youtube.com/watch?v=E8qQBMDJjso)

 **Related examples:**
+  [Well-Architected Lab - Turning cost & usage reports into efficiency reports](https://www.wellarchitectedlabs.com/sustainability/300_labs/300_cur_reports_as_efficiency_reports/)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
