---
source_url: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-failover.html
---

# Failover routing
<a name="routing-policy-failover"></a>

With failover routing, you can route traffic to a resource when it's healthy or to a different resource when the first one is unhealthy. The primary and secondary records can route traffic to anything from an Amazon S3 bucket set up as a website to a complex tree of records. For more information, see [Active-passive failover](dns-failover-types.md#dns-failover-types-active-passive).

You can use failover routing policy for records in a private hosted zone.

For information about values that you specify when you use the failover routing policy to create records, see the following topics:
+ [Values specific for failover records](resource-record-sets-values-failover.md)
+ [Values specific for failover alias records](resource-record-sets-values-failover-alias.md)
+ [Values that are common for all routing policies](resource-record-sets-values-shared.md)
+ [Values that are common for alias records for all routing policies](resource-record-sets-values-alias-common.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
