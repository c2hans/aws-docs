---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/userguide/next-gen-user-journey-guidelines.html
---

# Guidelines for defining user journeys
<a name="next-gen-user-journey-guidelines"></a>
+ Name user journeys after business capabilities, not technical components.
+ A user journey should represent something an end user does (for example, "Check balance," not "Database reads").
+ Start with your most critical user journeys and add more over time.
+ A service can belong to multiple user journeys – shared platform services often do.

The following table shows examples of systems and their corresponding user journeys:

| System | User journeys |
| --- | --- |
| E-commerce platform | Path to purchase, Product discovery, Order fulfillment, Returns |
| Trading system | Execute trade, Check portfolio, Transfer funds |
| Failover orchestration | Manage plans, Execute failover, Run reports |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
