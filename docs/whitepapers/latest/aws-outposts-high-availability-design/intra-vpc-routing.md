---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-outposts-high-availability-design/intra-vpc-routing.html
---

# Outposts Rack Intra-VPC routing
<a name="intra-vpc-routing"></a>

AWS Outposts rack supports [intra-VPC communication across multiple Outposts](https://aws.amazon.com/blogs/compute/introducing-intra-vpc-communication-across-multiple-outposts-with-direct-vpc-routing/). Resources on two separate logical Outposts can communicate with each other by routing traffic between subnets within the same VPC spanning across them using the Outpost local gateways (LGW). With intra-VPC communication across multiple Outposts, you can override the Local Route in your Outposts subnet associated route table by adding a more specific route to the other Outposts subnet using the local LGW as the next-hop. It can provide advantages to architecting applications that requires span a VPC between two logical Outposts as [Amazon ECS across two Outposts racks](https://community.aws/content/2k5wK9P1oSC9I4ZzuSLWynsiJaa/extend-amazon-ecs-across-two-outposts-racks) or [Amazon EKS cluster across AWS Outposts](https://aws.amazon.com/blogs/containers/deploy-an-amazon-eks-cluster-across-aws-outposts-with-intra-vpc-communication/).

![Diagram showing network paths for single VPC with multiple logical Outposts](http://docs.aws.amazon.com/whitepapers/latest/aws-outposts-high-availability-design/images/page-49-single-vpc-multiple-outposts.png)

Outposts-to-Outposts traffic routing through the Region is blocked as this is an anti-pattern. Such traffic would incur egress charges in both directions and significantly higher latency than routing the traffic across the customer WAN.
