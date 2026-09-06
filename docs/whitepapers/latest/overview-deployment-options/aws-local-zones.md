---
source_url: https://docs.aws.amazon.com/whitepapers/latest/overview-deployment-options/aws-local-zones.html
---

# AWS Local Zones
<a name="aws-local-zones"></a>

 An [AWS Local Zone](https://aws.amazon.com/about-aws/global-infrastructure/localzones/) is an extension of an AWS Region in close geographic proximity to your users. Local Zones have their own connections to the internet and support AWS Direct Connect. Resources that are created in a Local Zone can serve local users with low-latency communications. A Local Zone is represented by a Region code followed by an identifier that indicates the location (for example, us-west-2-lax-1a).

 Amazon ECS supports workloads that use Local Zones when low latency or local data processing is a requirement. The Amazon ECS control plane will always run in the AWS Region.

 Amazon EKS supports certain resources in Local Zones. This includes [self-managed Amazon EC2 nodes](https://docs.aws.amazon.com/eks/latest/userguide/worker.html), Amazon EBS volumes, and Application Load Balancers. The Amazon EKS managed Kubernetes control plane always runs in the AWS Region. The Amazon EKS managed Kubernetes control plane can't run in the Local Zone. Because Local Zones appear as a subnet within your VPC, Kubernetes sees your Local Zone resources as part of that subnet.
