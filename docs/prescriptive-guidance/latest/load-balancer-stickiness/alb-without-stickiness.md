---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/load-balancer-stickiness/alb-without-stickiness.html
---

# Application Load Balancer without stickiness
<a name="alb-without-stickiness"></a>

When you use an Application Load Balancer without any form of stickiness, by default, the load balancer uses the round robin method to determine the EC2 instance it should route traffic to.

**Template**: Use the CloudFormation template `basic.yml` (included in the attached .zip file) to try out this functionality.

**Note**
All CloudFormation templates included with this guide deploy a custom VPC, route tables, routes, an internet gateway, an Application Load Balancer, target groups, listeners, and Amazon EC2 instances, to illustrate a specific load balancer stickiness strategy.

## Common use cases
<a name="common-use-cases.55751a7a-9b0e-5ac1-bc45-6408358a25a0"></a>

Use an Application Load Balancer without stickiness in these scenarios:
+ You have a list of targets to route traffic to, but the targets do not maintain session state.
+ You're using web servers that do not maintain session state.
+ You're using application servers that do not maintain session state.

## Steps
<a name="steps.8620612a-c263-51dc-991a-b6eb8f5b3830"></a>

**Note**
NAT gateways incur a small cost, and multiple Amazon EC2 instances use up your free tier hours faster than a single instance.

1. Deploy the CloudFormation template `basic.yml` in a lab environment.

1. Wait until the health status of your target group instances changes from **initial** to **healthy**.

1. Navigate to the Application Load Balancer URL in a web browser, using HTTP (TCP/80).

   For example: `http://alb-123456789.us-east-1.elb.amazonaws.com/`

   The webpage displays **Instance 1 - TG1** or **Instance 2 - TG1**.

1. Refresh the page multiple times.

## Expected results
<a name="expected-results.271d29bf-61a3-5294-a34c-8a9cd0c78aef"></a>

The instance that loads the web page (Instance 1 or Instance 2) should change every time, as reflected in the page text. The load balancer logic manages the last target across multiple internal nodes, which may introduce a synchronization delay, so there's a possibility that you will be routed to the same target.

## How it works
<a name="how-it-works.dfb9a9f7-c668-5442-a44b-5fe2258ef1ef"></a>
+ In this example, two EC2 instances are assigned to a single target group. The EC2 instances have an Apache web server (`httpd`) installed, and the `index.html` page text on each EC2 instance is hardcoded to identify that instance.
+ The Application Load Balancer runs its internal round robin logic to determine which EC2 instance should receive the traffic.
+ Each time you reload the web page, the Application Load Balancer runs its routing logic, and the page displays **Instance 1 - TG1** or **Instance 2 - TG1**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
