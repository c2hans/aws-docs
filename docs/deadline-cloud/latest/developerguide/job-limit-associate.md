---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/job-limit-associate.html
---

# Associate a limit and a queue
<a name="job-limit-associate"></a>

After you create a limit, you can associate one or more queues with the limit. Only queues that are associated with a limit use the values specified in the limit.

You create an association with a queue using the Deadline Cloud console or the [CreateQueueLimitAssociation operation in the Deadline Cloud API](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_CreateQueueLimitAssociation.html).

**To associate a queue with a limit**

1. From the Deadline Cloud console ([Deadline Cloud console](https://console.aws.amazon.com/deadlinecloud/home)) dashboard, select the farm where you want to associate a limit with a queue.

1. Choose the **Limits ** tab, choose the limit to associate a queue with, and then choose **Edit limit**.

1. In the **Associate queues** section, choose the queues to associate with the limit.

1. Choose **Save changes**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
