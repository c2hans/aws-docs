---
source_url: https://docs.aws.amazon.com/solutions/automated-setup-for-amazon-elastic-vmware-service/index.html
---

---
title: 'Guidance for Automated Setup for Amazon Elastic VMware Service'
canonical_url: https://docs.aws.amazon.com/solutions/automated-setup-for-amazon-elastic-vmware-service/
source: aws-documentation
generated_on: 2026-09-25
---

# Guidance for Automated Setup for Amazon Elastic VMware Service

## Overview

This guidance demonstrates how to accelerate cloud adoption for VMware workloads by automating the deployment of Amazon EVS environments. Infrastructure and VMware administrators can leverage automated provisioning of essential AWS services, including VPCs, Route 53, and Transit Gateway, eliminating complex manual configurations. By implementing AWS best practices through infrastructure as code, organizations can quickly establish production-ready VMware environments in the cloud while reducing deployment time, minimizing configuration errors, and streamlining their migration journey.

## Benefits

### Accelerate VMware environment deployment

Deploy production-ready VMware Cloud Foundation environments using automated CloudFormation templates. Eliminate weeks of manual configuration while maintaining full control over your VMware architecture and operational processes.

### Maintain seamless hybrid connectivity

Extend your on-premises data center to AWS without IP address changes using AWS Direct Connect or Site-to-Site VPN and AWS Transit Gateway. Preserve existing network configurations and operational workflows while gaining cloud scalability and resilience.

### Reduce operational complexity significantly

Leverage Infrastructure as Code to automate complex networking and VMware stack provisioning. Free your IT teams from repetitive configuration tasks to focus on strategic business initiatives and innovation.

## How it works

### Service mapping and deployment

This reference architecture shows customers' on-premises VMware deployment and their Amazon Elastic VMware components in AWS.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/automated-setup-for-amazon-elastic-vmware-service.pdf)Step 1Developer/DevOps users use the AWS SDK, AWS CLI, and AWS CloudFormation for Infrastructure as Code (IaC) deployment of solution. These automation tools enable programmatic provisioning of Amazon Elastic VMware Service (Amazon EVS) through standardized AWS API and declarative CloudFormation template.Step 2CloudFormation provisions Amazon EVS as the primary service, integrated with essential AWS infrastructure services including Amazon Virtual Private Cloud (Amazon VPC) for network isolation, Amazon VPC Route Server, Amazon Route 53 for DNS resolution, and others.Step 3Using Amazon EVS, users can interact with familiar VMware tools and services: SDDC Manager for infrastructure management, vSphere for virtualization, vSAN for storage, NSX for networking, along with other AWS managed and core services that can integrate with the Amazon EVS environment.Step 4Multiple AWS services can be integrated with Amazon EVS such as: Amazon EC2, Amazon Elastic Load Balancing (ELB), Amazon FSx for storage, AWS System Manager, Amazon Simple Storage Service (S3), Amazon DynamoDB, Amazon Cloud Watch and others.### External Network access to Amazon EVS service

This reference architecture shows setting up network access to Amazon EVS via AWS Direct Connect and AWS Transit Gateway services.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/automated-setup-for-amazon-elastic-vmware-service.pdf)Step 1Create Amazon Route 53 forward and reverse hosted zones in the target AWS Region. Set up Amazon Route 53 inbound resolver endpoints so the Amazon Elastic Vmware (Amazon EVS) management components and ESXi hosts can resolve DNS names properly (implemented by CloudFormation template, see Slide 1).Step 2Amazon Virtual Private Cloud (Amazon VPC) is built with service access and public subnets in a single Availability Zone. Amazon Internet Gateway and NAT Gateway provide outbound internet access for private subnets. A custom DHCP Option Set is created to use the inbound resolvers from step 1 for DNS resolution and applied to the VPC. Deploy Amazon VPC Route Server with two endpoints in the service access subnet to handle BGP route exchange between Amazon EVS overlay networks and AWS underlay infrastructure.Step 3Provision AWS Transit Gateway with Amazon VPC attachment and connect to the service access subnet.Step 4For external connectivity, users may set up AWS Direct Connect Gateway to connect their corporate data center to the AWS Region and configure BGP routing to advertise routes between the on-premises network and AWS Transit Gateway for Amazon EVS workload migration.### Internal components connectivity and network topology

This reference architecture shows internal connectivity and network topology of Amazon Elastic VMware Service components.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/automated-setup-for-amazon-elastic-vmware-service.pdf)Step 1Amazon Elastic VMware Service (Amazon EVS) will provision Amazon EC2 i4i.metal type instances for ESXi hosts using user provided Broadcom keys and credentials. Amazon EVS will configure the initial VLAN subnets for host management, vMotion, vSAN, and NSX overlay networks.Step 2The Amazon EVS deployment process includes initializing vSphere cluster and deploying the VMware Cloud Foundation software including the vCenter Server, SDDC Manager, and Cloud Builder appliances in the VM Management VLAN network segments.Step 3The Amazon EVS deployment process will also deploy a three-node NSX Manager Cluster and a two-node NSX Edge Cluster.## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-automated-setup-for-elastic-vmware-service-on-aws)

[Read usage guidelines](/solutions/guidance-disclaimers/)
