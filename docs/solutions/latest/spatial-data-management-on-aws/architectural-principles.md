---
source_url: https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/architectural-principles.html
---

# Architectural Principles
<a name="architectural-principles"></a>

The solution follows AWS Well-Architected Framework principles:

## Separation of Concerns
<a name="separation-of-concerns"></a>

The architecture separates data storage (Amazon S3), business logic (Amazon API Gateway and AWS Lambda), and metadata management (Amazon DynamoDB and Amazon OpenSearch Serverless) into distinct layers for independent scaling and maintenance.

## Content-Addressable Storage
<a name="content-addressable-storage"></a>

Files are stored by content hash with automatic deduplication across assets, ensuring efficient storage and immutable file references.

## Event-Driven Architecture
<a name="event-driven-architecture"></a>

Amazon EventBridge routes events to Amazon SQS and AWS Lambda for asynchronous, scalable processing of asset changes and system events.

## Security by Design
<a name="security-by-design"></a>

The solution uses VPC isolation, private VPC endpoints, encryption at rest and in transit, fine-grained access control, and audit logging to protect data and operations.
