---
source_url: https://docs.aws.amazon.com/Monitron/latest/user-guide/how-monitron-works.html
---

Amazon Monitron is no longer open to new customers. Existing customers can continue to use the service as normal. For capabilities similar to Amazon Monitron, see our [blog post](https://aws.amazon.com/blogs/machine-learning/maintain-access-and-consider-alternatives-for-amazon-monitron).

# How Amazon Monitron works
<a name="how-monitron-works"></a>

Amazon Monitron is a machine learning end-to-end condition monitoring solution system that detects developing faults within machinery, enabling you to implement a predictive maintenance program and reduce lost productivity from unplanned machine downtime.

Amazon Monitron includes purpose-built sensors to capture vibration and temperature data, gateways to automatically transfer data to the AWS Cloud, and an application for system set up, analytics, and notiﬁcation when tracking equipment condition.

Amazon Monitron sensors use an ISO threshold model and a machine learning (ML) model to monitor vibration. The ISO model is used to analyze the magnitude of vibration (machine condition). The ML model is used to detect change in vibration (change in machine condition).

Reliability managers can deploy Amazon Monitron to track machine health of industrial equipment, such as bearings, motors, gearboxes, and pumps, without any development work or specialized training.

**Tip**
 Check your Amazon Monitron app regularly for updates and access to the latest features.

**Topics**
+ [The Amazon Monitron workflow](deployed-workflow.md)
+ [Amazon Monitron concepts](monitron-terminology.md)
+ [Amazon Monitron components](monitron-components.md)
+ [Amazon Monitron alerts](how-it-works-alerts.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Monitron. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Monitron` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
