---
source_url: https://docs.aws.amazon.com/prometheus/latest/APIReference/API_QueryLoggingConfigurationStatus.html
---

# QueryLoggingConfigurationStatus
<a name="API_QueryLoggingConfigurationStatus"></a>

The status information for a query logging configuration.

## Contents
<a name="API_QueryLoggingConfigurationStatus_Contents"></a>

 ** statusCode **   <a name="prometheus-Type-QueryLoggingConfigurationStatus-statusCode"></a>
The current status of the query logging configuration.
Type: String
Valid Values: `CREATING | ACTIVE | UPDATING | DELETING | CREATION_FAILED | UPDATE_FAILED`
Required: Yes

 ** statusReason **   <a name="prometheus-Type-QueryLoggingConfigurationStatus-statusReason"></a>
If there is a failure, the reason for the failure.
Type: String
Required: No

## See Also
<a name="API_QueryLoggingConfigurationStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amp-2020-08-01/QueryLoggingConfigurationStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amp-2020-08-01/QueryLoggingConfigurationStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amp-2020-08-01/QueryLoggingConfigurationStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Service for Prometheus. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prometheus` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
