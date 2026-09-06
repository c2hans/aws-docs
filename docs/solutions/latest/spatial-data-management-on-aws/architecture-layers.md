---
source_url: https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/architecture-layers.html
---

# Architecture Layers
<a name="architecture-layers"></a>

## Authentication Layer
<a name="authentication-layer"></a>

Manages user identity and access control using Amazon Cognito for user authentication and federated identity pools for temporary AWS credentials. This layer ensures secure access to both the Spatial Data Portal and programmatic APIs.

## Content Delivery Layer
<a name="content-delivery-layer"></a>

Amazon CloudFront serves the Spatial Data Portal web application and provides low-latency access to thumbnails and preview assets. CloudFront also acts as the entry point for API requests.

## API Layer
<a name="api-layer"></a>

Amazon API Gateway provides RESTful endpoints for all Spatial Data Management on AWS operations, including asset management, search, and metadata operations. AWS Lambda functions behind the API handle business logic, validation, and orchestration of backend services. The API layer runs within an Amazon Virtual Private Cloud (Amazon VPC) for secure access to data stores.

## Event Processing Layer
<a name="event-processing-layer"></a>

Amazon EventBridge and Amazon SQS provide event-driven architecture for asynchronous workflows. Amazon S3 events trigger processing pipelines, Lambda functions publish workflow events, and SQS queues buffer work items for reliable processing.

## Spatial Data Store
<a name="spatial-data-store"></a>

Amazon S3 serves as the central repository for all spatial asset files, providing scalable, durable storage with versioning and lifecycle management. This is the core data plane where actual spatial files reside.

## Application Data Layer
<a name="application-data-layer"></a>

Amazon DynamoDB stores metadata, relationships, and application state with single-digit millisecond latency. Amazon OpenSearch Serverless provides full-text search and geospatial query capabilities for asset discovery.

## Transforms and Integrations Layer
<a name="transforms-and-integrations-layer"></a>

AWS Deadline Cloud handles compute-intensive transformations like 3D rendering, format conversion, and thumbnail generation. This layer enables integration with external applications through REST APIs and direct S3 access.
