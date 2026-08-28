---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-zero-trust-architecture/introduction.html
---

# Embracing Zero Trust: A strategy for security modernization
<a name="introduction"></a>

*Greg Gooden, Amazon Web Services*

Today, more than ever, organizations are focusing on security as a key priority. This enables a wide range of benefits, from maintaining the trust of their customers, to improving the mobility of their workforce, to unlocking new digital business opportunities. As they do so, they continue to ask an age-old question: What are the optimal patterns to ensure the right levels of security and availability for my systems and data? Increasingly, Zero Trust has become the term used to describe the modern answer to this question.

Zero trust architecture (ZTA) is a conceptual model and an associated set of mechanisms that focus on providing security controls around digital assets that do not solely or fundamentally depend on traditional network controls or network perimeters. Instead, network controls are augmented with identity, device, behavior, and other rich context and signals to make more granular, intelligent, adaptive, and continuous access decisions. By implementing a ZTA model, you can achieve a meaningful next iteration in the continuous maturation of cybersecurity and concepts of defense in depth in particular.

## Decision-making processes
<a name="decision-making-processes"></a>

Implementing a ZTA strategy requires careful planning and decision-making. It involves evaluating various factors and aligning them with organizational goals. Key decision-making processes for embarking on a ZTA journey include:

1. Stakeholder engagement – It's crucial to engage other CxOs, VPs, and senior managers to understand their priorities, concerns, and vision for your organization's security posture. By involving key stakeholders from the outset, you can align the ZTA implementation with the overall strategic objectives and gains the necessary support and resources.

1. Risk assessment – Conducting a comprehensive risk assessment helps identify issues, excessive surface area, and critical assets, which helps you make informed decisions on security controls and investment. Evaluate your organization's existing security posture, identify potential weaknesses, and prioritize areas of improvement based on the risk landscape that is specific to your industry and operational environment.

1. Technology evaluation – Assessing the organization's existing technology landscape and identifying gaps helps in selecting appropriate tools and solutions that align with the ZTA principles. This evaluation should include a thorough analysis of the following:
   + Network architecture
   + Identity and access management systems
   + Authentication and authorization mechanisms
   + Unified endpoint management
   + Resource ownership tools and processes
   + Encryption technologies
   + Monitoring and logging capabilities
   + Choosing the right technology stack is crucial for building a robust ZTA model.

1. Change management – Recognizing the cultural and organizational impacts of adopting a ZTA model is essential. Implementing change management practices helps ensure smooth transition and acceptance throughout the organization. It involves educating employees about the principles and benefits of ZTA, providing training on new security practices, and fostering a security-conscious culture that encourages accountability and continuous learning.

This prescriptive guidance aims to provide CxOs, VPs, and senior managers with a comprehensive strategy for implementing ZTA. It will delve into the key aspects of ZTA, including the following:
+ Organizational readiness
+ Phased adoption approaches
+ Stakeholder collaboration
+ Best practices to achieve a secure and agile business transformation

By following this guidance, your organization can navigate the ZTA landscape and achieve successful outcomes in your security journey in the Amazon Web Services (AWS) Cloud. AWS offers a variety of services that you can use to implement a ZTA, such as AWS Verified Access, AWS Identity and Access Management (IAM), Amazon Virtual Private Cloud (Amazon VPC), Amazon VPC Lattice, Amazon Verified Permissions, Amazon API Gateway, and Amazon GuardDuty. These services can help to protect AWS resources from unauthorized access.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
