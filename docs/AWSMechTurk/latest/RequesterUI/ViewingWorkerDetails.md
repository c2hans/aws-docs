---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/RequesterUI/ViewingWorkerDetails.html
---

# View Worker statistics
<a name="ViewingWorkerDetails"></a>

Mechanical Turk enables you to view a Worker's statistics, which characterize what the Worker is good at.

**To view a Worker's statistics**

1. On the Mechanical Turk Requester website at [https://requester.mturk.com/](https://requester.mturk.com/), choose the **Manage** tab and then choose **Workers**.

1. On the **Manage Workers** page, the **Block Status** column can have the following values:
   + **Never Blocked** – Worker has never been blocked you.
   + **Blocked** – Worker is not allowed to work for you.
   + **Unblocked** – Worker was blocked by you at one time, but is no longer blocked.

1. To take a specific action on an individual Worker, choose a Worker ID.

1. On the **Manage Individual Worker** page, you can view the Worker's approval rating, in addition to the number of assignments you approved and rejected in the last 7 days, 30 days, or for all time (**Lifetime**).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Mechanical Turk. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSMechTurk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
