---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/sec_protect_data_transit_key_cert_mgmt.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# SEC09-BP01 Implement secure key and certificate management
<a name="sec_protect_data_transit_key_cert_mgmt"></a>

 Store encryption keys and certificates securely and rotate them at appropriate time intervals with strict access control. The best way to accomplish this is to use a managed service, such as [AWS Certificate Manager (ACM)](http://aws.amazon.com/certificate-manager). It lets you easily provision, manage, and deploy public and private Transport Layer Security (TLS) certificates for use with AWS services and your internal connected resources. TLS certificates are used to secure network communications and establish the identity of websites over the internet as well as resources on private networks. ACM integrates with AWS resources, such as Elastic Load Balancers (ELBs), AWS distributions, and APIs on API Gateway, also handling automatic certificate renewals. If you use ACM to deploy a private root CA, both certificates and private keys can be provided by it for use in Amazon Elastic Compute Cloud (Amazon EC2) instances, containers, and so on.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>
+  Implement secure key and certificate management: Implement your defined secure key and certificate management solution.
  + [AWS Certificate Manager ](https://aws.amazon.com/certificate-manager/)
  + [ How to host and manage an entire private certificate infrastructure in AWS](https://aws.amazon.com/blogs/security/how-to-host-and-manage-an-entire-private-certificate-infrastructure-in-aws/)
+  Implement secure protocols: Use secure protocols that offer authentication and confidentiality, such as Transport Layer Security (TLS) or IPsec, to reduce the risk of data tampering or loss. Check the AWS documentation for the protocols and security relevant to the services that you are using.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [AWS Documentation ](https://docs.aws.amazon.com/)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
