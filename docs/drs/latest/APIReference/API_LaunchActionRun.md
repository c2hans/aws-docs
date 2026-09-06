---
source_url: https://docs.aws.amazon.com/drs/latest/APIReference/API_LaunchActionRun.html
---

# LaunchActionRun
<a name="API_LaunchActionRun"></a>

Launch action run.

## Contents
<a name="API_LaunchActionRun_Contents"></a>

 ** action **   <a name="drs-Type-LaunchActionRun-action"></a>
Action.
Type: [LaunchAction](API_LaunchAction.md) object
Required: No

 ** failureReason **   <a name="drs-Type-LaunchActionRun-failureReason"></a>
Failure reason.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[0-9a-zA-Z ():/.,'-_#*;]*`
Required: No

 ** runId **   <a name="drs-Type-LaunchActionRun-runId"></a>
Run Id.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`
Required: No

 ** status **   <a name="drs-Type-LaunchActionRun-status"></a>
Run status.
Type: String
Valid Values: `IN_PROGRESS | SUCCEEDED | FAILED`
Required: No

## See Also
<a name="API_LaunchActionRun_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/drs-2020-02-26/LaunchActionRun)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/drs-2020-02-26/LaunchActionRun)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/drs-2020-02-26/LaunchActionRun)
