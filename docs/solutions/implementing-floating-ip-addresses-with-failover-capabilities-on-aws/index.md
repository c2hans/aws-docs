---
source_url: https://docs.aws.amazon.com/solutions/implementing-floating-ip-addresses-with-failover-capabilities-on-aws/index.html
---

---
title: 'Guidance for Implementing Floating IP Addresses with Failover Capabilities on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/implementing-floating-ip-addresses-with-failover-capabilities-on-aws/
source: aws-documentation
generated_on: 2026-10-06
---

# Guidance for Implementing Floating IP Addresses with Failover Capabilities on AWS

## Overview

This Guidance demonstrates how to implement floating IP addresses in AWS Cloud environments, offering a robust high-availability approach when traditional methods like DNS updates or multi-Availability Zone (AZ) network load balancers aren't options. The approach maintains system accessibility through a single, static IP address while enabling seamless failover across AZs—crucial for organizations with strict compliance requirements or technical constraints. The Guidance significantly reduces application downtime and simplifies network management by eliminating the need to update multiple IP addresses across infrastructure during failover events.

## Benefits

### Strengthen application reliability automatically

Implement health monitoring and automated failover without manual intervention. Use static IP addresses for use cases where alternative, managed approaches don't fit.

### Maximize operational insights

Gain visibility about the current and historical health of the application. Operate with confidence, based on data. Utilize systematic, automated processes to achieve high availability.

### Optimize resource utilization costs

Eliminate idle infrastructure costs through event-driven architecture. Pay only for actual failover operations while maintaining continuous availability protection.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/implementing-floating-ip-addresses-with-failover-capabilities-on-aws.pdf)

![Architecture diagram](/images/solutions/implementing-floating-ip-addresses-with-failover-capabilities-on-aws/images/implementing-floating-ip-addresses-with-failover-capabilities-on-aws-1.png)

1. **Step 1**: A client application connects to the target system through the floating IP address.
1. **Step 2**: An Amazon EventBridge scheduler invokes the AWS Step Functions flow every minute to orchestrate health checks and the failover process for the floating IP address (when applicable).
1. **Step 3**: The Step Functions workflow implementation iterates its tasks every N seconds, where N is configurable.
1. **Step 4**: As an initial step, the stored context (probing counter and last probing result) from the previous Step Functions workflow implementation is retrieved from Amazon DynamoDB.
1. **Step 5**: The AWS Lambda probing function is invoked, and context from its previous implementation is passed as an input.
1. **Step 6**: The Lambda probing function checks the health of the target of the floating IP address, which was initially set in the primary subnet and corresponding elastic network interface (ENI) attached to Amazon Elastic Compute Cloud (Amazon EC2). It then returns the probing result to the Step Functions implementation.
1. **Step 7**: The Lambda probing function logs metrics (such as response time and number of failed probes) to Amazon CloudWatch.
1. **Step 8**: If the set threshold of failed health checks (a deployment parameter) is reached, Step Functions initializes the failover procedure. The Lambda failover function is invoked to handle the failover process.
1. **Step 9**: The Lambda failover function updates one or more Amazon Virtual Private Cloud (Amazon VPC) route tables. It changes the target ENI attached to Amazon EC2 of the route associated with the floating IP address to the one set in a secondary subnet.
1. **Step 10**: The Lambda failover function logs failover count metrics to CloudWatch.
1. **Step 11**: By the end of the Step Functions workflow implementation, the implementation context is stored in the DynamoDB database.
1. **Step 12**: All relevant metrics stored in CloudWatch can be used to build comprehensive dashboards and create alarms for observability purposes.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-using-floating-virtual-fixed-ip-address-with-load-balancing-on-aws)

[Read usage guidelines](/solutions/guidance-disclaimers/)
