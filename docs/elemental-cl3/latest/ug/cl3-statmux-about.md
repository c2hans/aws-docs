---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/ug/cl3-statmux-about.html
---

# Working with AWS Elemental Statmux
<a name="cl3-statmux-about"></a>

Include AWS Elemental Statmux nodes in your AWS Elemental Conductor Live cluster if you want to create MPTS outputs. A multi-program transport stream (MPTS) is a UDP transport stream (TS) that carries multiple programs. Conductor Live lets you create an MPTS that contains all variable bitrate programs, a mix of variable and constant bitrate programs, or all constant bitrate programs.

You use AWS Elemental Statmux to ingest SPTS outputs from AWS Elemental Live and produce MPTSes.

For Elemental Statmux, Conductor Live is a requirement. You can't run MPTSes without Conductor Live.

**Topics**
+ [Components of AWS Elemental Statmux in a cluster](smux-cluster-usage-components.md)
+ [Features of AWS Elemental Statmux](cl3-statmux-features.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
