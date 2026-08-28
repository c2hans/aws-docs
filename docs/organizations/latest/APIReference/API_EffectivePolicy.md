---
source_url: https://docs.aws.amazon.com/organizations/latest/APIReference/API_EffectivePolicy.html
---

# EffectivePolicy
<a name="API_EffectivePolicy"></a>

Contains rules to be applied to the affected accounts. The effective policy is the aggregation of any policies the account inherits, plus any policy directly attached to the account.

## Contents
<a name="API_EffectivePolicy_Contents"></a>

 ** LastUpdatedTimestamp **   <a name="organizations-Type-EffectivePolicy-LastUpdatedTimestamp"></a>
The time of the last update to this policy.
Type: Timestamp
Required: No

 ** PolicyContent **   <a name="organizations-Type-EffectivePolicy-PolicyContent"></a>
The text content of the policy.
Type: String
Length Constraints: Minimum length of 1.
Pattern: `[\s\S]*`
Required: No

 ** PolicyType **   <a name="organizations-Type-EffectivePolicy-PolicyType"></a>
The policy type.
Type: String
Valid Values: `TAG_POLICY | BACKUP_POLICY | AISERVICES_OPT_OUT_POLICY | CHATBOT_POLICY | DECLARATIVE_POLICY_EC2 | SECURITYHUB_POLICY | INSPECTOR_POLICY | UPGRADE_ROLLOUT_POLICY | BEDROCK_POLICY | S3_POLICY | NETWORK_SECURITY_DIRECTOR_POLICY`
Required: No

 ** TargetId **   <a name="organizations-Type-EffectivePolicy-TargetId"></a>
The account ID of the policy target.
Type: String
Length Constraints: Maximum length of 100.
Pattern: `^(r-[0-9a-z]{4,32})|(\d{12})|(ou-[0-9a-z]{4,32}-[a-z0-9]{8,32})$`
Required: No

## See Also
<a name="API_EffectivePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/organizations-2016-11-28/EffectivePolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/organizations-2016-11-28/EffectivePolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/organizations-2016-11-28/EffectivePolicy)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Organizations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query organizations` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
