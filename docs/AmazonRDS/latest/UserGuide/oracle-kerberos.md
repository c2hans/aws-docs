---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/oracle-kerberos.html
---

# Configuring Kerberos authentication for Amazon RDS for Oracle
<a name="oracle-kerberos"></a>

You can use Kerberos authentication to authenticate users when they connect to your Amazon RDS for Oracle DB instance. In this configuration, your DB instance works with AWS Directory Service for Microsoft Active Directory, also called AWS Managed Microsoft AD. When users authenticate with an RDS for Oracle DB instance joined to the trusting domain, authentication requests are forwarded to the directory that you create with Directory Service.

Keeping all of your credentials in the same directory can save you time and effort. You have a centralized place for storing and managing credentials for multiple database instances. A directory can also improve your overall security profile.

**Topics**
+ [Region and version availability](oracle-kerberos-setting-up.RegionVersionAvailability.md)
+ [Setting up Kerberos for Oracle DB instances](oracle-kerberos-setting-up.md)
+ [Managing a DB instance in a domain](oracle-kerberos-managing.md)
+ [Connecting to Oracle with Kerberos authentication](oracle-kerberos-connecting.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
