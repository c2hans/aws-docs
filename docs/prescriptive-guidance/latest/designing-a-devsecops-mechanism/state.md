---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/designing-a-devsecops-mechanism/state.html
---

# State management
<a name="state"></a>

Infrastructure state management design decisions are sometimes overlooked during initial mechanism design and scoping. However, failing to account for needed flexibility in the design, such as development team tooling and pattern distinctions, can cause a significant amount of post-mechanism rework. When evaluating your state management approach, consider the following questions:
+ Who will manage the infrastructure and application state?
+ What happens when something breaks with the state?
+ Who will remediate a state issue?
+ If remediation is handled by a central team, will that approach cause developmental delays and downtime? How will you minimize this disruption?

As an example, imagine an organization that delivers a central state management solution. This greatly improves the speed to market for solutions because developers don't need to reinvent the wheel for each project. However, anything can break at times. State is no exception. When state breaks, consider the following points:
+ A clear point of contact (POC) should be in place.
+ The POC should have immediate availability to remediate the issue. For example, don't burden the POC with a full JIRA list of work with state management as an afterthought.
+ A mechanism with access is already in place to work and resolve the issue.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
