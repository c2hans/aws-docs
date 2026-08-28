---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/ug/container-design-mpts-workflow.html
---

# Designing an MPTS workflow
<a name="container-design-mpts-workflow"></a>

This section describes how to design a standard MPTS, and how to augment that standard MPTS by including passthrough elements.

You can configure the MPTS to include multiple programs.

You can configure the MPTS to generate the following SI/PSI tables:
+ PAT. Required if you want to create a compliant MPTS.
+ PMT for each program. Required if you want to create a compliant MPTS.
+ NIT. Always optional.
+ SDT. Always optional.
+ TDT. Always optional.

You can also configure the MPTS to pass through any SI/PSI tables that you pass in, both the tables the Elemental Statmux can generate, and those that it never generates.

**Topics**
+ [Creating a standard MPTS](mpts-design-step-channels.md)
+ [Including passthrough programs](mpts-passthrough-program.md)
+ [Passing through custom streams](mpts-passthrough-high-pids.md)
+ [Passing through SI/PSI tables](mpts-passthrough-PSI-pids.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
