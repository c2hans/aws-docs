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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
