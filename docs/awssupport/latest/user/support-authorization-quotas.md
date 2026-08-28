---
source_url: https://docs.aws.amazon.com/awssupport/latest/user/support-authorization-quotas.html
---

# AWS Support authorization quotas
<a name="support-authorization-quotas"></a>

The following tables list AWS Support authorization quotas.

**Resource quotas**

| Resource | Quota | Adjustable |
| --- | --- | --- |
| Support permits per account | 200 | No |

**Request rate quotas**

| Operation | Throttle rate | Throttle burst |
| --- | --- | --- |
| CreateSupportPermit | 3 tps | 5 tps |
| DeleteSupportPermit | 3 tps | 5 tps |
| GetSupportPermit | 3 tps | 5 tps |
| ListSupportPermits | 10 tps | 15 tps |
| ListSupportPermitRequests | 10 tps | 15 tps |
| RejectSupportPermitRequest | 3 tps | 5 tps |
| GetAction | 3 tps | 5 tps |
| ListActions | 10 tps | 15 tps |
| ListTagsForResource | 10 tps | 15 tps |
| TagResource | 3 tps | 5 tps |
| UntagResource | 3 tps | 5 tps |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Support. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query awssupport` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
