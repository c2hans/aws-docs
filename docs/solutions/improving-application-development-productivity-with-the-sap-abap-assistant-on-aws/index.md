---
source_url: https://docs.aws.amazon.com/solutions/improving-application-development-productivity-with-the-sap-abap-assistant-on-aws/index.html
---

---
title: 'Guidance for Improving Application Development Productivity with the SAP ABAP Assistant on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/improving-application-development-productivity-with-the-sap-abap-assistant-on-aws/
source: aws-documentation
generated_on: 2026-10-07
---

# Guidance for Improving Application Development Productivity with the SAP ABAP Assistant on AWS

## Overview

This Guidance demonstrates how to set up the SAP Advanced Business Application Programming (ABAP) Assistant, a plugin that integrates with Amazon Bedrock in the Eclipse integrated development environment (IDE). The SAP ABAP Assistant serves two primary functions: generating SAP ABAP code from natural language comments and creating natural language documentation from existing SAP ABAP code. The SAP ABAP Assistant aids developers in overcoming the difficulties of analyzing SAP ABAP code due to insufficient documentation and development resources. It accelerates the S/4HANA transformation journey by facilitating the understanding of existing custom ABAP code for both RISE with SAP and traditional license models. This analysis can help in refactoring the code into cloud-native extensions on the SAP Business Technology Platform (SAP BTP), adhering to the clean core principle for a future-proof and extensible SAP landscape. This Guidance provides instructions for using the SAP ABAP Assistant and can be adapted to include additional Amazon Bedrock models or custom logic as needed.

## How it works

### ABAP Assistant with AWS IAM Identity Center

This architecture diagram shows how SAP ABAP developers can improve their productivity by using the SAP ABAP Assistant in conjunction with Amazon Bedrock and AWS IAM Identity Center to generate SAP ABAP code and documentation.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/improving-application-development-productivity-with-the-sap-abap-assistant-on-aws.pdf#page=1)Step 1The SAP ABAP developer installs AWS Command Line Interface (AWS CLI) version 2 on either a Windows or Mac operating system. Additionally, the developer configures the AWS CLI to authenticate with the AWS IAM Identity Center using the aws configure sso command.Step 2With the AWS CLI, the developer authenticates with the IAM Identity Center by running the aws sso login --profile <profile-name> command.

Step 3The developer downloads the provided SAP ABAP Assistant plugin, installs it, and then configures the plugin within the Eclipse integrated development environment (IDE).Step 4The developer must authenticate and establish connections between the Eclipse IDE and one or more SAP systems that are hosted either within an Amazon Virtual Private Cloud (Amazon VPC), on-premises, or in the SAP Business Technology Platform (BTP) ABAP environment.
Within the Eclipse IDE, the developer opens an ABAP program and selects a specific block of ABAP code for which documentation needs to be generated. To initiate the code generation process, the developer writes a prompt in simple English within the ABAP program. The developer then invokes the SAP ABAP Assistant plugin using the "Ask Bedrock" menu option available in the Eclipse IDE.Step 5The SAP ABAP Assistant plugin sends a request with the selected prompts or ABAP code to Amazon Bedrock, a fully managed service that offers a choice of high-performing foundation models. Amazon Bedrock then uses large language models (LLMs), such as the Anthropic Claude model, to generate the corresponding ABAP code or documentation.Step 6The SAP ABAP Assistant plugin returns the generated response back to the ABAP editor in the case of code generation and displays the generated documentation within the console of the Eclipse IDE. The developer is then responsible for validating the generated code and, if necessary, modifying it to align with the specific use case requirements.### ABAP Assistant with IAM Roles Anywhere

