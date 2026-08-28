---
source_url: https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-request-components-for-http2-pseudo-headers.html
---

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html).

# Inspecting HTTP/2 pseudo headers in AWS WAF
<a name="waf-rule-statement-request-components-for-http2-pseudo-headers"></a>

This section explains how you can use AWS WAF to inspect HTTP/2 pseudo headers.

Protected AWS resources that support HTTP/2 traffic do not forward HTTP/2 pseudo headers to AWS WAF for inspection, but they provide contents of pseudo headers in web request components that AWS WAF inspects.

You can use AWS WAF to inspect only the pseudo headers that are listed in the following table.

**HTTP/2 pseudo header contents mapped to web request components**

| HTTP/2 pseudo header | Web request component to inspect | Documentation |
| --- | --- | --- |
| `:method` | HTTP method  | [HTTP method](waf-rule-statement-fields-list.md#waf-rule-statement-request-component-http-method) |
| `:authority` | `Host` header  | [Single header](waf-rule-statement-fields-list.md#waf-rule-statement-request-component-single-header) <br />[All headers](waf-rule-statement-fields-list.md#waf-rule-statement-request-component-headers) |
| `:path` URI path | URI path  | [URI path](waf-rule-statement-fields-list.md#waf-rule-statement-request-component-uri-path) |
| `:path` query | Query string | [Query string](waf-rule-statement-fields-list.md#waf-rule-statement-request-component-query-string)<br />[Single query parameter](waf-rule-statement-fields-list.md#waf-rule-statement-request-component-single-query-param)<br />[All query parameters](waf-rule-statement-fields-list.md#waf-rule-statement-request-component-all-query-params) |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
