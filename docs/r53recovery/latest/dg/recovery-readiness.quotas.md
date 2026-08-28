---
source_url: https://docs.aws.amazon.com/r53recovery/latest/dg/recovery-readiness.quotas.html
---

# Quotas for readiness check
<a name="recovery-readiness.quotas"></a>

**Note**
The readiness check feature in Amazon Application Recovery Controller (ARC) is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [Amazon Application Recovery Controller (ARC) readiness check availability change](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-readiness-availability-change.html).

Readiness check in Amazon Application Recovery Controller (ARC) is subject to the following quotas (formerly referred to as limits).

| Entity | Quota |
| --- | --- |
| Number of recovery groups per account | 5 |
| Number of cells per account | 15 |
| Number of nested cells per cell | 3 |
| Number of cells per recovery group | 3 |
| Number of resources per cell | 10 |
| Number of resources per recovery group | 10 |
| Number of resources per resource set | 6 |
| Number of resource sets per account | 200 |
| Number of readiness checks per account | 200 |
| Number of cross-account authorizations | 100 |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Application Recovery Controller. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query r53recovery` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
