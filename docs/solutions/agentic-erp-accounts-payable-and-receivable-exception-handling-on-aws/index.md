---
source_url: https://docs.aws.amazon.com/solutions/agentic-erp-accounts-payable-and-receivable-exception-handling-on-aws/index.html
---

---
title: 'Guidance for Agentic ERP Accounts Payable and Receivable Exceptions Handling on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/agentic-erp-accounts-payable-and-receivable-exception-handling-on-aws/
source: aws-documentation
generated_on: 2026-10-05
---

# Guidance for Agentic ERP Accounts Payable and Receivable Exceptions Handling on AWS

## Overview

This Guidance demonstrates how to accelerate ERP operations through intelligent exception handling using AWS AI agentic services, offering two distinct implementation patterns through Strands SDK and Amazon Quick Suite. It helps organizations streamline both Procure-to-Pay (P2P) and Order-to-Cash (OTC) processes by providing contextual recommendations for resolving various exception scenarios involving price variances, duplicate invoices, remittance matching and quantity errors. The solution shows how developers can build custom AI agents using Strands SDK for complex integration needs, while business personas can leverage Quick Suite's ready-to-use low code agentic capabilities. Furthermore, it demonstrates how to unify scattered data sources across ERP systems and knowledge bases, reducing manual research time and accelerating exception resolution through intelligent recommendations.

## Benefits

### Reduce Research Time for ERP Exceptions

Identify P2P and O2C exceptions and categorize transactions into different exception types.

### Improve ERP Exception Resolution Capabilities

Implement comprehensive exception handling with flexible integration patterns, observability, and audit trails. Ensure compliance with SOP while processing invoices, purchase orders, and goods receipts with automated two-way or three-way matching.

### Choose your Implementation Approach

Deploy with Strands SDK for custom agent development or Amazon Quick Suite for no-code automation. Match technical capabilities to your team's expertise and business needs.

## How it works

### Accounts Payable using Strands SDK

This architecture diagram provides a customizable solution to accelerate developers implementing ERP procure-to-pay (P2P) exception handling using intelligent AI agents powered by Strand Agents SDK and AWS Bedrock AgentCore.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/agentic-erp-accounts-payable-and-receivable-exception-handling-on-aws.pdf)Step 1Users access the application through a web client.Step 2The client communicates with the Amazon Bedrock AgentCore System, passing natural language user queries and questions related to escalated invoices and exceptions to the Strands Agent hosted on AgentCore Runtime.Step 3The Strands Agent authenticates credentials with Amazon Cognito.Step 4Strands Agent initializes the model context protocol (MCP) client that connects to the AgentCore Gateway endpoint.Step 5AgentCore Gateway discovers and invokes SAP procure-to-pay tools across AWS services and MCP-compatible APIs to update exceptions and related financial documentation.Step 6AgentCore Observability captures logging, metrics, and traces to monitor agent performance in production environments. Users can view collected data from Amazon CloudWatch.Step 7The AWS Lambda function processes the P2P exception called from AgentCore Gateway, enabling intelligent routing, escalation workflows, and database actions.Step 8AWS Lambda retrieves related invoice documents, goods receipts and customer information from the Amazon Bedrock Knowledge Base that uses Amazon Aurora with vector extension for vector storage and Amazon Simple Storage Service (Amazon S3) for document storage to form a context of the exception.Step 9AWS Lambda retrieves and processes customer and vendor data from SAP backend systems stored in Amazon DynamoDB.Step 10Amazon Simple Notification Service (Amazon SNS) delivers automated email notifications to vendors, financial analysts, and clients to keep them informed of status updates and required actions.### Accounts Receivable using Strands SDK

This architecture diagram provides a customizable solution to accelerate developers implementing ERP order-to-cash (OTC) exception handling using intelligent AI agents powered by Strand Agents SDK and AWS Bedrock AgentCore.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/agentic-erp-accounts-payable-and-receivable-exception-handling-on-aws.pdf)Step 1Users access the application through a web client.Step 2The client communicates with the Amazon Bedrock AgentCore System, passing natural language user queries and questions related to escalated invoices and exceptions to the Strands Agent hosted on AgentCore Runtime.Step 3The Strands Agent authenticates credentials with Amazon Cognito.Step 4Strands Agent initializes the model context protocol (MCP) client that connects to AgentCore Gateway endpoint.Step 5AgentCore Gateway discovers and invokes SAP order-to-cash tools across AWS services and MCP-compatible APIs to update exceptions and related financial documentation.Step 6AgentCore Observability captures logging, metrics, and traces to monitor agent performance in production environments. Users can view collected data from Amazon CloudWatch.Step 7The AWS Lambda function processes the order-to-cash exception called from AgentCore Gateway, enabling intelligent routing, escalation workflows, and database actions.Step 8AWS Lambda retrieves related invoice documents, goods, receipts, and customer information from the Amazon Bedrock Knowledge Base that uses Amazon Aurora with vector extension for vector storage and Amazon Simple Storage Service (Amazon S3) for document storage to form a context of the exception.Step 9AWS Lambda retrieves and processes customer and vendor data from SAP backend systems stored in Amazon DynamoDB.Step 10Amazon Simple Notification Service (Amazon SNS) delivers automated email notifications to vendors, financial analysts, and clients to keep them informed of status updates and required actions.### Accounts Payable using Amazon Quick Suite

This architecture diagram provides a customizable solution to accelerate developers implementing ERP procure-to-pay (P2P) exception handling using intelligent AI agents powered by Amazon Quick Suite and AWS Bedrock AgentCore.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/agentic-erp-accounts-payable-and-receivable-exception-handling-on-aws.pdf)Step 1Users authenticate to Amazon Quick Suite through Amazon Cognito User Pools using single sign-on credentials.Step 2Integrate with AgentCore Gateway through Amazon Cognito inbound authentication using authenticated credentials.Step 3Amazon Quick Suite Flows initializes a model context protocol (MCP) client that connects to AgentCore Gateway endpoint.Step 4AgentCore Gateway discovers and invokes SAP procure-to-pay tools across AWS services and MCP-compatible APIs to update exceptions and related financial documentation.Step 5AgentCore Observability captures logging, metrics, and traces to monitor agent performance in production environments. Users can view collected data from Amazon CloudWatch.Step 6The AWS Lambda function processes the P2P exception called from AgentCore Gateway, enabling intelligent routing, escalation workflows, and database actions.Step 7AWS Lambda retrieves related invoice documents, goods receipts and customer information from the Amazon Bedrock Knowledge Base that uses Amazon Aurora with vector extension for vector storage and Amazon Simple Storage Service (Amazon S3) for document storage to form a context of the exception.Step 8AWS Lambda retrieves and processes customer and vendor data from ERP backend systems stored in Amazon DynamoDB.Step 9Amazon Simple Notification Service (Amazon SNS) delivers automated email notifications to vendors, financial analysts, and clients to keep them informed of status updates and required actions.Step 10Amazon Quick Suite provides recommendations for resolving exceptions and returns the results of updated invoices and purchase orders with database operation status updates in natural language format.## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-agentic-erp-account-payable-and-receivable-exception-handling-on-aws)

[Read usage guidelines](/solutions/guidance-disclaimers/)
