---
source_url: https://docs.aws.amazon.com/solutions/latest/modern-data-architecture-accelerator/configurating-sharing-composition.html
---

# Configuration sharing and composition
<a name="configurating-sharing-composition"></a>

MDAA supports:
+ Sharing configurations across multiple domains and environments
+ Composing configurations from multiple files
+ Overriding configurations at different levels (global, domain, environment, module)

## Configuration Merging Rules
<a name="configuration-merging-rules"></a>
+ Lists on same config key will be merged across config files
+ Objects on same config key will be concatenated
+ Scalar values will be overridden, with later configs taking precedence

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Modern Data Architecture Accelerator. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
