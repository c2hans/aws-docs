---
source_url: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/best-practices-resolver-zone-walking.html
---

# DNS zone walking
<a name="best-practices-resolver-zone-walking"></a>

A DNS zone walking attack attempts to get all content from DNSSEC-signed DNS zones. If VPC Resolver team detects a traffic pattern that matches the ones generated when DNS zones are walked on your endpoint, the service team throttles the traffic on your endpoint. As a consequence you might observe a high percentage of your DNS queries timing out.

If you observe reduced capacity on your endpoints and believe that the endpoint have been throttled erroneously, go to https://console.aws.amazon.com/support/home\#/ to create a support case.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
