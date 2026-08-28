---
source_url: https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_CoreNetworkPolicyError.html
---

# CoreNetworkPolicyError
<a name="API_CoreNetworkPolicyError"></a>

Provides details about an error in a core network policy.

## Contents
<a name="API_CoreNetworkPolicyError_Contents"></a>

 ** ErrorCode **   <a name="networkmanager-Type-CoreNetworkPolicyError-ErrorCode"></a>
The error code associated with a core network policy error.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10000000.
Pattern: `[\s\S]*`
Required: Yes

 ** Message **   <a name="networkmanager-Type-CoreNetworkPolicyError-Message"></a>
The message associated with a core network policy error code.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10000000.
Pattern: `[\s\S]*`
Required: Yes

 ** Path **   <a name="networkmanager-Type-CoreNetworkPolicyError-Path"></a>
The JSON path where the error was discovered in the policy document.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10000000.
Pattern: `[\s\S]*`
Required: No

## See Also
<a name="API_CoreNetworkPolicyError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/CoreNetworkPolicyError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/CoreNetworkPolicyError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/CoreNetworkPolicyError)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Global Networks for Transit Gateways. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query networkmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
