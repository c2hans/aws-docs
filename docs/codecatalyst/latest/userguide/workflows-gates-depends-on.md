---
source_url: https://docs.aws.amazon.com/codecatalyst/latest/userguide/workflows-gates-depends-on.html
---

Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md).

# Sequencing gates and actions
<a name="workflows-gates-depends-on"></a>

In Amazon CodeCatalyst, you can set up a gate to run before or after a workflow action, action group, or gate. For example, you might set up an `Approval` gate to run before a `Deploy` action. In this case, the `Deploy` action is said to *depend on* the `Approval` gate.

To set up dependencies between gates and actions, configure the gate or action's **Depends on** property. For instructions, see [Setting up dependencies between actions](workflows-depends-on-set-up.md). The referenced instructions refer to workflow *actions* but apply equally to gates.

For an example of how to set up the **Depends on** property with a gate, see [Example: An 'Approval' gate](workflows-approval-example.md).

For more information about gates, see [Gating a workflow run](workflows-gates.md).

For more information about workflow actions, see [Configuring workflow actions](workflows-actions.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CodeCatalyst. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codecatalyst` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
