---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-zero-trust-architecture/key-takeaways.html
---

# Key takeaways
<a name="key-takeaways"></a>

This guide has explored the essential aspects of developing a successful zero trust architecture (ZTA) strategy. This section summarizes the key takeaways from the prescriptive guidance presented:
+ **Understand Zero Trust principles** – Zero Trust is a conceptual model and an associated set of mechanisms that focus on providing security controls around digital assets that do not solely or fundamentally depend on traditional network controls or network perimeters. Instead, network controls are augmented with identity, device, behavior, and other rich context and signals to make more granular, intelligent, adaptive, and continuous access decisions. Familiarize yourself with the core principles of Zero Trust, such as least privilege, micro-segmentation, continuous authentication, and adaptive authorization.
+ **Define clear objectives** – Clearly define the objectives and desired business outcomes of the ZTA adoption. Align these objectives with the principles of Zero Trust to help ensure a strong security foundation while enabling business growth and innovation.
+ **Conduct comprehensive assessments** – Perform a thorough assessment of your existing IT infrastructure, applications, and data assets. Identify dependencies, technical debt, and compatibility issues to inform your adoption strategy.
+ **Develop a ZTA adoption plan** – Create a detailed plan that outlines the step-by-step approach for moving workloads, applications, and data to the cloud. Consider factors such as compliance requirements and application modernization.
+ **Implement a robust ZTA** – Design and implement a ZTA that enforces granular access controls, strong authentication mechanisms, and continuous monitoring. For a more efficient ZTA adoption, use cloud-native Zero Trust services, such as AWS Verified Access and Amazon VPC Lattice.
+ **Prioritize data and application security** – Apply Zero Trust principles—strong identity, micro-segmentation, and authorization—to provide all available context. Use this context for users accessing systems and resources and for the flow of communications and data within and between backend components.
+ **Establish monitoring and incident response frameworks** – Implement robust security monitoring and incident response capabilities in the cloud environment. Use cloud-native security tools for real-time threat detection, log analysis, and incident response automation, such as Amazon Inspector, AWS Security Hub CSPM, and Amazon GuardDuty.
+ **Foster a culture of security and compliance** – Promote a culture of security awareness and compliance throughout the organization. Educate employees on security best practices and their role in maintaining a secure cloud environment.
+ **Continuously assess and optimize** – Regularly assess the cloud environment, security controls, and operational processes. To gather insights and optimize resource utilization, cost management, and performance, use cloud-native analytics and monitoring tools such as Amazon CloudWatch and AWS Security Hub CSPM.
+ **Establish governance and compliance frameworks** – Develop governance and compliance frameworks that align with industry standards and regulatory requirements. Define policies, procedures, and controls to help ensure adherence to security, privacy, and compliance standards.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
