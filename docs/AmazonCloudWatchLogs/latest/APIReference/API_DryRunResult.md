---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DryRunResult.html
---

# DryRunResult
<a name="API_DryRunResult"></a>

Contains the estimated impact of creating, updating, or deleting an account-level retention policy. The analysis compares the effective retention period of each log group, which accounts for all account-level retention policies that apply to it, before and after the change. Log groups in the Delivery class are not included.

## Contents
<a name="API_DryRunResult_Contents"></a>

 ** decreasedRetentionLogGroupCount **   <a name="CWL-Type-DryRunResult-decreasedRetentionLogGroupCount"></a>
The number of log groups whose effective retention period would become shorter.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** failedAnalysisCount **   <a name="CWL-Type-DryRunResult-failedAnalysisCount"></a>
The number of log groups in the scope of the policy that could not be analyzed. These log groups are not included in `totalMatchedLogGroups`.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** increasedRetentionLogGroupCount **   <a name="CWL-Type-DryRunResult-increasedRetentionLogGroupCount"></a>
The number of log groups whose effective retention period would become longer.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** topLogGroupsImpacted **   <a name="CWL-Type-DryRunResult-topLogGroupsImpacted"></a>
Up to 20 log groups in the scope of the policy, sorted by stored bytes in descending order. This list can include log groups whose effective retention period would not change.
Type: Array of [LogGroupImpact](API_LogGroupImpact.md) objects
Required: No

 ** totalMatchedLogGroups **   <a name="CWL-Type-DryRunResult-totalMatchedLogGroups"></a>
The number of log groups in the scope of the policy that were analyzed. This value is the sum of `increasedRetentionLogGroupCount`, `decreasedRetentionLogGroupCount`, and `unchangedRetentionLogGroupCount`, and does not include log groups that could not be analyzed.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** unchangedRetentionLogGroupCount **   <a name="CWL-Type-DryRunResult-unchangedRetentionLogGroupCount"></a>
The number of log groups whose effective retention period would not change.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_DryRunResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/DryRunResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/DryRunResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/DryRunResult)
