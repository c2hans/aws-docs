---
source_url: https://docs.aws.amazon.com/waf/latest/developerguide/view-automatic-app-layer-response-configuration.html
---

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html).

# Viewing the automatic application layer DDoS mitigation configuration for a resource
<a name="view-automatic-app-layer-response-configuration"></a>

You can view the automatic application layer DDoS mitigation configuration for a resource in the **Protected resources** page and in the individual protections pages.

**To view the automatic application layer DDoS mitigation configuration**

1. Sign in to the AWS Management Console and open the AWS WAF & Shield console at [https://console.aws.amazon.com/wafv2/](https://console.aws.amazon.com/wafv2/).

1. In the AWS Shield navigation pane, choose **Protected resources**. In the list of protected resources, the column **Automatic application layer DDoS mitigation** indicates whether automatic mitigation is enabled and, where enabled, the action that Shield Advanced is to use in its mitigations.

   You can also select any application layer resource to see the same information listed on the protections page for the resource.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
