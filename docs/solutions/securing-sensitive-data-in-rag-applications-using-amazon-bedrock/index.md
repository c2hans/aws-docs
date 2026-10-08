---
source_url: https://docs.aws.amazon.com/solutions/securing-sensitive-data-in-rag-applications-using-amazon-bedrock/index.html
---

---
title: 'Guidance for Securing Sensitive Data in RAG Applications Using Amazon Bedrock'
canonical_url: https://docs.aws.amazon.com/solutions/securing-sensitive-data-in-rag-applications-using-amazon-bedrock/
source: aws-documentation
generated_on: 2026-10-07
---

# Guidance for Securing Sensitive Data in RAG Applications Using Amazon Bedrock

## Overview

This Guidance demonstrates two security patterns for protecting sensitive data in retrieval augmented generation (RAG) applications built with Amazon Bedrock. It shows how to implement both a zero-trust architecture with pre-ingestion data redaction and a role-based access control system for precise data access management. The Guidance helps organizations maintain data privacy, regulatory compliance, and security by leveraging AWS AI services and integrated encryption. This approach helps ensure sensitive information remains protected throughout the RAG workflow, from initial data ingestion through final presentation, while maintaining system functionality and data integrity.

## Benefits

### Automate sensitive data protection at scale

Deploy an intelligent pipeline that automatically detects and redacts PII while providing secondary verification through Amazon Macie. Reduce risk exposure while maintaining operational efficiency.

### Enable secure knowledge sharing

Implement role-based access controls and guardrails to ensure users access only appropriate information. Confidently share organizational knowledge while protecting sensitive content.

### Streamline compliance workflows

Establish automated security controls with multi-layer verification and comprehensive audit trails. Maintain regulatory compliance while accelerating document processing for RAG applications.

## How it works

### Data redaction at storage level

This architecture diagram shows how customers can safely ingest sensitive documents through automated redaction and verification processes while enabling secure, guardrail-protected access to their knowledge base without compromising sensitive information.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/securing-sensitive-data-in-rag-applications-using-amazon-bedrock.pdf#page=1)Step 1The document ingestion flow initiates when documents containing sensitive data are uploaded to the source folder of the Amazon Simple Storage Service (Amazon S3) bucket.Step 2Amazon EventBridge triggers AWS Lambda Stage 1 function, which initiates the Amazon Comprehend personally identifiable information (PII) redaction process and records the job ID information in the Amazon DynamoDB table.Step 3The Amazon Comprehend job redacts PII entities, and redacted documents are moved to the macie folder in the S3 bucket.Step 4During the Amazon Comprehend redaction process, Amazon EventBridge triggers Lambda Stage 2 function to monitor the redaction job status.Step 5Upon completion of PII redaction, the Lambda Stage 2 function initiates a secondary verification using Amazon Macie.Step 6The Amazon Macie job scans for sensitive information. Documents with severity >= 3 are moved to a quarantine folder, while documents with severity < 3 are moved to the redacted folder.

Step 7Amazon Bedrock Knowledge Bases processes documents from the S3 bucket redacted folder, segments them into chunks, and securely indexes them in the Amazon OpenSearch Service vector store for RAG applications.Step 8Users submit requests through Amazon API Gateway with their prompt and login credentials.Step 9API Gateway authenticates credentials through Amazon Cognito, then forwards the user claims and prompt to the Lambda orchestrator.Step 10The input prompt undergoes validation against pre-configured Amazon Bedrock Guardrails, with requests being blocked if validation fails.Step 11Following successful guardrail validation, the prompt is sent for contextual retrieval and response generation using Amazon Bedrock Knowledge Bases.Step 12The generated response undergoes output guardrail evaluation; failed validations result in blocked responses. Successfully validated responses are securely transmitted back to the user through API Gateway.### Role based access to sensitive data

This architecture diagram shows how customers can implement role-based access control for sensitive data in RAG applications using metadata filtering and personalized guardrails, ensuring users only access information appropriate for their authorization level while maintaining the security of sensitive content.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/securing-sensitive-data-in-rag-applications-using-amazon-bedrock.pdf#page=3)Step 1Documents in the S3 bucket are processed and indexed by Amazon Bedrock Knowledge Bases with appropriate metadata attributes defining access permissions.Step 2Users authenticate through API Gateway, with Amazon Cognito validating credentials and determining the user's role (admin/non-admin).Step 3API Gateway forwards the authenticated request with user claims to the Lambda Orchestrator function.Step 4The Lambda Orchestrator analyzes user role information and applies the appropriate guardrail configuration—either admin guardrails (with full access) or non-admin guardrails (with restricted access).Step 5Amazon Bedrock Knowledge Bases processes the query with the appropriate guardrails, retrieving relevant documents from OpenSearch Service according to role-based metadata filters.## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **We'll walk you through it**: Dive deep into the implementation guide for additional customization options and service configurations to tailor to your specific needs.

[Open guide](https://aws-solutions-library-samples.github.io/ai-ml/securing-sensitive-data-in-rag-applications-using-amazon-bedrock.html)

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-securing-sensitive-data-in-rag-applications-using-amazon-bedrock)

[Read usage guidelines](/solutions/guidance-disclaimers/)
