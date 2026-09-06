---
source_url: https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_ScopeSummary.html
---

# ScopeSummary
<a name="API_ScopeSummary"></a>

A summary of information about a scope, including the ARN, target ID, and AWS Region.

## Contents
<a name="API_ScopeSummary_Contents"></a>

 ** scopeArn **   <a name="networkflowmonitor-Type-ScopeSummary-scopeArn"></a>
The Amazon Resource Name (ARN) of the scope.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:.*`
Required: Yes

 ** scopeId **   <a name="networkflowmonitor-Type-ScopeSummary-scopeId"></a>
The identifier for the scope that includes the resources that you want to get data results for. A scope ID is an internally-generated identifier that includes all the resources for the accounts in a scope.
Type: String
Required: Yes

 ** status **   <a name="networkflowmonitor-Type-ScopeSummary-status"></a>
The status for a scope. The status can be one of the following: `SUCCEEDED`, `IN_PROGRESS`, `FAILED`, `DEACTIVATING`, or `DEACTIVATED`.
A status of `DEACTIVATING` means that you've requested a scope to be deactivated and Network Flow Monitor is in the process of deactivating the scope. A status of `DEACTIVATED` means that the deactivating process is complete.
Type: String
Valid Values: `SUCCEEDED | IN_PROGRESS | FAILED | DEACTIVATING | DEACTIVATED`
Required: Yes

## See Also
<a name="API_ScopeSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkflowmonitor-2023-04-19/ScopeSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkflowmonitor-2023-04-19/ScopeSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkflowmonitor-2023-04-19/ScopeSummary)
