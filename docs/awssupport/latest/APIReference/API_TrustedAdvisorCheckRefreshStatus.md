---
source_url: https://docs.aws.amazon.com/awssupport/latest/APIReference/API_TrustedAdvisorCheckRefreshStatus.html
---

# TrustedAdvisorCheckRefreshStatus
<a name="API_TrustedAdvisorCheckRefreshStatus"></a>

The refresh status of a Trusted Advisor check.

## Contents
<a name="API_TrustedAdvisorCheckRefreshStatus_Contents"></a>

 ** checkId **   <a name="AWSSupport-Type-TrustedAdvisorCheckRefreshStatus-checkId"></a>
The unique identifier for the Trusted Advisor check.
Type: String

 ** millisUntilNextRefreshable **   <a name="AWSSupport-Type-TrustedAdvisorCheckRefreshStatus-millisUntilNextRefreshable"></a>
The amount of time, in milliseconds, until the Trusted Advisor check is eligible for refresh.
Type: Long

 ** status **   <a name="AWSSupport-Type-TrustedAdvisorCheckRefreshStatus-status"></a>
The status of the Trusted Advisor check for which a refresh has been requested:
+  `none` - The check is not refreshed or the non-success status exceeds the timeout
+  `enqueued` - The check refresh requests has entered the refresh queue
+  `processing` - The check refresh request is picked up by the rule processing engine
+  `success` - The check is successfully refreshed
+  `abandoned` - The check refresh has failed
Type: String

## See Also
<a name="API_TrustedAdvisorCheckRefreshStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/support-2013-04-15/TrustedAdvisorCheckRefreshStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/support-2013-04-15/TrustedAdvisorCheckRefreshStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/support-2013-04-15/TrustedAdvisorCheckRefreshStatus)
