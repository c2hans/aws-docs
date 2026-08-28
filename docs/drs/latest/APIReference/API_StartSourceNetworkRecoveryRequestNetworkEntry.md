---
source_url: https://docs.aws.amazon.com/drs/latest/APIReference/API_StartSourceNetworkRecoveryRequestNetworkEntry.html
---

# StartSourceNetworkRecoveryRequestNetworkEntry
<a name="API_StartSourceNetworkRecoveryRequestNetworkEntry"></a>

An object representing the Source Network to recover.

## Contents
<a name="API_StartSourceNetworkRecoveryRequestNetworkEntry_Contents"></a>

 ** sourceNetworkID **   <a name="drs-Type-StartSourceNetworkRecoveryRequestNetworkEntry-sourceNetworkID"></a>
The ID of the Source Network you want to recover.
Type: String
Length Constraints: Fixed length of 20.
Pattern: `sn-[0-9a-zA-Z]{17}`
Required: Yes

 ** cfnStackName **   <a name="drs-Type-StartSourceNetworkRecoveryRequestNetworkEntry-cfnStackName"></a>
CloudFormation stack name to be used for recovering the network.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z][-a-zA-Z0-9]*`
Required: No

## See Also
<a name="API_StartSourceNetworkRecoveryRequestNetworkEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/drs-2020-02-26/StartSourceNetworkRecoveryRequestNetworkEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/drs-2020-02-26/StartSourceNetworkRecoveryRequestNetworkEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/drs-2020-02-26/StartSourceNetworkRecoveryRequestNetworkEntry)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Disaster Recovery. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query drs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
