---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2020-09-10-shared-alb.html
---

# Release: Elastic Beanstalk introduces shared Application Load Balancers on September 10, 2020
<a name="release-2020-09-10-shared-alb"></a>

AWS Elastic Beanstalk added support for sharing an Application Load Balancer among multiple environments, to save on load balancer costs.

**Release date:** September 10, 2020

## Changes
<a name="release-2020-09-10-shared-alb.changes"></a>

An Application Load Balancer is one of the load balancer types that Elastic Beanstalk supports. It inspects traffic at the application network protocol layer to identify the request's path so that it can direct requests for different domains and paths to different destinations.

Until now, whenever you created a load-balanced, auto scaling environment and chose to use an Application Load Balancer, Elastic Beanstalk created a load balancer dedicated to your environment. In some situations you might want to save the cost of having multiple dedicated load balancers. This can be helpful when you have multiple environments, for example, if your application is a suite of microservices instead of a monolithic service.

To that end, we're introducing today the ability to use a *shared load balancer*. This is a load balancer that you create and manage yourself using the Amazon Elastic Compute Cloud (Amazon EC2) service, and then use in multiple Elastic Beanstalk environments.

For more information, see [Configuring a shared Application Load Balancer](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environments-cfg-alb-shared.html) in the *AWS Elastic Beanstalk Developer Guide*. To learn about configuration options relevant to a shared Application Load Balancer, see the [Shared Application Load Balancer namespaces](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environments-cfg-alb-shared.html#environments-cfg-alb-shared-namespaces) section on that page.

**Note**
In a related improvement, Elastic Beanstalk also added the ability to monitor environment health using new metrics at the target group level. An Application Load Balancer (both dedicated and shared) associates a target group (group of Amazon EC2 instances) with each Elastic Beanstalk environment. Target group metrics let you use Amazon CloudWatch to track an aggregated health overview for each environment using an Application Load Balancer.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Beanstalk. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticbeanstalk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
