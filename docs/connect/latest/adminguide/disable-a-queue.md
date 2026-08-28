---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/disable-a-queue.html
---

# Disable a queue temporarily using Connect Customer
<a name="disable-a-queue"></a>

You can quickly control the flow of contacts to queues by temporarily disabling a queue. When a queue is disabled, it's put in an offline mode. No new contacts are routed to the queue, but any existing contacts already in the queue are routed to agents.

Only users who have a security profile with **Routing** - **Queues** - ** Enable/Disable** permission can disable a queue.

![Security profile permissions table showing Queues row with Create checkbox selected.](http://docs.aws.amazon.com/connect/latest/adminguide/images/disable-queue.png)

**To temporarily disable an active queue**

1. Log in to the Connect Customer admin website at https://{{instance name}}.my.connect.aws/. Use an **Admin** account, or an account that has **Routing** - **Queues** - ** Enable/Disable** permission in its security profile.

1. On the Connect Customer admin website, on the navigation menu, choose **Routing**, **Queues**.

1. For the queue you want to disable, toggle the **Status** to **Disabled**, as shown in the following image.
![The Queues page, the Status toggle.](http://docs.aws.amazon.com/connect/latest/adminguide/images/disable-queue-power-button.png)

1. Choose **Disable** to confirm you want to disable the queue, as shown in the following image. You can immediately re-enable the queue if needed by toggling the button back to **Enabled**.
![The Disable queue confirmation box.](http://docs.aws.amazon.com/connect/latest/adminguide/images/disable-queue-confirm.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
