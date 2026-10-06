---
source_url: https://docs.aws.amazon.com/solutions/deep-application-observability-on-aws/index.html
---

---
title: 'Guidance for Deep Application Observability on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/deep-application-observability-on-aws/
source: aws-documentation
generated_on: 2026-10-05
---

# Guidance for Deep Application Observability on AWS

## Overview

This Guidance demonstrates observability in applications to get deeper insights from application stacks and infrastructure metrics. To improve resiliency across two AWS Regions, it is essential to monitor application and infrastructure components across the entire stack.

## How it works

Monitoring application and infrastructure components in Amazon Web Services (AWS) to improve resiliency across two AWS Regions requires deep monitoring across the entire stack. Absolute failures, grey failures, and service degradation need to be observed across both Regions and coupled with automated alerting and actioning.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/deep-application-observability-on-AWS.pdf)

![Architecture diagram](/images/solutions/deep-application-observability-on-aws/images/deep-application-observability-on-aws-1.png)

1. **Step 1**: All appropriate business and infrastructure metrics are collected using Amazon CloudWatch.
1. **Step 2**: Application-level logic, like in AWS Lambda, can be collected using specific monitoring services, such as AWS X-Ray.
1. **Step 3**: Amazon Route 53 health checks are used to monitor appropriate endpoints.
1. **Step 4**: Amazon CloudWatch metrics, logs, and alarms are displayed on Amazon CloudWatch dashboards.
1. **Step 5**: Amazon CloudWatch metrics, logs, and alarms are displayed on Amazon CloudWatch dashboards across Regions. Amazon CloudWatch instances are replicated across regions.
1. **Step 6**: AWS Systems Manager Automation runbooks are initiated on service degradation, grey failures, and absolute failures. They can be used to run tasks and notify the site reliability engineering (SRE) team.
1. **Step 7**: Upon receiving the notification, the SRE team can signal the Amazon Route 53 Application Recovery Controller to point to the secondary cluster and follow relevant failover procedures.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: The sample code is a starting point. It is industry validated, prescriptive but not definitive, and a peek under the hood to help you begin.

[Open sample code on GitHub](https://github.com/aws-solutions-library-samples/guidance-for-crossregion-failover-and-graceful-failback-and-observability-on-aws)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

Deep application observability (DAO) ensures that application observability is carried at every layer of your workload: infrastructure, application, and business metrics. What you monitor depends on your organizational KPIs and SLAs. It helps customers prepare for potential service degradations and/or region-level failures and operate with efficiency and automation where applicable. As customers get more familiar with key metrics related to their application, they can evolve further by potentially incorporating automated systems with other existing SOPs to handle a full regional failure as needed (often as an audit/compliance requirement). [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

All logs are encrypted at rest using AWS Key Management Service (AWS KMS). Access to the dashboards and any automated tasks running as a result of alarms will practice the principle of least privilege and only have the appropriate policies attached to their roles. Moreover, changing alarm thresholds, automated tasks, and other actions should be done by the appropriate personnel only. Changes should go through a change review process to ensure that business SLAs are always respected, and infrastructure metrics are leveraged to ensure business goals are met. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

DAO guidance aligns with the Reliability pillar by advocating for automatic recovery from failure using proactive observability. If a regional failover is required, it can be initiated manually or automatically. DAO also emphasizes the need to monitor business SLAs to ensure infrastructure capacity is optimized and if those SLAs are not met, appropriate alarms are tripped. The guidance further encourages regional failover to be tested regularly to ensure all failure pathways are discovered and thus reducing business risk. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

DAO encourages mechanical sympathy by recommending customers to monitor application workloads using the right tool, such as X-Ray for Lambda. DAO provides guidance on leveraging advanced technologies, such as CloudWatch Synthetics and canary testing, to ensure workload performance is measured through multiple dimensions. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

DAO guidance leverages CloudWatch metrics, alarms, and logs coupled with application-level tracing like X-Ray. Most of the guidance implementation will remain with the AWS Free Tier boundaries of CloudWatch and X-Ray, although as customer requirements vary, the cost aspect will need to be considered. For example, older CloudWatch logs can be pushed to Amazon Simple Storage Service (Amazon S3) to reduce costs further. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

The DAO guidance recommends that you monitor all layers of your workload to ensure that business SLAs are continuously met, and that you conduct a regional failover when degradation or failure occurs. DAO can also be used to ensure efficient use of resources and reduce over provisioning of infrastructure to ensure a sustainable long-term working environment. Moreover, because the secondary environment is in a passive state, we recommend the resources to be scaled down until they are needed in case of a regional failover. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
