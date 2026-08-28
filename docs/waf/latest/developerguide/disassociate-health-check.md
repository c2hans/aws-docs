---
source_url: https://docs.aws.amazon.com/waf/latest/developerguide/disassociate-health-check.html
---

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html).

# Disassociating a health check from your resource protected by Shield Advanced
<a name="disassociate-health-check"></a>

The following procedure shows how to disassociate an Amazon Route 53 health check from a protected resource.

**To disassociate a health check**

1. Sign in to the AWS Management Console and open the AWS WAF & Shield console at [https://console.aws.amazon.com/wafv2/](https://console.aws.amazon.com/wafv2/).

1. In the AWS Shield navigation pane, choose **Protected resources**.

1. On the **Protections** tab, select the resource that you want to disassociate from a health check.

1. Choose **Configure protections**.

1. Choose **Next** until you get to the page **Configure health check based DDoS detection - *optional***.

1. Under **Associated Health Check**, choose the empty option, listed as **-**.

1. Walk through the rest of the pages until you finish the configuration.

On the **Protections** page, the health check field for your resource is set to **-**, indicating no health check association.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
