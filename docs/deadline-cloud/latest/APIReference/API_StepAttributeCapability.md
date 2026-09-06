---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_StepAttributeCapability.html
---

# StepAttributeCapability
<a name="API_StepAttributeCapability"></a>

The list of step attributes.

## Contents
<a name="API_StepAttributeCapability_Contents"></a>

 ** name **   <a name="deadlinecloud-Type-StepAttributeCapability-name"></a>
The name of the step attribute.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `([a-zA-Z][a-zA-Z0-9]{0,63}:)?attr(\.[a-zA-Z][a-zA-Z0-9]{0,63})+`
Required: Yes

 ** allOf **   <a name="deadlinecloud-Type-StepAttributeCapability-allOf"></a>
Requires all of the step attribute values.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z_]([a-zA-Z0-9_\-]{0,99})`
Required: No

 ** anyOf **   <a name="deadlinecloud-Type-StepAttributeCapability-anyOf"></a>
Requires any of the step attributes in a given list.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z_]([a-zA-Z0-9_\-]{0,99})`
Required: No

## See Also
<a name="API_StepAttributeCapability_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/StepAttributeCapability)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/StepAttributeCapability)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/StepAttributeCapability)
