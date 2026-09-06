---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AutomationRulesFindingFieldsUpdateV2.html
---

# AutomationRulesFindingFieldsUpdateV2
<a name="API_AutomationRulesFindingFieldsUpdateV2"></a>

Allows you to define the structure for modifying specific fields in security findings.

## Contents
<a name="API_AutomationRulesFindingFieldsUpdateV2_Contents"></a>

 ** Comment **   <a name="securityhub-Type-AutomationRulesFindingFieldsUpdateV2-Comment"></a>
Notes or contextual information for findings that are modified by the automation rule.
Type: String
Pattern: `.*\S.*`
Required: No

 ** SeverityId **   <a name="securityhub-Type-AutomationRulesFindingFieldsUpdateV2-SeverityId"></a>
The severity level to be assigned to findings that match the automation rule criteria.
Type: Integer
Required: No

 ** StatusId **   <a name="securityhub-Type-AutomationRulesFindingFieldsUpdateV2-StatusId"></a>
The status to be applied to findings that match automation rule criteria.
Type: Integer
Required: No

## See Also
<a name="API_AutomationRulesFindingFieldsUpdateV2_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AutomationRulesFindingFieldsUpdateV2)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AutomationRulesFindingFieldsUpdateV2)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AutomationRulesFindingFieldsUpdateV2)
