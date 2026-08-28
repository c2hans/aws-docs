---
source_url: https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_ReputationOptions.html
---

# ReputationOptions
<a name="API_ReputationOptions"></a>

Enable or disable collection of reputation metrics for emails that you send using this configuration set in the current AWS Region.

## Contents
<a name="API_ReputationOptions_Contents"></a>

 ** LastFreshStart **   <a name="pinpoint-Type-ReputationOptions-LastFreshStart"></a>
The date and time (in Unix time) when the reputation metrics were last given a fresh start. When your account is given a fresh start, your reputation metrics are calculated starting from the date of the fresh start.
Type: Timestamp
Required: No

 ** ReputationMetricsEnabled **   <a name="pinpoint-Type-ReputationOptions-ReputationMetricsEnabled"></a>
If `true`, tracking of reputation metrics is enabled for the configuration set. If `false`, tracking of reputation metrics is disabled for the configuration set.
Type: Boolean
Required: No

## See Also
<a name="API_ReputationOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-email-2018-07-26/ReputationOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-email-2018-07-26/ReputationOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-email-2018-07-26/ReputationOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Pinpoint Email. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pinpoint-email` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
