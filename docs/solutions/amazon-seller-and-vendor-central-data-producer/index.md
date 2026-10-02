---
source_url: https://docs.aws.amazon.com/solutions/amazon-seller-and-vendor-central-data-producer/index.html
---

---
title: 'Guidance for Amazon Seller and Vendor Central Data Producer'
canonical_url: https://docs.aws.amazon.com/solutions/amazon-seller-and-vendor-central-data-producer/
source: aws-documentation
generated_on: 2026-10-02
---

# Guidance for Amazon Seller and Vendor Central Data Producer

## Overview

This Guidance demonstrates how Consumer Packaged Goods (CPG) companies can ingest data into a modern data environment to enable advanced analytics. Companies can develop efficient and secure applications that integrate with Amazon Seller and Vendor Central and gain valuable insights into their Amazon Retail data, including product catalog updates, sales, shipments, and payments.

## How it works

### Overview

This architecture uses serverless and managed services to help customers develop efficient and secure applications to integrate with Amazon Seller Central and Amazon Vendor Central. Customers can use this to ingest, process, and gain insights from their Amazon.com data.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/amazon-seller-and-vendor-central-data-producer.pdf)Step 1Authentication and AuthorizationStep 2Serverless Reports ApplicationStep 3Serverless Catalog Items and Listing Items ApplicationsStep 4Data Storage, Movement, and Insights### Authentication and Authorization

This architecture shows the registration process with Amazon Seller Central and Amazon Vendor Central. It includes: receiving a refresh token, secure token storage, exchanging for an access token, and using an authorized token to make API calls to the Selling Partner API (SP-API).

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/amazon-seller-and-vendor-central-data-producer.pdf)Step 1AWS Step Functions is used to create a serverless application to interact with the SP-API. The app is registered and authorized in Amazon Seller Central and Amazon Vendor Central.Step 2Once authorized, you get a Login with Amazon (LWA) refresh token. The LWA refresh token is a long-lived token which you can store in AWS Secrets Manager.Step 3In order to make API calls to the SP-API, your application needs an LWA access token. An AWS Lambda authentication function is used to first check with Secrets Manager to see if a valid LWA access token exists. If no valid LWA access token exists, the function retrieves an LWA refresh token from Secrets Manager, then exchanges the LWA refresh token for an LWA access token from the SP-API authentication server.Step 4The LWA access token expires one hour after it is issued. To avoid having to retrieve an access token for each API call, you can cache the LWA access token in Secrets Manager, which can then be used for successive calls until expiry.### Serverless Reports Application

This architecture shows how to create a serverless reports application to automatically ingest, process, and store data obtained from the Amazon Seller Central and Amazon Vendor Central Selling Partner API (SP-API).

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/amazon-seller-and-vendor-central-data-producer.pdf)Step 1Step Functions is used as a serverless orchestration service to centrally manage the workflow for integrating with the Selling Partner API (SP-API).Step 2The SP-API Reports API supports notifications to automate reports workflows. For this, a Lambda function is used to subscribe the application to the REPORT_PROCESSING_FINISHED notification type.Step 3In order to make calls to the SP-API, an authentication Lambda function is used to obtain a Login with Amazon (LWA) access token as described in the previous Authentication and Authorization diagram.Step 4The LWA access token from the authentication function is passed to a report creator Lambda function. This function uses regional endpoints, marketplace IDs, and report configurations data stored in Parameter Store, a capability of AWS Systems Manager, along with the LWA access token to make a createReport call to the SP-API.Step 5The SP-API will then generate the report and upon completion, a REPORT_PROCESSING_FINISHED notification event is sent to a Amazon Simple Queue Service (Amazon SQS) queue, which provides information when report processing is CANCELLED, DONE, or FATAL. This triggers a Lambda function to process the event. If the notification event has a status of DONE, a reportDocumentId will be included.Step 6The notification event is then passed to a data processing Lambda function in our Step Functions workflow. The data processing function uses the reportDocumentId to make a getReportDocument call to the SP-API. The SP-API returns a pre-signed URL for the location of the report document and the compression algorithm used, if the report document contents have been compressed.Step 7This response is then passed to a storage Lambda function which downloads the report document, decompresses it if applicable, and stores the report document in Amazon Simple Storage Service (Amazon S3).Step 8AWS Key Management Service (AWS KMS) is used to centrally mange encryption keys, which can be used to encrypt our secrets in Secrets Manager. Data is stored in Amazon S3 and Parameter Store.Step 9SP-API requests are limited using the token bucket algorithm, so an API client is recommended for rate limiting.### Serverless Catalog Items and Listing Items Applications

