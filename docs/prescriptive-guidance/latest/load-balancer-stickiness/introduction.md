---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/load-balancer-stickiness/introduction.html
---

# Choosing a stickiness strategy for your load balancer
<a name="introduction"></a>

*Ryan Griffin, Amazon Web Services*

*Stickiness *is a term that is used to describe the functionality of a load balancer to repeatedly route traffic from a client to a single destination, instead of balancing the traffic across multiple destinations. For example, traffic from client A can be continually  routed to a specific server, so that server can maintain session state data. If traffic from client A is routed to two distinct servers, each server might be missing important information that's available to the other server.

Therefore, it's often necessary to maintain a consistent client connection through a load balancer. There are two types of stickiness: sticky sessions and target group stickiness.
+ **Sticky sessions** - Maintaining local session data in an Amazon Elastic Compute Cloud (Amazon EC2) instance to simplify application architecture or to improve application performance, because the instance can maintain or cache the session state information locally. AWScurrently offers two types of sticky sessions, which this guide discusses in detail: application cookies and load balancer cookies.
+ **Target group stickiness** - In blue/green deployments you might have multiple versions of an application deployed, and you might want the client to continue to use the same version of the application during their session. In this case, you can use target group stickiness to route all communications from the client to the same target group instead of the same EC2 instance.

You can use these two stickiness strategies separately or together.

This guide describes different types of load balancer stickiness and applicable use cases, to help you choose a strategy. The guide includes CloudFormation templates that illustrate each strategy.

## Sample code
<a name="code"></a>

This guide provides an attached .zip file that includes four CloudFormation templates that you can deploy to build a basic architecture and try out each stickiness strategy. We recommend that you deploy these templates in a lab environment to test each approach.

The download includes these templates:
+ `basic.yml` – Sets up an Application Load Balancer without stickiness.
+ `targetgroupstickiness.yml` – Demonstrates stickiness based on target groups.
+ `stickysessionslb.yml` – Demonstrates sticky sessions with load balancer generated cookies.
+ `stickysessionsapp.yml` – Demonstrates sticky sessions with application-based cookies.

To deploy these templates, you will need an active AWS account and access to the [CloudFormation console](https://console.aws.amazon.com/cloudformation/). For step-by-steps instructions for deploying a CloudFormation template, see [Creating a stack](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.html) in the CloudFormation documentation.

## Attachments
<a name="attachments-698bb10a-1e2e-4f76-b428-a7d412d56d80"></a>

To access additional content that is associated with this document, download and unzip the following file:

[attachment.zip](samples/attachment.zip)
