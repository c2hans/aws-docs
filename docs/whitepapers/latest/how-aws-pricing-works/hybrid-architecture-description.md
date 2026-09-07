---
source_url: https://docs.aws.amazon.com/whitepapers/latest/how-aws-pricing-works/hybrid-architecture-description.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Hybrid architecture description
<a name="hybrid-architecture-description"></a>

 The following example shows an Outpost deployment with distributed Amazon EKS service extending to on-premises environments.

![AWS Outpost with Amazon EKS Control Plane and Data Plane Architecture](https://docs.aws.amazon.com/whitepapers/latest/how-aws-pricing-works/images/aws-outpost-with-amazon-eks-control-plane-and-data-plane-architecture.png)

## Architecture
<a name="architecture-1"></a>
+  The Control Plane for Amazon EKS remains in the Region, which means in the case of Amazon EKS, the Kubernetes Primary node will stay in the Availability Zone deployed to the Region (not on the Outposts).
+  The Amazon EKS worker nodes are deployed on the Outpost, controlled by a Primary node deployed in the Availability Zone.

## Traffic Flow
<a name="traffic-flow"></a>
+  The EKS Control Plane Traffic between EKS, AWS metrics, and CloudWatch transits third-party networks (AWS Direct Connect/AWS Site-to-Site VPN to the AWS Region).
+  The Application / Data Traffic is isolated from Control plane and distributed between Outposts and local network.
+  Distribution of Amazon Machine Images (AMIs) (deployed on Outpost) is driven by central Amazon ECR in Region; however, all images are cached locally on the Outpost.

## Load Balancers
<a name="load-balancers"></a>
+  Application Load Balancer is supported on Outpost as the only local ELB available.
+  The Network Load Balancer and Classic Load Balancer stay in the Region, but targets deployed at Outposts are supported (including Application Load Balancer).
+  On-premises (inside corporate DC) Load Balancers (for example, F5 BIG IP, NetScaler) can be deployed and routed via Local Gateway (inside AWS Outpost).
