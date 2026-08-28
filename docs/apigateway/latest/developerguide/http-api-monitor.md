---
source_url: https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-monitor.html
---

# Monitor HTTP APIs in API Gateway
<a name="http-api-monitor"></a>

You can use CloudWatch metrics and CloudWatch Logs to monitor HTTP APIs. By combining logs and metrics, you can log errors and monitor your API's performance.

**Note**
API Gateway might not generate logs and metrics in the following cases:
413 Request Entity Too Large errors
Excessive 429 Too Many Requests errors
400 series errors from requests sent to a custom domain that has no API mapping
500 series errors caused by internal failures

**Topics**
+ [Monitor CloudWatch metrics for HTTP APIs in API Gateway](http-api-metrics.md)
+ [Configure logging for HTTP APIs in API Gateway](http-api-logging.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon API Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apigateway` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
