---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/emla-setup-cluster.html
---

# Creating the cluster
<a name="emla-setup-cluster"></a>

You must create the networks, clusters, nodes, and SDI sources that you identified when you [designed](#emla-setup-cluster) the AWS Elemental MediaLive Anywhere cluster.

Create the networks first, then the clusters, then the nodes. There are no other rules about order of work. For example, you could create all the networks, then create all the clusters, then create all the nodes. Or you could create the networks for one cluster, then create the cluster, then create the nodes for that cluster.

**Topics**
+ [Create the networks](emla-setup-cl-networks.md)
+ [Create the clusters](emla-setup-cl-create.md)
+ [Create the nodes](emla-setup-cl-nodes-create.md)
+ [Create SDI sources](emla-setup-cl-sdi.md)
+ [Result of this setup](emla-setup-cl-result.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
