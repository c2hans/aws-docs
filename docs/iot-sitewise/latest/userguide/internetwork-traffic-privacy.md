---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/userguide/internetwork-traffic-privacy.html
---

# Internetwork traffic privacy for AWS IoT SiteWise
<a name="internetwork-traffic-privacy"></a>

Connections between AWS IoT SiteWise and on-premises applications, such as SiteWise Edge gateways, are secured over Transport Layer Security (TLS) connections. For more information, see [Data encryption in transit for AWS IoT SiteWise](encryption-in-transit.md).

AWS IoT SiteWise doesn't support connections between Availability Zones within an AWS Region or connections between AWS accounts.

<a name="cross-region-sso"></a>You can configure IAM Identity Center in only one Region at a time. SiteWise Monitor connects to the Region that you configured for IAM Identity Center. This means that you use one Region for IAM Identity Center access, but you can create portals in any Region.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
