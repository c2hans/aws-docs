---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/sec_incident_response_develop_management_plans.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# SEC10-BP02 Develop incident management plans
<a name="sec_incident_response_develop_management_plans"></a>

|  |
| --- |
| This best practice was updated with new guidance on July 13th, 2023. |

The first document to develop for incident response is the incident response plan. The incident response plan is designed to be the foundation for your incident response program and strategy.

 **Benefits of establishing this best practice:** Developing thorough and clearly defined incident response processes is key to a successful and scalable incident response program. When a security event occurs, clear steps and workflows will help you to respond in a timely manner. You might already have existing incident response processes. Regardless of your current state, it’s important to update, iterate, and test your incident response processes regularly.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>

An incident management plan is critical to respond, mitigate, and recover from the potential impact of security incidents. An incident management plan is a structured process for identifying, remediating, and responding in a timely matter to security incidents.

 The cloud has many of the same operational roles and requirements found in an on-premises environment. When creating an incident management plan, it is important to factor response and recovery strategies that best align with your business outcome and compliance requirements. For example, if you are operating workloads in AWS that are FedRAMP compliant in the United States, it’s useful to adhere to [NIST SP 800-61 Computer Security Handling Guide](https://nvlpubs.nist.gov/nistpubs/specialpublications/nist.sp.800-61r2.pdf). Similarly, when operating workloads with European personally identifiable information (PII) data, consider scenarios like how you might protect and respond to issues related to data residency as mandated by [EU General Data Protection Regulation (GDPR) Regulations](https://ec.europa.eu/info/law/law-topic/data-protection/reform/what-does-general-data-protection-regulation-gdpr-govern_en).

 When building an incident management plan for your workloads operating in AWS, start with the [AWS Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/) for building a defense-in-depth approach towards incident response. In this model, AWS manages security of the cloud, and you are responsible for security in the cloud. This means that you retain control and are responsible for the security controls you choose to implement. The [AWS Security Incident Response Guide](https://docs.aws.amazon.com/whitepapers/latest/aws-security-incident-response-guide/welcome.html) details key concepts and foundational guidance for building a cloud-centric incident management plan.

 An effective incident management plan must be continually iterated upon, remaining current with your cloud operations goal. Consider using the implementation plans detailed below as you create and evolve your incident management plan.

## Implementation steps
<a name="implementation-steps"></a>

 **Define roles and responsibilities**

 Handling security events requires cross-organizational discipline and an inclination for action. Within your organizational structure, there should be many people who are responsible, accountable, consulted, or kept informed during an incident, such as representatives from human resources (HR), the executive team, and legal. Consider these roles and responsibilities, and whether any third parties must be involved. Note that many geographies have local laws that govern what should and should not be done. Although it might seem bureaucratic to build a responsible, accountable, consulted, and informed (RACI) chart for your security response plans, doing so facilitates quick and direct communication and clearly outlines the leadership across different stages of the event.

 During an incident, including the owners and developers of impacted applications and resources is key because they are subject matter experts (SMEs) that can provide information and context to aid in measuring impact. Make sure to practice and build relationships with the developers and application owners before you rely on their expertise for incident response. Application owners or SMEs, such as your cloud administrators or engineers, might need to act in situations where the environment is unfamiliar or has complexity, or where the responders don’t have access.

 Lastly, trusted partners might be involved in the investigation or response because they can provide additional expertise and valuable scrutiny. When you don’t have these skills on your own team, you might want to hire an external party for assistance.

 **Understand AWS response teams and support**
+  **AWS Support**
  +  [Support](https://aws.amazon.com/premiumsupport/) offers a range of plans that provide access to tools and expertise that support the success and operational health of your AWS solutions. If you need technical support and more resources to help plan, deploy, and optimize your AWS environment, you can select a support plan that best aligns with your AWS use case.
  +  Consider the [Support Center](https://console.aws.amazon.com/support) in AWS Management Console (sign-in required) as the central point of contact to get support for issues that affect your AWS resources. Access to Support is controlled by AWS Identity and Access Management. For more information about getting access to Support features, see [Getting started with Support](https://docs.aws.amazon.com/awssupport/latest/user/getting-started.html#accessing-support).
+  **AWS Customer Incident Response Team (CIRT)**
  +  The AWS Customer Incident Response Team (CIRT) is a specialized 24/7 global AWS team that provides support to customers during active security events on the customer side of the [AWS Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/).
  +  When the AWS CIRT supports you, they provide assistance with triage and recovery for an active security event on AWS. They can assist in root cause analysis through the use of AWS service logs and provide you with recommendations for recovery. They can also provide security recommendations and best practices to help you avoid security events in the future.
  +  AWS customers can engage the AWS CIRT through an [Support case](https://docs.aws.amazon.com/awssupport/latest/user/case-management.html).
+  **DDoS response support**
  +  AWS offers [AWS Shield](https://aws.amazon.com/shield/), which provides a managed distributed denial of service (DDoS) protection service that safeguards web applications running on AWS. Shield provides always-on detection and automatic inline mitigations that can minimize application downtime and latency, so there is no need to engage Support to benefit from DDoS protection. There are two tiers of Shield: AWS Shield Standard and AWS Shield Advanced. To learn about the differences between these two tiers, see [Shield features documentation](https://aws.amazon.com/shield/features/).
+  **AWS Managed Services (AMS)**
  +  [AWS Managed Services (AMS)](https://aws.amazon.com/managed-services/) provides ongoing management of your AWS infrastructure so you can focus on your applications. By implementing best practices to maintain your infrastructure, AMS helps reduce your operational overhead and risk. AMS automates common activities such as change requests, monitoring, patch management, security, and backup services, and provides full-lifecycle services to provision, run, and support your infrastructure.
  +  AMS takes responsibility for deploying a suite of security detective controls and provides a 24/7 first line of response to alerts. When an alert is initiated, AMS follows a standard set of automated and manual playbooks to verify a consistent response. These playbooks are shared with AMS customers during onboarding so that they can develop and coordinate a response with AMS.

 **Develop the incident response plan**

 The incident response plan is designed to be the foundation for your incident response program and strategy. The incident response plan should be in a formal document. An incident response plan typically includes these sections:
+  **An incident response team overview:** Outlines the goals and functions of the incident response team.
+  **Roles and responsibilities:** Lists the incident response stakeholders and details their roles when an incident occurs.
+  **A communication plan:** Details contact information and how you will communicate during an incident.
+  **Backup communication methods:** It’s a best practice to have out-of-band communication as a backup for incident communication. An example of an application that provides a secure out-of-band communications channel is AWS Wickr.
+  **Phases of incident response and actions to take:** Enumerates the phases of incident response (for example, detect, analyze, eradicate, contain, and recover), including high-level actions to take within those phases.
+  **Incident severity and prioritization definitions:** Details how to classify the severity of an incident, how to prioritize the incident, and then how the severity definitions affect escalation procedures.

 While these sections are common throughout companies of different sizes and industries, each organization’s incident response plan is unique. You will need to build an incident response plan that works best for your organization.

## Resources
<a name="resources"></a>

 **Related best practices:**
+  [SEC04 (How do you detect and investigate security events?)](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/detection.html)

 **Related documents:**
+  [AWS Security Incident Response Guide](https://docs.aws.amazon.com/whitepapers/latest/aws-security-incident-response-guide/welcome.html)
+ [ NIST: Computer Security Incident Handling Guide ](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-61r2.pdf)
