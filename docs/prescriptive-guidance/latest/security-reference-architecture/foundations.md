---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/foundations.html
---

# Security foundations
<a name="foundations"></a>

The AWS SRA aligns to three AWS security foundations: the AWS Cloud Adoption Framework (AWS CAF), AWS Well-Architected, and the AWS Shared Responsibility Model.

AWS Professional Services created the [AWS CAF](https://aws.amazon.com/professional-services/CAF/) to help companies design and follow an accelerated path to successful cloud adoption. The guidance and best practices provided by the framework help you build a comprehensive approach to cloud computing across your enterprise and throughout your IT lifecycle. The AWS CAF organizes guidance into six areas of focus, called *perspectives*. Each perspective covers distinct responsibilities owned or managed by functionally related stakeholders. In general, the business, people, and governance perspectives focus on business capabilities; whereas the platform, security, and operations perspectives focus on technical capabilities.

The [security perspective of the AWS CAF](https://docs.aws.amazon.com/whitepapers/latest/overview-aws-cloud-adoption-framework/security-perspective.html) helps you structure the selection and implementation of controls across your business. Following the current AWS recommendations in the security pillar can help you meet your business and regulatory requirements.

[AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) helps cloud architects build a secure, high-performing, resilient, and efficient infrastructure for their applications and workloads. The framework is based on six pillars—operational excellence, security, reliability, performance efficiency, cost optimization, and sustainability—and provides a consistent approach for AWS customers and Partners to evaluate architectures and implement designs that can scale over time. We believe that having well-architected workloads greatly increases the likelihood of business success.

The [Well-Architected Framework security pillar](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html) describes how to take advantage of cloud technologies to help protect data, systems, and assets in a way that can improve your security posture. This will help you meet your business and regulatory requirements by following current AWS recommendations. There are additional Well-Architected Framework focus areas that provide more context for specific domains such as governance, serverless, AI/ML, and gaming. These are known as AWS Well-Architected lenses.

Security and compliance are a [shared responsibility between AWS and the customer](https://aws.amazon.com/compliance/shared-responsibility-model/). This shared model can help relieve your operational burden as AWS operates, manages, and controls the components from the host operating system and virtualization layer down to the physical security of the facilities in which the service operates. For example, you assume responsibility and management of the guest operating system (including updates and security patches), application software, server-side data encryption, network traffic route tables, and the configuration of the AWS-provided security group firewall. For abstracted services such as Amazon S3 and Amazon DynamoDB, AWS operates the infrastructure layer, the operating system, and platforms, and you access the endpoints to store and retrieve data. You are responsible for managing your data (including encryption options), classifying your assets, and using IAM tools to apply the appropriate permissions. This shared model is often described by saying that AWS is responsible for the security *of* the cloud (that is, for protecting the infrastructure that runs all the services offered in the AWS Cloud), and you are responsible for the security *in* the cloud (as determined by the AWS Cloud services that you select).

Within the guidance provided by these foundational documents, two sets of concepts are particularly relevant to the design and understanding of the AWS SRA: security capabilities and security design principles.

## Security capabilities
<a name="security-capabilities"></a>

The security perspective of the AWS CAF outlines nine capabilities that help you achieve the confidentiality, integrity, and availability of your data and cloud workloads.
+ *Security governance* to develop and communicate security roles, responsibilities, policies, processes, and procedures across your organization's AWS environment.
+ *Security assurance* to monitor, evaluate, manage, and improve the effectiveness of your security and privacy programs.
+ *Identity and access management* to manage identities and permissions at scale.
+ *Threat detection* to understand and identify potential security misconfigurations, threats, or unexpected behaviors.
+ *Vulnerability management* to continuously identify, classify, remediate, and mitigate security vulnerabilities.
+ *Infrastructure protection* to help validate that systems and services within your workloads are protected.
+ *Data protection* to maintain visibility and control over data, and how it is accessed and used in your organization.
+ *Application security* to help detect and address security vulnerabilities during the software development process.
+ *Incident response* to reduce potential harm by effectively responding to security incidents.

## Security design principles
<a name="security-principles"></a>

The [security pillar](https://docs.aws.amazon.com/wellarchitected/latest/framework/security.html) of the Well-Architected Framework captures a set of seven design principles that turn specific security areas into practical guidance that can help you strengthen your workload security. Where the security capabilities frame the overall security strategy, these Well-Architected Framework principles describe what you can start doing. They are reflected very deliberately in this AWS SRA and consist of the following:
+ *Implement a strong identity foundation* ‒ Implement the principle of least privilege, and enforce separation of duties with appropriate authorization for each interaction with your AWS resources. Centralize identity management, and aim to eliminate reliance on long-term static credentials.
+ *Enable traceability* ‒ Monitor, generate alerts, and audit actions and changes to your environment in real time. Integrate log and metric collection with systems to automatically investigate and take action.
+ *Apply security at all layers* ‒ Apply a defense-in-depth approach with multiple security controls. Apply multiple types of controls (for example, preventive and detective controls) to all layers, including edge of network, virtual private cloud (VPC), load balancing, instance and compute services, operating system, application configuration, and code.
+ *Automate security best practices* ‒ Automated, software-based security mechanisms improve your ability to securely scale more rapidly and cost-effectively. Create secure architectures, and implement controls that are defined and managed as code in version-controlled templates.
+ *Protect data in transit and at rest* ‒ Classify your data into sensitivity levels and use mechanisms such as encryption, tokenization, and access control where appropriate.
+ *Keep people away from data* ‒ Use mechanisms and tools to reduce or eliminate the need to directly access or manually process data. This reduces the risk of mishandling or modification and human error when handling sensitive data.
+ *Prepare for security events *‒ Prepare for an incident by having incident management and investigation policy and processes that align to your organizational requirements. Run incident response simulations and use tools with automation to increase your speed for detection, investigation, and recovery.

## How to use the AWS SRA with AWS CAF and AWS Well-Architected Framework
<a name="sra-caf-waf"></a>

The AWS CAF, AWS Well-Architected Framework, and AWS SRA are complementary frameworks that work together to support your cloud migration and modernization efforts.
+ The [AWS CAF](https://docs.aws.amazon.com/whitepapers/latest/overview-aws-cloud-adoption-framework/welcome.html) leverages AWS experience and best practices to help you align the values of cloud adoption to your desired business outcomes. Use the AWS CAF to identify and prioritize transformation opportunities, evaluate and improve cloud readiness, and iteratively evolve your transformation roadmap.
+ The [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html) provides AWS recommendations for building a secure, high-performing, resilient, and efficient infrastructure for a variety of applications and workloads that meet your business outcomes.
+ The AWS SRA helps you understand how to deploy and govern security services in a way that aligns with the recommendations of the AWS CAF and the AWS Well-Architected Framework.

For example, the AWS CAF security perspective suggests that you evaluate how to centrally manage your workforce identities and their authentication in AWS. Based on this information, you might decide to use a new or existing corporate identity provider (IdP) solution such as Okta, Active Directory, or Ping Identity for this purpose. You follow the guidance in the AWS Well-Architected Framework and decide to integrate your IdP with the AWS IAM Identity Center to give your employees a single sign-on experience that can synchronize their group memberships and permissions. You review the AWS SRA recommendation to enable IAM Identity Center in the management account of your AWS organization and administer it through a security tooling account used by your security operations team. This example illustrates how the AWS CAF helps you make initial decisions about your desired security posture, the AWS Well-Architected Framework provides the guidance on how to evaluate the AWS services that are available for meeting that objective, and the AWS SRA then provides recommendations on how to deploy and govern the security services you select.
