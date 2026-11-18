---
source_url: https://docs.aws.amazon.com/route53globalresolver/1.0/userguide/configure-dns-monitoring.html
---

# Configure DNS monitoring and logging with Amazon Route 53 Global Resolver
<a name="configure-dns-monitoring"></a>

Configure DNS monitoring in Amazon Route 53 Global Resolver to capture detailed information about DNS queries, responses, and security actions. This section covers the steps to set up logging destinations and configure monitoring tools.

## Setting the observability region
<a name="setting-observability-region"></a>

Before configuring DNS logging, you must set an observability region where logs and metrics will be stored. This region determines where your monitoring data is processed and stored.

1. Open the Amazon Route 53 Global Resolver console at [https://console.aws.amazon.com/route53globalresolver/](https://console.aws.amazon.com/route53globalresolver/).

1. In the navigation pane, choose **Settings**.

1. In the **Observability region** section, choose **Set region**.

1. Select the AWS Region where you want to store monitoring data, then choose **Set region**.

After setting the observability region, you can configure log delivery destinations in that region.
