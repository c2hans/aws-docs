---
source_url: https://docs.aws.amazon.com/solutions/cross-region-failover-and-graceful-failback-on-aws/index.html
---

---
title: 'Guidance for Cross Region Failover & Graceful Failback on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/cross-region-failover-and-graceful-failback-on-aws/
source: aws-documentation
generated_on: 2026-09-29
---

# Guidance for Cross Region Failover & Graceful Failback on AWS

## Overview

This Guidance helps customers design a resilient three-tier web application with a React front end, API/AWS Lambda middle tier, and Amazon Aurora global database back end. The application is deployed across two AWS Regions for automated failover and failback from one Region to another, achieving active and warm standby disaster recovery patterns. Additionally, Amazon CloudWatch supports observability instrumentation for this multi-Region architecture by obtaining insights from application stacks and aggregating them with relevant infrastructure metrics, which can help customers decide when to failover the application to another Region. Amazon Route53 Application Recovery Controller routes traffic between multiple Regions and automates failover through integration with AWS Systems Manager documents.

## How it works

### Application Running in Primary Region

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/cross-region-failover-and-graceful-failback-on-aws.pdf)Step 1The user opens the browser and enters the UI domain name system (DNS) endpoint hosted on Amazon Route 53.Step 2The request is routed to the Amazon CloudFront instance. The data plane for CloudFront is globally available.Step 3CloudFront delivers static content stored in Amazon Simple Storage Service (Amazon S3) buckets in the primary region (or, if it is not available, the secondary region in failover mode).Step 4CloudFront is protected by AWS WAF, which is configured with standard rules to protect against common web exploits.Step 5The UI is authenticated by an Amazon Cognito user pool configured in the primary region. Amazon Cognito is a regional service. If there is degradation or an outage in the Amazon Cognito service in the primary region, this may impact application failover.Step 6The Amazon Route 53 DNS-hosted zone is powered by Route 53 Application Recovery Controller (ARC), which contains an ARC control for the primary and secondary regions. The ARC controls the respective health checks, which power the respective DNS records in a Route 53-hosted zone. Initially, the primary region ARC control is turned on and the secondary region ARC control is turned off.Step 7The primary region health check becomes healthy and the secondary region health check becomes unhealthy. Consequently, the Route 53 API DNS endpoint resolves to the API endpoint in the primary region.Step 8The API endpoint in the primary region delegates the calls to corresponding AWS Lambda functions running in the primary region.Step 9The application uses an Amazon Aurora global database to store application transaction data. Initially, the primary Aurora database cluster is configured as the writer cluster, and the secondary Aurora database cluster is configured as a reader cluster. The primary Aurora database cluster automatically replicates data to the secondary Aurora database cluster, which enables the application to run from the secondary region (using the data replicated from primary database cluster to secondary database cluster).### Cross Region Failover

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/cross-region-failover-and-graceful-failback-on-aws.pdf)Step 1The user clicks the "Failover" button in the UI, which invokes the failover API endpoint hosted on Route 53.Step 2The Amazon Route 53 DNS-hosted zone routes to the API endpoint in the primary region based on the state of the Route 53 ARC controls.Step 3The primary API endpoint is invoked.Step 4The primary API endpoint delegates the invocation to the corresponding AWS Lambda function running in the primary region.Step 5The Lambda function calls the failover runbook, automated as an AWS Systems Manager Document. The runbook automates the three steps involved with the failover process.Step 6The runbook first fails over the Amazon Aurora global database from the primary to secondary regions, making the database cluster in the secondary region the writer cluster and the database cluster in the primary region the reader cluster.Step 7After failover, the Aurora global cluster is configured to automatically replicate data from the database cluster in the secondary region (writer) to the database cluster in the primary region (reader).Step 8The runbook updates the database secret in AWS Secrets Manager with the database endpoint of the Aurora database cluster in the secondary region so that Lambda functions use the new database endpoint to interact with the database.Step 9The runbook flips the Route 53 ARC controls, turning the ARC control for the primary region off and turning ARC control for the secondary region on. As a result, the secondary region health check becomes healthy and the primary region health check becomes unhealthy. Route 53 API DNS endpoint resolves to the API endpoint in the secondary region. This completes the failover. The application will be live in the secondary region, routing API traffic to the secondary region. It invokes Lambda functions in the secondary region, which interacts with the Aurora database cluster in the secondary region.## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-crossregion-failover-and-graceful-failback-and-observability-on-aws)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

This Guidance supports operational excellence by making sure that the business can continue to run business services through failover to a secondary region. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

Use WAF with CloudFront to protect application from common vulnerabilities and use Amazon Cognito to authenticate UI and API access. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Automate failure monitor workload’s key performance indicators (KPIs) and trigger automated failover when a threshold is breached. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Cost Optimization

Use Amazon API Gateway and Lambda to process transactions in order to avoid provisioned compute resources. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

This Guidance is serverless and minimizes your carbon footprint. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

## Related content

- **Video**: AWS Guidance for Resilience Use Cases

[Read usage guidelines](/solutions/guidance-disclaimers/)
