---
source_url: https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-authenticate-cluster-connections.html
---

# Authenticate to Amazon EMR cluster nodes
<a name="emr-authenticate-cluster-connections"></a>

SSH clients can use an Amazon EC2 key pair to authenticate to cluster instances. Alternatively, with Amazon EMR releases 5.10.0 and higher, you can configure Kerberos to authenticate users and SSH connections to the primary node. And with Amazon EMR releases 5.12.0 and higher, you can authenticate with LDAP.

**Topics**
+ [Use an EC2 key pair for SSH credentials for Amazon EMR](emr-plan-access-ssh.md)
+ [Use Kerberos for authentication with Amazon EMR](emr-kerberos.md)
+ [Use Active Directory or LDAP servers for authentication with Amazon EMR](ldap.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
