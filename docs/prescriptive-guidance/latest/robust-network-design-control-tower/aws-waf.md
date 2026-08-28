---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/robust-network-design-control-tower/aws-waf.html
---

# AWS WAF
<a name="aws-waf"></a>

You can use AWS WAF as a source to help protect your application from vulnerability attacks such as cross-site scripting, SQL injections, or DDoS. For the robust network approach, configure AWS WAF in front of the Application Load Balancer and define AWS WAF rules that should be followed across the organization. This will help ensure that any traffic reaching services hosted across the organization meets security best practices and that security is checked before traffic enters the organization's environment.

The following diagram shows inbound traffic coming through AWS WAF to the Application Load Balancer in the network account. From the network account, the traffic is routed to the Network Load Balancers or Application Load Balancer in the OU accounts and sent to the target EC2 instances.

![""](http://docs.aws.amazon.com/prescriptive-guidance/latest/robust-network-design-control-tower/images/guide-img/734c65f3-3001-4321-a428-6ffbda3b44b0/images/fca1cd0f-85c6-4b96-85fc-80fbb11c0ded.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