This architecture diagram shows how SAP ABAP developers can improve their productivity by using the SAP ABAP Assistant in conjunction with Amazon Bedrock and AWS IAM Roles Anywhere to generate SAP ABAP code and documentation.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/improving-application-development-productivity-with-the-sap-abap-assistant-on-aws.pdf#page=2)Step 1The SAP ABAP developer downloads the provided SAP ABAP Assistant plugin, then installs and configures the plugin in Eclipse IDE.Step 2The SAP ABAP developer authenticates and connects one or more SAP systems hosted in Amazon VPC, on-premises, or the SAP Business Technology Platform (BTP) ABAP environment to Eclipse IDE. The developer opens an ABAP program in Eclipse IDE and selects a block of ABAP code for which the documentation has to be generated. For code generation, the developer writes a prompt in simple English in the ABAP program. The developer invokes SAP ABAP Assistant plugin using the "Ask Bedrock" menu in Eclipse IDE.Step 3The SAP ABAP Assistant plugin sends a request to AWS Identity and Access Management (IAM) Roles Anywhere to generate temporary credentials using X.509 certificate issued by AWS Private Certificate Authority (AWS Private CA).Step 3aIAM Roles Anywhere works by bridging the trust model of AWS Identity and Access Management (IAM) and public key infrastructure (PKI). The model connects the role, the IAM Roles Anywhere service principal, and identities encoded in X.509 certificates, that are issued by a certificate authority.Step 4The SAP ABAP Assistant plugin sends a request with the selected prompts or ABAP code to Amazon Bedrock to call LLMs hosted by Amazon Bedrock, such as the Anthropic Claude model to produce ABAP code or documentation.Step 5The SAP ABAP Assistant plugin returns the response back to the ABAP editor in case of code generation or displays documentation in a console in Eclipse IDE. The developer will validate the generated code and, if required, modify it to the specific use case.## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Deploy this Guidance**: Use sample code to deploy this Guidance in your AWS account

[Sample code](https://github.com/aws-solutions-library-samples/guidance-for-improving-application-development-productivity-with-the-sap-abap-assistant-on-aws)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

AWS CloudFormation allows developers to define infrastructure and application resources as code, reducing manual errors and helping to ensure consistent deployment across different environments. Amazon CloudWatch Logs capture and store API requests from Amazon Bedrock, providing a searchable record of the full request and response data without requiring additional infrastructure. These services streamline resource management, minimize human error, and offer comprehensive logging capabilities, contributing to improved operational efficiency and reliability in the SAP ABAP development process. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

IAM Identity Center offers centralized identity management and granular access control. Since the code runs locally, IAM Identity Center authentication is used to provide AWS credentials. In addition, the AWS Identity and Access Management (IAM) policies in the permission set offer fine-grained permissions, allowing administrators to precisely control user access to AWS resources. This approach helps ensure that users have only the necessary permissions to perform their tasks, adhering to the principle of least privilege and strengthening the overall security posture of the SAP ABAP development environment. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Amazon Bedrock is a fully managed and serverless AWS service deployed across multiple Availability Zones by default. Its serverless architecture allows Amazon Bedrock to automatically scale up or down based on demand, supporting consistent performance regardless of workload fluctuations. Moreover, Amazon Bedrock inherits the high availability and fault tolerance features of the underlying AWS infrastructure. This design eliminates the need for manual scaling or infrastructure management, providing developers with a robust and resilient foundation for their SAP ABAP development tasks, even during periods of high demand or in the event of isolated failures. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Amazon Bedrock provides developers access to high-performing foundation models through a single API; developers can evaluate and select the best-fit foundation model for their specific requirements, supporting optimal performance for the application. By offering a range of models and simplifying the selection process, Amazon Bedrock allows developers to efficiently implement and fine-tune artificial intelligence (AI) capabilities in their SAP ABAP projects, leading to faster development cycles and improved application performance. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Amazon Bedrock offers a flexible, pay-as-you-go pricing model without long-term commitments or upfront investments, allowing developers to select the pricing option that aligns best with their usage patterns and budgets. Amazon Bedrock also streamlines cost management by charging only for the resources actually consumed and the number of input and output tokens processed by the foundation models. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Amazon Bedrock uses the energy-efficient infrastructure and data centers of the AWS Cloud. As a fully managed service, Amazon Bedrock eliminates the need for developers to provision and manage their own infrastructure, reducing the energy consumption and carbon footprint associated with running and maintaining physical servers. With the sustainable AWS infrastructure, developers have access to the innovative AI capabilities of Amazon Bedrock while minimizing their environmental impact. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
