---
source_url: https://docs.aws.amazon.com/security-lake/latest/userguide/route-53-logs.html
---

# Route 53 resolver query logs in Security Lake
<a name="route-53-logs"></a>

Route 53 resolver query logs track DNS queries made by resources within your Amazon Virtual Private Cloud (Amazon VPC). This helps you understand how your applications are operating and spot security threats.

When you add Route 53 resolver query logs as a source in Security Lake, Security Lake immediately starts collecting your resolver query logs directly from Route 53 through an independent and duplicated stream of events.

Security Lake doesn't manage your Route 53 logs or affect your existing resolver query logging configurations. To manage resolver query logs, you must use the Route 53 service console. For more information, see [Managing Resolver query logging configurations](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-query-logging-configurations-managing.html) in the *Amazon Route 53 Developer Guide*.

The following list provides GitHub repository links to the mapping reference for how Security Lake normalizes Route 53 logs to OCSF.

****GitHub OCSF repository for Route 53 logs****
+ Source version 1 [(v1.0.0-rc.2)](https://github.com/ocsf/examples/tree/main/mappings/markdown/AWS/v1.0.0-rc.2/Route53)
+ Source version 2 [(v1.1.0)](https://github.com/ocsf/examples/tree/main/mappings/markdown/AWS/v1.1.0/Route53)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Security Lake. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query security-lake` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
