---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsAmazonMqBrokerLogsDetails.html
---

# AwsAmazonMqBrokerLogsDetails
<a name="API_AwsAmazonMqBrokerLogsDetails"></a>

 Provides information about logs to be activated for the specified broker.

## Contents
<a name="API_AwsAmazonMqBrokerLogsDetails_Contents"></a>

 ** Audit **   <a name="securityhub-Type-AwsAmazonMqBrokerLogsDetails-Audit"></a>
 Activates audit logging. Every user management action made using JMX or the ActiveMQ Web Console is logged. Doesn't apply to RabbitMQ brokers.
Type: Boolean
Required: No

 ** AuditLogGroup **   <a name="securityhub-Type-AwsAmazonMqBrokerLogsDetails-AuditLogGroup"></a>
 The location of the CloudWatch Logs log group where audit logs are sent.
Type: String
Pattern: `.*\S.*`
Required: No

 ** General **   <a name="securityhub-Type-AwsAmazonMqBrokerLogsDetails-General"></a>
 Activates general logging.
Type: Boolean
Required: No

 ** GeneralLogGroup **   <a name="securityhub-Type-AwsAmazonMqBrokerLogsDetails-GeneralLogGroup"></a>
 The location of the CloudWatch Logs log group where general logs are sent.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Pending **   <a name="securityhub-Type-AwsAmazonMqBrokerLogsDetails-Pending"></a>
 The list of information about logs that are to be turned on for the specified broker.
Type: [AwsAmazonMqBrokerLogsPendingDetails](API_AwsAmazonMqBrokerLogsPendingDetails.md) object
Required: No

## See Also
<a name="API_AwsAmazonMqBrokerLogsDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsAmazonMqBrokerLogsDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsAmazonMqBrokerLogsDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsAmazonMqBrokerLogsDetails)
