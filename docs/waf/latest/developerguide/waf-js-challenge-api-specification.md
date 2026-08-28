---
source_url: https://docs.aws.amazon.com/waf/latest/developerguide/waf-js-challenge-api-specification.html
---

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html).

# Intelligent threat API specification
<a name="waf-js-challenge-api-specification"></a>

This section lists the specification for the methods and properties of the intelligent threat mitigation JavaScript APIs. Use these APIs for intelligent threat and CAPTCHA integrations.

**`AwsWafIntegration.fetch()`**
Sends the HTTP `fetch` request to the server using the AWS WAF integration implementation.

**`AwsWafIntegration.getToken()`**
Retrieves the stored AWS WAF token and stores it in a cookie on the current page with name `aws-waf-token`, and the value set to the token value.

**`AwsWafIntegration.hasToken()`**
Returns a boolean indicating whether the `aws-waf-token` cookie currently holds an unexpired token.

If you're also using the CAPTCHA integration, see the specification for that at [CAPTCHA JavaScript API specification](waf-js-captcha-api-specification.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
