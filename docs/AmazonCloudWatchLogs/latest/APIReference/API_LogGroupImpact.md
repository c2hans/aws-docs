---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_LogGroupImpact.html
---

# LogGroupImpact
<a name="API_LogGroupImpact"></a>

Describes the estimated effect of an account-level retention policy change on one log group.

## Contents
<a name="API_LogGroupImpact_Contents"></a>

 ** currentRetention **   <a name="CWL-Type-LogGroupImpact-currentRetention"></a>
The current effective retention period of the log group, in days. A value of `NEVER_EXPIRE` indicates that log events in the log group never expire.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 12.
Required: No

 ** logGroupName **   <a name="CWL-Type-LogGroupImpact-logGroupName"></a>
The name of the log group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\.\-_/#A-Za-z0-9]+`
Required: No

 ** proposedRetention **   <a name="CWL-Type-LogGroupImpact-proposedRetention"></a>
The effective retention period of the log group, in days, after the change. A value of `NEVER_EXPIRE` indicates that log events in the log group would never expire.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 12.
Required: No

 ** storedBytes **   <a name="CWL-Type-LogGroupImpact-storedBytes"></a>
The number of bytes stored in the log group.
Type: Long
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_LogGroupImpact_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/LogGroupImpact)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/LogGroupImpact)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/LogGroupImpact)
