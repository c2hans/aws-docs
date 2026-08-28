---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/sample-customer-queue-priority.html
---

# Sample customer queue priority flow in Connect Customer
<a name="sample-customer-queue-priority"></a>

**Note**
This sample flow is available in previous Connect Customer instances. In new instances, you can see this functionality in [Sample queue configurations flow in Connect Customer](sample-queue-configurations.md).

Type: Flow (inbound)

By default the priority for new contacts is 5. Lower values raise the priority of the contact. For example, a contact assigned a priority of 1 is routed first.

This sample shows how you can use the **Change routing priority/age block** to raise or lower the priority of a contact in a queue. Using this block, there are two ways you can raise or lower a customer's priority:
+ Assign them a new priority value, such as 1, to raise their priority.
+ Or, increase the routing age of the contact. Customers who are queued longer are routed first, when all contacts have the same queue priority value (such as 5).

## Option 1: Raise the priority
<a name="option1-sample-customer-queue-priority"></a>
+ The **Get Customer Input** block prompts the customer to press 1 to move to the front of the queue. This block gets the customer's input; it doesn't actually change the customer's priority.
+ If the customer presses 1, they go down the "Pressed 1" branch, which takes them to the **Change routing priority/age block**. This block changes their priority in the queue to 1, which is the highest priority.

## Option 2: Change the routing age
<a name="option2-sample-customer-queue-priority"></a>
+ The **Get Customer Input** block prompts the customer to press 2 to move behind existing contacts already in queue. This block gets the customer's input; it doesn't actually change the customer's priority.
+ If the customer presses 2, they go down the "Pressed 2" branch, which takes them to a different **Change routing priority/age** block. This block increases their routing age by 10 minutes. This has the effect of moving them ahead of others in the queue who have been waiting longer.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
