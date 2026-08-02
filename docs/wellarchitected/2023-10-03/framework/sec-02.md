---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-10-03/framework/sec-02.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# SEC 2. How do you manage authentication for people and machines?
<a name="sec-02"></a>

 There are two types of identities that you must manage when approaching operating secure AWS workloads. Understanding the type of identity you must manage and grant access helps you verify the right identities have access to the right resources under the right conditions.

Human Identities: Your administrators, developers, operators, and end users require an identity to access your AWS environments and applications. These are members of your organization, or external users with whom you collaborate, and who interact with your AWS resources via a web browser, client application, or interactive command line tools.

Machine Identities: Your service applications, operational tools, and workloads require an identity to make requests to AWS services, for example, to read data. These identities include machines running in your AWS environment such as Amazon EC2 instances or AWS Lambda functions. You may also manage machine identities for external parties who need access. Additionally, you may also have machines outside of AWS that need access to your AWS environment.

**Topics**
+ [SEC02-BP01 Use strong sign-in mechanisms](sec_identities_enforce_mechanisms.md)
+ [SEC02-BP02 Use temporary credentials](sec_identities_unique.md)
+ [SEC02-BP03 Store and use secrets securely](sec_identities_secrets.md)
+ [SEC02-BP04 Rely on a centralized identity provider](sec_identities_identity_provider.md)
+ [SEC02-BP05 Audit and rotate credentials periodically](sec_identities_audit.md)
+ [SEC02-BP06 Leverage user groups and attributes](sec_identities_groups_attributes.md)
