---
source_url: https://docs.aws.amazon.com/directconnect/latest/UserGuide/classic_connection.html
---

# Direct Connect Classic connection
<a name="classic_connection"></a>

A Classic connection offers a straightforward approach to establishing dedicated network connectivity between your on-premises infrastructure and AWS. This connection type is ideal for organizations that prefer to manage their own network configurations and have existing Direct Connect infrastructure in place. The Classic connection does not rely on the AWS Direct Connect Resiliency Toolkit.

Select Classic when you have existing connections and you want to add additional connections. A Classic connection has a 95% SLA. However, it does not provide resiliency or redundancy, which are found only in the AWS Direct Connect Resiliency Toolkit when creating a connection.

**Note**
Before you configure a Classic connection, familiarize yourself with the [Connection prerequisites](connection_options.md#connect-prereqs.title).

**Topics**
+ [Configure a Classic connection](toolkit-classic.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Direct Connect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query directconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
