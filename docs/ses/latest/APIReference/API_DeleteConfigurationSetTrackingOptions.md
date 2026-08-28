---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference/API_DeleteConfigurationSetTrackingOptions.html
---

# DeleteConfigurationSetTrackingOptions
<a name="API_DeleteConfigurationSetTrackingOptions"></a>

Deletes an association between a configuration set and a custom domain for open and click event tracking.

By default, images and links used for tracking open and click events are hosted on domains operated by Amazon SES. You can configure a subdomain of your own to handle these events. For information about using custom domains, see the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/dg/configure-custom-open-click-domains.html).

**Note**
Deleting this kind of association results in emails sent using the specified configuration set to capture open and click events using the standard, Amazon SES-operated domains.

## Request Parameters
<a name="API_DeleteConfigurationSetTrackingOptions_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ConfigurationSetName **
The name of the configuration set.
Type: String
Required: Yes

## Errors
<a name="API_DeleteConfigurationSetTrackingOptions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConfigurationSetDoesNotExist **
Indicates that the configuration set does not exist.
 ** ConfigurationSetName **
Indicates that the configuration set does not exist.
HTTP Status Code: 400

 ** TrackingOptionsDoesNotExist **
Indicates that the TrackingOptions object you specified does not exist.
 ** ConfigurationSetName **
Indicates that a TrackingOptions object does not exist in the specified configuration set.
HTTP Status Code: 400

## See Also
<a name="API_DeleteConfigurationSetTrackingOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/email-2010-12-01/DeleteConfigurationSetTrackingOptions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/email-2010-12-01/DeleteConfigurationSetTrackingOptions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/email-2010-12-01/DeleteConfigurationSetTrackingOptions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/email-2010-12-01/DeleteConfigurationSetTrackingOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/email-2010-12-01/DeleteConfigurationSetTrackingOptions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/email-2010-12-01/DeleteConfigurationSetTrackingOptions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/email-2010-12-01/DeleteConfigurationSetTrackingOptions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/email-2010-12-01/DeleteConfigurationSetTrackingOptions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/email-2010-12-01/DeleteConfigurationSetTrackingOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/email-2010-12-01/DeleteConfigurationSetTrackingOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SES Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ses` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
