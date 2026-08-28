---
source_url: https://docs.aws.amazon.com/redshift/latest/mgmt/best-practices-discovering-metadata.html
---

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025.

# Best practices for discovering metadata
<a name="best-practices-discovering-metadata"></a>

Amazon Redshift provides multiple ways to discover metadata. For applications and tools, including those built with AI agents, we recommend that you use the driver metadata API or `SHOW` commands for consistent, reliable, and performant metadata discovery.

**Topics**
+ [Use the Amazon Redshift driver metadata API for applications and tools](discovering-metadata-driver-api.md)
+ [Use SHOW commands](discovering-metadata-show-commands.md)
+ [Querying system tables](discovering-metadata-system-tables.md)
+ [Set the application name connection property](discovering-metadata-application-name.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
