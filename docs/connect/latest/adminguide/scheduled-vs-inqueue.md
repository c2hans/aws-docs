---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/scheduled-vs-inqueue.html
---

# How Initial delay affects Scheduled and In queue metrics in Connect Customer
<a name="scheduled-vs-inqueue"></a>

In the [Transfer to queue](transfer-to-queue.md) block, the **Initial delay** property affects when a callback is put in queue. For example, assume **Initial delay** is set to 30 seconds. Here's what appears in your real-time metrics report:

1. After 20 seconds, the callback has already been created, but it is not yet in queue because of the **Initial delay** setting. In the following image of the **Real-time metrics** page, **In queue** = 0 and **Scheduled** = 1.
![A contact that is scheduled but is not in queue.](http://docs.aws.amazon.com/connect/latest/adminguide/images/rtm-callback-scheduled.png)

1. After 35 seconds, the callback contact has been placed in queue. In the following image, the callback is now **In queue**. It is no longer scheduled.
![The In queue column has a 1, the Scheduled column has a 0.](http://docs.aws.amazon.com/connect/latest/adminguide/images/rtm-callback-in-queue2.png)

1. Assume that after 40 seconds, an agent accepts the callback. The **In queue** column = 0, the **Scheduled** column = 0.
![The In queue column has a 1, the Scheduled column has a 0.](http://docs.aws.amazon.com/connect/latest/adminguide/images/rtm-callback-accepted-by-agent.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
