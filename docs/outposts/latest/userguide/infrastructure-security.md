---
source_url: https://docs.aws.amazon.com/outposts/latest/userguide/infrastructure-security.html
---

# Infrastructure security in AWS Outposts
<a name="infrastructure-security"></a>

As a managed service, AWS Outposts is protected by AWS global network security. For information about AWS security services and how AWS protects infrastructure, see [AWS Cloud Security](https://aws.amazon.com/security/). To design your AWS environment using the best practices for infrastructure security, see [Infrastructure Protection](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/infrastructure-protection.html) in *Security Pillar AWS Well‐Architected Framework*.

You use AWS published API calls to access AWS Outposts through the network. Clients must support the following:
+ Transport Layer Security (TLS). We require TLS 1.2 and recommend TLS 1.3.
+ Cipher suites with perfect forward secrecy (PFS) such as DHE (Ephemeral Diffie-Hellman) or ECDHE (Elliptic Curve Ephemeral Diffie-Hellman). Most modern systems such as Java 7 and later support these modes.

For more information about the infrastructure security provided for the EC2 instances and EBS volumes running on your Outpost, see [Infrastructure Security in Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/infrastructure-security.html).

VPC Flow Logs function the same way as they do in an AWS Region. This means that they can be published to CloudWatch Logs, Amazon S3, or to Amazon GuardDuty for analysis. Data needs to be sent back to the Region for publication to these services, so it is not visible from CloudWatch or other services when the Outpost is in a disconnected state.

## Tamper monitoring on AWS Outposts equipment
<a name="w2aac27c21c17"></a>

Ensure that no one modifies, alters, reverse engineers, or tampers with the AWS Outposts equipment. AWS Outposts equipment may be equipped with tamper monitoring to ensure compliance with the [AWS Service Terms](https://aws.amazon.com/service-terms/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Outposts. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query outposts` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
