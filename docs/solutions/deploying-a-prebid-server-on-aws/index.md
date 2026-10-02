---
source_url: https://docs.aws.amazon.com/solutions/deploying-a-prebid-server-on-aws/index.html
---

---
title: 'Guidance for Deploying a Prebid Server on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/deploying-a-prebid-server-on-aws/
source: aws-documentation
generated_on: 2026-10-02
---

# Guidance for Deploying a Prebid Server on AWS

## Overview

This Guidance demonstrates how publishers can address the challenge of efficiently capturing and processing bids from multiple demand sources for their ad units by implementing a highly-available, multi-region prebid server deployment that scales automatically with demand. The system validates incoming traffic through CloudFront and WAF protection before distributing requests across containerized prebid servers that send concurrent bid requests to multiple bidders simultaneously. CloudWatch monitoring enables automatic scaling of the container cluster as traffic patterns change, while ElastiCache stores bid responses and creative content for fast retrieval during ad auctions. You can deploy changes to your prebid infrastructure in minutes while maintaining high availability across regions and automatically scaling to handle traffic spikes without manual intervention.

## Benefits

### Protect ad revenue at the edge

Defend your programmatic auctions from invalid traffic and DDoS attacks using integrated edge security, so you protect bid integrity and maximize monetizable impressions for every publisher.

### Scale auctions without managing servers

Run Prebid Server on containerized, auto-scaling infrastructure so your platform handles traffic spikes automatically, reducing operational overhead and keeping latency low during peak demand.

### Unlock deep auction performance insights

Automatically collect, transform, and catalog auction metrics from every container so you can query granular bidding data and make faster, data-driven yield optimization decisions.

## How it works

### Prebid server deployment

This architecture diagram illustrates how to effectively support Prebid server deployment on AWS. It shows the key components and their interactions,providing an overview of the architecture's structure and functionality.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/deploying-a-prebid-server-on-aws.pdf)Step 1A user browses to a page on a website that hosts ads. The publisher site returns the page source to the browser with resources, and one or more script modules (also called wrappers) that enable real-time bid requests and responses for ads of given dimensions, types, topics, and other criteria.Step 2The ad requests are received from the browser at the Amazon CloudFront endpoint integrated with AWS Web Application Firewall (AWS WAF) for entry into the solution. This step helps validate legitimate traffic from malicious requests, such as penetration or denial-of-service attempts. Traffic can be received here as HTTP or HTTPS.Step 3The request is forwarded to Application Load Balancer (ALB). ALB determines which container running Prebid Server in the cluster is at a utilization level that can accept more requests. ALB has a network interface on the public internet and one in each private subnet where containers are hosted within Amazon Virtual Private Cloud (Amazon VPC).Step 4The request arrives at an Amazon Elastic Container Service (Amazon ECS) container, is parsed and validated, and requests to different bidding services are sent concurrently to the internet through the default internet gateway.Step 5The NAT gateway and Internet gateway allow containers to initiate outbound requests to the internet and receive responses. These resources are primarily used for Prebid Server containers to request and gather bids for ad auctions.Step 6Bidders receive one or more bid requests over the internet from a Prebid Server container. Bidders respond with zero or more bids for the various requests. The response, including the body of the winning creative(s), is sent back to the browser.Step 7The optional custom Prebid adapter code sends bid request to a simulated bidder through AWS RTB Fabric Service. The adapter sends the requests through the AWS RTB Fabric configured Elastic Network Interface (ENI)Step 8The bid request passes through the AWS RTB Fabric Requester Gateway resource to the Responder Gateway of the bidder simulator applicationStep 9The AWS RTB Fabric Responder Gateway routes this request to the Application Load balancer of the Bidder simulator application and to the lambda function that processes the request and sends back bid response.Step 10The Prebid server completes the auction, stores the bid response information along with Ad creative details in an Amazon ElastiCache Serverless cluster. The read and write of cache items from the Prebid server and Prebid.js code through the AWS CloudFront and external load balancer and allows storage and retrieval of ad creative content including VAST tagsStep 11During normal operation, Amazon CloudWatch metrics are collected from various resources involved in handling requests and responses through the solution. As the load changes throughout the cluster, CloudWatch alarms are used to determine when to scale-out or scale-in the container cluster.Step 12An Amazon Elastic Container Service(ECS) service definition (Prebid ECS service) is responsible for tracking the health of the cluster, performing scale-out and scale-in operations, and managing the collection of containers available for ALB. The Prebid ECS service uses AWS Fargate instances.Step 13The Prebid server auction metrics are collected though an optional Custom Prebid adapter for log analytics component. Detailed architecture of log analytics is explained in the next page.Step 14The optional demo website runs Prebid.js and allows publishers to quickly do an end-to-end test of the Prebid server deployment with banner, instream and outstream video ads.### Prebid server container auction metrics

This architecture diagram illustrates how the Prebid server container auction metrics are collected and organized to allow publishers to have access todeep insights about the auctions and full control of their yield optimization.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/deploying-a-prebid-server-on-aws.pdf)Step 1Metrics log files for each container are stored to a shared Amazon Elastic File System (Amazon EFS) using NFS protocol. This file system is mounted to each Prebid Server container during start-up. A single metrics log file is written for a limited time and then closed and rotated, so that it can be included in the next stage of processing. EFS is used as temporary locationStep 2AWS DataSync replicates rotated log files from EFS to Amazon Simple Storage Service (Amazon S3) on a recurring schedule. DataSync verifies each transferred file and provides a report of the completed work to an AWS Lambda function.Step 3The DataSync Logs S3 bucket receives the replicated log files from EFS using the same folder structure. Log files arrive in this bucket because of the DataSync process. An AWS Lambda function runs after the DataSync process completes in step 12 and removes transferred and verified log file data from EFS.Step 4An AWS Glue job performs an ETL operation on the metrics data in the DataSync Logs S3 bucket.Step 5The ETL operation structures the metric data into a single database with several tables, partitions the physical data, and writes it to an S3 bucket. The Metrics S3 bucket contains the metric log data transformed and partitioned through ETL.Step 6The data in this bucket is made available to AWS Glue clients for queries. Many different types of clients use AWS Glue Data Catalog to access the Prebid Server metric data.## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **We'll walk you through it**: Dive deep into the implementation guide for additional customization options and service configurations to tailor to your specific needs.

[Open guide](/solutions/latest/prebid-server-deployment-on-aws/solution-overview.html?refid=sl_card)

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/prebid-server-deployment-on-aws)

[Read usage guidelines](/solutions/guidance-disclaimers/)
