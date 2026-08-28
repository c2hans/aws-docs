---
source_url: https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_CanaryRunStatus.html
---

# CanaryRunStatus
<a name="API_CanaryRunStatus"></a>

This structure contains the status information about a canary run.

## Contents
<a name="API_CanaryRunStatus_Contents"></a>

 ** State **   <a name="synthetics-Type-CanaryRunStatus-State"></a>
The current state of the run.
Type: String
Valid Values: `RUNNING | PASSED | FAILED`
Required: No

 ** StateReason **   <a name="synthetics-Type-CanaryRunStatus-StateReason"></a>
If run of the canary failed, this field contains the reason for the error.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** StateReasonCode **   <a name="synthetics-Type-CanaryRunStatus-StateReasonCode"></a>
If this value is `CANARY_FAILURE`, either the canary script failed or Synthetics ran into a fatal error when running the canary. For example, a canary timeout misconfiguration setting can cause the canary to timeout before Synthetics can evaluate its status.
 If this value is `EXECUTION_FAILURE`, a non-critical failure occurred such as failing to save generated debug artifacts (for example, screenshots or har files).
If both types of failures occurred, the `CANARY_FAILURE` takes precedence. To understand the exact error, use the [StateReason](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_CanaryRunStatus.html) API.
Type: String
Valid Values: `CANARY_FAILURE | EXECUTION_FAILURE`
Required: No

 ** TestResult **   <a name="synthetics-Type-CanaryRunStatus-TestResult"></a>
Specifies the status of canary script for this run. When Synthetics tries to determine the status but fails, the result is marked as `UNKNOWN`. For the overall status of canary run, see [State](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_CanaryRunStatus.html).
Type: String
Valid Values: `PASSED | FAILED | UNKNOWN`
Required: No

## See Also
<a name="API_CanaryRunStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/synthetics-2017-10-11/CanaryRunStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/synthetics-2017-10-11/CanaryRunStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/synthetics-2017-10-11/CanaryRunStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch Synthetics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonSynthetics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
