---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/RequesterUI/BlockingaWorker.html
---

# Block a Worker
<a name="BlockingaWorker"></a>

If Workers aren't performing to your standards, you can block them from working on your Human Intelligence Tasks (HIT).

**Note**
Blocking a Worker prevents the Worker from accepting more of your HITs. However, it does not prevent the Worker from submitting assignments that they accepted before you blocked them.

**To block a Worker**

1. On the Mechanical Turk Requester website at [https://requester.mturk.com/](https://requester.mturk.com/), choose the **Manage** tab and then choose **Workers**.

1. On the **Manage Workers** page, choose the Worker ID of the Worker that you want to block.

1. On the **Manage Individual Worker** page, choose **Block Worker**.

1. In the **Block Worker** dialog box, enter a reason for blocking the Worker and then choose **Block**.

The Worker receives a message with the reason you are blocking them.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Mechanical Turk. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSMechTurk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
