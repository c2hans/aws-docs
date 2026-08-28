---
source_url: https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dg-create-workflow.html
---

# Creating a workflow in Amazon SWF
<a name="swf-dg-create-workflow"></a>

Creating a basic sequential workflow involves the following stages.
+ Modeling a workflow, registering its type, and registering its activity types
+ Developing and launching activity workers that perform activity tasks
+ Developing and launching deciders that use the workflow history to determine what to do next
+ Developing and launching workflow starters, that is, applications that start workflow executions

## Modeling Your Workflow and Its Activities
<a name="modeling-workflow-and-activities"></a>

To use Amazon SWF, model the logical steps in your application as activities. An activity represents a single logical step or task in your workflow. For example, authorizing a credit card is an activity that involves providing a credit card number and other information, and receiving an approval code or a message that the card was declined.

In addition to defining activities, you also need to define the coordination logic that handles decision points. For example, the coordination logic might schedule a different follow-up activity depending on whether the credit card was approved or declined.

The following figure shows an example of a sequential customer order workflow with four activities (Verify Order, Charge Credit Card, Ship Order, and Record Completion).

![Customer Order Workflow](http://docs.aws.amazon.com/amazonswf/latest/developerguide/images/swf-overview-workflow.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Workflow Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonswf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
