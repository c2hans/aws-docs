---
source_url: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-using-old-apis.html
---

# Using health checks with Amazon Route 53 API versions earlier than 2012-12-12
<a name="dns-failover-using-old-apis"></a>

Health checks are supported starting with the 2012-12-12 version of the Amazon Route 53 API. If a hosted zone contains records that health checks are configured for, we recommend that you use only the 2012-12-12 API or later. Note the following restrictions on using health checks with earlier API versions.
+ The `ChangeResourceRecordSets` action cannot create or delete records that include the `EvaluateTargetHealth`, `Failover`, or `HealthCheckId` elements.
+ The `ListResourceRecordSets` action can list records that include these elements, but the elements are not included in the output. Instead, the `Value` element of the response contains a message that says the record includes an unsupported attribute.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
