---
source_url: https://docs.aws.amazon.com/whitepapers/latest/nhs-cloud-security-guidance-using-aws/principle-14-secure-use-of-the-service.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Principle 14: Secure use of the service
<a name="principle-14-secure-use-of-the-service"></a>

****
 The security of cloud services and the data held within them can be undermined if you use the service poorly. Consequently, you will have certain responsibilities when using the service in order for your data to be adequately protected.

 Cloud computing introduces a significant shift in how technology is obtained, used, and managed, and each organisation’s cloud adoption journey is unique. To successfully achieve cloud adoption, customers need to understand their organization’s current state, the target state, and the transition required to achieve that target state. Knowing this will help set goals and create workstreams that will enable the organisation to thrive in the cloud.

 As workstreams are implemented, organisations can take advantage of the [AWS Cloud Adoption Framework](https://aws.amazon.com/professional-services/CAF/) (AWS CAF) to understand how to communicate dependencies between different stakeholders. The AWS CAF structure can also help ensure that the strategies and plans across organisations are complete and aligned to business goals and outcomes.

 Maintaining Security and Compliance is an ongoing effort, due to changing application requirements, operating system patches, configurations updates, and so on, all creating a “configuration drift” away from the ideal established at the implementation, in addition to the changing threat landscape and compliance regime.

 AWS offers customers the opportunity to build adaptive and highly resilient security programmes for their workloads, much more effectively than is possible using traditional infrastructure.

 As per the AWS Shared Responsibility Model, and due to the self-service nature of cloud computing, a successful security programme starts from the preparation phase, before moving into design, implementation, operation, and then continuous improvement.

 AWS offers customers many resources to help and guide them throughout the entire process. In addition to the AWS Cloud Adoption Framework mentioned above, customers can take advantage of the following resources:
+  The [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html);
+  The associated [Security Pillar](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html);
+  A variety of [AWS security best practices](https://aws.amazon.com/security/security-resources/); and
+  [AWS Architecture Center](https://aws.amazon.com/answers/) to common questions on a variety of topics, including account management, big data, networking, and security. The AWS Architecture Center outlines AWS best practices and provides prescriptive architectural guidance, as well as automated solutions deployable to an AWS account in very short timescales.

 These frameworks and best practices, in addition to more in-depth consultancy available from [AWS Professional Services](https://aws.amazon.com/professional-services/) or [AWS Partners](https://aws.amazon.com/partners/), can assist customers in all phases of their cloud journey and align with the *Secure use of the service* Principle of the [Good Practice Guide](https://digital.nhs.uk/data-and-information/looking-after-information/data-security-and-information-governance/nhs-and-social-care-data-off-shoring-and-the-use-of-public-cloud-services).

## Advice for specific Guidance points:
<a name="advice-for-specific-guidance-points"></a>

****
 The Service User should use a security-hardened primary operating system image to build guest servers.

 **Applicable risk classes**: All

## Instance-based services
<a name="instance-based-services"></a>

 Services that expose virtual instances to customers, such as Amazon EC2, Amazon Elastic Container Service (Amazon ECS), and so on, enable those instances to be completely controlled by the customer, and by default, provide full root access or administrative control over accounts, services, and applications on them. However, AWS recommends that customers implement a base set of security best practices, including disabling password-only access, and utilising some form of multi-factor authentication to gain access to instances (or at a minimum certificate-based SSH Version 2 access). Additionally, customers should employ a privilege escalation mechanism, with per-user logging. The publicly available [Center for Internet Security (CIS) Benchmarks](https://docs.aws.amazon.com/inspector/latest/userguide/inspector_cis.html) provide comprehensive advice on what can be done, how to do it, and how to audit it.

 For example, if the guest OS is Linux, and the customer wants to enable remote terminal access, then after hardening the instance, the customer should utilise certificate-based SSHv2 for that access, disable remote root login, use command line logging, and use ‘sudo’ for privilege escalation. Customers should also generate their own key pairs to guarantee that they are unique and not shared with other customers or with AWS.

 Virtual instances are launched from an Amazon Machine Image (AMI) selected by the customer. AWS supplies a set of default AMIs for guest operating systems supported on AWS, which customers may harden further and store as custom AMIs to use as the template for launching additional instances for use in their AWS environments.

 AWS also supports the use of the Secure Shell (SSH) network protocol to enable secure login to the instances. Authentication for SSH used with AWS is via a public/private key pair to reduce the risk of unauthorised access to the instance. Customers can also connect remotely to a Windows instance with Remote Desktop Protocol (RDP) by using an RDP certificate generated for the instance.

 The recommended approach from AWS, however, is not to permit direct remote terminal access to EC2 instances, but rather to make use of the AWS Systems Manager services, which enables remote management to be performed more securely and with centralised oversight, using the appropriate elements of that service. See [AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html) for more details.

## Serverless services
<a name="serverless-services"></a>

 The majority of services on the AWS Cloud platform are serverless, that is, the management of the underlying virtual instances is the responsibility of AWS, including their security (which will entail the use of security-hardened primary images). AWS recommends customers consider using these services where possible, in order to take advantage of the additional security (as well as operational agility and potential for cost reduction) available through this approach.

 Examples of such services for generalised compute include AWS Fargate (for managed containers) and AWS Lambda, which integrate with natively with related services such as Amazon API Gateway, Amazon Kinesis (for applications processing streaming data), and so on.

****
 The Service User should utilise integrated security monitoring and policy management facilities to help detect threats and weaknesses, due to poor design or misconfiguration.

 **Applicable risk classes:** All
+  **Customer notification mechanisms** — Mechanisms are in place to allow the AWS Support team to be made aware of operational issues that impact the customer experience. A [Service Health Dashboard](https://status.aws.amazon.com/) is available and maintained by the AWS Support team to alert customers to any issues that may be of broad impact. The customer-specific instance of this is known as the [AWS Health Dashboard](https://aws.amazon.com/premiumsupport/technology/personal-health-dashboard/), showing a view of operational issues that may affect individual customer accounts. [AWS Cloud Security](https://aws.amazon.com/security/) is available to provide customers with security and compliance details about AWS.

   Customers can also subscribe to AWS Support offerings that include direct communication with the AWS support team and proactive alerts to any customer impacting issues.
+  [https://aws.amazon.com/premiumsupport/technology/trusted-advisor/](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/) — Some AWS Support plans include access to the AWS Trusted Advisor tool, which offers a one-view snapshot of the service portfolio in use and helps identify common security misconfigurations, suggestions for improving system performance, and underutilised resources.

   Trusted Advisor checks for compliance with the following security recommendations:
+  Limited access to common administrative ports to only a small subset of addresses. This includes ports 22 (SSH), 23 (Telnet) 3389 (RDP), and 5500 (VNC).
+  Limited access to common database ports. This includes ports 1433 (MSSQL Server), 1434 (MSSQL Monitor), 3306 (MySQL), Oracle (1521), and 5432 (PostgreSQL).
+  IAM is configured to help ensure secure access control of AWS resources.
+  Multi-factor authentication (MFA) token is enabled to provide two-factor authentication for the root AWS account.

****
 The Service User should undertake annual assessment against a recognised standard such as ISO, CyberEssentials to test the "security monitoring".

 **Applicable risk classes:** III-V

 Should the scope of such an assessment include the AWS services used by customer systems, the associated burden may be considerably reduced by referring to the controls detailed in the relevant AWS compliance documentation, such as SOC reports, ISO27001, 27017, and 27018 certifications, among others.
