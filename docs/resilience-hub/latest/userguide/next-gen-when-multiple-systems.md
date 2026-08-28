---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/userguide/next-gen-when-multiple-systems.html
---

# When to create multiple systems
<a name="next-gen-when-multiple-systems"></a>

Create **separate systems** when:
+ Applications or services are independently operated by different teams.
+ You want separate resilience posture tracking for each application.

Use a **single system** when:
+ Multiple services work together to deliver business value.
+ You want to assess resilience across related services as a group.
+ Services share infrastructure (for example, a common Amazon EKS platform).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
