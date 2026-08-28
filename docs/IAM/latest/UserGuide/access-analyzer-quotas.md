---
source_url: https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-quotas.html
---

# IAM Access Analyzer quotas
<a name="access-analyzer-quotas"></a>

IAM Access Analyzer has the following quotas:

| Resource | Default quota | Maximum quota |
| --- | --- | --- |
| Maximum account-level analyzers per analyzer type per AWS account per Region | 1 | 1 |
| Maximum organization-level external or unused access analyzers per analyzer type per AWS account per Region | 5 | 20¹ |
| Maximum organization-level internal access analyzers per AWS organization per Region | 1 | 1 |
| Maximum archive rules per analyzer | 100<br />Each archive rule can have up to 20 values per criterion. | 1,000¹ |
| Maximum number of access previews per analyzer per hour | 1,000 | 1,000 |
| AWS CloudTrail log files processed per policy generations | 100,000 | 100,000 |
| Concurrent policy generations | 1 | 1 |
| Policy generation AWS CloudTrail data size | 25 GB | 25 GB |
| Policy generation AWS CloudTrail time range | 90 days | 90 days |
| Policy generations per day | Africa (Cape Town): 5<br />Asia Pacific (Hong Kong): 5<br />Asia Pacific (Jakarta): 5<br />Europe (Milan): 5<br />Middle East (Bahrain): 5<br />All other supported regions: 50 Canceled policy generation requests apply to the daily quota.  | Africa (Cape Town): 5<br />Asia Pacific (Hong Kong): 5<br />Asia Pacific (Jakarta): 5<br />Europe (Milan): 5<br />Middle East (Bahrain): 5<br />All other supported regions: 50 |

¹Some quotas are customer-configurable using [Service Quotas](https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Identity and Access Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query IAM` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
