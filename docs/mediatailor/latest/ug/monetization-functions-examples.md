---
source_url: https://docs.aws.amazon.com/mediatailor/latest/ug/monetization-functions-examples.html
---

# Function examples
<a name="monetization-functions-examples"></a>

Before working through these examples, you should be familiar with:
+ [Lifecycle hooks](monetization-functions-hooks.md) — Input fields and output namespaces available at each lifecycle hook.
+ [Function types and composition](monetization-functions-types.md) — How each function type works and its configuration fields.
+ [Creating and managing](monetization-functions-managing.md) — How to create functions and attach them to playback configurations.

This page provides complete, working function configurations for common use cases. Each example includes the scenario, the full configuration, the function mapping, and an explanation of what happens when the function runs.

| Example | Scenario description |
| --- | --- |
| [Example 1: Data enrichment](monetization-functions-examples-enrichment.md) | Fetch a LiveRamp identity envelope at session start and store it in player parameters. |
| [Example 2: A/B traffic split](monetization-functions-examples-ab.md) | Split ad request traffic evenly between two ad decision server URLs for A/B testing. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaTailor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediatailor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
