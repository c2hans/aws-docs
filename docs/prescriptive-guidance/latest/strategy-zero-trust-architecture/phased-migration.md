---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-zero-trust-architecture/phased-migration.html
---

# Phased approach to Zero Trust
<a name="phased-migration"></a>

Adoption of a zero trust architecture (ZTA) requires careful planning and implementation. We recommend a phased adoption approach to smooth transition and minimize disruption to business operations. This section provides guidance on the key phases involved in adopting a ZTA.

## Phase 1: Assessment and planning
<a name="phase-1"></a>

The first phase of Zero Trust implementation is assessment and planning. This phase is critical to the success of the overall implementation, because it involves identifying and addressing any gaps in your organization's current security posture. By taking the time to assess your current state and define your security objectives, you can lay the foundation for a successful Zero Trust implementation.

At the same time, a perfectly complete and accurate assessment might not be always realistic. To avoid analysis paralysis that prevents you from moving on to further phases, be prepared to compartmentalize or otherwise accept some level of imperfection.

1. **Assess the current state** – Conduct an assessment of your existing security infrastructure, policies, and controls. Identify potential vulnerabilities, gaps in security, and areas where the implementation of Zero Trust principles can provide improvements.

1. **Define security objectives** – Based on the current state assessment findings, define security objectives that align with the principles of Zero Trust. These security objectives should also align with your organization's overall security strategy and address identified vulnerabilities and gaps.

1. **Design the architecture** – Develop a ZTA that supports your organization's security goals. This architecture should include the necessary components, such as identity and access management solutions, network segmentation mechanisms, and continuous monitoring systems. The architecture should also be scalable, adaptable, and capable of accommodating future growth and technological advancements. Ideally, this architecture should be represented in a format that's easily consumed by the teams responsible for implementing it, such as an AWS CloudFormation template, not just as a document or diagram.

1. **Engage stakeholders** – Involve all stakeholders, including business units, IT teams, and security teams, to gain insights and align their objectives with the ZTA implementation plan. Encourage collaboration and communication to establish a shared understanding of the benefits and requirements of the Zero Trust approach.

## Phase 2: Piloting and implementation
<a name="phase-2"></a>

The second phase of Zero Trust implementation is piloting and implementation. This phase involves testing the ZTA in a small-scale, controlled environment, and then iteratively deploying it across your organization. It's important to educate employees on the new security measures and their roles in maintaining a Zero Trust environment.

1. **Pilot the deployment** – Test the ZTA in a small-scale, controlled environment. Implement the necessary components and security controls that were defined in the architecture design phase. Monitor the pilot deployment closely, gather feedback, and make any necessary adjustments. Be prepared to be flexible early in the process, when Zero Trust moves from being a hypothetical exercise to one that you're building real experience with.

1. **Deploy iteratively** – Based on the lessons learned from the pilot deployment, begin the iterative deployment of Zero Trust across the organization. Build momentum through a flywheel effect that doesn't require an extensive campaign to achieve critical deployment mass. Reserve leadership mandates or escalations for the longer tail of the rollout where they might be required.

1. **Provide user training and raise awareness** – Educate employees on the new security measures and their roles in maintaining a Zero Trust environment. Emphasize the importance of secure practices, such as strong passwords, multi-factor authentication, and regular security updates.

1. **Manage change** – Create a comprehensive change management plan to address the organizational and cultural changes associated with Zero Trust adoption. Communicate the benefits and rationale behind the adoption to employees, and address any concerns or resistance. Provide ongoing support and guidance to facilitate a smooth transition.

## Phase 3: Monitoring and continuous improvement
<a name="phase-3"></a>

The third and final phase of Zero Trust implementation is monitoring and continuous improvement. This phase involves establishing a comprehensive monitoring and analytics program, creating a comprehensive incident response plan, and regularly soliciting feedback from stakeholders and users.

1. **Monitor continuously** – Establish a comprehensive monitoring and analytics program to assess the security posture continuously and detect any potential anomalies. Use advanced security tools and technologies to monitor user behavior, network traffic, and system activities.

1. **Plan incident response and remediation** – Create a comprehensive incident response plan that aligns with the Zero Trust principles. Establish clear escalation paths, define roles and responsibilities, and implement automated incident response mechanisms where possible. Regularly test and update the incident response plan.

1. **Obtain feedback and evaluation** – Regularly solicit feedback from stakeholders and users to gather insights into the effectiveness of the zero trust architecture (ZTA). Conduct periodic evaluations and assessments to measure the impact on security posture, operational efficiency, and user experience. Use the feedback and evaluation results to identify areas for improvement. Expect that your ZTAs will change over time, and consider how development teams will implement these updates with minimal effort or disruptions.

## Section summary
<a name="phased-approach-summary"></a>

By following this phased adoption approach, organizations can effectively transition to a ZTA while minimizing risks and disruptions. The next section discusses best practices for achieving success with Zero Trust implementation, covering key considerations and recommendations for CxOs, VPs, and senior managers.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
