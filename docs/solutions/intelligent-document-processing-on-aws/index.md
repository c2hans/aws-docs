---
source_url: https://docs.aws.amazon.com/solutions/intelligent-document-processing-on-aws/index.html
---

---
title: 'Guidance for Intelligent Document Processing on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/intelligent-document-processing-on-aws/
source: aws-documentation
generated_on: 2026-10-07
---

# Guidance for Intelligent Document Processing on AWS

## Overview

This Guidance demonstrates how to implement Intelligent Document Processing (IDP) using AWS AI agents to transform traditional document-heavy workflows into streamlined, automated processes. It helps organizations significantly reduce operational costs while accelerating decision-making and customer service delivery. The solution shows how businesses can eliminate manual data entry, minimize errors, and reallocate human resources to higher-value tasks. Furthermore, it demonstrates how to leverage extracted document data for advanced analytics and machine learning applications, enabling real-time business insights, fraud detection, and new revenue opportunities. This architecture brings together proven AWS services to help organizations modernize their document processing workflows and achieve greater operational efficiency.

## How it works

### Prompt Flows

This architecture diagram shows how you can automate document processing with AWS artificial intelligence and machine learning (AI/ML) services, allowingyou to speed up business processes, improve decision quality, and reduce overall costs.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/intelligent-document-processing-on-aws.pdf)Step 1Business documents including purchase orders, invoices, shipping tickets, and other transactional records arrive via Amazon Simple Email Service (Amazon SES) or direct upload to Amazon Simple Storage Service (Amazon S3).Step 2Amazon EventBridge invokes an AWS Lambda function when new documents arrive in Amazon S3.Step 3The Lambda function creates a tracking job in Amazon DynamoDB and invokes Amazon Bedrock AgentCore Runtime to orchestrate document processing through Strands Agents.Step 4Amazon Bedrock AgentCore Runtime queries Amazon Bedrock AgentCore Identity for machine-to-machine credentials, enabling secure access to AWS resources and third-party services. Amazon Bedrock AgentCore Identity retrieves a workload access token from Amazon Cognito.Step 5Using this token, Amazon Bedrock AgentCore Runtime discovers and accesses tools from Amazon Bedrock AgentCore Gateway. The agent selects tools based on document type and processing requirements.Step 6Amazon Bedrock AgentCore Gateway transforms existing APIs and Lambda functions into agent-compatible tools with minimal code. It provides a searchable Model Context Protocol (MCP) interface for AWS resources, external tools, and databases, enabling secure discovery and communication.Step 7Agents extract text from documents using Amazon Textract, classify entities using vector embeddings in Amazon S3, and determine next processing steps.Step 8Agents access Enterprise Data via MCP servers to validate extracted content against business rules.Step 9Users monitor status and perform administrative actions through a chat-enabled dashboard hosted on Amazon Elastic Container Service (Amazon ECS).Step 10The dashboard invokes Amazon Bedrock AgentCore Runtime, enabling users to troubleshoot document processing issues in real-time.Step 11Amazon Bedrock AgentCore Observability traces, debugs, and monitors agent performance by automatically logging telemetry data to Amazon CloudWatch. This provides detailed visualizations of each workflow step, enabling inspection of execution paths and identification of performance bottlenecks.### AgentCore: Overview

This architecture implements an intelligent document processing system using Amazon Bedrock AgentCore, where multiple specialized agents collaborate through graph-based workflows to automatically identify, extract, validate, and learn from business documents with minimal human intervention.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/intelligent-document-processing-on-aws.pdf)Step 1Amazon Bedrock AgentCore orchestrates document processing through a multi-agent system built with Strands Agents, using graph-based workflows to automate processing tasks.Step 2When a new document arrives in Amazon S3, an AWS Lambda function creates a job record and asynchronously invokes the Orchestrator Agent to begin processing. The Orchestrator first identifies the document type and sender, then queries the knowledge base to determine if this document type has existing processing rules.Step 3If a match exists, the Orchestrator initiates the Automation Workflow to process the document using the stored processing rules.Step 4The Automation Workflow extracts and validates data according to processing rules. Valid data is automatically sent downstream systems. Invalid data triggers the Troubleshooter agent, which reviews errors against the source document and rules, then sends corrective instructions to the Extractor. After three failed attempts, the document is routed for human review.Step 5If no match is found, the Orchestrator routes the document to the Trainer Workflow. This workflow creates a new processing blueprint by extracting and validating data from the document. Upon successful extraction, the workflow adds the new blueprint to the knowledge base and triggers human review before enabling automated processing for this document type.Step 6Throughout processing, the Orchestrator tracks document progress and updates job status in Amazon DynamoDB. Upon completion, processed documents are stored in Amazon S3 for downstream processing and integration. Users can monitor processing status, review extraction results, and access completed documents through the web dashboard interface.### AgentCore: Multi-Agent Orchestration

