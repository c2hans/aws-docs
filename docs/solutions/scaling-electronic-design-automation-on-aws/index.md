---
source_url: https://docs.aws.amazon.com/solutions/scaling-electronic-design-automation-on-aws/index.html
---

# Guidance for Scaling Electronic Design Automation (EDA) on AWS

## Overview

This Guidance demonstrates how to implement a cloud-bursting solution that seamlessly extends your on-premises semiconductor workflows to the cloud. It allows you to run hybrid or entirely cloud-based semiconductor design and verification workflows on AWS while utilizing your existing on-premises chip design environments based on IBM Spectrum Load Sharing Facility (LSF) and NetApp storage.

## How it works

This architecture diagram shows how to provide compute capacity with design data caching using a multi-Region approach.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/scaling-electronic-design-automation-on-aws.pdf)

![Architecture diagram](/images/solutions/scaling-electronic-design-automation-on-aws/images/scaling-electronic-design-automation-on-aws-1.png)

1. **Step 1**: The user logs in to the NICE DCV desktop to submit the job through a multi-cluster of IBM Spectrum LSF, which is deployed using a multi-Region (or hybrid cloud) approach.
1. **Step 2**: The peered LSF server forwards the job to the receiver queue in the other LSF primary when the user submits a job in the sender queue.
1. **Step 3**: Once the job is received, the LSF server spins up the Amazon Elastic Compute Cloud (Amazon EC2) instance based on the resource requirements of the user job and the defined Amazon EC2 resource configuration by using EC2 fleet.
1. **Step 4**: The user's job reads all related data from Amazon FSx for NetApp ONTAP that mounted the FlexCache volume on the spun-up EC2 instance.
1. **Step 5**: The user job writes data to the FSx for ONTAP volume that has cache configured to the FlexCache volume. The data result is located in the same path for output (/scratch), so the user doesn't need to log in to another cluster to view the data.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-cloud-scale-eda-on-aws)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

AWS Lambda deploys the FlexCache configuration for FSx for ONTAP, automating the process and accelerating FSx for ONTAP adoption. This automation (using Lambda) helps streamline the deployment of FSx for ONTAP with FlexCache. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

AWS Secrets Manager enhances the security of the storage virtual machine's administrator access and NICE DCV external access by storing passwords as encrypted secret values. Secrets Manager protects access passwords through encryption, improving overall security. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Lambda can launch additional instances of your function to handle increased load if a function receives a request while processing a previous one. This scalability helps ensure that you can configure the file system and deploy FSx for ONTAP FlexCache through an API. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

IBM Spectrum LSF manages jobs and resources through Amazon EC2 (fleet) API calls, enabling EC2 instances to scale across multiple Regions. This approach allows for efficient utilization of resources and improved performance by dynamically adjusting compute capacity. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

FSx for ONTAP with FlexCache caches only metadata rather than all data from the source to the target file system. EDA workloads consume substantial disk space and require copying to remote clusters for processing. FlexCache reduces the size of data to move, saving costs. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

FSx for ONTAP maximizes utilization by supporting the modification of throughput capacity and increasing SSD storage and IOPS. FSx for ONTAP reduces downstream workloads once activated, contributing to sustainability efforts through efficient resource utilization. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
