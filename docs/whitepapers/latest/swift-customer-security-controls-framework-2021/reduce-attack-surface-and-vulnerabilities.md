---
source_url: https://docs.aws.amazon.com/whitepapers/latest/swift-customer-security-controls-framework-2021/reduce-attack-surface-and-vulnerabilities.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Requirement 2 - Reduce attack surface and vulnerabilities
<a name="reduce-attack-surface-and-vulnerabilities"></a>

## Internal data flow security
<a name="internal-data-flow-security"></a>

 The internal data flow security control objective can be accomplished by securing server-to-server traffic using authentication with one-way Transport Layer Security (TLS), or two-way TLS. This control is applicable for the communications between all applications, messaging interfaces, and database connections. The communication between SWIFT applications, Alliance Messaging Hub (AMH), Alliance Access (SAA), Alliance Gateway (SAG), and SWIFTNet Link (SNL), have the mechanism enforced in the application configuration. From the AWS perspective, here is the list of guidance by architecture components:
+  **[Amazon MQ](https://aws.amazon.com/amazon-mq/)** — Amazon MQ requires a user ID and password to connect to the message broker. Amazon MQ protocols have TLS 1.2 enabled. Refer to [https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/data-protection.html#data-protection-encryption-in-transit](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/data-protection.html#data-protection-encryption-in-transit).
+  **[Amazon RDS for Oracle](https://aws.amazon.com/rds/oracle/)** — Amazon RDS for Oracle supports authentication and TLS 1.2 and higher encryption in transit. Refer to [Oracle Secure Sockets Layer](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.Options.SSL.html).
+  ** [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/)** — The user ID, password, and connection information can be safely stored in AWS Secrets Manager. The password should be rotated regularly. AWS Secrets Manager supports password rotation natively.
+  **[AWS Certificate Manager Private Certificate Authority](https://aws.amazon.com/certificate-manager/private-certificate-authority/)** (CA) — For issuing, managing, and renewal of certificates when using two-way TLS for communication.
+  **[AWS Systems Manager Session Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager.html)** — Communication between EC2 instances and AWS Systems Manager Session Manager is always encrypted with TLS. An IAM assume role with MFA and source IP condition enforced should be used for gaining access to the AWS Systems Manager.
+  **Security Group** — Security groups act as a stateful firewall for the components in the SWIFT secure zone. It should be set up so that only the intended traffic is allowed between components.

## Security updates
<a name="security-updates"></a>

 Leveraging container services greatly simplifies the security updates process for many customers. By using Amazon MQ and Amazon RDS for Oracle in the SWIFT secure zone, you do not need to worry about maintaining and patching the underlying EC2 instances. AWS is responsible for maintaining updates for the underlying EC2 instances for AWS Managed Services. In this model, it is your responsibility to upgrade the Amazon MQ broker version and Amazon RDS for Oracle major and minor versions. Refer to the following diagrams:

![A diagram depicting The AWS Shared Responsibility Model for infrastructure services, container services, and abstracted services.](http://docs.aws.amazon.com/whitepapers/latest/swift-customer-security-controls-framework-2021/images/shared-responsibility-2.jpeg)

![A diagram depicting AWS/customer management plan.](http://docs.aws.amazon.com/whitepapers/latest/swift-customer-security-controls-framework-2021/images/aws-customer-management.jpeg)

 You are responsible for maintaining security updates for the EC2 instances in the SWIFT secure zone. You can opt to use immutable infrastructure and [blue/green deployment strategy](https://docs.aws.amazon.com/whitepapers/latest/overview-deployment-options/bluegreen-deployments.html) for deploying security updates for EC2 instances. In this topology, you would have a “golden” AMI pipeline to create the up-to-date operating system (OS) image, and another AMI pipeline to bundle the golden image with SWIFT applications and third-party libraries. The updated AMI is deployed and tested in the Dev / Test environment, and is subsequently promoted to the production environment. This testing and promotion process can be orchestrated in a pipeline created with AWS CodePipeline, or your existing CI / CD pipeline.

## System hardening
<a name="system-hardening"></a>

 Customers are responsible for maintaining the security configuration standards for their resources provisioned on AWS. These standards must be consistent with industry- accepted system hardening standards, and include the customer’s configuration of AWS services. AWS has published extensive security guides for the platform and individual services. The base set of these are:
+  [Center for Internet Security (CIS) Benchmark for AWS](https://www.cisecurity.org/benchmark/amazon_web_services/)
+  [CIS Benchmarks for EC2 instance types](https://docs.aws.amazon.com/inspector/latest/userguide/inspector_cis.html)
+  [AWS Trusted Advisor](https://aws.amazon.com/premiumsupport/trustedadvisor/)
+  [AWS Security Checklist](https://d1.awsstatic.com/whitepapers/Security/AWS_Security_Checklist.pdf)
+  [AWS Well-Architected Framework: Security Pillar](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/wellarchitected-security-pillar.pdf)

 There are various options to archive this control objective. For example, you can launch the pre-hardened EC2 instance using a [CIS-provided AMI in the AWS Marketplace](https://aws.amazon.com/marketplace/pp/B084Q6BF6K/?ef=_ptnr_cis_website&trk=el_a134p000006gAouAAE&trkCampaign=AWSMP_PDP_CIS_AmazonLinux22&sc_channel=el&sc_campaign=el_seller-led_programad&sc_outcome=Marketplace).

 Another option is to leverage the AMI pipeline to build the hardened EC2 AMI. If you are using EC2 Image Builder for the AMI pipeline, EC2 Image Builder provides [EC2 Image Builder STIG components](https://docs.aws.amazon.com/imagebuilder/latest/userguide/image-builder-stig.html) for EC2 hardening.

## Back-office data flow security
<a name="back-office-data-flow-security"></a>

 This control objective is similar to [Internal data flow security](#internal-data-flow-security), but this is an advisory control and primarily focuses on the edge connection to the secure zone. A backend payment application on-premises connecting to the Amazon MQ that resides in the SWIFT secure zone VPC is an example for such a connection. The principles and the requirements of the two controls are the same, so the guidance is the same as 2.1.

 If you use a hybrid architecture, such as one in which the back-office applications reside in an on-premises data center and the SWIFT secure zone is on AWS, consider using an internet protocol security (IPsec) VPN tunnel or Media Access control Security (MACsec) to encrypt the networking traffic in between. Refer to:
+  [AWS Site-to-Site VPN](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html)
+  [AWS Direct Connect MAC Security](https://docs.aws.amazon.com/directconnect/latest/UserGuide/direct-connect-mac-sec-getting-started.html)

 Besides encryption in transit using IPsec and MACsec, it is important to use Security Groups and Network ACLs (NACLs) to control the connection to the edge of the SWIFT secure zone. For example, if the entry point of the secure zone is Amazon MQ, the Security Group for Amazon MQ should allow incoming connections from the on- premises IP CIDR range, while other components in the secure zone should not allow incoming connection from the same range. NACLs can be applied in addition to Security Groups to provide an additional layer of access control.

## External transmission data protection
<a name="external-transmission-data-protection"></a>

 [AWS KMS](https://aws.amazon.com/kms/) is a managed service that makes it easy for you to create and control [AWS KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#master_keys) (CMKs), the encryption keys you can use to encrypt your data. AWS KMS CMKs are protected by hardware security modules (HSMs) that are validated by the [FIPS 140-2 Cryptographic Module Validation Program](https://csrc.nist.gov/projects/cryptographic-module-validation-program/Certificate/3139), except in the China (Beijing) and China (Ningxia) Regions.

 This control objective concerns the compromising of trusted backup data and loss of sensitive data confidentiality.

 In an AWS environment, data backup is automatically encrypted by the same Key Management Service (KMS) encryption key as your data store. For more information, refer to [Encryption for backups in AWS](https://docs.aws.amazon.com/aws-backup/latest/devguide/encryption.html). Encryption of the data stores in the SWIFT secure zone (such as RDS Oracle and EBS volumes) can satisfy this requirement.

## Operator session confidentiality and integrity
<a name="operator-session-confidentiality-and-integrity"></a>

 There are two aspects to consider for meeting control objectives:
+  Ensure access to the jump server / SWIFT component hosts are properly authenticated and encrypted.
+  Implement proper timeout / inactivity lockout on the operator sessions so it limits the minimal timeframe necessary to perform business-as-usual duties.

 When AWS Systems Manager Session Manager is used in place of the jump server for operator access, the first implementation guidance is satisfied. All AWS-provided services, including AWS Systems Manager Session Manager, require authentication, and the traffic is required to be encrypted using TLS. Choose one of the [options for logging session activity](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-logging.html) in your AWS account with the appropriate encryption mechanism enabled.

 In addition to providing information about current and completed sessions in the Systems Manager console, Session Manager provides you with options for logging session activity in your AWS account. This enables you to:
+  Create and store session logs for archival purposes.
+  Generate a report showing details of every connection made to your instances using Session Manager over the past 30 days.
+  Generate notifications of session activity in your AWS account, such as [Amazon Simple Notification Service](https://aws.amazon.com/sns/) (Amazon SNS) notifications.
+  Automatically initiate another action on an AWS resource as the result of session activity, such as running an [AWS Lambda](https://aws.amazon.com/lambda/) function, starting an AWS CodePipeline pipeline, or running an AWS Systems Manager Run Command document.

 AWS System Manager Session Manager supports idle session timeout. It enables you to specify the amount of time to allow a user to be inactive before a session ends. By default, sessions time out after 20 minutes of inactivity. You can modify this setting to specify that a session times out between one and 60 minutes of inactivity.

## Vulnerability scanning
<a name="vulnerability-scanning"></a>

 You can employ [Amazon Inspector](https://aws.amazon.com/inspector/) to help you achieve the vulnerability scanning control objective. Amazon Inspector is an automated security assessment service that helps improve the security and compliance of applications deployed on AWS. Amazon Inspector automatically assesses applications for exposure, vulnerabilities, and deviations from best practices. With Amazon Inspector, you can automate security vulnerability assessments throughout your development and deployment pipelines, or on EC2 instances. Amazon Inspector also offers an agent that you can install on Linux or Windows EC2 instances to scan for vulnerabilities. The Amazon Inspector agent also monitors the behavior of the EC2 instances, including network, file system, and process activity.

 In addition, there are many [AWS Partner solutions](https://aws.amazon.com/marketplace/solutions/security) available in this space which you can use.

## Application hardening
<a name="application-hardening"></a>

 Guidance for securing Messaging and Communication interfaces for SWIFT applications (AMH, SAA, SAG, SNL) are in SWIFT Knowledge Centers.
