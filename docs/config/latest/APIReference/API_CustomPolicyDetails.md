---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_CustomPolicyDetails.html
---

# CustomPolicyDetails
<a name="API_CustomPolicyDetails"></a>

Provides the runtime system, policy definition, and whether debug logging enabled. You can specify the following CustomPolicyDetails parameter values only for AWS Config Custom Policy rules.

## Contents
<a name="API_CustomPolicyDetails_Contents"></a>

 ** PolicyRuntime **   <a name="config-Type-CustomPolicyDetails-PolicyRuntime"></a>
The runtime system for your AWS Config Custom Policy rule. Guard is a policy-as-code language that allows you to write policies that are enforced by AWS Config Custom Policy rules. For more information about Guard, see the [Guard GitHub Repository](https://github.com/aws-cloudformation/cloudformation-guard).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `guard\-2\.x\.x`
Required: Yes

 ** PolicyText **   <a name="config-Type-CustomPolicyDetails-PolicyText"></a>
The policy definition containing the logic for your AWS Config Custom Policy rule.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10000.
Required: Yes

 ** EnableDebugLogDelivery **   <a name="config-Type-CustomPolicyDetails-EnableDebugLogDelivery"></a>
The boolean expression for enabling debug logging for your AWS Config Custom Policy rule. The default value is `false`.
Type: Boolean
Required: No

## See Also
<a name="API_CustomPolicyDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/CustomPolicyDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/CustomPolicyDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/CustomPolicyDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
