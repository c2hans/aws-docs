---
source_url: https://docs.aws.amazon.com/waf/latest/developerguide/nsd-concepts.html
---

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html).

# Key concepts in network security director
<a name="nsd-concepts"></a>

**Note**
AWS Shield network security director is in public preview release and is subject to change.

**Resources**
The compute, networking, and security resources that handle your application traffic:
+ *Compute* – Amazon Elastic Compute Cloud instances
+ *Networking* – Application Load Balancers, Amazon API Gateways, Amazon CloudFront distributions, VPC subnets, and VPC elastic network interfaces (ENIs)
+ *Security* – AWS WAF web ACLs, VPC security groups, and VPC network access control lists (NACLs)

**Findings**
Alerts about missing or misconfigured network security services, with severity levels of NONE, INFORMATIONAL, LOW, MEDIUM, HIGH, or CRITICAL. network security director generates findings by evaluating configuration settings and threat intelligence for each resource.

**Severity**
A measure of a resource's vulnerability to potential security events, based on AWS best practices and threat intelligence. Severity assessment considers both potential vulnerabilities and existing protections. A resource's severity level matches its most severe finding, or shows as none if there are no findings.

**Network topology**
A visual representation of your network that shows resource connections, internet exposure, and tag-based relationships. Use the topology view to investigate resources and their findings.

## Understanding network security director findings
<a name="nsd-findings-concepts"></a>

**Note**
AWS Shield network security director is in public preview release and is subject to change.

Network security director generates specific findings for each type of resource it analyzes. These findings help you identify security issues and take appropriate action. The following table lists all possible findings by resource type.

**network security director findings by resource type**

| Resource type | Finding description |
| --- | --- |
| Application Load Balancer |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/waf/latest/developerguide/nsd-concepts.html)  |
| Amazon API Gateway |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/waf/latest/developerguide/nsd-concepts.html)  |
| Amazon CloudFront |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/waf/latest/developerguide/nsd-concepts.html)  |
| Amazon Elastic Compute Cloud (EC2) instance |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/waf/latest/developerguide/nsd-concepts.html)  |
| VPC security group |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/waf/latest/developerguide/nsd-concepts.html)  |
| VPC network access control list (NACL) |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/waf/latest/developerguide/nsd-concepts.html)  |
| AWS WAF web ACL |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/waf/latest/developerguide/nsd-concepts.html)  |
