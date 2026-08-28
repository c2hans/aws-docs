---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AutomationRulesActionV2.html
---

# AutomationRulesActionV2
<a name="API_AutomationRulesActionV2"></a>

Allows you to configure automated responses.

## Contents
<a name="API_AutomationRulesActionV2_Contents"></a>

 ** Type **   <a name="securityhub-Type-AutomationRulesActionV2-Type"></a>
The category of action to be executed by the automation rule.
Type: String
Valid Values: `FINDING_FIELDS_UPDATE | EXTERNAL_INTEGRATION`
Required: Yes

 ** ExternalIntegrationConfiguration **   <a name="securityhub-Type-AutomationRulesActionV2-ExternalIntegrationConfiguration"></a>
The settings for integrating automation rule actions with external systems or service.
Type: [ExternalIntegrationConfiguration](API_ExternalIntegrationConfiguration.md) object
Required: No

 ** FindingFieldsUpdate **   <a name="securityhub-Type-AutomationRulesActionV2-FindingFieldsUpdate"></a>
The changes to be applied to fields in a security finding when an automation rule is triggered.
Type: [AutomationRulesFindingFieldsUpdateV2](API_AutomationRulesFindingFieldsUpdateV2.md) object
Required: No

## See Also
<a name="API_AutomationRulesActionV2_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AutomationRulesActionV2)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AutomationRulesActionV2)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AutomationRulesActionV2)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
