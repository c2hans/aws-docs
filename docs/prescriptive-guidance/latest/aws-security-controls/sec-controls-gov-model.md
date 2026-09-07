---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-security-controls/sec-controls-gov-model.html
---

# Security controls in the governance framework
<a name="sec-controls-gov-model"></a>

It is important to plan from a foundational level. How does one start? The following figure shows how you can build a security governance strategy based on a policy, control objectives, standards, and security controls.

![The layers of a security governance framework.](https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-security-controls/images/guide-img/4d22877b-9cac-4bc5-8ae8-4555441015fe/images/dba2aaf8-ee84-4add-996e-9ab35817ce75.png)

The following are the hierarchical components of a governance strategy for security:
+ **Policy** – A *policy* is the foundation of any cybersecurity governance strategy. It is a document that states the expectations of the company, such as statutory, regulatory, or contractual obligations that it must meet. Policies can vary by industry and region.
+ **Control objectives** – *Control objectives* are targets, such as industry-recognized best practices, that help you meet the intent of a policy. For cloud computing, many companies adopt the [Cloud Controls Matrix (CCM)](https://cloudsecurityalliance.org/research/cloud-controls-matrix/) (Cloud Security Alliance website), which is a framework of cybersecurity control objectives.
+ **Standards** – *Standards* are formally established requirements that satisfy a control objective. Standards might include processes, actions, or configurations, and they are quantifiable so that you can measure performance against the standard.
+ **Security controls** – *Security controls *are the technical or administrative mechanisms you put in place to implement the standards. All security controls map to standards, but not all standards map to security controls. Testing of security controls is designed to monitor and measure whether you are effectively meeting the defined standards.

This guide focuses on how to design and implement common types of security controls in the AWS Cloud.
