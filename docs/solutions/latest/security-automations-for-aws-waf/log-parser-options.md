---
source_url: https://docs.aws.amazon.com/solutions/latest/security-automations-for-aws-waf/log-parser-options.html
---

# Log parser options
<a name="log-parser-options"></a>

As described in the [Architecture overview](architecture-overview.md), there are three options to handle HTTP flood and scanner and probe protections. The following sections explain each of these options in more detail.

## AWS WAF rate-based rule
<a name="aws-waf-rate-based-rule"></a>

Rate-based rules are available for HTTP flood protection. By default, a rate-based rule aggregates and rate limits requests based on the request IP address. This solution allows you to specify the number of web requests that a client IP allows in a trailing, continuously updated five-minute period. If an IP address breaches the configured quota, AWS WAF blocks new requests blocked until the request rate is less than the configured quota.

We recommend selecting the rate-based rule option if the request quota is more than 2,000 requests per five minutes and you don’t need to implement customizations. For example, you don’t consider static resource access when counting requests.

You can further configure the rule to use various other aggregation keys and key combinations. For more information, see [Aggregation options and keys](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-type-rate-based-aggregation-options.html).

## Amazon Athena log parser
<a name="amazon-athena-log-parser"></a>

Both **HTTP Flood Protection** and **Scanner & Probe** **Protection** template parameters provide the Athena log parser option. When activated, CloudFormation provisions an Athena query and a scheduled Lambda function responsible for orchestrating Athena to run, process result output, and update AWS WAF. This Lambda function is invoked by a CloudWatch event configured to run every five minutes. This is configurable with the **Athena Query Run Time Schedule** parameter.

We recommend selecting this option when you can’t use AWS WAF rate-based rules and you have familiarity with SQL to implement customizations. For more information about how to change the default query, refer to [View Amazon Athena queries](view-amazon-athena-queries.md).

HTTP flood protection is based on AWS WAF access log processing and uses WAF log files. The WAF access log type has a lower lag time, which you can use to identify HTTP flood origins more quickly when compared to CloudFront or ALB log delivery time. However, you must select the CloudFront or ALB log type in the **Activate Scanner & Probe Protection** template parameter to receive response status codes.

**Note**
If a bad bot bypasses the honeypot and directly interacts with ALB or CloudFront, the system detects malicious behavior through log analysis unless both HTTP Flood Protection and Scanner & Probe Protection are not using the Lambda log parser.

## AWS Lambda log parser
<a name="aws-lambda-log-parser"></a>

The **HTTP Flood Protection** and **Scanner & Probe Protection** template parameters provide the **AWS Lambda Log Parser** option. Use the Lambda log parser only when the **AWS WAF rate-based rule** and **Amazon Athena log parser** options aren’t available. A known limitation of this option is that information is processed within the context of the file being processed. For example, an IP might generate more requests or errors than the defined quota, but because this information is split into different files, each file doesn’t store enough data to exceed the quota.

**Note**
Additionally, if a bad bot bypasses the honeypot and interacts directly with ALB or CloudFront, detection relies on the chosen log parser option to effectively identify and block malicious activity.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Security Automations for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
