---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_Annotation.html
---

# Annotation
<a name="API_Annotation"></a>

The `Annotation` data type.

A `GetHookResult` call returns detailed information and remediation guidance from Control Tower, Guard, Lambda, or custom Hooks for a Hook invocation result.

## Contents
<a name="API_Annotation_Contents"></a>

 ** AnnotationName **
An identifier for the evaluation logic that was used when invoking the Hook. For Control Tower, this is the control ID. For Guard, this is the rule ID. For Lambda and custom Hooks, this is a user-defined identifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** RemediationLink **
A URL that you can access for additional remediation guidance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 5120.
Required: No

 ** RemediationMessage **
Suggests what to change if your Hook returns a `FAILED` status. For example, "Block public access to the bucket".
Type: String
Length Constraints: Minimum length of 1. Maximum length of 16384.
Required: No

 ** SeverityLevel **
The relative risk associated with any violations of this type.
Type: String
Valid Values: `INFORMATIONAL | LOW | MEDIUM | HIGH | CRITICAL`
Required: No

 ** Status **
The status of the Hook invocation from the downstream service.
Type: String
Valid Values: `PASSED | FAILED | SKIPPED`
Required: No

 ** StatusMessage **
The explanation for the specific status assigned to this Hook invocation. For example, "Bucket does not block public access".
Type: String
Length Constraints: Minimum length of 1. Maximum length of 16384.
Required: No

## See Also
<a name="API_Annotation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/Annotation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/Annotation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/Annotation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
