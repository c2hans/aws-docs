---
source_url: https://docs.aws.amazon.com/whitepapers/latest/best-practices-wordpress/scaling-the-web-tier.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Scaling the web tier
<a name="scaling-the-web-tier"></a>

 To evolve your single-server architecture into a multi-server, scalable architecture, you must use five key components:
+ Amazon EC2 instances
+ Amazon Machine Images (AMIs)
+ Load balancers
+ Automatic scaling
+ Health checks

 AWS provides a wide variety of EC2 instance types so you can choose the best server configuration for both performance and cost. Generally speaking, the compute-optimized (for example, C4) instance type may be a good choice for a WordPress web server. You can deploy your instances across multiple Availability Zones within an AWS Region to increase the reliability of the overall architecture.

 Because you have complete control of your EC2 instance, you can log in with root access to install and configure all of the software components required to run a WordPress website. After you are done, you can save that configuration as an AMI, which you can use to launch new instances with all the customizations that you've made.

 To distribute end-user requests to multiple web server nodes, you need a load balancing solution. AWS provides this capability through [Elastic Load Balancing](https://aws.amazon.com/elasticloadbalancing/), a highly available service that distributes traffic to multiple EC2 instances. Because your website is serving content to your users via HTTP or HTTPS, we recommend that you make use of the Application Load Balancer, an application-layer load balancer with content routing and the ability to run multiple WordPress websites on different domains, if required.

 Elastic Load Balancing supports distribution of requests across multiple Availability Zones within an AWS Region. You can also configure a health check so that the Application Load Balancer automatically stops sending traffic to individual instances that have failed (for example, due to a hardware problem or software crash). AWS recommends using the WordPress admin login page (`/wp-login.php`) for the health check because this page confirms both that the web server is running and that the web server is configured to serve PHP files correctly.

You may choose to build a custom health check page that checks other dependent resources, such as database and cache resources. For more information, refer to [Health checks for your target groups](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/target-group-health-checks.html) in the *Application Load Balancer* *Guide*.

 Elasticity is a key characteristic of the AWS Cloud. You can launch more compute capacity (for example, web servers) when you need it and run less when you don't. [Amazon EC2 Auto Scaling](https://aws.amazon.com/ec2/autoscaling/) is an AWS service that helps you automate this provisioning to scale your Amazon EC2 capacity up or down according to conditions you define with no need for manual intervention. You can configure Amazon EC2 Auto Scaling so that the number of EC2 instances you’re using increases seamlessly during demand spikes to maintain performance and decreases automatically when traffic diminishes, so as to minimize costs.

 Elastic Load Balancing also supports dynamic addition and removal of Amazon EC2 hosts from the load-balancing rotation. Elastic Load Balancing itself also dynamically increases and decreases the load-balancing capacity to adjust to traffic demands with no manual intervention.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
