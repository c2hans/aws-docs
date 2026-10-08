---
source_url: https://docs.aws.amazon.com/solutions/photo-search-on-aws/index.html
---

---
title: 'Guidance for Photo Search on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/photo-search-on-aws/
source: aws-documentation
generated_on: 2026-10-07
---

# Guidance for Photo Search on AWS

## Overview

This Guidance helps users organize and implement search capabilities so they can efficiently locate the right photo from a large library of images. This Guidance uses artificial intelligence and machine learning (AI/ML) to find the right photo for immediate utilization, such as an image of a celebrity, politician, or well-known expert. With this Guidance, users can register images of a person with their name, detect human faces in images, search and analyze millions of photos, and compare images against one another to determine similarities – all through a simple user interface to add and search for images.

## How it works

This architecture shows a robust automated registration method that catalogs millions of photos and implements search capabilities. This method can help you identify photos containing distinctive human faces.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/photo-search-on-aws.pdf)

![Architecture diagram](/images/solutions/photo-search-on-aws/images/photo-search-on-aws-1.png)

1. **Step 1**: An Amazon CloudFront distribution with a web console is hosted in Amazon Simple Storage Service (Amazon S3) along with AWS Amplify to provide the architecture's front-end web user interface (UI). AWS WAF is used for source IP restriction.
1. **Step 2**: An AWS Lambda function called through the Amazon API Gateway returns pre-signed URLs. All following requests to the API Gateway are authorized by Amazon Cognito.
1. **Step 3**: An S3 bucket stores your image library. Use the pre-signed URLs to upload images to the library.
1. **Step 4**: Uploading an image to Amazon S3 invokes a Lambda function. The Lambda function stores the metadata in Amazon OpenSearch Service and registers the image to Amazon Rekognition using the IndexFaces API.
1. **Step 5**: The register-name Lambda function assigns names to images. The set-tags Lambda function adds tags to images.
1. **Step 6**: The get-faces Lambda function searches the catalog of images against similar faces. It returns dimensions of faces detected in the image using the DetectFaces API.
1. **Step 7**: The get-similars Lambda function calls the SearchFacesByImage API to find images with faces similar to the one in the image the user specified. The function returns the images' URLs on Amazon S3.
1. **Step 8**: The get-photos Lambda function searches for images using names or tags. The function returns the images' URLs on Amazon S3 after it searches the URLs using OpenSearch Service.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

By choosing Lambda and Amazon S3, you can implement shared design standards. You can also use Amazon CloudWatch logs for Lambda to monitor your Lambda functions’ logs, troubleshoot issues, and create custom metrics based on log data. Additionally, you can enable Amazon S3 access logs to capture detailed information about every request made to the S3 bucket. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

This Guidance uses managed services to help you reduce security maintenance tasks, as part of the shared responsibility model. Managed services help you ensure AWS API calls are all done through HTTPS endpoints using transport layer security (TLS) communication, thus protecting data in transit. Data within Amazon Cognito is encrypted at rest in accordance with industry standards. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

API Gateway helps ensure highly available network connectivity for the public endpoint in this Guidance. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

With managed serverless services, you can offload the need to manage scaling requirements. For example, Lambda enables you to simply upload your code, and the service will manage everything required to run and scale that code. API Gateway handles all the tasks involved in accepting and processing up to hundreds of thousands of concurrent API calls. The distributed nature of OpenSearch Service enables this service to process large volumes of data in parallel to quickly find the best matches for your queries. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

This Guidance uses serverless services, such as Lambda with API Gateway, to remove the need to manage resources. With managed and serverless services, you can set attributes that help ensure you have sufficient capacity without paying for additional unused resources. You must set and monitor these attributes to keep your excess capacity to a minimum while still maximizing performance. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Managed services remove the need to identify periods of low or no resource usage. Examples of managed services in this Guidance include Lambda, Amazon S3, API Gateway, CloudFront, OpenSearch Service, Amazon Rekognition, Amazon Cognito, Amplify, and AWS WAF. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
