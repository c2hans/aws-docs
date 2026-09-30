---
source_url: https://docs.aws.amazon.com/solutions/model-based-systems-engineering-on-aws/index.html
---

---
title: 'Guidance for Model-Based Systems Engineering on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/model-based-systems-engineering-on-aws/
source: aws-documentation
generated_on: 2026-09-30
---

# Guidance for Model-Based Systems Engineering on AWS

## Overview

This Guidance helps you accelerate your product development lifecycle by using AWS as the foundation for a model-based systems engineering (MBSE) approach to engineering and design. MBSE allows you to securely transform traditional document-based engineering environments to a modern model-based cloud computing platform. This multi-disciplinary and multi-application model helps aerospace companies adopt agile product development practices, connect with other aerospace teams across the globe, and gain the the support they need at every stage of MBSE adoption and automation.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/model-based-systems-engineering-on-aws.pdf)

![Architecture diagram](/images/solutions/model-based-systems-engineering-on-aws/images/model-based-systems-engineering-on-aws-1.png)

1. **Step 1**: Use AWS CloudFormation to deploy Scale-Out-Computing on AWS (SOCA) and build a centralized engineering environment (e.g., high-performance computing [HPC] and virtual desktop infrastructure [VDI]), where you can deploy MBSE tool. Bring your own MBSE tools, or find them on AWS Marketplace. (Option A.)
1. **Step 2**: Use Amazon AppStream 2.0 for non-persistent VDI or Amazon Workspaces for persistent VDI to access MBSE tool. Bring your own MBSE tools, or find them on AWS Marketplace. (Option B.)
1. **Step 3**: Use AWS IoT TwinMaker to create digital twins along with MBSE.
1. **Step 4**: Amazon API Gateway is the center of communications among applications and environments. API-based microservices integrate new technologies and complementary services. AWS AppSync is also an applicable option.
1. **Step 5**: Use Amazon EventBridge to trigger workflows based on all events, including MBSE.
1. **Step 6**: Amazon Simple Queue Service (Amazon SQS) ensures the message is processed. AWS Step Functions builds state machine-based workflows executed by AWS Lambda functions.
1. **Step 7**: Based on workflow selection, compute instances create ephemeral simulations; Amazon DynamoDB tables track engineering activities; Amazon Simple Storage Service (Amazon S3) stores objects (output files) in the bucket; and Amazon Simple Notification Service (Amazon SNS) performs team communications.
1. **Step 8**: Store engineering documents and objects in a centralized data lake.
1. **Step 9**: Amazon Textract and Amazon Comprehend extract text from documents. Amazon OpenSearch Service unlocks insights. AWS Glue crawls and catalogs data for engineering use cases. Amazon Neptune creates ontology and multi-domain relationship knowledge graphs for artifacts and users.
1. **Step 10**: Artifact store, comprising Amazon OpenSearch Service, AWS Glue Data Catalog, and Amazon Neptune, feeds data back to MBSE tools on AWS via Amazon API Gateway.
1. **Step 11**: Amazon Elastic Compute Cloud (Amazon EC2) Auto Scaling, Amazon Elastic Load Balancing (ELB), Amazon Elastic Block Store (Amazon EBS), and Amazon EC2 deliver connectivity of heterogeneous enterprise apps and associated data models across design and operational environments.
1. **Step 12**: AWS provides lifecycle governance controls for permissioning, monitoring, and responding. To enable data supply for the US Government, reference Cross-Domain Solutions with AWS.
1. **Step 13**: AWS CodePipeline automates DevSecOps for continuous integration and continuous development (CI/CD) in MBSE workflows and operations.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

Whether you are just starting out with MSBE as a tool or putting MSBE at the center of your enterprise strategy, this architecture provides the flexibility for you to get started. You can use Option A to incorporate MSBE into your existing environment or use tools like SOCA to centralize MSBE. The services in this architecture and the data lake approach enable centralized management and visibility for IT and security teams. Additionally, the architecture uses data analytics services to generate insights for engineering teams, so they can forecast how changes will impact larger systems. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

This architecture uses AWS Identity and Access Management (IAM) and Amazon CloudWatch to protect data. IAM provides role-based access control, giving data access privileges to only the roles that need it. With CloudWatch, you can set up metrics to monitor application activity from multiple AWS accounts within a Region. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

This architecture uses a microservices approach, which decouples services for a particular engineering function from services that support a different engineering function. By decoupling these services, you can experiment with new technologies for one function without altering the operability of other functions. The services in the Human-Machine Engineering Workflow capture, document, and respond to all events, maintaining a single “source of truth” for all event-based activity and communications. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

The services in this architecture allow for data interoperability across multiple stages of the data lifecycle. The AWS Management Console gives you visibility into data access patterns of your data, such as requests or changes to data and velocity or size of data. You can then build business logic based on traffic patterns and execute the logic with extensible APIs. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

This architecture uses cost-saving features such as automation through CodePipeline, scalability through Amazon S3, and centralized administration through AWS Organizations. These features allow for early detection and correction of defects in the design process, which reduces total development costs and schedule overruns. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

This architecture uses services that scale resources up and down based on usage. These services help monitor the throughput of the file system and dynamically adjust the throughput mode to “provisioned” or “bursting” to maximize resource optimization. With the “Detective” services in this architecture, you can visualize productivity metrics, emissions, or cost-out targets through dashboards and adjust business priorities to meet target metrics for sustainability. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

## Related content

- **Computational Fluid Dynamics on AWS**: The scalable nature and variable demand of computational fluid dynamics (CFD) workloads makes them well suited for a cloud computing environment. This whitepaper describes best practices for running CFD workloads on Amazon Web Services (AWS).

[Learn more](/whitepapers/latest/computational-fluid-dynamics-on-aws/computational-fluid-dynamics-on-aws.html)

- **DoD-Compliant Implementations in AWS**: This whitepaper provides security best practices and architectural recommendations that can help you properly design and deploy DoD-compliant infrastructure to host your mission applications and protect your data and assets in the AWS Cloud.

[Learn more](https://d1.awsstatic.com/whitepapers/compliance/AWS_DOD_CSM_Reference_Architecture.pdf)

- **Model Based Systems Engineering (MBSE) on AWS: From Migration to Innovation**: Model Based Systems Engineering (MBSE) is a modern approach to the conventional practice of document-based systems engineering. This whitepaper addresses both MBSE developers who develop MBSE technologies and MBSE users who use MBSE tools.

[Learn more](/whitepapers/latest/model-based-systems-engineering/model-based-systems-engineering.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
