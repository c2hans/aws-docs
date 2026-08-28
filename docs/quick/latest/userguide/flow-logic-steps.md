---
source_url: https://docs.aws.amazon.com/quick/latest/userguide/flow-logic-steps.html
---

# Flow logic steps
<a name="flow-logic-steps"></a>

Flow logic steps control how your flow runs.

## Reasoning Group
<a name="reasoning-group-step"></a>

Reasoning groups give you control over how parts of your flow run using natural language instructions. A reasoning group contains its own set of steps — like an isolated workflow within your larger workflow — that runs based on conditions you define. You can add most step types to a reasoning group, except reasoning groups and research steps. Templates are available to help you get started.

### Loops
<a name="reasoning-group-loops"></a>

You can repeat the steps in a group for each value in a list from a previous step's output. Reference the previous step in your instructions, and the Flows runtime handles the iteration for you. For example, if a previous step returns a list of customer emails, a reasoning group can process each email in turn.

### Conditions
<a name="reasoning-group-conditions"></a>

You can run the steps in a group based on natural language conditions that evaluate a previous step's output. For example, "Run if @Customer Priority is HIGH PRIORITY" routes only urgent items through the group's steps.

### Validation
<a name="reasoning-group-validation"></a>

You can check inputs or outputs before proceeding. For example, a reasoning group can verify that a required field is present before passing data to an action step.

For configuration instructions, see [Editing flows](editing-flows.md). For reasoning group limits, see [Quick Flows limits](quick-flows-limits.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quick` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
