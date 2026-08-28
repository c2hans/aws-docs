---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsAmazonMqBrokerLogsPendingDetails.html
---

# AwsAmazonMqBrokerLogsPendingDetails
<a name="API_AwsAmazonMqBrokerLogsPendingDetails"></a>

 Provides information about logs to be activated for the specified broker.

## Contents
<a name="API_AwsAmazonMqBrokerLogsPendingDetails_Contents"></a>

 ** Audit **   <a name="securityhub-Type-AwsAmazonMqBrokerLogsPendingDetails-Audit"></a>
 Activates audit logging. Every user management action made using JMX or the ActiveMQ Web Console is logged. Doesn't apply to RabbitMQ brokers.
Type: Boolean
Required: No

 ** General **   <a name="securityhub-Type-AwsAmazonMqBrokerLogsPendingDetails-General"></a>
 Activates general logging.
Type: Boolean
Required: No

## See Also
<a name="API_AwsAmazonMqBrokerLogsPendingDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsAmazonMqBrokerLogsPendingDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsAmazonMqBrokerLogsPendingDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsAmazonMqBrokerLogsPendingDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
