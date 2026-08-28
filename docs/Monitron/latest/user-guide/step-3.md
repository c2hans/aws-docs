---
source_url: https://docs.aws.amazon.com/Monitron/latest/user-guide/step-3.html
---

Amazon Monitron is no longer open to new customers. Existing customers can continue to use the service as normal. For capabilities similar to Amazon Monitron, see our [blog post](https://aws.amazon.com/blogs/machine-learning/maintain-access-and-consider-alternatives-for-amazon-monitron).

# Understanding warnings and alerts
<a name="step-3"></a>

**Note**
This section focuses on using the Amazon Monitron mobile app. To learn about the Amazon Monitron web app, see [Understanding sensor measurements](https://docs.aws.amazon.com/Monitron/latest/user-guide/anom-monitoring-chapter.html) in the *Amazon Monitron User Guide*.

After a sensor is paired to an asset, Amazon Monitron starts monitoring the asset's condition. When it detects an abnormal machine condition, it sends you a notification ( ![Red warning icon with exclamation mark inside a white triangle.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/notification.png)) and changes the asset state. The alert notification is generated using a combination of machine learning and ISO 20816 standards for machine vibration.

To monitor the data and respond to alerts about abnormalities, you use the Amazon Monitron mobile app.

Your administrator will send you an email with information about how to log in for the first time and connect to your project.

**Topics**
+ [Step 1: Understanding asset health](gsg-asset-list.md)
+ [Step 2: Viewing asset conditions](gsg-monitoring.md)
+ [Step 3: Viewing and acknowledging a machine abnormality](gsg-acknowledging.md)
+ [Step 4: Resolving a machine abnormality](gs-resolving-anomalies.md)
+ [Step 5: Muting and unmuting alerts](gs-muting-alerts.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Monitron. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Monitron` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