This diagram details the multi-agent workflow running within Amazon Bedrock AgentCore Runtime from the previous architecture, showing how specialized AI agents collaborate through graph-based orchestration to automatically process documents, with dual workflows handling known document types through automated extraction and validation, while unknown documents trigger blueprint creation with human oversight for continuous system learning.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/intelligent-document-processing-on-aws.pdf)Step 1Business documents including purchase orders, invoices, shipping tickets, and other transactional records arrive via Amazon Simple Email Service (Amazon SES) or direct upload to Amazon Simple Storage Service (Amazon S3).Step 2Amazon EventBridge invokes an AWS Lambda function when new documents arrive in Amazon S3.Step 3The Lambda function creates a tracking job in Amazon DynamoDB and invokes Amazon Bedrock AgentCore Runtime to orchestrate document processing through Strands Agents.Step 4Amazon Bedrock AgentCore Runtime queries Amazon Bedrock AgentCore Identity for machine-to-machine credentials, enabling secure access to AWS resources and third-party services. Amazon Bedrock AgentCore Identity retrieves a workload access token from Amazon Cognito.Step 5Using this token, Amazon Bedrock AgentCore Runtime discovers and accesses tools from Amazon Bedrock AgentCore Gateway. The agent selects tools based on document type and processing requirements.Step 6Amazon Bedrock AgentCore Gateway transforms existing APIs and Lambda functions into agent-compatible tools with minimal code. It provides a searchable Model Context Protocol (MCP) interface for AWS resources, external tools, and databases, enabling secure discovery and communication.Step 7Agents extract text from documents using Amazon Textract, classify entities using vector embeddings in Amazon S3, and determine next processing steps.Step 8Agents access Enterprise Data via MCP servers to validate extracted content against business rules.Step 9Users monitor status and perform administrative actions through a chat-enabled dashboard hosted on Amazon Elastic Container Service (Amazon ECS).Step 10The dashboard invokes Amazon Bedrock AgentCore Runtime, enabling users to troubleshoot document processing issues in real-time.Step 11Amazon Bedrock AgentCore Observability traces, debugs, and monitors agent performance by automatically logging telemetry data to Amazon CloudWatch. This provides detailed visualizations of each workflow step, enabling inspection of execution paths and identification of performance bottlenecks.## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-samples/aws-ai-intelligent-document-processing)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

The Intelligent Document Processing architecture can be fully deployed using infrastructure as code (IaC) methodologies. The serverless infrastructure components can be provisioned using the AWS Cloud Development Kit (CDK) found below and orchestrated through the low-code visual workflow service, AWS Step Functions. This automation can be seamlessly integrated into your development pipeline, enabling rapid iteration and consistent deployments. Observability for this Guidance is achieved through the use of Amazon CloudWatch logs, which capture telemetry data from the AWS AI agents employed, such as Amazon Textract and Amazon Comprehend. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

The AI services in this Guidance support security for both resting and transitional data. Amazon Textract, Amazon Comprehend, and Amazon Comprehend Medical support encryption at rest with Amazon S3 buckets and AWS Key Management Service (AWS KMS). In addition, Amazon Textract provides an asynchronous API and Amazon Comprehend Medical services support in-memory data processing. In addition, Intelligent Document Processing can be orchestrated with a serverless backend with AWS Identity and Access Management (IAM) for authentication and secure validation. You can also define separation of access control per user role. For example, you can give the owner full access to all documents, but allow an operator to access only de-identified documents. Finally, this architecture includes the capability to categorize documents accurately by using Amazon Comprehend to detect personally identifiable information (PII). Also, when you want to detect Protected Health Information (PHI), use Amazon Comprehend Medical PHI identification and redaction options to scan clinical text. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

The Intelligent Document Processing architecture uses managed, Regional AI services provided by AWS. The reliability and availability of these services within the selected AWS Region are maintained by AWS. The inherent nature of the managed AI services helps ensure resilience to failures and high availability. Should you choose to use Amazon S3 as the scalable data store, it is recommended to consider enabling Amazon S3 cross-Region replication. This additional measure can further increase the reliability of this and provide access to disaster recovery options. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

The serverless and event-driven architecture of this Guidance promotes efficiency, as resources are not wasted when documents are not being processed. It can be scaled in a particular Region to accommodate for large scale document processing, achieved by increasing the call rates for the AI agents and Lambda. You can also design a serverless decoupled architecture with Amazon SNS and Amazon SQS for concurrent processing of multiple documents. Lastly, Intelligent Document Processing can be configured to operate in real-time with response times in seconds, or in asynchronous mode, depending on your specific requirements. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Intelligent Document Processing minimizes costs by using a serverless, event-driven architecture, where you only pay for the time and resources consumed during document processing. Amazon Comprehend offers options to train custom models in addition to utilizing pre-defined entity extraction capabilities. For urgent, real-time document processing requirements, the Amazon Comprehend resource endpoints can be used for custom models. However, if your use case can accommodate asynchronous or batch processing, it is recommended to use asynchronous jobs for Amazon Comprehend custom models to optimize costs. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

By extensively using managed services and dynamic scaling capabilities, the environmental impact of the backend infrastructure supporting this Guidance is minimized. AWS managed services handle the provisioning, scaling, and maintenance of the underlying compute, storage, and networking resources, offloading the operational overhead you and your team. Additionally, the dynamic scaling capabilities inherent in managed services and serverless architectures helps ensure that resources are provisioned and utilized only when needed to process incoming workloads, preventing over-provisioning and optimizing the environmental footprint of the backend services powering this Guidance. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

## Related content

- **Intelligent document processing with AWS AI services: Part 1**: This blog post demonstrates how intelligent document processing (IDP) helps automate information extraction from documents of different types and formats, quickly and with high accuracy.

[Learn more](https://aws.amazon.com/blogs/machine-learning/part-1-intelligent-document-processing-with-aws-ai-services/)

- **Intelligent document processing with AWS AI services: Part 2**: This blog demonstrates how we can extend the IDP pipeline by looking at Amazon Comprehend default and custom entities in the extraction phase, perform document enrichment, and also briefly look at the capabilities of Amazon Augmented AI (Amazon A2I) to include a human review workforce in the review and validation stage.

[Learn more](https://aws.amazon.com/blogs/machine-learning/part-2-intelligent-document-processing-with-aws-ai-services/)

[Read usage guidelines](/solutions/guidance-disclaimers/)
