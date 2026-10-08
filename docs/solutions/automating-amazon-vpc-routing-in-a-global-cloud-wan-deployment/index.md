---
source_url: https://docs.aws.amazon.com/solutions/automating-amazon-vpc-routing-in-a-global-cloud-wan-deployment/index.html
---

---
title: 'Guidance for Automating Amazon VPC Routing in a Global Cloud WAN Deployment'
canonical_url: https://docs.aws.amazon.com/solutions/automating-amazon-vpc-routing-in-a-global-cloud-wan-deployment/
source: aws-documentation
generated_on: 2026-10-08
---

# Guidance for Automating Amazon VPC Routing in a Global Cloud WAN Deployment

## Overview

This Guidance demonstrates how to automatically update the routing tables of your Amazon Virtual Private Cloud (Amazon VPC) when the Amazon VPC is attached or detached from an AWS Cloud WAN segment. It provides an automated Amazon VPC routing solution where workloads residing within Amazon VPCs have network connectivity to each other regardless of which Region the Amazon VPC resides.

## How it works

This diagram shows how to create an end-to-end global routing cloud network. You can deploy an Amazon Virtual Private Cloud (Amazon VPC) in multiple AWS Regions and automate your global Amazon VPC routing with this event-driven architecture.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/automating-amazon-vpc-routing-in-a-global-cloud-wan-deployment.pdf?target=_blank)

![Architecture diagram](/images/solutions/automating-amazon-vpc-routing-in-a-global-cloud-wan-deployment/images/automating-amazon-vpc-routing-in-a-global-cloud-wan-deployment-1.png)

1. **Step 1**: A new Amazon Virtual Private Cloud (Amazon VPC) is attached to AWS Cloud WAN.
1. **Step 2**: A network administrator attaches metadata (for example: a key-value pair tag) on the Amazon VPC attachment. This ensures the Amazon VPC attachment lands in the right AWS Cloud WAN segment. For this Guidance, the key-value pair tag must be in the 'department:<department-name>' format. For example, department:Finance.
1. **Step 3**: AWS Cloud WAN generates an event when an Amazon VPC is attached into a segment. This event includes a JSON object that contains details such as 'attachment-id' and 'VPC-id.'
1. **Step 4**: Amazon EventBridge captures this event. An EventBridge rule invokes a Regional AWS Lambda function.
1. **Step 5**: Lambda accepts the event's JSON string as an input.
1. **Step 6**: Lambda checks Amazon VPC IP Address Manager (IPAM) for a pool that has the same tag value as the Amazon VPC attachment, provided in step 2. In this example, the expected tag is Finance.
1. **Step 7**: IPAM returns the Classless Inter-Domain Routing (CIDR) associated with the IPAM pool to Lambda.
1. **Step 8**: Lambda adds a route to the Amazon VPC routing table with the CIDR that was obtained in step 7. The target for this route is the AWS Cloud WAN core network.
1. **Step 9**: The same steps can be applied to Amazon VPCs in a different Region.
1. **Step 10**: This completes the end-to-end routing for a multi-Region AWS Cloud WAN deployment
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-automating-amazon-vpc-routing-in-a-global-cloud-wan-deployment)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

AWS Cloud WAN provides a central dashboard for making connections between multiple Amazon VPCs, allowing you to build a global network quickly. The dashboard generates a full view of your AWS networks to monitor for security and performance. The AWS Service Health dashboard will show if any of the services are down and help you respond to incidents and events, thanks to the use of AWS managed services. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

Use AWS Identity and Access Management (IAM) policies to grant access to Lambda, which is needed to make an API call or update an Amazon VPC routing table. IAM roles used in this Guidance follow the least privilege permission model. Operations on AWS Cloud WAN will generate events, while EventBridge will carry the events securely to the right Region and invoke a Lambda function. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

This Guidance uses AWS Cloud WAN, IPAM, and EventBridge services that are highly available by default. Lambda makes an API call to an Amazon VPC within the same Region, so there are no cross-Region dependencies. Additionally, Lambda automatically monitors Lambda functions on your behalf and sends logs to Amazon CloudWatch. Your Lambda function comes with a CloudWatch Logs group and a log stream for each instance of your function. There are some limits you should be aware of that may affect reliability. EventBridge has a limit of 50 requests for every second. But it is unlikely you would accumulate 50 Amazon VPCs for every second to your global network. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

The services selected in this Guidance were purpose-built for this use, providing an end-to-end fully automated global network solution: AWS Cloud WAN: Orchestrates the creation of a global network. Amazon VPC: A logically isolated construct where you can deploy your services. Each VPC connects into AWS Cloud WAN. IPAM: The container for each department’s routing information. EventBridge: The carrier for events generated by AWS Cloud WAN and invokes the right Lambda function. Lambda: Adds the right route in a newly attached Amazon VPC routing table. We recommend you deploy the Lambda functions in the Regions of your operations to decrease latency and improve performance. EventBridge will always invoke the local or Regional Lambda function to minimize latency. This Guidance also pushes the right route to each Amazon VPC routing table, helping ensure only the expected traffic patterns are enabled. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

This Guidance, as with the vast majority of our cloud services, uses a pay-as-you-go approach. You pay only for the services you need, for as long as you use them. AWS Cloud WAN and EventBridge automatically scale based on demand and with only the minimum resources required. If setting AWS Cloud WAN as a default route to Amazon VPCs, all outgoing traffic from the VPC that matches the default route would be sent to AWS Cloud WAN, which would incur data processing charges. This Guidance pushes only the individual's network route in the Amazon VPC routing table, helping you to save on cost. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Lambda is optimized for this Guidance, offering automatic scaling to help ensure you are using only the minimal resources while continuously matching the demand of your workloads. Metadata is derived from an AWS Cloud WAN event-driven mechanism where data is not stored anywhere, only carried by EventBridge. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
