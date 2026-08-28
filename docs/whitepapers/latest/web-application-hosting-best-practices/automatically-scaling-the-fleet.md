---
source_url: https://docs.aws.amazon.com/whitepapers/latest/web-application-hosting-best-practices/automatically-scaling-the-fleet.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Automatically scaling the fleet
<a name="automatically-scaling-the-fleet"></a>

One of the key differences between the AWS Cloud architecture and the traditional hosting model is that AWS can automatically scale the web application fleet on demand to handle changes in traffic. In the traditional hosting model, traffic forecasting models are generally used to provision hosts ahead of projected traffic. In AWS, instances can be provisioned on the fly according to a set of triggers for scaling the fleet out and back in.

The [Auto Scaling](https://aws.amazon.com/autoscaling/) service can create capacity groups of servers that can grow or shrink on demand. Auto Scaling also works directly with CloudWatch for metrics data and with Elastic Load Balancing to add and remove hosts for load distribution. For example, if the web servers are reporting greater than 80 percent CPU utilization over a period of time, an additional web server could be quickly deployed and then automatically added to the load balancer for immediate inclusion in the load balancing rotation.

As shown in the AWS web hosting architecture model, you can create multiple Auto Scaling groups for different layers of the architecture, so that each layer can scale independently. For example, the web server Auto Scaling group might trigger scaling in and out in response to changes in network I/O, whereas the application server Auto Scaling group might scale out and in according to CPU utilization. You can set minimums and maximums to help ensure 24/7 availability and to cap the usage within a group.

Auto Scaling triggers can be set both to grow and to shrink the total fleet at a given layer to match resource utilization to actual demand. In addition to the Auto Scaling service, you can scale Amazon EC2 fleets directly through the Amazon EC2 API, which allows for launching, terminating, and inspecting instances.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
