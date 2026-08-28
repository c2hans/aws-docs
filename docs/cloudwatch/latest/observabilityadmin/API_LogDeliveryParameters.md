---
source_url: https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_LogDeliveryParameters.html
---

# LogDeliveryParameters
<a name="API_LogDeliveryParameters"></a>

The configuration parameters for log delivery, including `logType` settings. Applies to resource types that support configurable log delivery, such as Amazon Bedrock Knowledge Bases and Elastic Load Balancing Application Load Balancers.

## Contents
<a name="API_LogDeliveryParameters_Contents"></a>

 ** LogTypes **   <a name="cwoa-Type-LogDeliveryParameters-LogTypes"></a>
The types of logs to collect from the resource.
Type: Array of strings
Valid Values: `APPLICATION_LOGS | USAGE_LOGS | SECURITY_FINDING_LOGS | ACCESS_LOGS | CONNECTION_LOGS | S3_SERVER_ACCESS_LOGS | ALB_ACCESS_LOGS | ALB_CONNECTION_LOGS | ALB_HEALTH_CHECK_LOGS`
Required: No

## See Also
<a name="API_LogDeliveryParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/observabilityadmin-2018-05-10/LogDeliveryParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/observabilityadmin-2018-05-10/LogDeliveryParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/observabilityadmin-2018-05-10/LogDeliveryParameters)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudwatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
