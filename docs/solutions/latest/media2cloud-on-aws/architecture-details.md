---
source_url: https://docs.aws.amazon.com/solutions/latest/media2cloud-on-aws/architecture-details.html
---

# Architecture details
<a name="architecture-details"></a>

 The AWS CloudFormation template deploys three logical components: a front-end web application, orchestration workflows (ingestion and analysis), and data storage. The web application provides an interface for customers to upload media content, and view and manage their archive collection. The ingestion and analysis workflows are initiated when a customer uploads content to the application. The ingestion workflow orchestrates tasks to ingest source videos, images, audio, and documents in a serverless manner. The analysis workflow analyzes and extracts machine learning metadata from content. When you upload a media asset to the Amazon S3 ingestion bucket, the ingestion workflow creates a standardized proxy file and thumbnails for analysis. The analysis workflow analyzes the content and extracts metadata using AWS AI services.

 The Amazon S3 ingestion bucket has an [Amazon S3 lifecycle policy](https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lifecycle-mgmt.html) that allows the solution to move uploaded videos and images to [Amazon Simple Storage Service Glacier](https://aws.amazon.com/glacier/) (Amazon Glacier) for archiving. Additionally, the AWS CloudFormation template deploys multiple Amazon DynamoDB tables to store metadata about each processed content, such as *pointers* to where its proxy files are stored in Amazon S3 and the types of AI/ML analysis performed on it. The solution also deploys an Amazon OpenSearch Service cluster that allows customers to search and discover technical media metadata or AI/ML generated metadata.
