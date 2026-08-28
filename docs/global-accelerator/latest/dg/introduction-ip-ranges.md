---
source_url: https://docs.aws.amazon.com/global-accelerator/latest/dg/introduction-ip-ranges.html
---

# Location and IP address ranges of Global Accelerator Edge servers
<a name="introduction-ip-ranges"></a>

For a list of Global Accelerator edge server locations, see *Global Edge Network* on the [AWS Global Accelerator features](https://aws.amazon.com/global-accelerator/features/) page.

AWS publishes its current IP address ranges in JSON format. To view the current ranges, download [ ip-ranges.json](https://ip-ranges.amazonaws.com/ip-ranges.json). For more information, see [AWS IP address ranges](https://docs.aws.amazon.com/general/latest/gr/Welcome.html#aws-ip-ranges) in the *Amazon Web Services General Reference*.

Before you work with the `ip-ranges.json` file, first review the following information:
+ To find the IP address ranges that are associated with AWS Global Accelerator Edge servers, search `ip-ranges.json` for the following string:

  `"service": "GLOBALACCELERATOR"`
+ Global Accelerator entries that include `"region": "GLOBAL"` refer to the static IP addresses that are allocated to accelerators. If you want to filter for traffic through your accelerator that comes from points of presence (POPs) in one area, filter for entries that include a specific geographical area, such as `us-*` or `eu-*`. So, for example, if you filter for `us-*`, you will see only traffic coming through POPs in the United States (U.S.).
+ Global Accelerator supports two ways of routing traffic: using client IP address preservation or using network address translation (NAT). The way that traffic is routed determines the client IP address that AWS WAF can apply rules to. When you use client IP address preservation, AWS WAF rules target the client IP address—that is, the IP address of the clients who access your service. When you use NAT, AWS WAF rules are applied to the global IP addresses that Global Accelerator uses to route traffic.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Global Accelerator. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query global-accelerator` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
