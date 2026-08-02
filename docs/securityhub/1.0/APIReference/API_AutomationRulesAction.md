---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AutomationRulesAction.html
---

# AutomationRulesAction
<a name="API_AutomationRulesAction"></a>

 One or more actions that AWS Security Hub CSPM takes when a finding matches the defined criteria of a rule.

## Contents
<a name="API_AutomationRulesAction_Contents"></a>

 ** FindingFieldsUpdate **   <a name="securityhub-Type-AutomationRulesAction-FindingFieldsUpdate"></a>
 Specifies that the automation rule action is an update to a finding field.
Type: [AutomationRulesFindingFieldsUpdate](API_AutomationRulesFindingFieldsUpdate.md) object
Required: No

 ** Type **   <a name="securityhub-Type-AutomationRulesAction-Type"></a>
 Specifies the type of action that Security Hub CSPM takes when a finding matches the defined criteria of a rule.
Type: String
Valid Values: `FINDING_FIELDS_UPDATE`
Required: No

## See Also
<a name="API_AutomationRulesAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AutomationRulesAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AutomationRulesAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AutomationRulesAction)
