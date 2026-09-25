---
source_url: https://docs.aws.amazon.com/solutions/enterprise-contact-center-user-management-on-amazon-connect-customer/index.html
---

---
title: 'Guidance for Enterprise Contact Center User Management on Amazon Connect Customer'
canonical_url: https://docs.aws.amazon.com/solutions/enterprise-contact-center-user-management-on-amazon-connect-customer/
source: aws-documentation
generated_on: 2026-09-25
---

# Guidance for Enterprise Contact Center User Management on Amazon Connect Customer

## Overview

This Guidance helps enterprise contact centers maintain consistent user data across large-scale Amazon Connect Customer deployments with thousands of agents through automated synchronization and bulk update capabilities. The approach combines scheduled incremental syncing every 15 minutes with event-driven updates that capture real-time user changes, ensuring data consistency across distributed contact center instances. Administrators can initiate bulk user updates through a web application while automated processes handle full data retrieval and queue processing to keep Amazon Connect Customer user information current. You can reduce manual administrative overhead, eliminate data inconsistencies, and scale your contact center operations efficiently across multiple Amazon Connect Customer instances.

## Benefits

### Streamline agent management

Deploy a comprehensive user management framework that synchronizes agent data across multiple Amazon Connect Customer instances. Reduce administrative overhead while maintaining consistent agent profiles through automated real-time and batch processes.

### Enhance operational agility

Respond quickly to changing contact center needs with event-driven updates and scheduled synchronization processes. Enable administrators to implement bulk changes efficiently through a web application, improving productivity and reducing manual configuration tasks.

### Scale with confidence

Support thousands of contact center agents with a resilient architecture that handles both real-time events and scheduled updates. Leverage serverless AWS services that automatically scale to accommodate growing agent populations without performance degradation.

## How it works

Guidance for user management and synchronization framework for contact centers managing 1000s of agents across Amazon Connect Customer instances

[Download the architecture diagram](downloads/enterprise-contact-center-user-management-on-amazon-connect-customer.pdf)

![Architecture diagram](/images/solutions/enterprise-contact-center-user-management-on-amazon-connect-customer/images/enterprise-contact-center-user-management-on-amazon-connect.png)

1. **Step 1**: Full Users Data Pull - AWS Lambda initiates a complete user data retrieval from Amazon Connect Customer. Retrieved data is queued in Amazon Simple Queue Services (Amazon SQS) for processing.
1. **Step 2**: Scheduled Incremental Sync (Every 15 Minutes) - Amazon EventBridge triggers on a 15-minute schedule and AWS Lambda executes incremental synchronization logic. Changed data is sent to Amazon SQS queue.
1. **Step 3**: Event-Driven Updates - Amazon Connect Customer generates real-time user events and Amazon EventBridge captures and routes these events. Events are queued in Amazon SQS.
1. **Step 4**: Bulk User Update - Amazon Connect Customer Admin users initiates bulk changes through User Management Web Application via Amazon CloudFront. CloudFront invokes Bulk Amazon API gateway and AWS Lambda. And the update requests are queued in Amazon SQS.
1. **Step 5**: An AWS Lambda function processes the data from Amazon SQSs and update Amazon Connect Customer.
[Read usage guidelines](/solutions/guidance-disclaimers/)