This architecture shows how to create a serverless application to integrate with the Catalog Items and Listing Items APIs from the Amazon Seller Central and Amazon Vendor Central Selling Partner API.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/amazon-seller-and-vendor-central-data-producer.pdf)Step 1Step Functions is used as a serverless orchestration service to centrally manage the workflow for integrating with the Selling Partner API (SP-API).Step 2In order to make calls to the SP-API, an authentication Lambda function is used to obtain a Login with Amazon (LWA) access token as described in the previous Authentication and Authorization diagram.Step 3The LWA access token from the authentication function is passed to a data processing Lambda function. This function uses regional endpoints and marketplace IDs stored in Parameter Store, and ASINs, SKUs, and Seller IDs stored in Amazon DynamoDB along with the LWA access token to make an API call to the Catalog Items or Listing Items API of the SP-API.Step 4When a response is returned, it is then passed to a storage Lambda function which stores the data in Amazon S3.Step 5AWS KMS is used to centrally mange encryption keys, which can be used to encrypt our secrets in Secrets Manager and our data stored in Amazon S3, DynamoDB, and Parameter Store.Step 6SP-API requests are limited using the token bucket algorithm, so an API client is recommended for rate limiting.### Data Storage, Movement, and Insights

This architecture shows how to build a data analytics pipeline using a Modern Data Analytics approach to derive insights from the data.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/amazon-seller-and-vendor-central-data-producer.pdf)Step 1AWS Lake Formation is used to build the scalable data lake, and Amazon S3 is used as the data lake storage.Step 2Lake Formation is also used to enable unified governance to centrally manage the security, access control, and audit trails.Step 3AWS Glue and AWS Glue DataBrew are used to catalog, transform, enrich, move, and replicate data across multiple data stores and the data lake.Step 4Amazon Athena enables interactive querying, analyzing, and processing capabilities.Step 5Amazon Redshift is used as a Cloud Data Warehouse.Step 6Amazon QuickSight provides machine learning-powered business intelligence.Step 7Amazon EMR provides the cloud big data platform for processing vast amounts of data using open source tools.Step 8Amazon OpenSearch Service can be used for operational analytics.Step 9Amazon SageMaker can be used to build, train, and deploy machine learning models, and add intelligence to your applications.## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

This Guidance consists of serverless services such as Lambda, Step Functions, and Amazon S3 that are loosely coupled and have built-in version control capabilities for implementing changes. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

This Guidance uses a self-authorization model with Amazon Vendor Central. Applications you create are registered in Vendor Central, where you receive a Login with Amazon (LWA) refresh token. These refresh tokens are securely stored in Secrets Manager. LWA refresh tokens are exchanged for LWA access tokens. The LWA access tokens, along with IAM and AWS STS, are used to securely make API calls to Amazon Vendor Central, leveraging well-defined user access permissions. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

This Guidance consists of serverless and fully managed services with built-in reliability due to a combination of a service-oriented architecture (like the use of Step Functions to create a serverless application) and microservices (where Step Functions uses AWS STS to execute the call). Selling Partner API requests are limited using the token bucket algorithm, so an API client is recommended for rate limiting. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Scalable and highly available services such as Amazon S3, Lambda, DynamoDB, and Amazon SQS are used as core components to increase performance. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

This architecture is designed with a serverless-first approach, leveraging services such as Step Functions, Lambda, DynamoDB, and Amazon S3 for cost efficiency. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Consisting of mostly serverless services, this Guidance reduces the number of resources consumed, contributing to greater sustainability. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

## Related content

- **Ingest Amazon Retail Data into a Serverless Modern Data Architecture**: This post provides an overview of a Retail and CPG client application leveraging Amazon Web Services, Inc. (AWS) serverless and managed services, and how to integrate that application with a Modern Data Architecture using SP-APIs.

[Learn more](https://aws.amazon.com/blogs/industries/ingest-amazon-retail-data-into-a-serverless-modern-data-architecture/)

[Read usage guidelines](/solutions/guidance-disclaimers/)
