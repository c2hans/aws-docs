---
source_url: https://docs.aws.amazon.com/whitepapers/latest/nhs-cloud-security-guidance-using-aws/principle-11-external-interface-protection.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Principle 11: External interface protection
<a name="principle-11-external-interface-protection"></a>

****
 All access to service interfaces should be constrained to authenticated and authorised individuals.
 The Service User should ensure their system has AWS WAF protection. This may be provided by the cloud vendor or a third party.

 **Applicable risk classes:** III-V

 To fulfil this aspect of the Guidance, customers may avail themselves of three complementary AWS services: [AWS WAF](https://aws.amazon.com/waf/) (Web Application Firewall, in conjunction with the [Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html) content distribution service, [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html), or an [Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html)), AWS Shield, and AWS Firewall Manager.

 AWS WAF helps protect applications and web service components against application-level attacks, using a customer-configurable ruleset. Request types, source IP addresses and other request properties may be configured as the criteria for allow lists or deny lists which can even be updated automatically. More specialised requirements in this category may be met by a relevant product from the AWS Marketplace. For details on how to use this service, see [AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html).

 AWS Shield is a Distributed Denial of Service (DDoS) protection service for preventing internet-facing web applications from being overwhelmed with requests intending to compromise their availability. AWS Shield is offered at two levels: AWS Shield Standard (for which there is no additional charge) and AWS Shield Advanced. For more information, see [AWS Shield](https://docs.aws.amazon.com/waf/latest/developerguide/shield-chapter.html).

 AWS Firewall Manager provides customers with a single point of management for all AWS WAF-protected resources across their AWS accounts, enabling AWS WAF and Shield Advanced operations to be streamlined. See [AWS Firewall Manager](https://docs.aws.amazon.com/waf/latest/developerguide/fms-chapter.html) for more information.

****
 The Service User should ensure that the implemented design protects data by ensuring it is at least two "firewall" hops from the external network, architected in such a way that the compromise of one firewall will not affect the other.

 **Applicable risk classes:** III-V

 AWS network security includes security groups, which are logical firewalls that may be applied to single instances or sets of instances. Because of how the security group mechanism operates, this threat is less of a risk in the AWS environment, but should customers choose to implement this part of the guidance, it can be achieved by deploying one or more instances running virtual firewalls to the Virtual Private Cloud as the gatekeeper for all in- and out-bound traffic, in conjunction with security groups.

****
 The Service User should correctly implement firewall rulesets using the "Deny All" First and then Add Exceptions principle.

 **Applicable risk classes:** All
+  **Security group and network access control list (network ACL) rules** — These two security features implement this principle as standard; customers may add exceptions based on source IP address, range or Security Group; and source TCP port (or range). Security Groups may then be applied to individual or sets of virtual instances, thus controlling the destination addresses to which they apply. Network ACLs operate on a similar basis, except that they apply to subnets rather than instances, and are stateless in nature.

   For more details, see [Internetwork traffic privacy in Amazon VPC](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Security.html) in the *Amazon Virtual Private Cloud User Guide*.

## Additional applicable security controls
<a name="additional-applicable-security-controls"></a>
+  **Amazon Virtual Private Cloud (Amazon VPC)** gives customers with a secure logical section of the AWS Cloud, which provides private subnets for their instances and other resources. VPCs created by customers do not have internet access by default; an Internet Gateway component must be configured to enable this.
+  **NAT Gateway** is an optional component of the VPC that enables instances deployed to subnets with no direct in- or out-bound access from and to networks outside the VPC to access the internet (for say, downloading patches).
+  **Virtual Private Network** helps customers restrict access to their AWS resources in a VPC to a corporate network. Customers may set up an IPsec VPN over the internet between these using the optional Customer Gateway component of the VPC.
+  **AWS Direct Connect (DX)** is a dedicated remote link to AWS that is private to the customer.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
