---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/userguide/next-gen-troubleshoot-resources-vs-topology.html
---

# Difference between discovered resources and topology resources
<a name="next-gen-troubleshoot-resources-vs-topology"></a>

You might see more resources in the `ListResources` API response than appear in your topology diagram. Not all discovered resources appear in the topology view. The topology is a connectivity graph that shows how resources interact. Next generation Resilience Hub removes resources from the topology view that have no connections to other resources.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
