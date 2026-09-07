---
source_url: https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/architecture-details.html
---

# Architecture details
<a name="architecture-details"></a>

This section provides detailed technical information about the Spatial Data Management on AWS architecture, including component interactions, data flows, and AWS services used.

## Architecture Components and Flow
<a name="architecture-components-and-flow"></a>

![Detailed architecture diagram showing the complete Spatial Data Management on AWS architecture with numbered data flows](https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/images/architecture-diagram.svg)

The diagram shows the complete Spatial Data Management on AWS architecture with numbered data flows indicating the sequence of operations across different layers.

## Architecture Flow
<a name="architecture-flow"></a>

This section walks through a typical user workflow to illustrate how the architecture components work together.

### Prerequisites
<a name="architecture-prerequisites"></a>

Before general users can interact with Spatial Data Management on AWS, two setup steps must be completed:

 **Step 1: IT Administrator Setup** – The IT Administrator deploys Spatial Data Management on AWS to the AWS account using the AWS CloudFormation template, which provisions all required AWS services, configures security settings, and establishes the infrastructure foundation.

 **Step 2: Application Administrator Configuration** – The Application Administrator configures the solution through the Spatial Data Portal by setting up user groups, defining access policies, onboarding users into Amazon Cognito, and assigning permissions to spatial data collections and resources.

### Example: Uploading and Processing a Spatial Asset
<a name="example-uploading-and-processing-a-spatial-asset"></a>

The numbered steps in the architecture diagram illustrate the complete workflow:

 **Step 3: User Authentication** – A general user accesses the Spatial Data Portal (web or desktop client) and authenticates through Amazon Cognito, which provides temporary AWS credentials.

 **Step 4: Portal Access** – The user accesses the Spatial Data Portal on the client application or in a web browser delivered through Amazon CloudFront, which provides low-latency content delivery.

 **Step 5: Credential Provisioning** – Cognito Identity Pool provides federated credentials to the API Gateway for secure API access.

 **Step 6: Asset Upload Initiation** – The user initiates an upload through the portal, which sends the request via CloudFront to API Gateway to access the REST APIs.

 **Step 7: API Processing** – API Gateway invokes a Lambda function that verifies the user has authorization for the project they are planning to upload to, validates the request, and then creates temporary credentials for accessing Amazon S3.

 **Step 8: Credential Return** – API Gateway returns the S3 bucket to use and upload credentials to the client.

 **Step 9: Direct Upload to S3** – The client uploads the spatial asset file directly to Amazon S3 using the temporary credentials from the previous step. The architecture supports direct S3 uploads to use S3’s native APIs for efficient large file transfers.

 **Step 10: Event Notification** – Amazon S3 publishes an object creation event to Amazon EventBridge when the upload completes.

 **Step 11: Workflow Orchestration** – EventBridge routes the event to an Amazon SQS queue based on configured rules, which buffers work items for processing Lambda functions. SQS triggers Lambda functions to process the queued events.

 **Step 12: Resource Record Creation** – Lambda functions update Amazon DynamoDB to create application resource records and related relationships.

 **Step 13: Search Indexing** – Asset metadata is indexed in Amazon OpenSearch Serverless for full-text and geospatial search capabilities.

 **Step 14: Asset Processing** – Lambda functions invoke AWS Deadline Cloud to generate previews, extract additional metadata, convert formats, or perform other transformations on the spatial asset.

 **Step 15: Processing Results** – AWS Deadline Cloud stores processing results (previews, converted formats) back to Amazon S3, and Lambda functions publish completion events to EventBridge for downstream workflows.

This flow demonstrates how Spatial Data Management on AWS uses serverless architecture for scalability, event-driven processing for automation, and direct S3 access for performance.
