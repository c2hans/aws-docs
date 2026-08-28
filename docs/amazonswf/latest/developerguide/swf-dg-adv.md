---
source_url: https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dg-adv.html
---

# Advanced workflow concepts in Amazon SWF
<a name="swf-dg-adv"></a>

The e-commerce example in the [](swf-dg-basic.md) section represents a simplified workflow scenario. In reality, you are likely to want your workflow to do concurrent tasks (send an order confirmation email while authorizing a credit card), record major events (all items are packed), update the order with changes (add or remove an item), and make other more advanced decisions as part of your workflow execution. This section describes advanced workflow concepts that you can use to construct your workflows.

**Topics**
+ [Versioning](swf-dev-adv-versioning.md)
+ [Signals](swf-dev-adv-signals.md)
+ [Child workflows](swf-dev-adv-child-workflows.md)
+ [Markers](swf-dev-adv-markers.md)
+ [Tags](swf-dev-adv-tags.md)
+ [Exclusive choice](swf-dg-exclusive-choice.md)
+ [Timers](swf-dg-timers.md)
+ [Cancelling activity tasks](swf-dg-task-cancellation.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Workflow Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonswf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
