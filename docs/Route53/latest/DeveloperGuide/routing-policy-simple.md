---
source_url: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-simple.html
---

# Simple routing
<a name="routing-policy-simple"></a>

With simple routing, you can set up standard DNS records, with no special Route 53 routing such as weighted or latency. You typically route traffic to a single resource, for example, to a web server for your website.

You can use simple routing policy for records in a private hosted zone.

If you choose the simple routing policy in the Route 53 console, you can't create multiple records with the same name and type, but you can specify multiple values in the same record, such as multiple IP addresses. (If you choose the simple routing policy for an alias record, you can specify only one AWS resource or one record in the current hosted zone.) If you specify multiple values in a record, Route 53 returns all values to the recursive resolver in random order, and the resolver returns the values to the client (such as a web browser) that sent the DNS query. The client then chooses a value and resends the query. With simple routing, although you can specify multiple IP addresses, they are not health checked.

For information about values that you specify when you use the simple routing policy to create records, see the following topics:
+ [Values specific for simple records](resource-record-sets-values-basic.md)
+ [Values specific for simple alias records](resource-record-sets-values-alias.md)
+ [Values that are common for all routing policies](resource-record-sets-values-shared.md)
+ [Values that are common for alias records for all routing policies](resource-record-sets-values-alias-common.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
