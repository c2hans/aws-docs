---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-customer-profiles_RuleBasedMatchingResponse.html
---

# RuleBasedMatchingResponse
<a name="API_connect-customer-profiles_RuleBasedMatchingResponse"></a>

The response of the Rule-based matching request.

## Contents
<a name="API_connect-customer-profiles_RuleBasedMatchingResponse_Contents"></a>

 ** AttributeTypesSelector **   <a name="connect-Type-connect-customer-profiles_RuleBasedMatchingResponse-AttributeTypesSelector"></a>
Configures information about the `AttributeTypesSelector` where the rule-based identity resolution uses to match profiles.
Type: [AttributeTypesSelector](API_connect-customer-profiles_AttributeTypesSelector.md) object
Required: No

 ** ConflictResolution **   <a name="connect-Type-connect-customer-profiles_RuleBasedMatchingResponse-ConflictResolution"></a>
How the auto-merging process should resolve conflicts between different profiles.
Type: [ConflictResolution](API_connect-customer-profiles_ConflictResolution.md) object
Required: No

 ** Enabled **   <a name="connect-Type-connect-customer-profiles_RuleBasedMatchingResponse-Enabled"></a>
The flag that enables the rule-based matching process of duplicate profiles.
Type: Boolean
Required: No

 ** ExportingConfig **   <a name="connect-Type-connect-customer-profiles_RuleBasedMatchingResponse-ExportingConfig"></a>
Configuration information about the S3 bucket where Identity Resolution Jobs writes result files.
You need to give Customer Profiles service principal write permission to your S3 bucket. Otherwise, you'll get an exception in the API response. For an example policy, see [Amazon Connect Customer Profiles cross-service confused deputy prevention](https://docs.aws.amazon.com/connect/latest/adminguide/cross-service-confused-deputy-prevention.html#customer-profiles-cross-service).
Type: [ExportingConfig](API_connect-customer-profiles_ExportingConfig.md) object
Required: No

 ** MatchingRules **   <a name="connect-Type-connect-customer-profiles_RuleBasedMatchingResponse-MatchingRules"></a>
Configures how the rule-based matching process should match profiles. You can have up to 15 `MatchingRule` in the `MatchingRules`.
Type: Array of [MatchingRule](API_connect-customer-profiles_MatchingRule.md) objects
Array Members: Minimum number of 1 item. Maximum number of 15 items.
Required: No

 ** MaxAllowedRuleLevelForMatching **   <a name="connect-Type-connect-customer-profiles_RuleBasedMatchingResponse-MaxAllowedRuleLevelForMatching"></a>
Indicates the maximum allowed rule level.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 15.
Required: No

 ** MaxAllowedRuleLevelForMerging **   <a name="connect-Type-connect-customer-profiles_RuleBasedMatchingResponse-MaxAllowedRuleLevelForMerging"></a>
 [MatchingRule](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_MatchingRule.html)
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 15.
Required: No

 ** Status **   <a name="connect-Type-connect-customer-profiles_RuleBasedMatchingResponse-Status"></a>
PENDING
+ The first status after configuration a rule-based matching rule. If it is an existing domain, the rule-based Identity Resolution waits one hour before creating the matching rule. If it is a new domain, the system will skip the `PENDING` stage.
IN\_PROGRESS
+ The system is creating the rule-based matching rule. Under this status, the system is evaluating the existing data and you can no longer change the Rule-based matching configuration.
ACTIVE
+ The rule is ready to use. You can change the rule a day after the status is in `ACTIVE`.
Type: String
Valid Values: `PENDING | IN_PROGRESS | ACTIVE`
Required: No

## See Also
<a name="API_connect-customer-profiles_RuleBasedMatchingResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/RuleBasedMatchingResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/RuleBasedMatchingResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/RuleBasedMatchingResponse)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
