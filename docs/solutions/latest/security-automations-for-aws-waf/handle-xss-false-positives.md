---
source_url: https://docs.aws.amazon.com/solutions/latest/security-automations-for-aws-waf/handle-xss-false-positives.html
---

# Handle XSS false positives
<a name="handle-xss-false-positives"></a>

This solution configures an AWS WAF rule that inspects commonly explored elements of incoming requests to identify and block XSS attacks. This detection pattern is less effective if your workload allows legitimate users to compose and submit HTML, for example, using a rich text editor in a content management system. In this scenario, consider creating an exception rule that bypasses the default XSS rule for specific URL patterns that accept rich text input, and implement alternate mechanisms to protect those excluded URLs.

Additionally, some image or custom data formats can cause false positives because they contain patterns indicating a potential XSS attack in HTML content. For example, an SVG file might contain a `<script>` tag. If you expect this type of content from legitimate users, narrowly tailor your XSS rules to allow HTML requests that include these other data formats.

Complete the following steps to update XSS rule to exclude URLs that accept HTML as input. Refer to the [Amazon WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/) for detailed instructions.

1. Sign in to the [AWS WAF console](https://console.aws.amazon.com/wafv2/).

1.  [Create a string match or regex condition](https://docs.aws.amazon.com/waf/latest/developerguide/getting-started.html#getting-started-wizard-create-string-condition).

1. Configure the filter settings to inspect URI and list values that you want to accept against the XSS rule.

1. Edit this solution’s **XSS Rule** and [add the new condition](https://docs.aws.amazon.com/waf/latest/developerguide/getting-started.html#getting-started-wizard-create-rule) that you created.

   For example, to exclude all URLs in the list, choose the following for **When a request** :
   +  **does not**
   +  **match at least one of the filers in the string match condition**
   +  **XSS Allowlist**

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Security Automations for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
