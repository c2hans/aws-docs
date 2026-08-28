---
source_url: https://docs.aws.amazon.com/managedservices/latest/appguide/app-security.html
---

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html).

# Application security considerations
<a name="app-security"></a>

Application security includes considering what permissions the application will need to run, what firewall rules, what IAM roles should be enabled for access to the application.

To better understand general AWS security, see [Best Practices for Security, Identity, & Compliance](https://aws.amazon.com/architecture/security-identity-compliance/).

## Access for configuration management
<a name="access-config-mgmt"></a>

AWS Managed Services (AMS) seeks to provide you with a headache-free infrastructure so you don’t have to worry about security issues, patching issues, backup issues, etc. To do that, AMS recommends minimal IAM roles allowing only a specific group or a master server, if using an application deployment tool, access to the instances running your application.

## Application access firewall rules
<a name="app-access-fw-rules"></a>

Just like the operating system (OS), all application access should be governed using Active Directory (AD) groups. Using Amazon Relational Database Service (Amazon RDS) as an example, you must break the mirror (replication) to add a new user. The best approach is to create a group in AD and add it at database creation time. Having the groups in your AMS AD means that you can create CTs for application access. For information on the official grouping strategy for AD, see [ Using Group Nesting Strategy – AD Best Practices for Group Strategy](http://blogs.msmvps.com/acefekay/2012/01/06/using-group-nesting-strategy-ad-best-practices-for-group-strategy/).

To learn more about domain trees and parent/child domains, see [How Domains and Forests Work](https://technet.microsoft.com/en-us/library/cc783351%28v=ws.10%29.aspx).

The following rules illustrate a solution appropriate for a multi-domain forest trust with users located in child domains.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Managed Services. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managedservices` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
