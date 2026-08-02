---
source_url: https://docs.aws.amazon.com/solutions/multimodal-data-processing-using-amazon-bedrock-data-automation/index.html
---

# Guidance for Multimodal Data Processing Using Amazon Bedrock Data Automation

Simplify data extraction and process automation across multimodal data-centric workflows, including Intelligent Document Processing (IDP)

## Overview

This Guidance shows how Amazon Bedrock Data Automation streamlines the generation of valuable insights from unstructured multimodal content such as documents, images, audio, and videos through a unified multi-modal inference API. Amazon Bedrock Data Automation helps developers build generative AI applications or automate multi-modal data centric workflows like IDP, media analysis, or retrieval augmented generation (RAG) quickly and cost-effectively. By following this Guidance, you can simplify complex tasks such as document splitting, classification, data extraction, output format normalization, and data validation, significantly enhancing your processing scalability.

## How it works

### Intelligent document processing

This architecture diagram shows how to perform document classification and extraction using a loan origination processing example for a financial services company.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/multimodal-data-processing-using-amazon-bedrock-data-automation.pdf#page=1)Step 1The data science team uploads sample documents to an Amazon Simple Storage Service (Amazon S3) bucket.Step 2The data science team uses provided blueprints and creates new custom blueprints for each document class: W2, Pay Slip, Drivers License, 1099, and Bank Statement. Each sample is processed, and generative AI prompts extract fields (such as first and last name, gross pay, capital gains, and closing balance).Step 3The blueprints are tested and refined. Key normalizations, transformations, and validations are added.Step 4The blueprints are managed and stored in the Amazon Bedrock Data Automation feature.Step 5Using an "Object Created" event, Amazon EventBridge triggers an AWS Lambda function when documents are uploaded to Amazon S3. This Lambda function then uses the Amazon Bedrock Data Automation feature to process the uploaded documents.Step 6The processing workflow in the Amazon Bedrock Data Automation feature includes document splitting based on logical boundaries, with each split containing up to 20 pages. Each page is classified into a specific document type and matched to appropriate blueprints. The corresponding blueprint is then invoked for each page, executing key normalizations, transformations, and validations. This entire process operates asynchronously, allowing for efficient handling of multiple documents and large data volumes.Step 7Amazon Bedrock Data Automation stores the results in a Amazon S3 bucket for later processing and triggers EventBridge.Step 8EventBridge triggers the Lambda function to process the JSON results of Amazon Bedrock Data Automation. The processing results are sent to downstream processing systems.### Medical claims processing

This architecture diagram shows how to automate medical claims processing with multimodal input data and processing to improve efficiency and accuracy.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/multimodal-data-processing-using-amazon-bedrock-data-automation.pdf#page=2)Step 1Providers submit claims documents, images, and videos to Amazon S3.Step 2A workflow is triggered in Amazon Bedrock Data Automation.Step 3Developers create blueprints in Amazon Bedrock Data Automation to extract relevant data.Step 4Amazon Bedrock Data Automation processes documents, images, and videos by extracting text, tables, objects, transcripts; normalizing structuring the data; and flagging low-confidence items for review. Amazon Bedrock Data Automation stores the data in Amazon S3 and triggers EventBridge.Step 5EventBridge triggers Lambda, which retrieves the Amazon Bedrock Data Automation output from the S3 bucket.Step 6Amazon Bedrock Agents uses the Lambda function to fetch the patient's insurance plan details from Amazon Aurora.Step 7Amazon Bedrock Agents then updates the claims database in Aurora.Step 8Adjudicators verify important fields and focus on low-confidence items.Step 9Explanation of Coverage (EoC) documents, images, and videos are stored in Amazon S3. Amazon Bedrock Data Automation processes multimodal data with a single API and stores it in Amazon S3. It is then processed, embedded, and stored in a vector collection for Amazon Bedrock Knowledge Bases.Step 10Amazon Bedrock Agents calculates eligibility using extracted data and indexed information.Step 11Amazon Bedrock Agents updates the claims database and notifies the adjudicator. The adjudicator reviews and approves or adjusts the claim efficiently.## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Deploy this Guidance**: Use sample code to deploy this Guidance in your AWS account

[Sample code](https://github.com/aws-solutions-library-samples/guidance-for-multimodal-data-processing-using-amazon-bedrock-data-automation)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

Amazon S3, EventBridge, and Lambda create a seamless, automated workflow for document processing and data extraction through secure storage for various document types. Amazon Bedrock Data Automation streamlines the extraction and normalization of data, reducing manual effort and increasing accuracy. Amazon Bedrock Knowledge Bases index the processed information, making it easily searchable and accessible, while Amazon Bedrock Agents leverages this structured data to make intelligent decisions and route claims efficiently. Aurora serves as a robust database for storing and retrieving critical information. Together, these services enable a highly efficient, scalable, and reliable system that minimizes human intervention and maximizes productivity. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

Amazon S3 offers encrypted storage, Lambda executes code in isolated environments, and Amazon Bedrock leverages secure AWS infrastructure with built-in encryption and access controls. Aurora provides advanced database security features. These services create a comprehensive security approach that protects data throughout its lifecycle while maintaining strict access controls and audit trails. The ability to centrally manage security policies and leverage continuous AWS security updates and improvements allows you to maintain a strong security posture while focusing on your core business operations. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Amazon S3 provides durable and highly available storage for documents. EventBridge helps ensures consistent event-driven processing by reliably triggering Lambda functions, which scale seamlessly to handle varying workloads without downtime. Aurora, a highly available database, offers automated backups and failover capabilities. These services offer a robust, fault-tolerant system that can withstand component failures, scale automatically, and maintain consistent performance under high loads, minimizing downtime and data loss risks. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

AWS services enhance performance efficiency through scalable, high-performance solutions for document processing. Amazon S3 provides low-latency access to stored documents, while EventBridge enables real-time event processing. Lambda offers rapid, on-demand compute power. The serverless nature of Lambda and EventBridge eliminates bottlenecks associated with server provisioning. Additionally, Amazon Bedrock leverages AI models for efficient processing of complex data analysis tasks. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

AWS services contribute to cost optimization through pay-as you-go models (meaning you only pay for resources consumed) and elimination of upfront infrastructure investments. Amazon S3 offers tiered storage options balancing performance and cost. The serverless nature of EventBridge and Lambda means paying only for actual compute time used. Amazon Bedrock provides AI capabilities without expensive in-house infrastructure or expertise, and Aurora offers performance comparable to commercial databases at a fraction of the cost. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

AWS services contribute to sustainability by optimizing resource utilization and energy efficiency. Amazon S3 uses efficient storage technologies, while EventBridge and Lambda provide serverless architectures that minimize idle capacity. These cloud-based services significantly reduce on-premises infrastructure, lowering energy consumption and carbon emissions. Their scalability ensures optimal resource use, avoiding over-provisioning and waste. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
