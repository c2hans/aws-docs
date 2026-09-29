---
source_url: https://docs.aws.amazon.com/solutions/using-google-tag-manager-for-server-side-website-analytics-on-aws/index.html
---

---
title: 'Guidance for Using Google Tag Manager for Server-Side Website Analytics on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/using-google-tag-manager-for-server-side-website-analytics-on-aws/
source: aws-documentation
generated_on: 2026-09-29
---

# Guidance for Using Google Tag Manager for Server-Side Website Analytics on AWS

Enhance real-time data analytics to get better insights on website interactions

## Overview

This Guidance helps you implement server-side tagging to collect event data and perform data analysis in near real-time. You can then ingest this data to both AWS and Google Analytics™ services. Server-side tagging is a new way to use Google Tag Manager to instrument your application across devices. Server containers use the same tag, trigger, and variable model that customers have already been using, while also providing new tools that allow you to measure user activity. This Guidance deploys a Google Tag Manager server-side container to Amazon Elastic Container Service (Amazon ECS) and provides the necessary infrastructure to collect event data from a test website and emit event data to AWS analytics services.

## How it works

### How it works

This architecture diagram demonstrates how to use Amazon API Gateway to build a near-real time website activity data collection and analytics stack on AWS with Google’s Server Side Tagging Service.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/using-google-tag-manager-for-server-side-website-analytics-on-aws.pdf)Step 1The Google Tag Manager user interface (UI) acts as the control plane. The UI configures pixel tags that capture business-relevant user interactions on web properties in Server Side Tagging mode.Step 2As users interact with the website, the pixel code loaded in the browser from the Google Tag Manager configuration fires events.Step 3Amazon Route 53 and Application Load Balancer send these events to a backend service.Step 4Google's Server Side Tag Manager Service is deployed on Amazon Elastic Container Service (Amazon ECS). The Server Side Tagging Service acts as the data collector and receives events from Application Load Balancer.Step 5The Server Side Tagging Preview Service deployed on Amazon ECS tests and previews the tag configuration. This service is connected to the client side and the Server Side Tagging Service through an Application Load Balancer and Route 53 private hosted zone DNS record.Step 6The Server Side Tagging Service sends HTTPS Post requests to an internal, private Amazon API Gateway endpoint. This endpoint is connected to the Amazon Virtual Private Cloud (Amazon VPC) with an interface endpoint.Step 7These events are also sent to the Google Analytics service and any third-party data collectors that are already in use, requiring no changes to the front-end code.Step 8Amazon Kinesis Data Steams receives requests from API Gateway through a direct integration.Step 9Amazon Data Firehose receives data from Kinesis Data Streams and stores it in an Amazon Simple Storage Service (S3) bucket for long-term storage and historical or ad-hoc analysis.Step 10Optionally, use AWS Lambda with Data Firehose to enrich events or remove sensitive data from the events before storing them in Amazon S3.Step 11AWS Glue Crawler and AWS Glue Data Catalog capture the metadata, enabling Amazon Athena to query the data.Step 12Amazon QuickSight builds interactive dashboards and uses Athena to query data.Step 13Lambda is configured to act as a secondary receiver of the same Kinesis Data Streams event stream.Step 14The Lambda function, integrated with Kinesis Data Streams, loads data into Amazon OpenSearch Service for near real-time analysis and observability.Step 15Website event data stored in Amazon S3 serves as a foundation for building a customer 360 profile, web personalization using Amazon Personalize, privacy-enhanced data collaboration with advertising partners using AWS Clean Rooms, and artificial intelligence and machine learning (AI/ML) use cases.### How it works

