---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/load-balancer-stickiness/alb-cookies-stickiness.html
---

# Sticky sessions with load balancer generated cookies
<a name="alb-cookies-stickiness"></a>

When you use an Application Load Balancer with a load balancer generated cookie:
+ The Application Load Balancer uses the target group weight to determine how to balance the incoming traffic between the target groups.
+ By default, the Application Load Balancer uses the round robin method to route requests to the EC2 instances in the destination target group.
+ After traffic has been initially routed to an instance, subsequent traffic will *stick* to that EC2 instance for a specified duration.

**Template**: Use the CloudFormation template `stickysessionslb.yml` (included in the attached .zip file) to try out sticky sessions with load balancer generated cookies.

## Common use cases
<a name="common-use-cases.583cac00-544d-5cd7-a4a4-f2b04014ac1b"></a>

Use sticky sessions with load balancer generated cookies in these scenarios:
+ PHP web servers
+ Servers that maintain temporary session data such as logs, shopping carts, or chat conversations

## Code changes from basic.yml
<a name="code-changes-from-basic.yml.cc7d1732-f39b-5a31-a243-1bd0d21bede9"></a>

The relevant code changes are in the target group configuration, to set the stickiness type to lb\_cookie and the duration to 10 seconds.

|  |  |
| --- |--- |
| `basic.yml` | `stickysessionslb.yml` |
| <pre>TG1:<br />   Type: 'AWS::ElasticLoadBalancingV2::TargetGroup'<br />   Properties:<br />     Name: TG1<br />     Protocol: HTTP<br />     Port: 80<br />     TargetType: instance<br />     Targets:<br />       - Id: !Ref Instance1<br />       - Id: !Ref Instance2<br />VpcId: !Ref CustomVPC</pre> | <pre>TG1:<br />   Type: 'AWS::ElasticLoadBalancingV2::TargetGroup'<br />   Properties:<br />     Name: TG1<br />     Protocol: HTTP<br />     Port: 80<br />     TargetType: instance<br />     Targets:<br />       - Id: !Ref Instance1<br />       - Id: !Ref Instance2<br />     VpcId: !Ref CustomVPC<br />     TargetGroupAttributes:<br />       - Key: stickiness.enabled<br />         Value: true<br />       - Key: stickiness.type<br />         Value: lb_cookie<br />       - Key: stickiness.lb_cookie.duration_seconds<br />Value: 10</pre> |

## Steps
<a name="steps.7180f7e7-2d1e-5d2f-89af-81828265c234"></a>

**Note**
NAT gateways incur a small cost, and multiple Amazon EC2 instances use up your free tier hours faster than a single instance.

1. Deploy the CloudFormation template `stickysessionslb.yml` in a lab environment.

1. Wait until the health status of your target group instances changes from **initial** to **healthy**.

1. Navigate to the Application Load Balancer URL in a web browser, using HTTP (TCP/80).

   For example: `http://alb-123456789.us-east-1.elb.amazonaws.com/`

   The webpage displays one of the following: **Instance 1 - TG1,** **Instance 2 - TG1**.

1. Refresh the page multiple times.

## Expected results
<a name="expected-results.6d50d033-d2a3-59e4-b5ea-eb1301baf714"></a>

**Note**
The CloudFormation template in this example configures the stickiness to last 10 seconds.

The instance that loads the web page should stay the same within the 10-second duration, as reflected in the page text. After approximately 10 seconds, the stickiness is released and the destination instance might change.

## How it works
<a name="how-it-works.b06e335f-00e2-558b-a472-564f2e2b1180"></a>
+ In this example, two EC2 instances are present in one target group. The EC2 instances have an Apache web server (`httpd`) installed, and the `index.html` page text on each EC2 instance is hardcoded to be distinct.
+ The Application Load Balancer creates a binding for the user's session, which binds toward the destination with an expiration time.
+ When you reload the page, the Application Load Balancer checks whether the binding exists and has not expired.
  + If the binding has expired or doesn't exist, the Application Load Balancer runs its routing logic and determines the destination instance.
  + If the binding has not expired, the Application Load Balancer routes traffic to the same destination instance.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
