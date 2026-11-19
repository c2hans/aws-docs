---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-startup-security-baseline/wkld-10.html
---

# WKLD.10 Deploy private resources into private subnets

Deploy resources that don't require direct internet access (such as [Amazon Elastic Compute Cloud (Amazon EC2)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/) instances, databases, queues, caches, or other infrastructure) into a VPC private subnet. Private subnets don't have a route declared in their route table to an attached internet gateway and can't receive internet traffic. Traffic from a private subnet that is destined for the internet must go through network address translation (NAT). You can use a managed AWS NAT gateway or an Amazon EC2 instance running NAT processes in a public subnet. For more information about network isolation, see [Infrastructure security in Amazon VPC](https://docs.aws.amazon.com/vpc/latest/userguide/infrastructure-security.html) in the Amazon Virtual Private Cloud (Amazon VPC) documentation.

Use the following practices when creating private resources and subnets:
+ When creating a private subnet, disable **Auto-assign public IPv4 address**.
+ When creating private Amazon EC2 instances, disable **Auto-assign Public IP**. This setting prevents AWS from assigning a public IP address if you unintentionally deploy the instance into a public subnet because of a misconfiguration.
+ When creating [AWS Fargate](https://aws.amazon.com/fargate/) tasks and services, deploy them into private subnets and set **Assign public IP** to **TURNED OFF**. Fargate tasks that you deploy in a public subnet can receive a public IP address, which exposes them directly to the internet. For more information, see [AWS Fargate task networking](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/fargate-task-networking.html) in the Amazon Elastic Container Service (Amazon ECS) documentation.

When deploying a resource, specify the private subnet in the resource's network configuration.

**Note**
Private subnets are available at no additional charge. If your private resources require outbound internet access, an AWS NAT gateway incurs an hourly charge and a per-GB data processing charge. For more information, see [Amazon VPC pricing](https://aws.amazon.com/vpc/pricing/).
