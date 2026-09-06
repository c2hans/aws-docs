---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/load-balancer-stickiness/target-group-stickiness.html
---

# Target group stickiness
<a name="target-group-stickiness"></a>

When you use an Application Load Balancer with target group stickiness:
+ The Application Load Balancer uses the [target group weight](https://aws.amazon.com/premiumsupport/knowledge-center/elb-make-weighted-target-groups-for-alb/) to determine how to balance the incoming traffic between the target groups.
+ By default, the Application Load Balancer uses the round robin method [to route requests to the EC2 instances](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-target-groups.html#modify-routing-algorithm) in the destination target group.

**Template**: Use the CloudFormation template `targetgroupstickiness.yml` (included in the attached .zip file) to try out target group stickiness.

## Common use cases
<a name="common-use-cases.504b6d2c-d57c-5467-868d-56c45ab163d9"></a>

Use target group stickiness in these scenarios:
+ There are multiple target groups assigned to the load balancer, and the traffic from a client should be consistently routed to instances within that target group.
+ Blue/green deployments.

## Code changes from basic.yml
<a name="code-changes-from-basic.yml.a50cd53e-724b-55ec-bbba-6ca779d95ec1"></a>

A single change has been made to the listener: We modified the Application Load Balancer default actions to specify two target groups (TG1 and TG2) of equal weight, with a stickiness configuration.

|  |  |
| --- |--- |
| `basic.yml` | `targetgroupstickiness.yml` |
| <pre>Listener1:<br />  Type: 'AWS::ElasticLoadBalancingV2::Listener'<br />  Properties:<br />    LoadBalancerArn: !Ref ALB<br />    Protocol: HTTP<br />    Port: 80<br />    DefaultActions:<br />      - TargetGroupArn: !Ref TG1<br />        Type: forward</pre> | <pre>Listener1:<br />  Type: 'AWS::ElasticLoadBalancingV2::Listener'<br />  Properties:<br />    LoadBalancerArn: !Ref ALB<br />    Protocol: HTTP<br />    Port: 80<br />    DefaultActions:<br />      - ForwardConfig:<br />          TargetGroups:<br />            - TargetGroupArn: !Ref TG1<br />              Weight: 1<br />            - TargetGroupArn: !Ref TG2<br />              Weight: 1<br />          TargetGroupStickinessConfig:<br />              DurationSeconds: 10<br />              Enabled: true<br />        Type: forward</pre> |

## Steps
<a name="steps.b724720f-f496-55d0-bf46-3facded34e9d"></a>

**Note**
NAT gateways incur a small cost, and multiple Amazon EC2 instances use up your free tier hours faster than a single instance.

1. Deploy the CloudFormation template `targetgroupstickiness.yml`  in a lab environment.

1. Wait until the health status of your target group instances changes from **initial** to **healthy**.

1. Navigate to the Application Load Balancer URL in a web browser, using HTTP (TCP/80).

   For example: `http://alb-123456789.us-east-1.elb.amazonaws.com/`

   The webpage displays one of the following: **Instance 1 - TG1,** **Instance 2 - TG1**, **Instance 3 - TG2,** or **Instance 4 - TG1**.

1. Refresh the page multiple times.

## Expected results
<a name="expected-results.4701e76d-43d0-598e-9a14-86710526a13c"></a>

**Note**
The CloudFormation template in this example configures the stickiness to last 10 seconds.

The instances that load the web page should stay within the target group (TG1 or TG2) within the 10-second duration, as reflected in the page text.

After approximately 10 seconds, the stickiness is released and the target group instance set might change.

## How it works
<a name="how-it-works.8a464488-2150-5f3f-a99b-b500644e2ed8"></a>
+ In this example, four EC2 instances are split across two target groups, with two instances per target group. The EC2 instances have an Apache web server (`httpd`) installed, and the `index.html` page text on each EC2 instance is hardcoded to be distinct.
+ The Application Load Balancer creates a a binding for the user's session toward the destination target group, with an expiration time.
+ When you reload the page, the Application Load Balancer checks whether the binding exists and has not expired.
  + If the binding has expired or doesn't exist, the Application Load Balancer runs its routing logic and determines the destination target group.
  + If the binding has not expired, the Application Load Balancer routes traffic to the same target group, but not necessarily to the same EC2 instance.
