---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/cyber-threat-intelligence-sharing/architecture-threat-intelligence-platform.html
---

# Deploying a threat intelligence platform
<a name="architecture-threat-intelligence-platform"></a>

A threat intelligence platform ingests, aggregates, and organizes threat intelligence data from multiple sources and in different formats. It allows analysts to view, prioritize, and act on cyber threat intelligence (CTI) that has been received from their trust community.

[OpenCTI](https://github.com/OpenCTI-Platform/opencti) and [MISP](https://www.misp-project.org) are common open source threat intelligence platforms. There are also solutions available from AWS Partners on the [AWS Marketplace](https://aws.amazon.com/marketplace/). You should consider the skill level of your security team when choosing a threat intelligence platform. MISP can be powerful yet complex, and OpenCTI has a more intuitive user interface.

When choosing a threat intelligence platform, consider the following:
+ **Features** – Does the platform offers features such as real-time monitoring, threat detection, and analysis?
+ **Data sources** – Does the platform use a variety of sources, including threat feeds, dark web intelligence, social media, and open-source intelligence?
+ **Data quality** – Does the platform have processes to make sure that the information is accurate and reliable?
+ **Scalability** – Can the platform adapt to your organization's changing needs, such as growth and evolving threats?
+ **Integration** – Can the platform can integrate with your existing security tools and infrastructure?
+ **User experience** – Is the platform easy to navigate and use?
+ **Customization** – Can the platform be customized to meet your organization's specific needs?
+ **Cost** – Is the platform cost-effective, including licensing costs and maintenance requirements?

You can deploy your threat intelligence platform within your virtual private cloud (VPC). You can deploy it directly on an Amazon Elastic Compute Cloud (Amazon EC2) instance or by using container technology, such as Amazon Elastic Container Service (Amazon ECS) or AWS Fargate. For more information about choosing the right AWS container service for your modern application development, see [Choosing an AWS container service](https://docs.aws.amazon.com/decision-guides/latest/containers-on-aws-how-to-choose/choosing-aws-container-service.html).
