---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_LoggingConfiguration.html
---

# LoggingConfiguration
<a name="API_LoggingConfiguration"></a>

Defines an association between logging destinations and a web ACL resource, for logging from AWS WAF. As part of the association, you can specify parts of the standard logging fields to keep out of the logs and you can specify filters so that you log only a subset of the logging records.

If you configure data protection for the web ACL, the protection applies to the data that AWS WAF sends to the logs.

**Note**
You can define one logging destination per web ACL.

You can access information about the traffic that AWS WAF inspects using the following steps:

1. Create your logging destination. You can use an Amazon CloudWatch Logs log group, an Amazon Simple Storage Service (Amazon S3) bucket, or an Amazon Kinesis Data Firehose.

   The name that you give the destination must start with `aws-waf-logs-`. Depending on the type of destination, you might need to configure additional settings or permissions.

   For configuration requirements and pricing information for each destination type, see [Logging web ACL traffic](https://docs.aws.amazon.com/waf/latest/developerguide/logging.html) in the * AWS WAF Developer Guide*.

1. Associate your logging destination to your web ACL using a `PutLoggingConfiguration` request.

When you successfully enable logging using a `PutLoggingConfiguration` request, AWS WAF creates an additional role or policy that is required to write logs to the logging destination. For an Amazon CloudWatch Logs log group, AWS WAF creates a resource policy on the log group. For an Amazon S3 bucket, AWS WAF creates a bucket policy. For an Amazon Kinesis Data Firehose, AWS WAF creates a service-linked role.

For additional information about web ACL logging, see [Logging web ACL traffic information](https://docs.aws.amazon.com/waf/latest/developerguide/logging.html) in the * AWS WAF Developer Guide*.

## Contents
<a name="API_LoggingConfiguration_Contents"></a>

 ** LogDestinationConfigs **   <a name="WAF-Type-LoggingConfiguration-LogDestinationConfigs"></a>
The logging destination configuration that you want to associate with the web ACL.
You can associate one logging destination to a web ACL.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `.*\S.*`
Required: Yes

 ** ResourceArn **   <a name="WAF-Type-LoggingConfiguration-ResourceArn"></a>
The Amazon Resource Name (ARN) of the web ACL that you want to associate with `LogDestinationConfigs`.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `.*\S.*`
Required: Yes

 ** LoggingFilter **   <a name="WAF-Type-LoggingConfiguration-LoggingFilter"></a>
Filtering that specifies which web requests are kept in the logs and which are dropped. You can filter on the rule action and on the web request labels that were applied by matching rules during web ACL evaluation.
Type: [LoggingFilter](API_LoggingFilter.md) object
Required: No

 ** LogScope **   <a name="WAF-Type-LoggingConfiguration-LogScope"></a>
The owner of the logging configuration, which must be set to `CUSTOMER` for the configurations that you manage.
The log scope `SECURITY_LAKE` indicates a configuration that is managed through Amazon Security Lake. You can use Security Lake to collect log and event data from various sources for normalization, analysis, and management. For information, see [Collecting data from AWS services](https://docs.aws.amazon.com/security-lake/latest/userguide/internal-sources.html) in the *Amazon Security Lake user guide*.
The log scope `CLOUDWATCH_TELEMETRY_RULE_MANAGED` indicates a configuration that is managed through Amazon CloudWatch Logs for telemetry data collection and analysis. For information, see [What is Amazon CloudWatch Logs ?](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html) in the *Amazon CloudWatch Logs user guide*.
Default: `CUSTOMER`
Type: String
Valid Values: `CUSTOMER | SECURITY_LAKE | CLOUDWATCH_TELEMETRY_RULE_MANAGED`
Required: No

 ** LogType **   <a name="WAF-Type-LoggingConfiguration-LogType"></a>
Used to distinguish between various logging options. Currently, there is one option.
Default: `WAF_LOGS`
Type: String
Valid Values: `WAF_LOGS`
Required: No

 ** ManagedByFirewallManager **   <a name="WAF-Type-LoggingConfiguration-ManagedByFirewallManager"></a>
Indicates whether the logging configuration was created by AWS Firewall Manager, as part of an AWS WAF policy configuration. If true, only Firewall Manager can modify or delete the configuration.
The logging configuration can be created by AWS Firewall Manager for use with any web ACL that Firewall Manager is using for an AWS WAF policy. Web ACLs that Firewall Manager creates and uses have their `ManagedByFirewallManager` property set to true. Web ACLs that were created by a customer account and then retrofitted by Firewall Manager for use by a policy have their `RetrofittedByFirewallManager` property set to true. For either case, any corresponding logging configuration will indicate `ManagedByFirewallManager`.
Type: Boolean
Required: No

 ** RedactedFields **   <a name="WAF-Type-LoggingConfiguration-RedactedFields"></a>
The parts of the request that you want to keep out of the logs.
For example, if you redact the `SingleHeader` field, the `HEADER` field in the logs will be `REDACTED` for all rules that use the `SingleHeader` `FieldToMatch` setting.
If you configure data protection for the web ACL, the protection applies to the data that AWS WAF sends to the logs.
Redaction applies only to the component that's specified in the rule's `FieldToMatch` setting, so the `SingleHeader` redaction doesn't apply to rules that use the `Headers` `FieldToMatch`.
You can specify only the following fields for redaction: `UriPath`, `QueryString`, `SingleHeader`, and `Method`.
This setting has no impact on request sampling. You can only exclude fields from request sampling by disabling sampling in the web ACL visibility configuration or by configuring data protection for the web ACL.
Type: Array of [FieldToMatch](API_FieldToMatch.md) objects
Array Members: Maximum number of 100 items.
Required: No

## See Also
<a name="API_LoggingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/LoggingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/LoggingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/LoggingConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
