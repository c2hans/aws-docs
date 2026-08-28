---
source_url: https://docs.aws.amazon.com/whitepapers/latest/blue-green-deployments/implementation-techniques.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Implementation Techniques
<a name="implementation-techniques"></a>

 The following techniques are examples of how you can implement blue/green on AWS. While AWS highlights specific services in each technique, you may have other services or tools to implement the same pattern. Choose the appropriate technique based on the existing architecture, the nature of the application, and the goals for software deployment in your organization. Experiment as much as possible to gain experience for your environment and to understand how the different deployment risk factors affect your specific workload.

**Topics**
+ [Update DNS Routing with Amazon Route 53](update-dns-routing-with-amazon-route-53.md)
+ [Swap the Auto Scaling Group Behind the Elastic Load Balancer](swap-the-auto-scaling-group-behind-elastic-load-balancer.md)
+ [Update Auto Scaling Group launch configurations](update-auto-scaling-group-launch-configurations.md)
+ [Swap the Environment of an Elastic Beanstalk Application](swap-the-environment-of-an-elastic-beanstalk-application.md)
+ [Clone a Stack in AWS OpsWorks and Update DNS](clone-a-stack-in-aws-opsworks-and-update-dns.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
