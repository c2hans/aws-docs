---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/userguide/next-gen-modeling-how-it-works.html
---

# How application modeling works
<a name="next-gen-modeling-how-it-works"></a>

To model your application in the next generation of Resilience Hub, follow these steps:

1. **Create a resilience policy** – Define your availability, disaster recovery, and data recovery targets. See [Resilience policies](next-gen-resilience-policies.md).

1. **Create a system** – Define the top-level business application. See [Create a system](next-gen-create-system.md).

1. **Create user journeys** – Define the critical business paths within your system. See [Creating and managing user journeys](next-gen-managing-user-journeys.md).

1. **Create services** – Define the building blocks and specify input sources for resource discovery. See [Creating and managing services](next-gen-managing-services.md).

1. **Run an assessment** – Start a failure mode assessment to identify resilience gaps. See [Failure mode assessments](next-gen-failure-mode-assessments.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
