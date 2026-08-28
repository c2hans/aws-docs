---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/ops_ready_to_support_personnel_capability.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# OPS07-BP01 Ensure personnel capability
<a name="ops_ready_to_support_personnel_capability"></a>

 Have a mechanism to validate that you have the appropriate number of trained personnel to provide support for operational needs. Train personnel and adjust personnel capacity as necessary to maintain effective support.

 You will need to have enough team members to cover all activities (including on-call). Ensure that your teams have the necessary skills to be successful with training on your workload, your operations tools, and AWS.

 AWS provides resources, including the [AWS Getting Started Resource Center](https://aws.amazon.com/getting-started/), [AWS Blogs](https://aws.amazon.com/blogs/), [AWS Online Tech Talks](https://aws.amazon.com/getting-started/), [AWS Events and Webinars](https://aws.amazon.com/events/), and the [AWS Well-Architected Labs](https://wellarchitectedlabs.com/), that provide guidance, examples, and detailed walkthroughs to educate your teams. Additionally, [AWS Training and Certification](https://aws.amazon.com/training/) provides some free training through self-paced digital courses on AWS fundamentals. You can also register for instructor-led training to further support the development of your teams’ AWS skills.

 **Common anti-patterns:**
+  Deploying a workload without team members skilled to support the platform and services in use.
+  Deploying a workload without team members available during intended hours of support.
+  Deploying a workload without sufficient team members to support it if there are team members on leave or out sick.
+  Deploying additional workloads without reviewing the additional impact on team members support it and other workloads.

 **Benefits of establishing this best practice:** Having skilled team members enables effective support of your workload.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>
+  Personnel capability: Validate that there are sufficient trained personnel to effectively support the workload.
  +  Team size: Ensure that you have enough team members to cover operational activities, including on-call duties.
  +  Team skill: Ensure that your team members have sufficient training on AWS, your workload, and your operations tools to perform their duties.
    +  [AWS Events and Webinars](https://aws.amazon.com/about-aws/events/)
    +  [Welcome to AWS Training and Certification](https://aws.amazon.com/training/)
  +  Review capabilities: Review team size and skill as operating conditions and workloads change, to ensure there is sufficient capability to maintain operational excellence. Make adjustments to ensure that team size and skill match the operational requirements for the workloads that the team supports.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [AWS Blogs](https://aws.amazon.com/blogs/)
+  [AWS Events and Webinars](https://aws.amazon.com/about-aws/events/)
+  [AWS Getting Started Resource Center](https://aws.amazon.com/getting-started/)
+  [AWS Online Tech Talks](https://aws.amazon.com/getting-started/)
+  [Welcome to AWS Training and Certification](https://aws.amazon.com/training/)

 **Related examples:**
+  [Well-Architected Labs](https://wellarchitectedlabs.com/)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
