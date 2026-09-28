---
source_url: https://docs.aws.amazon.com/solutions/building-a-spot-placement-score-tracker-dashboard-on-aws/index.html
---

---
title: 'Guidance for Building a Spot Placement Score Tracker Dashboard on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/building-a-spot-placement-score-tracker-dashboard-on-aws/
source: aws-documentation
generated_on: 2026-09-28
---

# Guidance for Building a Spot Placement Score Tracker Dashboard on AWS

## Overview

This Guidance shows how to build an Amazon Elastic Compute Cloud (Amazon EC2) Spot placement score tracker to monitor unused Amazon EC2 Spot Instance capacity. Those who use Spot Instances often have questions about configuring workloads for optimal resilience and savings. Key questions include which instances to use, whether to diversify across instance types and Availability Zones (AZs), which Regions work best for particular configurations, and how time of day impacts capacity. Running cloud workloads cost-effectively on Spot Instances requires flexibility across these dimensions. This Guidance helps provide those answers by automatically tracking real-time capacity metrics across Regions, AZs, and instance types. The result is that you gain insights that can guide you on instance choice, workload placement, and diversity strategies that align with AWS best practices for fault-tolerant Spot Instance usage.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/building-a-spot-placement-score-tracker-dashboard-on-aws.pdf)

![Architecture diagram](/images/solutions/building-a-spot-placement-score-tracker-dashboard-on-aws/images/building-a-spot-placement-score-tracker-dashboard-on-aws-1.png)

1. **Step 1**: An Amazon EventBridge cron expression invokes the AWS Lambda function spotPlacementScoresLambda every 5 minutes. This updates the Spot placement scores displayed on Amazon CloudWatch dashboards.
1. **Step 2**: The Lambda function retrieves dashboard configuration files in YAML format from Amazon Simple Storage Service (Amazon S3).
1. **Step 3**: The Lambda function handles batches of metric requests. For each request, it queries the Amazon Elastic Cloud Compute (Amazon EC2) API's Spot placement score feature to obtain a Spot placement score.
1. **Step 4**: The Lambda function receives Spot placement score responses. It then creates and stores metrics in CloudWatch based on a metrics configurations specified in the project Metric configuration (Metric conf.) file.
1. **Step 5**: CloudWatch collects metrics for various workloads as specified in the Metric conf. file. These metrics populate the CloudWatch Spot placement score dashboards. Users can access these dashboards to optimize their Amazon EC2 Spot Instance Requests.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: A detailed guide is provided to experiment and use within your AWS account. Each stage of building the Guidance, including deployment, usage, and cleanup, is examined to prepare it for deployment. The sample code is a starting point. It is industry validated, prescriptive but not definitive, and a peek under the hood to help you begin.

[Open implementation guide](https://aws-solutions-library-samples.github.io/compute/building-a-spot-placement-score-tracker-dashboard-on-aws.html)
[Open sample code on GitHub](https://github.com/aws-solutions-library-samples/guidance-for-ec2-spot-placement-score-tracker)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

The Spot placement score is a valuable metric that indicates how likely a Spot Instance request will succeed in a particular AWS Region or Availability Zone. This Guidance uses several AWS services to enable automated tracking and visualization of the Spot placement score for improving workload optimization. CloudWatch stores the Spot placement score metrics while also providing monitoring capabilities and dashboards to analyze the historical data. Amazon S3 hosts the dashboard configuration files in a durable and scalable storage layer. And the Lambda functions automate key steps through responsive serverless processing. Together, these services enhance operational excellence by boosting efficiency, reliability, and responsiveness within dynamic Spot-based workloads. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

AWS Identity and Access Management (IAM) is used to control and manage access to AWS services and resources, limiting access to only authorized users. IAM roles and policies are scoped down to the minimum permissions required. The Lambda function is also configured to run with least privilege access, meaning it has only the permissions necessary to perform its tasks, reducing the risk of unauthorized access to other resources. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Amazon EC2 Spot placement scores provide personalized recommendations on the optimal AWS Region or Availability Zone based on reliability requirements and real-time Spot capacity. This is made possible through a number of AWS Services with capabilities for computing, storing, and monitoring the metrics for Spot Instances. For example, Lambda is a service that enables the consistent, scheduled collection of Spot placement scores every 5 minutes. This serverless service scales automatically as needed. Also, Amazon S3 is a service that provides durable and fault-tolerant storage for both the Spot placement score metrics and the dashboard configuration data. Lastly, CloudWatch is a service that monitors this solution end-to-end, sending you alerts for quick issue detection. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

The EventBridge event bus invokes the Lambda function on a scheduled basis to collect Amazon EC2 Spot placement scores, which provide optimized recommendations for Spot Instance requests. EventBridge seamlessly connects the data flows between services, while Lambda minimizes manual tasks to boost efficiency. CloudWatch aids optimization through surveillance, allowing you to visualize performance over time. This serverless automation provides consistent metrics to inform ideal workload placement, while the monitoring capability allows for ongoing refinement of resource utilization. By leveraging these capabilities, the Spot placement score feature ensures Spot Instance resources are fully utilized and cost savings are achieved through proper capacity planning. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

The recommended services demonstrated throughout this Guidance provide cost-effective solutions tailored to meet the diverse needs of your workloads. For example, Amazon S3 provides cost-efficient storage for metrics and dashboards, enabling pay-as-you-go data access to inform analysis and planning. Lambda allows for automation costs to align with workloads through utilization-based billing. CloudWatch eliminates unnecessary expenditures by storing only essential infrastructure metrics. And finally, Amazon EC2 Spot placement scoring optimizes instance deployment, reducing spending by up to 90 percent. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Less computing overall lowers your carbon footprints organization-wide by maximizing resource utility. Here, Amazon S3 has the capability to store data in tiers to help optimize resource utilization, while the serverless compute capability of Lambda aligns usage with your workload needs. These services minimize waste and promote high infrastructure utilization, which are critical for sustainable workloads. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

## Related content

- **Optimizing Amazon EC2 Spot Instances with Spot Placement Scores**: This blog post demonstrates how to use Spot placement scores to reduce interruptions, acquire greater capacity, and identify optimal configurations, times, and locations to run workloads on Spot Instances.

[Optimizing Amazon EC2 Spot Instances with Spot Placement Scores](https://aws.amazon.com/blogs/compute/optimizing-amazon-ec2-spot-instances-with-spot-placement-scores/)

[Read usage guidelines](/solutions/guidance-disclaimers/)
