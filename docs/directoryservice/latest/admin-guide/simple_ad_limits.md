---
source_url: https://docs.aws.amazon.com/directoryservice/latest/admin-guide/simple_ad_limits.html
---

# Simple AD quotas
<a name="simple_ad_limits"></a>

**Important Notice**
Simple AD is no longer open to new customers. For capabilities similar to Simple AD, explore AWS Managed Microsoft AD or AD Connector. For more information, see [Simple AD availability changes](simple-ad-availability-change.md).

Generally, you should not add more than 500 users to a Small Simple AD directory and no more than 5,000 users to a Large Simple AD directory. For more flexible scaling options and additional Active Directory features, consider using AWS Directory Service for Microsoft Active Directory (Standard Edition or Enterprise Edition) instead.

The following are the default quotas for Simple AD. Each quota is per Region unless otherwise noted.

**Simple AD quotas**

| Resource | Default quota |
| --- | --- |
| Simple AD directories | 10 |
| Manual snapshots \* | 5 per Simple AD |

\* The manual snapshot quota cannot be changed.

**Note**
You cannot attach a public IP address to your AWS elastic network interface (ENI).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Directory Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query directoryservice` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
