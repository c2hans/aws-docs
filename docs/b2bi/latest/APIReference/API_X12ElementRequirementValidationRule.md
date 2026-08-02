---
source_url: https://docs.aws.amazon.com/b2bi/latest/APIReference/API_X12ElementRequirementValidationRule.html
---

# X12ElementRequirementValidationRule
<a name="API_X12ElementRequirementValidationRule"></a>

Defines a validation rule that modifies the requirement status of a specific X12 element within a segment. This rule allows you to make optional elements mandatory or mandatory elements optional, providing flexibility to accommodate different trading partner requirements and business rules. The rule targets a specific element position within a segment and sets its requirement status to either OPTIONAL or MANDATORY.

## Contents
<a name="API_X12ElementRequirementValidationRule_Contents"></a>

 ** elementPosition **   <a name="b2bi-Type-X12ElementRequirementValidationRule-elementPosition"></a>
Specifies the position of the element within an X12 segment for which the requirement status will be modified. The format follows the pattern of segment identifier followed by element position (e.g., "ST-01" for the first element of the ST segment).
Type: String
Required: Yes

 ** requirement **   <a name="b2bi-Type-X12ElementRequirementValidationRule-requirement"></a>
Specifies the requirement status for the element at the specified position. Valid values are OPTIONAL (the element may be omitted) or MANDATORY (the element must be present).
Type: String
Valid Values: `OPTIONAL | MANDATORY`
Required: Yes

## See Also
<a name="API_X12ElementRequirementValidationRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/b2bi-2022-06-23/X12ElementRequirementValidationRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/b2bi-2022-06-23/X12ElementRequirementValidationRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/b2bi-2022-06-23/X12ElementRequirementValidationRule)
