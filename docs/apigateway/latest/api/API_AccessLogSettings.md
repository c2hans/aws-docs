---
source_url: https://docs.aws.amazon.com/apigateway/latest/api/API_AccessLogSettings.html
---

# AccessLogSettings
<a name="API_AccessLogSettings"></a>

Access log settings, including the access log format and access log destination ARN.

## Contents
<a name="API_AccessLogSettings_Contents"></a>

 ** destinationArn **   <a name="apigw-Type-AccessLogSettings-destinationArn"></a>
The Amazon Resource Name (ARN) of the CloudWatch Logs log group or Kinesis Data Firehose delivery stream to receive access logs. If you specify a Kinesis Data Firehose delivery stream, the stream name must begin with `amazon-apigateway-`.
Type: String
Required: No

 ** format **   <a name="apigw-Type-AccessLogSettings-format"></a>
A single line format of the access logs of data, as specified by selected $context variables. The format must include at least `$context.requestId`.
Type: String
Required: No

## See Also
<a name="API_AccessLogSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apigateway-2015-07-09/AccessLogSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apigateway-2015-07-09/AccessLogSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apigateway-2015-07-09/AccessLogSettings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon API Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apigateway` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
