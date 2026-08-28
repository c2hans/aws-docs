---
source_url: https://docs.aws.amazon.com/b2bi/latest/APIReference/API_X12ValidationRule.html
---

# X12ValidationRule
<a name="API_X12ValidationRule"></a>

Represents a single validation rule that can be applied during X12 EDI processing. This is a union type that can contain one of several specific validation rule types: code list validation rules for modifying allowed element codes, element length validation rules for enforcing custom length constraints, or element requirement validation rules for changing mandatory/optional status. Each validation rule targets specific aspects of EDI document validation to ensure compliance with trading partner requirements and business rules.

## Contents
<a name="API_X12ValidationRule_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** codeListValidationRule **   <a name="b2bi-Type-X12ValidationRule-codeListValidationRule"></a>
Specifies a code list validation rule that modifies the allowed code values for a specific X12 element. This rule enables you to customize which codes are considered valid for an element, allowing for trading partner-specific code requirements.
Type: [X12CodeListValidationRule](API_X12CodeListValidationRule.md) object
Required: No

 ** elementLengthValidationRule **   <a name="b2bi-Type-X12ValidationRule-elementLengthValidationRule"></a>
Specifies an element length validation rule that defines custom length constraints for a specific X12 element. This rule allows you to enforce minimum and maximum length requirements that may differ from the standard X12 specification.
Type: [X12ElementLengthValidationRule](API_X12ElementLengthValidationRule.md) object
Required: No

 ** elementRequirementValidationRule **   <a name="b2bi-Type-X12ValidationRule-elementRequirementValidationRule"></a>
Specifies an element requirement validation rule that modifies whether a specific X12 element is required or optional within a segment. This rule provides flexibility to accommodate different trading partner requirements for element presence.
Type: [X12ElementRequirementValidationRule](API_X12ElementRequirementValidationRule.md) object
Required: No

## See Also
<a name="API_X12ValidationRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/b2bi-2022-06-23/X12ValidationRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/b2bi-2022-06-23/X12ValidationRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/b2bi-2022-06-23/X12ValidationRule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS B2B Data Interchange. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query b2bi` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
