---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/ug/smux-cluster-usage-components.html
---

# Components of AWS Elemental Statmux in a cluster
<a name="smux-cluster-usage-components"></a>

To create an MPTS using Elemental Statmux, you need:
+ Elemental Live channels that produce an SPTS output.
+ An MPTS that you create using Elemental Statmux. Elemental Statmux*muxes* two or more SPTS outputs into one MPTS output.

![Diagram showing three channels converging into a single MPTS output.](http://docs.aws.amazon.com/elemental-cl3/latest/ug/images/diagram-cmpts.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
