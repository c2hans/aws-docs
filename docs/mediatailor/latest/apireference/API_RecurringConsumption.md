---
source_url: https://docs.aws.amazon.com/mediatailor/latest/apireference/API_RecurringConsumption.html
---

# RecurringConsumption
<a name="API_RecurringConsumption"></a>

The settings that determine how and when MediaTailor places prefetched ads into upcoming ad breaks for recurring prefetch scedules.

## Contents
<a name="API_RecurringConsumption_Contents"></a>

 ** AvailMatchingCriteria **   <a name="mediatailor-Type-RecurringConsumption-AvailMatchingCriteria"></a>
The configuration for the dynamic variables that determine which ad breaks that MediaTailor inserts prefetched ads in.
Type: Array of [AvailMatchingCriteria](API_AvailMatchingCriteria.md) objects
Required: No

 ** RetrievedAdExpirationSeconds **   <a name="mediatailor-Type-RecurringConsumption-RetrievedAdExpirationSeconds"></a>
The number of seconds that an ad is available for insertion after it was prefetched.
Type: Integer
Required: No

## See Also
<a name="API_RecurringConsumption_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediatailor-2018-04-23/RecurringConsumption)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediatailor-2018-04-23/RecurringConsumption)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediatailor-2018-04-23/RecurringConsumption)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaTailor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediatailor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
