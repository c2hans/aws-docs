---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/userguide/next-gen-resilience-testing-iam-multi-account.html
---

# Multi-account execution roles
<a name="next-gen-resilience-testing-iam-multi-account"></a>

For a multi-account test, AWS FIS uses a role chain. AWS FIS assumes the *orchestrator role* in the account that runs the experiment. The orchestrator role then assumes a *target role* in each account that contains targeted resources. Create the orchestrator role once, and create a target role in every target account.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
