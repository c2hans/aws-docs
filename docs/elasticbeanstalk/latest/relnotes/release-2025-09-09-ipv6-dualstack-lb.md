---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2025-09-09-ipv6-dualstack-lb.html
---

# Release: Elastic Beanstalk supports IPv6 in dualstack configuration for Application and Network Load Balancers on September 9, 2025
<a name="release-2025-09-09-ipv6-dualstack-lb"></a>

AWS Elastic Beanstalk adds support for IPv6 network protocol with dual stack configuration for Application and Network Load Balancers.

**Release date:** September 9, 2025

## Changes
<a name="release-2025-09-09-ipv6-dualstack-lb.changes"></a>

Elastic Beanstalk now offers support for your environment to serve both IPv4 and IPv6 protocols by providing the dual-stack configuration option for Application and Network Load Balancers. Elastic Beanstalk will automatically configure your load balancer with dual-stack support when you set the `aws:elbv2:loadbalancer` namespace option `IpAddressType` to *dualstack*.

This feature is available in all AWS Regions where Elastic Beanstalk is supported.

For more information, see [ Configuring dual-stack Elastic Beanstalk load balancers](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environments-cfg-elbv2-ipv6-dualstack.html) in the *AWS Elastic Beanstalk Developer Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Beanstalk. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticbeanstalk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
