---
source_url: https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-prefix-lists.html
---

# AWS Cloud WAN prefix list associations
<a name="cloudwan-prefix-lists"></a>

You can use customer managed prefix lists in your Cloud WAN routing policy to simplify rules management. You need to associate your prefix list with the core network with the create-core-network-prefix-list-association API. The prefix list must be defined in the Cloud WAN home region (us-west-2). Although defined in Cloud WAN home region, the prefix-list based policy will apply globally to all the relevant core network edges (regions) in your core network.

Before you can create a prefix list association, you must first have created a prefix list. For more information about creating prefix lists, see [Consolidate and manage network CIDR blocks with managed prefix lists](https://docs.aws.amazon.com/vpc/latest/userguide/managed-prefix-lists.html) in the *Amazon Virtual Private Cloud User Guide*.

**Note**
Creating or deleting prefix list associations will move the state of your core network to updating. The status of the association is based on the core network state, once it is finished updating the association will either be fully available or deleted.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Network Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query network-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
