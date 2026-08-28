---
source_url: https://docs.aws.amazon.com/recovery-cluster/latest/api/examples-cli-control.html
---

# CLI Examples for the Recovery Control Configuration API
<a name="examples-cli-control"></a>

This section includes CLI examples for working with the APIs for Recovery Control Configuration with Amazon Application Recovery Controller (ARC).

ARC is a global service that supports endpoints in multiple AWS Regions but you must specify the US West (Oregon) Region (that is, specify the parameter `--region us-west-2`) in most ARC CLI commands. For example, to create resources such as routing controls or clusters.

When you create a cluster, ARC provides you with a set of Regional endpoints. To get or update routing control states, you must specify the Regional endpoint (the AWS Region and the endpoint URL) in your CLI command.

**Topics**
+ [Create a cluster](create-cluster.md)
+ [List clusters](list-clusters.md)
+ [Describe a cluster](describe-cluster.md)
+ [Update a cluster](update-cluster.md)
+ [Delete a cluster](delete-cluster.md)
+ [Create a control panel](create-control-panel.md)
+ [List control panels](list-control-panels.md)
+ [Describe a control panel](describe-control-panel.md)
+ [Delete a control panel](delete-control-panel.md)
+ [Create a routing control](create-routing-control.md)
+ [List routing controls](list-routing-controls.md)
+ [Describe a routing control](describe-routing-control.md)
+ [Delete a routing control](delete-routing-control.md)
+ [Create safety rules](create-safety-rule.md)
+ [List safety rules](list-safety-rules.md)
+ [Describe a safety rule](describe-safety-rule.md)
+ [Delete a safety rule](delete-safety-rule.md)
+ [Get routing control state](get-routing-control-state.md)
+ [Update state for one routing control](update-routing-control-state.md)
+ [Update state for two routing controls at the same time, in a batch](update-routing-control-state-batch.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Application Recovery Controller. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query recovery-cluster` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
