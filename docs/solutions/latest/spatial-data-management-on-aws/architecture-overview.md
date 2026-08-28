---
source_url: https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/architecture-overview.html
---

# Architecture overview
<a name="architecture-overview"></a>

This document describes the technical architecture of Spatial Data Management on AWS, including the AWS services used and how they interact.

## High-Level Architecture
<a name="high-level-architecture"></a>

![High-level architecture diagram showing the three main layers of Spatial Data Management on AWS](http://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/images/high_level_architecture_interfaces.svg)

The Spatial Data Management on AWS solution is deployed entirely within your AWS account. The architecture consists of three main layers:

### Client Layer
<a name="client-layer"></a>

Users and external applications access the solution through multiple interfaces:
+  **Spatial Data Portal** – Web application (Amazon CloudFront and React) and desktop application (Tauri and Rust)
+  **REST APIs** – Programmatic access via Amazon API Gateway
+  **CLI Tools** – Python-based command-line interface
+  **Direct S3 Access** – Temporary credentials for large file uploads and downloads

### SDMA Deployment (Your AWS Account)
<a name="sdma-deployment"></a>

The core solution includes:
+  **Control Plane** – Amazon API Gateway and AWS Lambda functions for business logic and orchestration
+  **Data Plane** – Amazon S3 for spatial asset storage with content-addressable architecture
+  **Metadata Layer** – Amazon DynamoDB for resource metadata and Amazon OpenSearch Serverless for full-text search
+  **Integration Layer** – Amazon EventBridge, Amazon SQS, and connectors for external system integration
+  **Security Layer** – Amazon Cognito for authentication and Amazon Verified Permissions for authorization

### External Applications
<a name="external-applications"></a>

Third-party systems integrate through:
+  **REST APIs** – Standard HTTP/HTTPS endpoints
+  **S3 APIs** – Direct access to spatial assets with temporary credentials
+  **Webhooks** – Event notifications for asset changes
+  **Connectors** – Pre-built integrations for common platforms (Digital Twin, Geographic Information Systems (GIS), and Computer-Aided Design (CAD) tools)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Spatial Data Management on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
