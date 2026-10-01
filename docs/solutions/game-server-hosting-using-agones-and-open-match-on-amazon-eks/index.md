---
source_url: https://docs.aws.amazon.com/solutions/game-server-hosting-using-agones-and-open-match-on-amazon-eks/index.html
---

---
title: 'Guidance for Game Server Hosting Using Agones and Open Match on Amazon EKS'
canonical_url: https://docs.aws.amazon.com/solutions/game-server-hosting-using-agones-and-open-match-on-amazon-eks/
source: aws-documentation
generated_on: 2026-10-01
---

# Guidance for Game Server Hosting Using Agones and Open Match on Amazon EKS

Set up, install, and host an open source container-based game server hosting and matchmaking solution on Amazon EKS

## Overview

This Guidance shows game developers how to automate the setup of global game servers. It provides step-by-step instructions for configuring a Kubernetes cluster that orchestrates the Agones and OpenMatch open source frameworks on Amazon Elastic Kubernetes Service (Amazon EKS). By leveraging infrastructure as code, this approach simplifies the deployment process on Amazon EKS and allows developers to run the same system locally on Kubernetes. The architecture diagram also demonstrates how to establish a multi-cluster configuration for optimizing game session placement based on global latency. This not only reduces lag and improves response times but also enhances the overall gameplay experience.

## How it works

This architecture diagram shows how to use Agones and Open Match to build a global matchmaking and game server structure.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/game-server-hosting-using-agones-and-open-match-on-amazon-eks.pdf)

![Architecture diagram](/images/solutions/game-server-hosting-using-agones-and-open-match-on-amazon-eks/images/game-server-hosting-using-agones-and-open-match-on-amazon-eks-1.png)

1. **Step 1**: Connect to AWS Global Accelerator endpoint asking for match allocation.
1. **Step 2**: Route the request through a Network Load Balancer to the Open Match Game Frontend container.
1. **Step 3**: Amazon CloudWatch enables observability as the Director container receives and processes match requests with player data.
1. **Step 4**: Group the players' tickets with the Match Making function, according to the function's criteria, and return a match ticket to the Director container.
1. **Step 5**: Request a match allocation from the Agones Allocator container. The request can specify a different Region, defined by the Match Making function.
1. **Step 6**: If the Region 1 has the lowest latency to the players, allocate a game server on the same Region with the Agones Allocator container.
1. **Step 7**: Alternatively, route the request to the Agones Allocator on Region 2, through a virtual private cloud (VPC) peering connection and Classic Load Balancer, and allocate a server in that Region.
1. **Step 8**: Return the internal IP address and port of the game server to the Director container.
1. **Step 9**: Translate the internal IP address and port to the equivalent Global Accelerator address and port for the Director container. Then, send the translated internal IP address to the Frontend container.
1. **Step 10**: Send the game server connection details, containing a Global Accelerator address and custom routing port, back to the players.
1. **Step 11**: Connect to the Global Accelerator for the designated cluster in a port that gets routed to the allocated game container for the match.
1. **Step 12**: Route the connection to the allocated game container.
1. **Step 13**: Encrypt Agones and Open Match certificates with AWS Key Management Service (AWS KMS).
1. **Notes**: Steps 1-10 use gRPC with TLS/SSL. Steps 11-12 use the game specific protocol. All the containers are pulled from Amazon Elastic Container Registry (Amazon ECR).
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-game-server-hosting-on-amazon-eks)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

This Guidance uses the Amazon Elastic Kubernetes Service (Amazon EKS) control plane to provision clusters with Amazon Elastic Compute Cloud (Amazon EC2) managed node groups. The nodes are built using a launch template. By providing you with a consistent and repeatable way to build clusters through the Amazon EKS API, the amount of human error and lead time are both reduced. Also, for containers running on the Amazon EKS cluster, you can export logs and metrics to Amazon CloudWatch, which allows for observability on the cluster to proactively identify issues. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

An AWS KMS key is created implicitly by Terraform scripts when an Amazon EKS cluster is launched. That key is used to encrypt Kubernetes secrets stored in Amazon EKS (including Docker registry credentials to pull images, TLS keys, and other certificates used by Agones and Open Match). This implements envelope encryption, which is considered a security best practice for an in-depth security strategy. Amazon GuardDuty is another service designed to protect accounts and can be configured with this architecture. It surfaces security risks by analyzing audit logs and runtime activity on the Amazon EKS cluster. Amazon EKS is also used for runtime monitoring in GuardDuty to detect potential threats in the game servers and matchmaking components. Global Accelerator also supports a secure infrastructure. It gives you the ability to have fine-grained control over source ports, protocols, and client affinity. This allows traffic to flow from game clients on the internet to game servers running on Amazon EC2 worker nodes and launched by Amazon EKS. You can restrict access from source IPs that are not safe. Since Global Accelerator is used, you also benefit from AWS Shield Standard protection to mitigate distributed denial-of-service (DDoS) attempts. With Shield Standard, only valid traffic from safe client IPs is allowed to flow through the accelerator and reach endpoint groups for the game containers. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Network Load Balancer and Classic Load Balancer provide ingress (routing traffic from outside the cluster) to deployments running inside the Amazon EKS cluster. Ingress traffic is routed to a Kubernetes service that terminates traffic on a Kubernetes pod. Network Load Balancer and Classic Load Balancer provide fixed ingress endpoints in the Regions for each Amazon EKS cluster where internet traffic is routed from Global Accelerator. Containers on Amazon EKS clusters can be upgraded in a rolling fashion while Network Load Balancer and Classic Load Balancer continue to redirect traffic to the services without disruption. Network Load Balancer provides ingress for the frontend service on the primary Amazon EKS cluster. With Network Load Balancer, you can scale your frontend by running multiple pods for the deployment and expose the frontend service as targets through the load balancer. If one frontend pod crashes or is unavailable, then Network Load Balancer will route traffic to the next available pod. Classic Load Balancer provides ingress for the allocator service running on the secondary Amazon EKS cluster. With Classic Load Balancer, you can scale the allocator service by running multiple pods for the deployment and exposing them as targets through the load balancer. If one allocator pod crashes or is unavailable, then the Classic Load Balancer will route traffic to the next available pod. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Since Amazon ECR is integrated directly with Amazon EKS, it simplifies the delivery of Agones and Open Match containers that are deployed on the Amazon EKS cluster. Amazon ECR eliminates the need to operate and scale the infrastructure required to store and pull container images for the game containers, Agones, and Open Match components. Regardless of the size of the Amazon EKS clusters in terms of pods, Amazon ECR will scale to the deployment. Amazon ECR provides the ability to pull and push images in the same Region where the Amazon EKS clusters live, which provides the best performance in terms of latency and data transfer costs. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

The Amazon EKS worker nodes running game servers can be configured to run on Amazon EC2 Spot Instances. Amazon EKS worker nodes running Agones and Open Match components can leverage Savings Plans. Nodes that run the game servers and Kubernetes kube-system can also potentially use AWS Graviton Processors-based instances. You can save up to 90% on the compute costs for game server hosting when using Spot Instances to run game servers. You can optimize the compute costs for Agones and Open Match containers by up to 72% with Graviton instances covered by Savings Plans. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

The AWS Carbon Footprint Tool allows you to track and measure carbon emissions from Amazon EKS clusters and improve the impact of worker nodes to support sustainable workloads. With these services, you can manage and track carbon emissions to prevent waste and achieve sustainable computing. They optimize the usage of Amazon EKS worker nodes at the Region level and provide mechanisms to quickly react when carbon emissions goals are not met. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
