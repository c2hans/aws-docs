---
source_url: https://docs.aws.amazon.com/whitepapers/latest/security-at-the-edge/appendix-aws-services-for-edge-computing.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Appendix: AWS services for edge computing
<a name="appendix-aws-services-for-edge-computing"></a>

 This appendix provides additional information on the AWS services described in the paper. Further detail can also be found at the AWS websites provided.

## Edge services
<a name="edge-services"></a>

### Amazon CloudFront
<a name="amazon-cloudfront"></a>

 [Amazon CloudFront](https://aws.amazon.com/cloudfront/) is a fast content delivery network (CDN) service that securely delivers data, videos, applications, and APIs to customers globally with low latency, high transfer speeds, all within a developer-friendly environment.

 Amazon CloudFront offers the most advanced security capabilities, including field level encryption and HTTPS support, seamlessly running with [AWS Shield](https://aws.amazon.com/shield/), [AWS Web Application Firewall](https://aws.amazon.com/waf/), and [Amazon Route 53](https://aws.amazon.com/route53/) to protect against multiple types of attacks, including network and application layer DDoS attacks. These services co-reside at AWS edge locations – globally scaled and connected via the AWS network backbone – providing a more secure, performant, and available experience for your users.

### FreeRTOS
<a name="freertos"></a>

 [FreeRTOS](https://aws.amazon.com/freertos/) is an open source, real-time operating system for microcontrollers that makes small, low-power edge devices easy to program, deploy, secure, connect, and manage. Distributed freely under the MIT open-source license, FreeRTOS includes a kernel and a growing set of software libraries suitable for use across industry sectors and applications. This includes securely connecting your small, low-power devices to AWS Cloud services like [AWS IoT Core](https://aws.amazon.com/iot-core/), or to more powerful edge devices running [AWS IoT Greengrass](https://aws.amazon.com/greengrass/).

### AWS IoT Greengrass
<a name="aws-iot-greengrass"></a>

 [AWS IoT Greengrass](https://aws.amazon.com/greengrass/) is an IoT open-source edge runtime and cloud service that helps you build, deploy, and manage device software. Customers use AWS IoT Greengrass for their IoT applications on millions of devices in homes, factories, vehicles, and businesses. You can program your devices to act locally on the data they generate, make predictions based on ML models, filter and aggregate device data, and transmit only necessary information to the cloud.

### AWS Snow Family
<a name="aws-snow-family"></a>

 The [AWS Snow Family](https://aws.amazon.com/snow/) helps customers that need to run operations in austere, non-data center environments, and in locations where there's a lack of consistent network connectivity. The AWS Snow Family, comprised of [AWS Snowcone,](https://aws.amazon.com/snowcone/) [AWS Snowball Edge](https://aws.amazon.com/snowball/), and [AWS Snowmobile](https://aws.amazon.com/snowmobile/), offers a number of physical devices and capacity points, most with built-in computing capabilities. These services help physically transport up to exabytes of data into and out of AWS. AWS Snow Family devices are owned and managed by AWS and integrate with AWS security, monitoring, storage management, and computing capabilities.

### AWS Storage Gateway
<a name="aws-storage-gateway"></a>

 [AWS Storage Gateway](https://aws.amazon.com/storagegateway/) is a hybrid cloud storage service that gives you on-premises access to virtually unlimited cloud storage. Customers use AWS Storage Gateway to simplify storage management and reduce costs for key hybrid cloud storage use cases. These include moving backups to the cloud, using on-premises file shares backed by cloud storage, and providing low latency access to data in AWS for on-premises applications.

### AWS Outposts
<a name="aws-outposts"></a>

 [AWS Outposts](https://aws.amazon.com/outposts/) is a fully managed service that offers the same AWS infrastructure, AWS services, APIs, and tools to virtually any data center, co-location space, or on-premises facility for a truly consistent hybrid experience. AWS Outposts is ideal for workloads that require low latency access to on-premises systems, local data processing, data residency, and migration of applications with local system interdependencies.

### AWS Wavelength
<a name="aws-wavelength"></a>

 [AWS Wavelength](https://aws.amazon.com/wavelength/) is an AWS Infrastructure offering optimized for mobile edge computing applications. [Wavelength Zones](https://docs.aws.amazon.com/wavelength/latest/developerguide/wavelength-quotas.html#concepts-available-zones) are AWS infrastructure deployments that embed AWS compute and storage services within communications service providers’ (CSP) data centers at the edge of the 5G network, so application traffic from 5G devices can reach application servers running in Wavelength Zones without leaving the telecommunications network.

## AWS services that support security at the edge
<a name="aws-services-that-support-security-at-the-edge"></a>

### Amazon API Gateway
<a name="amazon-api-gateway"></a>

 [Amazon API Gateway](https://aws.amazon.com/api-gateway/) is a fully managed service that makes it easy for developers to publish, maintain, monitor, secure, and operate APIs at any scale. It’s a pay-as-you-go service that takes care of all of the undifferentiated heavy lifting involved in securely and reliably running APIs at scale.

### AWS Certificate Manager
<a name="aws-certificate-manager"></a>

 [AWS Certificate Manager](https://aws.amazon.com/certificate-manager/) enables you to easily provision, manage, and deploy public and private Secure Sockets Layer/Transport Layer Security (SSL/TLS) certificates for use with AWS services and your internal connected resources. SSL/TLS certificates are used to secure network communications and establish the identity of websites over the internet as well as resources on private networks. AWS Certificate Manager removes the time-consuming manual process of purchasing, uploading, and renewing SSL/TLS certificates.

### AWS CloudHSM
<a name="aws-cloudhsm"></a>

 [AWS CloudHSM](https://aws.amazon.com/cloudhsm/) is a cloud-based hardware security module (HSM) that enables you to easily generate and use your own encryption keys on the AWS Cloud. With CloudHSM, you can manage your own encryption keys using FIPS 140-2 Level 3 validated HSMs.

### AWS CloudTrail
<a name="aws-cloudtrail"></a>

 [AWS CloudTrail](https://aws.amazon.com/cloudtrail/) enables governance, compliance, operational auditing, and risk auditing of your AWS account. With AWS CloudTrail, you can log, continuously monitor, and retain account activity related to actions across your AWS infrastructure. AWS CloudTrail provides event history of your AWS account activity, including actions taken through the [AWS Management Console](https://aws.amazon.com/console/), [AWS SDKs](https://aws.amazon.com/tools/), command line tools, and other AWS services. This event history simplifies security analysis, resource change tracking, and troubleshooting. In addition, you can use AWS CloudTrail to detect unusual activity in your AWS accounts. These capabilities help simplify operational analysis and troubleshooting.

### Amazon Cognito
<a name="amazon-cognito"></a>

 [Amazon Cognito](https://aws.amazon.com/cognito/) is an access control service that enables you to add user sign-up, sign-in, and access control to your web and mobile apps quickly and easily. Amazon Cognito scales to millions of users and supports sign-in with social identity providers, such as Apple, Facebook, Google, and Amazon, and enterprise identity providers via SAML 2.0 and OpenID Connect.

### AWS Config
<a name="aws-config"></a>

 [AWS Config](https://aws.amazon.com/config/?c=sc&sec=srv) enables you to assess, audit, and evaluate the configurations of your AWS resources. AWS Config continuously monitors and records your AWS resource configurations and allows you to automate the evaluation of recorded configurations against desired configurations.

### Amazon Detective
<a name="amazon-detective"></a>

 [Amazon Detective](https://aws.amazon.com/detective/) makes it easy to analyze, investigate, and quickly identify the root cause of potential security issues or suspicious activities. Amazon Detective automatically collects log data from your AWS resources and uses ML, statistical analysis, and graph theory to build a linked set of data that enables you to easily conduct faster and more efficient security investigations.

### AWS Firewall Manager
<a name="aws-firewall-manager"></a>

 [AWS Firewall Manager](https://aws.amazon.com/firewall-manager/) is a security management service that enables you to centrally configure and manage firewall rules across your accounts and applications in [AWS Organizations](https://aws.amazon.com/organizations/). As new applications are created, Firewall Manager makes it easy to bring new applications and resources into compliance by enforcing a common set of security rules. This single service can build firewall rules, create security policies, and enforce them in a consistent, hierarchical manner across your entire infrastructure, from a central administrator account.

### AWS Global Accelerator
<a name="aws-global-accelerator"></a>

 [AWS Global Accelerator](https://aws.amazon.com/global-accelerator/?blogs-global-accelerator.sort-by=item.additionalFields.createdDate&blogs-global-accelerator.sort-order=desc&aws-global-accelerator-wn.sort-by=item.additionalFields.postDateTime&aws-global-accelerator-wn.sort-order=desc) is a networking service that sends your user’s traffic through the AWS global network infrastructure, improving your internet user performance by up to 60%. When the internet is congested, the AWS Global Accelerator automatic routing optimizations helps keep your packet loss, jitter, and latency consistently low.

### Amazon GuardDuty
<a name="amazon-guardduty"></a>

 [Amazon GuardDuty](https://aws.amazon.com/guardduty/) is a threat detection service that continuously monitors for malicious activity and unauthorized behavior to protect your AWS accounts, workloads, and data stored in S3. With the cloud, the collection and aggregation of account and network activities is simplified, but it can be time consuming for security teams to continuously analyze event log data for potential threats. With GuardDuty, you now have an intelligent and cost-effective option for continuous threat detection in AWS. The service uses ML, anomaly detection, and integrated threat intelligence to identify and prioritize potential threats.

### AWS Identity and Access Management
<a name="aws-identity-and-access-management"></a>

 [AWS Identity and Access Management](https://aws.amazon.com/iam/) (IAM) enables you to manage access to AWS services and resources securely. Using AWS IAM, you can create and manage AWS users and groups, and use permissions to allow and deny their access to AWS resources. AWS IAM is a feature of your AWS account offered at no additional charge. You will be charged only for use of other AWS services by your users.

### AWS Key Management Service
<a name="aws-key-management-service"></a>

 [AWS Key Management Service](https://aws.amazon.com/kms/) (KMS) makes it easy for you to create and manage cryptographic keys and control their use across a wide range of AWS services and in your applications. AWS KMS is a secure and resilient service that uses hardware security modules that have been validated under FIPS 140-2, or are in the process of being validated, to protect your keys. AWS KMS runs with [AWS CloudTrail](https://aws.amazon.com/cloudtrail/) to provide you with logs of all key usage to help meet your regulatory and compliance needs.

### Amazon Macie
<a name="amazon-macie"></a>

 [Amazon Macie](https://aws.amazon.com/macie/) is a fully managed data security and data privacy service that uses ML and pattern matching to discover and protect your sensitive data in AWS.

### AWS Network Firewall
<a name="aws-network-firewall"></a>

 [AWS Network Firewall](https://aws.amazon.com/network-firewall/?whats-new-cards.sort-by=item.additionalFields.postDateTime&whats-new-cards.sort-order=desc) is a managed service that makes it easy to deploy essential network protections for all of your [Amazon Virtual Private Clouds](https://aws.amazon.com/vpc/) (VPCs). The service can be set up with just a few clicks and scales automatically with your network traffic, so you don't have to worry about deploying and managing any infrastructure.

 The AWS Network Firewall flexible rules engine enables you to define firewall rules that give you fine-grained control over network traffic, such as blocking outbound Server Message Block (SMB) requests to prevent the spread of malicious activity. You can also import rules you’ve already written in common open-source rule formats as well as enable integrations with managed intelligence feeds sourced by AWS Partners.

### Amazon Route 53
<a name="amazon-route-53"></a>

 [Amazon Route 53](https://aws.amazon.com/route53/) is a highly available and scalable cloud Domain Name System (DNS) web service. It is designed to give developers and businesses an extremely reliable and cost-effective way to route end users to internet applications by translating names such as “www.example.com” into the numeric IP addresses, such as 192.0.2.1, that computers use to connect to each other. Route 53 is fully compliant with IPv6 as well.

 Amazon Route 53 effectively connects user requests to infrastructure running in AWS, such as Amazon EC2 instances, Elastic Load Balancing load balancers, or S3 buckets, and can be used to route users to infrastructure outside of AWS. You can use Amazon Route 53 to configure DNS health checks to route traffic to healthy endpoints or to independently monitor the health of your application and its endpoints.

### AWS Shield Advanced
<a name="aws-shield-advanced"></a>

 [AWS Shield Advanced](https://aws.amazon.com/shield/) is a managed service that builds a customized DDoS protection capability specifically for your applications needs. You receive tailored detection based on the specific traffic patterns of your application, protection against Layer 7 DDoS attacks including AWS WAF at no additional cost, access to 24x7 specialized support from the AWS Shield Response Team (SRT), centralized management of security policies through AWS Firewall Manager, and cost protection to safeguard against scaling charges resulting from DDoS-related usage spikes. For more information on Shield Advanced, see [AWS Shield Advanced documentation](https://docs.aws.amazon.com/waf/latest/developerguide/getting-started-ddos.html).

 **AWS WAF**

 [AWS WAF](https://aws.amazon.com/waf/) is a web application firewall that helps protect your web applications or APIs against common web exploits that may affect availability, compromise security, or consume excessive resources. AWS WAF gives you control over how traffic reaches your applications by enabling you to create security rules that block common attack patterns, such as SQL injection or cross-site scripting, and rules that filter out specific traffic patterns you define.

 You can get started quickly using [Managed Rules for AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups.html), a pre-configured set of rules managed by AWS or AWS Marketplace Sellers. The Managed Rules for AWS WAF address issues like the OWASP Top 10 security risks. These rules are regularly updated as new issues emerge. AWS WAF includes a full-featured API that you can use to automate the creation, deployment, and maintenance of security rules.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
