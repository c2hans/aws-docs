---
source_url: https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/confluence-server-limitations.html
---

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Known limitations for the Amazon Q Business Confluence (Server/Data Center) connector
<a name="confluence-server-limitations"></a>

The Amazon Q Confluence (Server/Data Center) connector has the following known limitation:
+ Because Amazon Q Business uses email addresses as unique identifiers, each user must have a unique email address.
+ The Confluence (Server/Data Center) connector may not accurately differentiate between Confluence users with duplicate email addresses when mapping access control lists (ACLs). This can lead to inconsistent search results, in which a user might be able to see restricted content intended for one Confluence user with a shared email, but not other restricted content intended for a different Confluence user with the same email.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
