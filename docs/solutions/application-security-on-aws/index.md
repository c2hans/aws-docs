---
source_url: https://docs.aws.amazon.com/solutions/application-security-on-aws/index.html
---

---
title: 'Guidance for Application Security on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/application-security-on-aws/
source: aws-documentation
generated_on: 2026-10-07
---

# Guidance for Application Security on AWS

Enhance application security and catch security vulnerabilities through integrated security automation

## Overview

This Guidance shows how to build a strong application security capability on AWS. Application security helps you address application-level threats, like unauthorized access and privilege escalation. By using the AWS security services in this Guidance, you can log application security, protect and manage your resources, and detect anomalous behavior in client interactions with your application.

## How it works

This architecture diagram shows how to integrate AWS security services to protect and manage your cloud resources and log application security as you build a reliable, secure, and scalable cloud environment.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/application-security-on-aws.pdf)

![Architecture diagram](/images/solutions/application-security-on-aws/images/application-security-on-aws-1.png)

1. **Step 1**: Within AWS Organizations, enable Amazon GuardDuty, Amazon Inspector, AWS Security Hub, Amazon Macie, and Amazon Detective for your home and operational AWS Regions.
1. **Step 2**: Set up GuardDuty for threat monitoring and Amazon Inspector for automated vulnerability scanning of Amazon Elastic Compute Cloud (Amazon EC2) instances, Amazon Elastic Container Registry (Amazon ECR) images, and AWS Lambda functions.
1. **Step 3**: Configure Security Hub in your home and operational Regions to centralize security incidents within your AWS environment and maintain compliance with industry standards and best practices.
1. **Step 4**: Enable and configure Macie in your home and operational Regions to identify sensitive data.
1. **Step 5**: Enable and configure Detective in your home and operational Regions to streamline security analysis and conduct efficient security investigations.
1. **Step 6**: Provide security teams with least privilege access to security services and the AWS environment using a federated solution. Review AWS Identity and Access Management (IAM) access using IAM Access Analyzer. Forward findings to Security Hub.
1. **Step 7**: Use AWS Certificate Manager to provision and manage SSL or TLS certificates. Use AWS Key Management Service (AWS KMS) to manage keys associated with application resources.
1. **Step 8**: Use AWS Secrets Manager to securely store and manage credentials such as database logins, API keys, and other secrets.
1. **Step 9**: Send application security logs to a centralized log storage bucket for compliance retention and analysis.
## Additional Considerations

### What is Application Security?

Application Security describes the security measures used at the application level to protect data or code within the app from being stolen or hijacked. It includes security concerns during application development and design, but it also includes methods and procedures to safeguard apps after they are launched. Application security should be applied at all stages of development, including design, development, and deployment.

### Monitoring and updating

Application Security not only emphasizes preventing vulnerabilities and threats in software applications but also stresses the importance of constant monitoring and updating to address new challenges and threats as they emerge. Regular security assessments, including code reviews, penetration testing, and the use of automated security tools, play a crucial role in identifying and mitigating potential security issues before they can be exploited.

[Read usage guidelines](/solutions/guidance-disclaimers/)
