---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference/API_UpdateConfigurationSetReputationMetricsEnabled.html
---

# UpdateConfigurationSetReputationMetricsEnabled
<a name="API_UpdateConfigurationSetReputationMetricsEnabled"></a>

Enables or disables the publishing of reputation metrics for emails sent using a specific configuration set in a given AWS Region. Reputation metrics include bounce and complaint rates. These metrics are published to Amazon CloudWatch. By using CloudWatch, you can create alarms when bounce or complaint rates exceed certain thresholds.

You can execute this operation no more than once per second.

## Request Parameters
<a name="API_UpdateConfigurationSetReputationMetricsEnabled_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ConfigurationSetName **
The name of the configuration set to update.
Type: String
Required: Yes

 ** Enabled **
Describes whether or not Amazon SES publishes reputation metrics for the configuration set, such as bounce and complaint rates, to Amazon CloudWatch.
Type: Boolean
Required: Yes

## Errors
<a name="API_UpdateConfigurationSetReputationMetricsEnabled_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConfigurationSetDoesNotExist **
Indicates that the configuration set does not exist.
 ** ConfigurationSetName **
Indicates that the configuration set does not exist.
HTTP Status Code: 400

## See Also
<a name="API_UpdateConfigurationSetReputationMetricsEnabled_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/email-2010-12-01/UpdateConfigurationSetReputationMetricsEnabled)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/email-2010-12-01/UpdateConfigurationSetReputationMetricsEnabled)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/email-2010-12-01/UpdateConfigurationSetReputationMetricsEnabled)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/email-2010-12-01/UpdateConfigurationSetReputationMetricsEnabled)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/email-2010-12-01/UpdateConfigurationSetReputationMetricsEnabled)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/email-2010-12-01/UpdateConfigurationSetReputationMetricsEnabled)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/email-2010-12-01/UpdateConfigurationSetReputationMetricsEnabled)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/email-2010-12-01/UpdateConfigurationSetReputationMetricsEnabled)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/email-2010-12-01/UpdateConfigurationSetReputationMetricsEnabled)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/email-2010-12-01/UpdateConfigurationSetReputationMetricsEnabled)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SES Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ses` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
