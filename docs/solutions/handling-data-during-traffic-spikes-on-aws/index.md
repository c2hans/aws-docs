---
source_url: https://docs.aws.amazon.com/solutions/handling-data-during-traffic-spikes-on-aws/index.html
---

---
title: 'Guidance for Handling Data during Traffic Spikes on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/handling-data-during-traffic-spikes-on-aws/
source: aws-documentation
generated_on: 2026-10-06
---

# Guidance for Handling Data during Traffic Spikes on AWS

## Overview

This Guidance shows how to handle sudden traffic spikes in Amazon Aurora using a mixed-configuration architecture that combines a provisioned Aurora cluster with Aurora Serverless v2 instances and custom auto-scaling. It demonstrates near real-time response to unpredictable traffic fluctuations, preventing database overload and service disruptions. With this Guidance, you can promote service continuity and protect against revenue loss from database-related outages, even with unexpected traffic spikes from marketing events or new product launches.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/handling-data-during-traffic-spikes-on-aws.pdf)

![Architecture diagram](/images/solutions/handling-data-during-traffic-spikes-on-aws/images/handling-data-during-traffic-spikes-on-aws-1.png)

1. **Step 1**: Add Amazon Aurora Serverless v2 (replica) to the Aurora Provisioned Cluster, and create each custom endpoint pointing to the replica.
1. **Step 2**: Configure a private hosted zone on Amazon Route 53, and create a weight-based record with the same record name for each endpoint. Set the weight of the record pointing to the Aurora Serverless v2 to zero.
1. **Step 3**: Enable the Enhanced Monitoring feature on all instances to automatically collect RDSOSMetrics information in Amazon CloudWatch.
1. **Step 4**: Create an AWS Lambda function that refines the information collected in the RDSOSMetrics log group to create custom metrics for the target instances for monitoring.
1. **Step 5**: Use aws-embedded-metric to push the refined custom metrics to CloudWatch in near-real time.
1. **Step 6**: Based on your stored custom metrics, configure CloudWatch alarms for weight adjustment.
1. **Step 7**: When the alarm for weight adjustment occurs, it calls AWS Step Functions. Step Functions adjusts the weight of the Route 53 record to distribute and recover traffic to Aurora Serverless v2.
1. **Step 8**: Set up an autoscaling policy based on the custom metric alarms collected using AWS Auto Scaling. When an autoscaling alarm occurs, it invokes autoscaling for the provisioned replica instance.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: The sample code is a starting point. It is industry validated, prescriptive but not definitive, and a peek under the hood to help you begin.

[Open sample code on GitHub](https://github.com/aws-solutions-library-samples/guidance-for-handling-data-during-traffic-spikes-on-aws)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

Aurora Serverless v2 enables automatic scaling through its serverless architecture, while AWS Auto Scaling dynamically adds provisioned instances to scale out read replicas. This Guidance allows for elastic scaling of resources up or down based on actual traffic demand, achieving cost efficiency and system stability simultaneously. Even during sudden traffic spikes, stable database performance can be maintained. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

CloudWatch logs encrypt and securely transfer log data, while AWS Identity and Access Management (IAM) grants the minimum required permissions to services and resources, following the principle of least privilege. By protecting log information and restricting access to only authorized entities, you can reduce the risk of security breaches and protect data integrity. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Aurora and Route 53 provide high availability and fault tolerance for databases through multi-Availability Zone (AZ) deployments and automatic failover capabilities. Route 53 weight-based routing distributes traffic efficiently to only healthy instances and enables rapid automated recovery and service continuity in the event of infrastructure failures. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Aurora Serverless v2 automatically scales computing resources during traffic spikes, improving read performance. Route 53 weight-based records dynamically route traffic to Aurora Serverless v2 instances, reducing load on provisioned instances. High-resolution CloudWatch custom metrics detect traffic spikes within 10 seconds, allowing for quick response and maintenance of application responsiveness and stability. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Aurora Serverless automatically responds to actual traffic patterns, eliminating costs from overprovisioning. AWS Auto Scaling provisions only the required number of Aurora read replicas. Custom CloudWatch metrics enable precise scaling decisions at the right time, preventing unnecessary resource wastage. Lambda functions incur costs only on an event-driven basis, further optimizing costs. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

The dynamic scaling capabilities of Aurora and Aurora Serverless v2 minimize environmental impact. These services provision only the resources required for actual workloads, preventing overprovisioning and wasted resources. By elastically scaling resources up and down based on actual demands, you can reduce energy consumption and associated carbon emissions. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

## Related content

- **How ktown4u built a custom auto scaling architecture using an Amazon Aurora mixed-configuration cluster to respond to sudden traffic spikes**: This blog post demonstrates how ktown4u built a custom auto scaling architecture using an Amazon Aurora mixed-configuration cluster to respond to sudden traffic spikes.

[Learn more](https://aws.amazon.com/blogs/database/how-ktown4u-built-a-custom-auto-scaling-architecture-using-an-amazon-aurora-mixed-configuration-cluster-to-respond-to-sudden-traffic-spikes/)

[Read usage guidelines](/solutions/guidance-disclaimers/)
