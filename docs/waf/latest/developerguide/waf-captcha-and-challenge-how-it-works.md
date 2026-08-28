---
source_url: https://docs.aws.amazon.com/waf/latest/developerguide/waf-captcha-and-challenge-how-it-works.html
---

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html).

# How the AWS WAF CAPTCHA and Challenge rule actions work
<a name="waf-captcha-and-challenge-how-it-works"></a>

This section explains how CAPTCHA and Challenge work.

AWS WAF CAPTCHA and Challenge are standard rule actions, so they're relatively easy to implement. To use either of them, you create the inspection criteria for your rule that identifies the requests that you want to inspect, and then specify one of the two rule actions. For general information about rule action options, see [Using rule actions in AWS WAF](waf-rule-action.md).

In addition to implementing silent challenges and CAPTCHA puzzles from the server side, you can integrate silent challenges in your JavaScript and iOS and Android client applications, and you can render CAPTCHA puzzles in your JavaScript clients. These integrations allow you to provide your end users with better performance and CAPTCHA puzzle experiences, and they can reduce costs associated with using the rule actions and the intelligent threat mitigation rule groups. For more information about these options, see [Client application integrations in AWS WAF](waf-application-integration.md). For pricing information, see [AWS WAF Pricing](https://aws.amazon.com/waf/pricing/).

**Topics**
+ [CAPTCHA and Challenge action behavior](waf-captcha-and-challenge-actions.md)
+ [CAPTCHA and Challenge actions in the logs and metrics](waf-captcha-and-challenge-logs-metrics.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
