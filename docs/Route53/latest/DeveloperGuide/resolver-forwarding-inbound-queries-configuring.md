---
source_url: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-forwarding-inbound-queries-configuring.html
---

# Configuring inbound forwarding
<a name="resolver-forwarding-inbound-queries-configuring"></a>

To create an inbound endpoint, perform the following procedure.<a name="resolver-forwarding-inbound-queries-configuring-procedure"></a>

**To create an inbound endpoint**

1. Sign in to the AWS Management Console and open the Route 53 console at [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/).

1. In the navigation pane, choose **Inbound endpoints**.

1. On the navigation bar, choose the Region where you want to create an inbound endpoint.

1. Choose **Create inbound endpoint**.

1. Enter the applicable values. For more information, see [Values that you specify when you create or edit inbound endpoints](resolver-forwarding-inbound-queries-values.md).

1. Choose **Create**.

1. Configure DNS resolvers on your network to forward the applicable DNS queries to the IP addresses for your inbound endpoint. For more information, refer to the documentation for your DNS application.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
