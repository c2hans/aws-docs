---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference/API_ListConfigurationSets.html
---

# ListConfigurationSets
<a name="API_ListConfigurationSets"></a>

Provides a list of the configuration sets associated with your Amazon SES account in the current AWS Region. For information about using configuration sets, see [Monitoring Your Amazon SES Sending Activity](https://docs.aws.amazon.com/ses/latest/dg/monitor-sending-activity.html) in the *Amazon SES Developer Guide.*

You can execute this operation no more than once per second. This operation returns up to 1,000 configuration sets each time it is run. If your Amazon SES account has more than 1,000 configuration sets, this operation also returns `NextToken`. You can then execute the `ListConfigurationSets` operation again, passing the `NextToken` parameter and the value of the NextToken element to retrieve additional results.

## Request Parameters
<a name="API_ListConfigurationSets_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** MaxItems **
The number of configuration sets to return.
Type: Integer
Required: No

 ** NextToken **
A token returned from a previous call to `ListConfigurationSets` to indicate the position of the configuration set in the configuration set list.
Type: String
Required: No

## Response Elements
<a name="API_ListConfigurationSets_ResponseElements"></a>

The following elements are returned by the service.

 **ConfigurationSets.member.N**
A list of configuration sets.
Type: Array of [ConfigurationSet](API_ConfigurationSet.md) objects

 ** NextToken **
A token indicating that there are additional configuration sets available to be listed. Pass this token to successive calls of `ListConfigurationSets`.
Type: String

## Errors
<a name="API_ListConfigurationSets_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ListConfigurationSets_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/email-2010-12-01/ListConfigurationSets)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/email-2010-12-01/ListConfigurationSets)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/email-2010-12-01/ListConfigurationSets)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/email-2010-12-01/ListConfigurationSets)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/email-2010-12-01/ListConfigurationSets)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/email-2010-12-01/ListConfigurationSets)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/email-2010-12-01/ListConfigurationSets)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/email-2010-12-01/ListConfigurationSets)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/email-2010-12-01/ListConfigurationSets)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/email-2010-12-01/ListConfigurationSets)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SES Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ses` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
