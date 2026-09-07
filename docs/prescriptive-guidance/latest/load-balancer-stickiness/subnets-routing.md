---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/load-balancer-stickiness/subnets-routing.html
---

# Load balancer subnets and routing
<a name="subnets-routing"></a>

Let's start with an illustration of how traffic flows when you configure an [Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html) that faces the internet, to Amazon Elastic Compute Cloud (Amazon EC2) instances in a private subnet. This architecture reflects best practices when deploying an Application Load Balancer that's open to the internet.

## Inbound traffic path
<a name="inbound-path"></a>

The following diagram illustrates the virtual private cloud (VPC) subnets and routing associated with the incoming traffic flow, with the return traffic removed from the diagram for clarity.

![Inbound traffic path associated with an Application Load Balancer.](https://docs.aws.amazon.com/prescriptive-guidance/latest/load-balancer-stickiness/images/guide-img/698bb10a-1e2e-4f76-b428-a7d412d56d80/images/29ca40b5-196a-457b-b713-933704a871b1.png)

1. Traffic from the internet flows in to the Application Load Balancer DNS name.

1. The Application Load Balancer is associated with two public subnets in the scenario that's illustrated. The Elastic Load Balancing service creates load balancer capacity in each enabled Availability Zone, and sends traffic through the Availability Zone to determine the appropriate routing logic. The Application Load Balancer uses its internal logic to determine which target group and instance to route the traffic to.

1. The Application Load Balancer routes the request to the EC2 instance through a node that's associated with the public subnet in the same Availability Zone. (These nodes are configured, managed and scaled by the Elastic Load Balancing service and aren't visible to users.)

1. The route table routes the traffic locally within the VPC, between the public subnet and the private subnet, and to the EC2 instance.

## Return traffic path
<a name="outbound-path"></a>

The following diagram illustrates the VPC subnets and routing associated with the traffic path back out to the internet, with the incoming traffic removed from the diagram for clarity.

![Outbound traffic path associated with an Application Load Balancer.](https://docs.aws.amazon.com/prescriptive-guidance/latest/load-balancer-stickiness/images/guide-img/698bb10a-1e2e-4f76-b428-a7d412d56d80/images/291e24b9-3680-491a-9fe4-d2863aedadc2.png)

1. The EC2 instance in the private subnet routes the outbound traffic through the route table.

1. The route table has a local route to the public subnet. It reaches the Application Load Balancer capacity that the traffic entered on, in the corresponding public subnet, by following the path back the way the traffic entered.

1. The Application Load Balancer routes traffic out through its public interface.

1. The public subnet's route table has a default route pointing to an internet gateway, which routes the traffic back out to the internet.

## Complete traffic flow diagram
<a name="roundtrip-path"></a>

The following diagram combines the inbound and return traffic flows to provide a complete illustration of load balancer routing.

![Round trip traffic path associated with an Application Load Balancer.](https://docs.aws.amazon.com/prescriptive-guidance/latest/load-balancer-stickiness/images/guide-img/698bb10a-1e2e-4f76-b428-a7d412d56d80/images/dc21d14b-d1b6-42d3-81f2-e532314f4ae9.png)

1. Traffic from the internet flows in to the Application Load Balancer DNS name.

1. The Application Load Balancer is associated with two public subnets in the scenario that's illustrated. The Elastic Load Balancing service creates load balancer capacity in each enabled Availability Zone, and sends traffic through the Availability Zone to determine the appropriate routing logic. The Application Load Balancer uses its internal logic to determine which target group and instance to route the traffic to.

1. The Application Load Balancer routes the request to the EC2 instance through a node that's associated with the public subnet in the same Availability Zone. (These nodes are configured, managed, and scaled by the Elastic Load Balancing service and aren't visible to users.)

1. The route table routes the traffic locally within the VPC, between the public subnet and the private subnet, and to the EC2 instance.

1. The EC2 instance in the private subnet routes the outbound traffic through the route table.

1. The route table has a local route to the public subnet. It reaches the Application Load Balancer capacity that the traffic entered on, in the corresponding public subnet, by following the path back the way the traffic entered.

1. The Application Load Balancer routes traffic out through its public interface.

1. The public subnet's route table has a default route pointing to an internet gateway, which routes the traffic back out to the internet.
