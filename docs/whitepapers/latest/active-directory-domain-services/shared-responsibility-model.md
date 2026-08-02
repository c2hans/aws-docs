---
source_url: https://docs.aws.amazon.com/whitepapers/latest/active-directory-domain-services/shared-responsibility-model.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Shared responsibility model
<a name="shared-responsibility-model"></a>

 When operating in the AWS Cloud, Security and Compliance is a [shared responsibility](https://aws.amazon.com/compliance/shared-responsibility-model/) between AWS and the customer. AWS is responsible for security “of” the cloud, whereas customers are responsible for security “in” the cloud.

![Diagram showing the Shared Responsibility Model when operating in AWS Cloud](http://docs.aws.amazon.com/whitepapers/latest/active-directory-domain-services/images/shared-responsibility-model.jpg)

 AWS is responsible for securing its software, hardware, and the facilities where AWS services are located, including securing its computing, storage, networking, and database services. In addition, AWS is responsible for the security configuration of AWS Managed Services, like Amazon DynamoDB, Amazon Relational Database Service (Amazon RDS), Amazon Redshift, Amazon EMR, Amazon WorkSpaces, and so on.

 Customers are responsible for implementing appropriate access control policies using AWS Identity and Access Management (IAM), configuring AWS Security Groups (Firewall) to prevent unauthorized access to ports, and enabling AWS CloudTrail.

 Customers are also responsible for enforcing appropriate data loss prevention policies to ensure compliance with internal and external policies, as well as detecting and remediating threats arising from stolen account credentials or malicious or accidental misuse of AWS.

 If you decide to run your own Active Directory on Amazon EC2 instances, you have full administrative control of the operating system and the Active Directory environment. You can set up custom configurations and create a complex hybrid deployment topology. However, you must operate and support it in the same manner as you do with on-premises Active Directory.

 If you use AWS Managed Microsoft AD, AWS provides instance deployment in one or multiple regions, operational management of your directory, monitoring, backup, patching, and recovery services. You configure the service and perform administrative management of users, groups, computers, and policies.

 AWS Managed Microsoft AD has been audited and approved for use in deployments that require Federal Risk and Authorization Management (FedRAMP), Payment Card Industry Data Security Standard (PCI DSS), U.S. Health Insurance Portability and Accountability Act (HIPAA), or Service Organizational Control (SOC) compliance. When used with compliance requirements, it is your responsibility to configure the directory password policies and ensure that the entire application and infrastructure deployment meets your compliance requirements. For more information, see [Manage Compliance](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_compliance.html) [for AWS Managed Microsoft AD](https://aws.amazon.com/compliance/services-in-scope/).
