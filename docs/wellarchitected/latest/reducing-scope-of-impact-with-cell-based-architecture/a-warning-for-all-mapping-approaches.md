---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/reducing-scope-of-impact-with-cell-based-architecture/a-warning-for-all-mapping-approaches.html
---

# A warning for all mapping approaches
<a name="a-warning-for-all-mapping-approaches"></a>

 Regardless of partition mapping approach, it's important to also use an override table to force specific keys to specific cells (except for [full mapping](full-mapping.md), which natively provides this support). This can be useful for testing, quarantining, and special-case routing for particularly heavy partition keys.

 Another consideration is that the task of mapping a new customer to a cell and registering it in the cell router is the control plane's task. After this provisioning of the client and the cell router loads this configuration, the strategy defined in this section starts to work

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
