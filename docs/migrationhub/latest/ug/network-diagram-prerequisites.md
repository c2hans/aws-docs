---
source_url: https://docs.aws.amazon.com/migrationhub/latest/ug/network-diagram-prerequisites.html
---

AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform).

# Prerequisites for using the network diagram in AWS Migration Hub
<a name="network-diagram-prerequisites"></a>

The following are the prerequisites for using the network diagram in AWS Migration Hub:
+  AWS Application Discovery Service Discovery Agent must be running on all of the on-premises servers that you want mapped in the diagram. For more information, see [Setting up Agent Based Discovery](https://docs.aws.amazon.com/application-discovery/latest/userguide/setting-up-agents.html) in the *Application Discovery Service User Guide*.
+ AWS recommends that server and network connection data be collected for two to six weeks to capture important connection patterns, such as month-end or year-end business cycles.
+ To grant access to the network diagram when creating an identity-based policy that allows or denies access to AWS Application Discovery Service or Migration Hub, you might need to add the `discovery:GetNetworkConnectionGraph` action to the policy. For more information, see [Granting permissions to use the network diagram](https://docs.aws.amazon.com/application-discovery/latest/userguide/security_iam_id-based-policy-examples.html#security_iam_id-based-policy-examples-network-connection-graph) in the *Application Discovery Service User Guide*.

The network diagram has the following limits:
+ Currently, data ingestion stops after 180 days.
+ The network diagram can visualize up to 1,500 server nodes.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Migration Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query migrationhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
