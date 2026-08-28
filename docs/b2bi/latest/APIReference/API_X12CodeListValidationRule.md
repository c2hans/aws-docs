---
source_url: https://docs.aws.amazon.com/b2bi/latest/APIReference/API_X12CodeListValidationRule.html
---

# X12CodeListValidationRule
<a name="API_X12CodeListValidationRule"></a>

Defines a validation rule that modifies the allowed code values for a specific X12 element. This rule allows you to add or remove valid codes from an element's standard code list, providing flexibility to accommodate trading partner-specific requirements or industry variations. You can specify codes to add to expand the allowed values beyond the X12 standard, or codes to remove to restrict the allowed values for stricter validation.

## Contents
<a name="API_X12CodeListValidationRule_Contents"></a>

 ** elementId **   <a name="b2bi-Type-X12CodeListValidationRule-elementId"></a>
Specifies the four-digit element ID to which the code list modifications apply. This identifies which X12 element will have its allowed code values modified.
Type: String
Required: Yes

 ** codesToAdd **   <a name="b2bi-Type-X12CodeListValidationRule-codesToAdd"></a>
Specifies a list of code values to add to the element's allowed values. These codes will be considered valid for the specified element in addition to the standard codes defined by the X12 specification.
Type: Array of strings
Required: No

 ** codesToRemove **   <a name="b2bi-Type-X12CodeListValidationRule-codesToRemove"></a>
Specifies a list of code values to remove from the element's allowed values. These codes will be considered invalid for the specified element, even if they are part of the standard codes defined by the X12 specification.
Type: Array of strings
Required: No

## See Also
<a name="API_X12CodeListValidationRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/b2bi-2022-06-23/X12CodeListValidationRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/b2bi-2022-06-23/X12CodeListValidationRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/b2bi-2022-06-23/X12CodeListValidationRule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS B2B Data Interchange. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query b2bi` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
