---
source_url: https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_CoreNetworkPolicyVersion.html
---

# CoreNetworkPolicyVersion
<a name="API_CoreNetworkPolicyVersion"></a>

Describes a core network policy version.

## Contents
<a name="API_CoreNetworkPolicyVersion_Contents"></a>

 ** Alias **   <a name="networkmanager-Type-CoreNetworkPolicyVersion-Alias"></a>
Whether a core network policy is the current policy or the most recently submitted policy.
Type: String
Valid Values: `LIVE | LATEST`
Required: No

 ** ChangeSetState **   <a name="networkmanager-Type-CoreNetworkPolicyVersion-ChangeSetState"></a>
The status of the policy version change set.
Type: String
Valid Values: `PENDING_GENERATION | FAILED_GENERATION | READY_TO_EXECUTE | EXECUTING | EXECUTION_SUCCEEDED | OUT_OF_DATE`
Required: No

 ** CoreNetworkId **   <a name="networkmanager-Type-CoreNetworkPolicyVersion-CoreNetworkId"></a>
The ID of a core network.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `^core-network-([0-9a-f]{8,17})$`
Required: No

 ** CreatedAt **   <a name="networkmanager-Type-CoreNetworkPolicyVersion-CreatedAt"></a>
The timestamp when a core network policy version was created.
Type: Timestamp
Required: No

 ** Description **   <a name="networkmanager-Type-CoreNetworkPolicyVersion-Description"></a>
The description of a core network policy version.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

 ** PolicyVersionId **   <a name="networkmanager-Type-CoreNetworkPolicyVersion-PolicyVersionId"></a>
The ID of the policy version.
Type: Integer
Required: No

## See Also
<a name="API_CoreNetworkPolicyVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/CoreNetworkPolicyVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/CoreNetworkPolicyVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/CoreNetworkPolicyVersion)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Global Networks for Transit Gateways. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query networkmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
