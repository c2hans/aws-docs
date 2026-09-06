---
source_url: https://docs.aws.amazon.com/drs/latest/APIReference/API_LaunchActionsStatus.html
---

# LaunchActionsStatus
<a name="API_LaunchActionsStatus"></a>

Launch actions status.

## Contents
<a name="API_LaunchActionsStatus_Contents"></a>

 ** runs **   <a name="drs-Type-LaunchActionsStatus-runs"></a>
List of post launch action status.
Type: Array of [LaunchActionRun](API_LaunchActionRun.md) objects
Required: No

 ** ssmAgentDiscoveryDatetime **   <a name="drs-Type-LaunchActionsStatus-ssmAgentDiscoveryDatetime"></a>
Time where the AWS Systems Manager was detected as running on the launched instance.
Type: String
Length Constraints: Minimum length of 19. Maximum length of 32.
Pattern: `[1-9][0-9]*-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])T([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](\.[0-9]+)?Z`
Required: No

## See Also
<a name="API_LaunchActionsStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/drs-2020-02-26/LaunchActionsStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/drs-2020-02-26/LaunchActionsStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/drs-2020-02-26/LaunchActionsStatus)
