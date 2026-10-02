---
source_url: https://docs.aws.amazon.com/solutions/disaster-recovery-for-vmware-workloads-on-aws/index.html
---

---
title: 'Guidance for Disaster Recovery for VMware Workloads on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/disaster-recovery-for-vmware-workloads-on-aws/
source: aws-documentation
generated_on: 2026-10-02
---

# Guidance for Disaster Recovery for VMware Workloads on AWS

## Overview

This Guidance demonstrates how to implement disaster recovery for VMware workloads to AWS using AWS Elastic Disaster Recovery (AWS DRS). It helps organizations establish continuous replication and automated failover capabilities for both on-premises VMware environments and Amazon Elastic VMware Service (EVS). By leveraging private connectivity and the provided CloudFormation template, you can perform recovery drills and execute failovers without exposing traffic to the public internet, delivering a flexible and secure foundation that adapts to your organization's specific resilience and business continuity requirements.

## Benefits

### Automate disaster recovery deployment

Deploy a complete VMware disaster recovery solution in minutes using AWS CloudFormation and AWS Lambda. Eliminate manual configuration while establishing secure connectivity between your on-premises environment and AWS.

### Maintain business continuity confidently

Protect your VMware workloads with continuous replication to AWS. Test recovery procedures without disrupting production systems and failover quickly when disasters occur.

### Secure your recovery environment

Keep all disaster recovery traffic private using VPC endpoints and Site-to-Site VPN. Replicate data securely to AWS while maintaining control over your network architecture and access policies.

## How it works

This guidance displays a comprehensive approach to disaster recovery for VMware workloads to AWS, covering strategic planning, technical implementation, and cost optimization across the entire DR lifecycle.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/disaster-recovery-for-vmware-workloads-on-aws.pdf)

![Architecture diagram](/images/solutions/disaster-recovery-for-vmware-workloads-on-aws/images/disaster-recovery-for-vmware-workloads-on-aws-1.png)

1. **Step 1**: Deploy the AWS CloudFormation template in the chosen AWS account and Region by using the AWS Management Console.
1. **Step 2**: The AWS CloudFormation stack creates the AWS Site-to-Site VPN (virtual private gateway, customer gateway, VPN connection, and routes) for private connectivity; then configure the on-premises VPN device using the downloaded VPN configuration.
1. **Step 3**: Within the target Amazon Virtual Private Cloud (VPC), the stack creates private subnets and the required Amazon VPC interface and gateway endpoints (AWS Elastic Disaster Recovery (AWS DRS), Amazon Elastic Compute Cloud (Amazon EC2), Amazon Simple Storage Service (Amazon S3), Amazon Route 53, Amazon CloudWatch) so service traffic stays on private connectivity.
1. **Step 4**: An AWS Lambda backed custom resource initializes AWS DRS and applies default replication and launch configuration settings based on specified parameters.
1. **Step 5**: Install the AWS Replication Agent on selected VMware VMs in the on-premises environment so they register as source servers and can send changed data to AWS.
1. **Step 6**: AWS DRS uses the staging subnet to create replication Amazon EC2 servers and Amazon Elastic Block Storage (Amazon EBS) staging volumes and launches recovery Amazon EC2 instances and Amazon EBS volumes into the recovery subnet during drills or failover.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **We'll walk you through it**: Dive deep into the implementation guide for additional customization options and service configurations to tailor to your specific needs.

[Open guide](https://github.com/aws-solutions-library-samples/guidance-for-disaster-recovery-of-vmware-workloads-using-aws-elastic-disaster-recovery-service/blob/main/PrescriptiveGuidance_ElasticDisasterRecovery.md)

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-disaster-recovery-of-vmware-workloads-using-aws-elastic-disaster-recovery-service)

[Read usage guidelines](/solutions/guidance-disclaimers/)
