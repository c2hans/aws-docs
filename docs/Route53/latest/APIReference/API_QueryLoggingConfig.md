---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_QueryLoggingConfig.html
---

# QueryLoggingConfig
<a name="API_QueryLoggingConfig"></a>

A complex type that contains information about a configuration for DNS query logging.

## Contents
<a name="API_QueryLoggingConfig_Contents"></a>

 ** CloudWatchLogsLogGroupArn **   <a name="Route53-Type-QueryLoggingConfig-CloudWatchLogsLogGroupArn"></a>
The Amazon Resource Name (ARN) of the CloudWatch Logs log group that Amazon Route 53 is publishing logs to.
Type: String
Required: Yes

 ** HostedZoneId **   <a name="Route53-Type-QueryLoggingConfig-HostedZoneId"></a>
The ID of the hosted zone that CloudWatch Logs is logging queries for.
Type: String
Length Constraints: Maximum length of 32.
Required: Yes

 ** Id **   <a name="Route53-Type-QueryLoggingConfig-Id"></a>
The ID for a configuration for DNS query logging.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Required: Yes

## See Also
<a name="API_QueryLoggingConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/QueryLoggingConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/QueryLoggingConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/QueryLoggingConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
