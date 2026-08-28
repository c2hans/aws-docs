---
source_url: https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/data-protection.html
---

# Data protection
<a name="data-protection"></a>

The Spatial Data Management Application (SDMA) protects both customer content and metadata.

## Encryption at rest
<a name="encryption-at-rest"></a>

The solution encrypts all stored data at rest using industry-standard encryption:

### Customer content (spatial assets)
<a name="_customer-content-spatial-assets"></a>

 **Amazon S3** The solution encrypts all spatial asset files (for example, point clouds, 3D models, images, E57, and LAS files) using server-side encryption with Amazon S3 managed keys (SSE-S3).

### Metadata and application data
<a name="_metadata-and-application-data"></a>

 **Amazon DynamoDB** The solution encrypts all DynamoDB tables using AWS owned keys (default encryption). Backups are encrypted with the same keys. **Amazon OpenSearch Serverless** Data is encrypted at rest using AWS managed encryption.

### Logs and audit data
<a name="_logs-and-audit-data"></a>

 **Amazon CloudWatch Logs** – Log data is encrypted using AWS KMS. **AWS CloudTrail** – Audit logs stored in S3 are encrypted using SSE-S3. **S3 access logs** – Access logs are encrypted using SSE-S3.

### Message queues
<a name="_message-queues"></a>

 **Amazon SQS** All queues use AWS KMS encryption for messages at rest.

## Encryption in transit
<a name="encryption-in-transit"></a>

The solution encrypts all transmitted data in transit:

 **API communications**
+  **Amazon API Gateway** – All API endpoints require HTTPS/TLS 1.2 or later. The solution deploys an Amazon API Gateway REST API with the default endpoint and SSL certificate. The default endpoint uses the TLSv1 security policy. For production deployments, use the TLS\_1\_2 security policy with a custom domain name and custom SSL certificate to enforce TLSv1.2 or later. For more information, see [Choosing a minimum TLS version for a custom domain](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-custom-domain-tls-version.html) and [Setting up custom domain names](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-custom-domains.html).
+  **SSL/TLS enforcement** – HTTP requests are automatically redirected to HTTPS.
+  **Certificate management** – AWS Certificate Manager (ACM) manages SSL/TLS certificates.

 **Content Delivery**
+  **Amazon CloudFront** – This solution deploys a web portal hosted in an Amazon S3 bucket. To help reduce latency and improve security, this solution includes a CloudFront distribution with an origin access identity, which is a CloudFront user that provides public access to the solution’s website bucket contents. For more information, see [Restricting access to an Amazon S3 origin](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html) in the Amazon CloudFront Developer Guide.
  + All distributions enforce HTTPS for content delivery
  +  **Signed URLs** – CloudFront signed URLs provide time-limited, secure access to thumbnails and preview files. Full asset uploads and downloads use S3 APIs with temporary credentials for secure direct access.
  +  **Origin Access** – CloudFront to S3 communication uses AWS internal network encryption
  +  **TLS Configuration** – Amazon CloudFront is deployed using the default CloudFront domain name and TLS certificate. To use a later TLS version, use your own custom domain name and custom SSL certificate. For more information, refer to [using alternate domain names and HTTPS](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html#DownloadDistValues-security-policy) in the Amazon CloudFront Developer Guide.

 **Service-to-Service Communication**
+  **VPC Endpoints** – AWS PrivateLink endpoints ensure traffic between Lambda functions and AWS services never leaves the AWS network
+  **Lambda to DynamoDB** – Communication uses TLS encryption over VPC endpoints
+  **Lambda to S3** – Communication uses TLS encryption over VPC endpoints
+  **Lambda to OpenSearch** – Communication uses HTTPS over VPC endpoints

 **Client Uploads/Downloads**
+  **Direct S3 Access** – Clients use temporary SIGv4 credentials with HTTPS for direct uploads/downloads
+  **Pre-signed URLs** – All pre-signed URLs enforce HTTPS
+  **CloudFront Downloads** – All asset downloads use HTTPS through CloudFront

## Key Management
<a name="key-management"></a>

 **Customer-Managed Keys (KMS)** - **Pagination Token Encryption**: One customer-managed KMS key encrypts API pagination tokens - Automatic yearly key rotation enabled - Key policy restricts access to authorized Lambda functions only - CloudWatch alarms monitor key usage

 **AWS-Managed Keys** - **Lambda Encryption** (`alias/aws/lambda`) - Used for encrypting Lambda function environment variables, code, layers, and sensitive configurations - **Secrets Manager** (`alias/aws/secretsmanager`) - Used for encrypting secrets stored in AWS Secrets Manager - Protects sensitive configuration values, API keys, passwords, and certificates

 **Key Rotation** - Customer-managed keys: Automatic yearly rotation (pagination tokens only) - AWS-managed keys: Automatic rotation managed by AWS - AWS owned keys: Automatic rotation managed by AWS

## Internetwork Traffic Privacy
<a name="internetwork-traffic-privacy"></a>

The solution is designed to minimize exposure to the public internet:

 **VPC Isolation** - Lambda functions run in private VPC subnets with no direct internet access - AWS service access is through VPC endpoints (AWS PrivateLink), keeping traffic within the AWS network - NAT Gateways provide controlled internet access only when required for external integrations

 **VPC Endpoints (AWS PrivateLink)**

The solution uses 8 VPC endpoints to ensure private connectivity:
+ OpenSearch Serverless (interface endpoint)
+ DynamoDB (gateway endpoint)
+ S3 (gateway endpoint)
+ Secrets Manager (interface endpoint)
+ Lambda (interface endpoint)
+ CloudWatch Logs (interface endpoint)
+ SQS (interface endpoint)
+ EC2 (interface endpoint for ENI management)

 **Public Access Controls**
+  **S3 Buckets**: All buckets have "Block Public Access" enabled for all settings
+  **API Gateway**: Public endpoint with authentication required (Cognito or IAM)
+  **CloudFront**: Public distribution for content delivery with signed URLs for protected content
+  **No Public Resources**: DynamoDB, Lambda, OpenSearch, SQS, and SNS are not publicly accessible

 **Network Segmentation**
+  **Public Subnets**: NAT Gateways and internet gateway only
+  **Private Subnets**: Lambda functions with internet access via NAT
+  **Isolated Subnets**: Lambda functions with no internet access (Asset Watcher)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Spatial Data Management on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
