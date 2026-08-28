---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/ug/smx-node-design.html
---

# Number of primary Elemental Statmux nodes
<a name="smx-node-design"></a>

Determine the number of *primary nodes *you need:
+ Identify the density of all the SPTS channels that you want to mux into MPTSes. Then consult with your AWS Elemental sales person for help to identify your node requirements.
+ Keep in mind that you can run more than one MPTS on a node.

**Note**
You might have acquired a high-compute-power Elemental Statmux node with the intention of implementing Simulcrypt encryption, when it becomes available in Elemental Statmux.
Simulcrypt has high compute-power requirements. You might want to plan fewer MPTSes on the node. In this way, you will be able to implement Simulcrypt later without moving any MPTSes to another node.

After you have determined the number of primary nodes, you should identify your redundant node requirements. See [Worker node redundancy](redundancy-worker.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
