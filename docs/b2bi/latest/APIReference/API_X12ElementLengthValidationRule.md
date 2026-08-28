---
source_url: https://docs.aws.amazon.com/b2bi/latest/APIReference/API_X12ElementLengthValidationRule.html
---

# X12ElementLengthValidationRule
<a name="API_X12ElementLengthValidationRule"></a>

Defines a validation rule that specifies custom length constraints for a specific X12 element. This rule allows you to override the standard minimum and maximum length requirements for an element, enabling validation of trading partner-specific length requirements that may differ from the X12 specification. Both minimum and maximum length values must be specified.

## Contents
<a name="API_X12ElementLengthValidationRule_Contents"></a>

 ** elementId **   <a name="b2bi-Type-X12ElementLengthValidationRule-elementId"></a>
Specifies the four-digit element ID to which the length constraints will be applied. This identifies which X12 element will have its length requirements modified.
Type: String
Required: Yes

 ** maxLength **   <a name="b2bi-Type-X12ElementLengthValidationRule-maxLength"></a>
Specifies the maximum allowed length for the identified element. This value defines the upper limit for the element's content length.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000000.
Required: Yes

 ** minLength **   <a name="b2bi-Type-X12ElementLengthValidationRule-minLength"></a>
Specifies the minimum required length for the identified element. This value defines the lower limit for the element's content length.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000000.
Required: Yes

## See Also
<a name="API_X12ElementLengthValidationRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/b2bi-2022-06-23/X12ElementLengthValidationRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/b2bi-2022-06-23/X12ElementLengthValidationRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/b2bi-2022-06-23/X12ElementLengthValidationRule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS B2B Data Interchange. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query b2bi` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