This architecture diagram demonstrates how to use Amazon Kinesis Producer Service to build a near-real time website activity data collection and analytics stack on AWS with Google’s Server Side Tagging Service.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/using-google-tag-manager-for-server-side-website-analytics-on-aws.pdf)Step 1The Google Tag Manager user interface (UI) acts as the control plane. The UI configures pixel tags that capture business-relevant user interactions on web properties in Server Side Tagging mode.Step 2As users interact with the website, the pixel code loaded in the browser from the Google Tag Manager configuration fires events.Step 3Amazon Route 53 and Application Load Balancer send these events to a backend service.Step 4Google's Server Side Tag Manager Service is deployed on Amazon Elastic Container Service (Amazon ECS). The Server Side Tagging Service acts as the data collector and receives events from Application Load Balancer.Step 5The Server Side Tagging Preview Service deployed on Amazon ECS tests and previews the tag configuration. This service is connected to the client side and the Server Side Tagging Service through an Application Load Balancer and Route 53 private hosted zone DNS record.Step 6The Server Side Tagging Service sends events to third-party collectors, Google Analytics, and Amazon Kinesis Producer Service.Step 7Kinesis Producer Service then sends events to Amazon Kinesis Data Steams using an Amazon VPC endpoint.Step 8Amazon Data Firehose receives data from Kinesis Data Streams and stores it in an Amazon Simple Storage Service (S3) bucket for long-term storage and historical or ad-hoc analysis.Step 9Optionally, use AWS Lambda with Data Firehose to enrich events or remove sensitive data from the events before storing them in Amazon S3.Step 10AWS Glue Crawler and AWS Glue Data Catalog capture the metadata, enabling Amazon Athena to query the data.Step 11Amazon QuickSight builds interactive dashboards and uses Athena to query data.Step 12Lambda is configured to act as a secondary receiver of the same Kinesis Data Streams event stream.Step 13The Lambda function, integrated with Kinesis Data Streams, loads data into Amazon OpenSearch Service for near real-time analysis and observability.Step 14Website event data stored in Amazon S3 serves as a foundation for building a customer 360 profile, web personalization using Amazon Personalize, privacy-enhanced data collaboration with advertising partners using AWS Clean Rooms, and artificial intelligence and machine learning (AI/ML) use cases.## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Dive deep into the implementation guide for additional customization options and service configurations to tailor to your specific needs.

[Open guide](https://aws-solutions-library-samples.github.io/advertising-marketing/using-google-tag-manager-for-server-side-website-analytics-on-aws.html)
[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-using-google-tag-manager-for-server-side-website-analytics-on-aws)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

This Guidance provides built-in observability. Each service in this Guidance publishes metrics to Amazon CloudWatch, through which you can configure dashboards and alarms. You can then use alarms or Amazon Simple Notification Service (Amazon SNS) to notify incident management systems of events and escalate based on event severity. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

The data at rest in the S3 bucket is encrypted using AWS Key Management Service (AWS KMS) keys. The data in transit is encrypted and transferred over HTTPS. The Amazon ECS clusters run in an Amazon VPC. The connectivity between Amazon ECS clusters also run in Amazon VPC, and the connectivity between Amazon ECS and API Gateway is routed through a secure Amazon VPC interface endpoint. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

You can use OpenSearch Service-automated snapshots for backup and recovery. You can back up Kinesis Data Firehose data to Amazon S3, and static content is stored in Amazon S3, which offers industry-leading storage durability. Amazon ECS clusters come with capabilities to stop non-responding containers and create new ones that handle incoming traffic without manual interventions. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

All components of this Guidance are co-located in a single AWS Region and multiple Availability Zones. This Guidance also uses a serverless stack so that you don’t have to make infrastructure decisions about locations, aside from your choice of Region and Availability Zone. You can use automated deployments to deploy the Guidance components into any Region quickly, providing you with reduced latency and support for data residency requirements. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

This Guidance uses a multi-Availability Zone deployment to support the high availability and resilience requirements for server-side tagging and the near real-time event collection workload. There will be charges for data transfer within the Region and charges for data transfer out to Google Analytics™ service and each third-party collector service. As an industry standard, we recommend estimating your data transfer out charges early on in the deployment. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

All of the services used in this architecture are managed services. With Amazon ECS, you can horizontally scale and implement an elastic scaling mechanism. Additionally, by decoupling microservices within the architecture, you can scale services in a way that allocates instance types and number of instances based on the exact amount of resources used by your workloads. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

## Related content

- **Guidance for Near Real-Time Personalized Recommendations on AWS**: This Guidance helps businesses build a real-time recommendation pipeline using Amazon Personalize.

[Learn more](https://aws.amazon.com/solutions/guidance/near-real-time-personalized-recommendations-on-aws/)

- **Clickstream Analytics on AWS**: This solution collects, ingests, analyzes, and visualizes clickstream data from your websites and mobile applications

[Learn more](/solutions/clickstream-analytics-on-aws/)

[Read usage guidelines](/solutions/guidance-disclaimers/)
