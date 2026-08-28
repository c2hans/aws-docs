---
source_url: https://docs.aws.amazon.com/Monitron/latest/user-guide/anom-acknowledge-anom.html
---

Amazon Monitron is no longer open to new customers. Existing customers can continue to use the service as normal. For capabilities similar to Amazon Monitron, see our [blog post](https://aws.amazon.com/blogs/machine-learning/maintain-access-and-consider-alternatives-for-amazon-monitron).

# Acknowledging a machine abnormality
<a name="anom-acknowledge-anom"></a>

After receiving a notification, the admin user or technician must acknowledge it. Acknowledging the notification lets other users know that the issue has been noted and that action will be taken.

**Topics**
+ [To view and acknowledge a machine abnormality](#anom-acknowledge)

## To view and acknowledge a machine abnormality
<a name="anom-acknowledge"></a>

1. From the **Assets** list, choose the asset that is reporting an abnormality.

1. To view the issue, choose the position with the abnormality.

   Sensor measurements that show the anomaly are displayed.
![Vibration monitoring dashboard showing total and single axis vibration graphs with ISO alarm threshold exceeded.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/web-understand-sensor-measurement.png)

1. Choose **Acknowledge**.

   The status of the asset changes to **Maintenance**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Monitron. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Monitron` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
