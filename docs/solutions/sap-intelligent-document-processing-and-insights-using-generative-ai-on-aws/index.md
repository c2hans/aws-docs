---
source_url: https://docs.aws.amazon.com/solutions/sap-intelligent-document-processing-and-insights-using-generative-ai-on-aws/index.html
---

---
title: 'Guidance for SAP Intelligent Document Processing and Insights using Generative AI on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/sap-intelligent-document-processing-and-insights-using-generative-ai-on-aws/
source: aws-documentation
generated_on: 2026-10-01
---

# Guidance for SAP Intelligent Document Processing and Insights using Generative AI on AWS

## Overview

This Guidance demonstrates how to automate unstructured document processing and subsequent auditing and analysis using AWS AI/ML and generative AI Services. It includes Amazon Textract to extract, classify, and process documents, AWS SDK for SAP ABAP for SAP Clean Core extensions, and Amazon Bedrock to build smart audit chatbot assistants to build audit summaries and to improve business user productivity. This Guidance is designed to be extensible, allowing you to seamlessly incorporate additional components or integrate with other AWS services.

## How it works

### SAP in-stack extensions

This architecture diagram shows how to build SAP in-stack extensions and intelligently process your documents to streamline your SAP business process using AI/ML and generative AI services.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/sap-intelligent-document-processing-and-insights-using-generative-ai-on-aws.pdf)Step 1Documents can be sourced from various channels. Users can upload through mobile clients to the frontend application, an Integration Platform as a Service (iPaaS), or content servers that can directly integrate through a batch process.Step 2Users manage document processing through the Fiori front-end server.Step 3The Fiori application calls the AWS SDK for SAP ABAP, orchestrating the calls to AWS services natively for processing. AWS Security Token Service (AWS STS) is used to generate temporary security credentials, helping ensure secure access and interactions between the application, users, and AWS services.Step 4Amazon Simple Storage Service (Amazon S3) is used for storing the documents being processed and managed within the workflow.Step 5Amazon Textract extracts information from documents using pre-trained AI/ML models.Step 6Amazon Translate is used to enable translations.Step 7The processed documents are stored in the SAP HANA database using SAP APIs.Step 8Amazon Simple Notification Service (Amazon SNS) is used to send notifications and updates related to the document processing activities.Step 9Amazon Bedrock provides a secure and scalable environment to build auditing knowledge bases based on data in Amazon S3, using the large language model (LLM), a foundation model (FM), and retrieval-augmented generation features.Step 10The audit assistant uses the knowledge base built on Amazon Bedrock to perform intelligent auditing of the processed documents and associated activities.### SAP side-by-side extensions

This architecture diagram shows how to build external SAP extensions to intelligently process your documents.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/sap-intelligent-document-processing-and-insights-using-generative-ai-on-aws.pdf)Step 1Documents can be sourced from various channels. Users can upload through mobile clients to the frontend application, or iPaaS can directly integrate using the SAP Cloud Application Programming (CAP) model application for batch processing.Step 2Users manage document processing through the Fiori front-end server.Step 3The CAP extension application is built on the SAP Business Technology Platform (BTP). It serves OData API which receives documents from sources and orchestrates the calls to AWS services natively using AWS SDK for JAVA for processing. AWS STS is used to generate temporary security credentials for secure access and interactions between the application, users, and AWS services.Step 4Amazon S3 is used for storing the documents being processed and managed within the workflow.Step 5Amazon Textract extracts information from documents using pre-trained AI/ML models.Step 6Amazon Translate is used to enable translations.Step 7The processed documents are posted from the CAP application to SAP ECC/S/4HANA through SAP APIs.Step 8Amazon SNS is used to send notifications and updates related to the document processing activities.Step 9Amazon Bedrock provides a secure and scalable environment to build auditing knowledge bases based on data in Amazon S3, using the large language model (LLM) and retrieval-augmented generation (RAG) features.Step 10The audit assistant uses the knowledge base built on Amazon Bedrock to perform intelligent auditing of the processed documents and associated activities.## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-sap-intelligent-document-processing-and-insights-using-generative-ai-on-aws)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

Amazon CloudWatch and AWS CloudTrail provide monitoring and logging capabilities so you can detect and respond to performance issues, security threats, and configuration changes. For example, CloudWatch monitors application performance and resource utilization, while CloudTrail tracks API calls and resource changes, providing a complete audit trail. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

AWS provides a range of security services to help you secure your AWS resources and data. AWS Identity and Access Management (IAM) offers least privilege access and key management capabilities so only authorized users and applications can interact with your AWS resources. Amazon S3 bucket policies and access control lists (ACLs) further control access to Amazon S3 buckets and objects, enforce data encryption, and block public access. Additionally, AWS Config provides a resource inventory, configuration history, and compliance reports to help track and manage security best practices. When integrating SAP data with Amazon Bedrock, it is important to implement appropriate security measures. This includes using IAM roles and permissions to restrict access to AWS resources based on the principle of least privilege. Additionally, Amazon S3 bucket policies and ACLs should be used to control access to any sensitive SAP data stored in Amazon S3. Finally, ongoing monitoring and management of resource configurations using AWS Config can help ensure the security posture is maintained over time. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Amazon Textract, Amazon Bedrock, and Amazon S3 have built-in redundancy and fault tolerance across multiple Availability Zones (AZs), where high availability is achieved without the need for manual configuration or additional infrastructure. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Amazon Textract offers document extraction capabilities using pre-built machine learning models to extract information from invoices and other documents. Amazon Bedrock further allows the use of large-scale machine learning models to enhance the performance and accuracy of applications. Amazon S3, a highly scalable and durable object storage service, facilitates efficient storage and retrieval of data, enabling applications to quickly and reliably access the information they require. Additionally, Amazon Translate, a neural language translation service, offers the capability to reliably translate documents with a high degree of accuracy. Notably, these AWS services are all serverless in nature, automatically scaling to accommodate fluctuations in workload demand. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

The AWS services featured in this Guidance, including Amazon Textract, Amazon Translate, Amazon Bedrock, and Amazon S3, are designed to deliver scalable and efficient approaches for your workloads while minimizing operational costs. Specifically, Amazon Textract enables cost-effective intelligent document processing by allowing extraction of information from documents using pre-built LLM models, while Amazon S3 offers highly scalable and durable object storage with pay-as-you-go pricing. Amazon Translate facilitates multilingual applications at scale, and Amazon Bedrock enables the construction of cost-effective RAG workflows. You can further optimize costs by using the serverless nature of these services, using the lifecycle policies in Amazon S3, and monitoring usage with AWS Cost Explorer and CloudWatch. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

The AWS services featured in this Guidance all contribute to sustainability by optimizing resource usage and reducing environmental impact. For instance, Amazon Bedrock, a fully managed service that offers a range of foundation models, helps you to develop advanced AI models with reduced computational requirements, leading to improved energy efficiency. Amazon S3 promotes efficient data storage and management, reducing the need for physical data centers and associated energy usage. Additionally, Amazon Athena facilitates data analysis without the need for resource-intensive data warehousing for efficient use of your cloud-based resources. Furthermore, the cloud-native, serverless architecture of these services eliminates the need for resource provisioning and reduces energy consumption. Lastly, the use of Amazon S3 for durable and highly available data storage helps minimize e-waste by reducing the need for redundant storage. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
