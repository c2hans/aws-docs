---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/view-contacts-in-queue.html
---

# View the number of contacts waiting in an Connect Customer contact center queue
<a name="view-contacts-in-queue"></a>

**To view the number of contacts waiting in a queue for an agent**

1. Log in to the Connect Customer admin website at https://{{instance name}}.my.connect.aws/. Use an **Admin** account, or an account assigned to a security profile that has **Real-time metrics** - **Access metrics** permissions.

1. In Connect Customer, on the left navigation menu, choose **Analytics and Optimization**, **Real-time metrics**, and then choose **Queues**.

1. In the **Queues** table, check the **In queue** column.

   The **In queue** value shows the total number of customers who are waiting for an agent, including those who have requested a callback.
![The In queue column in the Queues table.](http://docs.aws.amazon.com/connect/latest/adminguide/images/rtm-waiting-in-queue.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
