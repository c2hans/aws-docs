---
source_url: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/gr-configure-dns-monitoring.html
---

# Configure DNS monitoring and logging with Route 53 Global Resolver
<a name="gr-configure-dns-monitoring"></a>

Configure DNS monitoring in Route 53 Global Resolver to capture detailed information about DNS queries, responses, and security actions. This section covers the steps to set up logging destinations and configure monitoring tools.

## Setting the observability Region
<a name="gr-setting-observability-region"></a>

Before configuring DNS logging, you must set an observability Region where logs and metrics will be stored. This region determines where your monitoring data is processed and stored.

1. Open the Route 53 Global Resolver console at [https://console.aws.amazon.com/route53globalresolver/](https://console.aws.amazon.com/route53globalresolver/).

1. In the navigation pane, choose **Settings**.

1. In the **Observability region** section, choose **Set region**.

1. Select the AWS Region where you want to store monitoring data, then choose **Set region**.

After setting the observability region, you can configure log delivery destinations in that Region.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
