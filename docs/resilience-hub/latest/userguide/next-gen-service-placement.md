---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/userguide/next-gen-service-placement.html
---

# Service placement: same account vs. different account
<a name="next-gen-service-placement"></a>

**Same account as system (simple):** The system and service are in the same AWS account. A single invoker role covers everything. This approach is best for small teams and single-account workloads.

**Different account than system (enterprise):** The system is in a central account and services are in spoke accounts. This approach requires cross-account roles or AWS Organizations. It is best for large organizations with distributed ownership.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
