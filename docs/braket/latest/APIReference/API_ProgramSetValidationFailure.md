---
source_url: https://docs.aws.amazon.com/braket/latest/APIReference/API_ProgramSetValidationFailure.html
---

# ProgramSetValidationFailure
<a name="API_ProgramSetValidationFailure"></a>

Contains information about validation failures that occurred during the processing of a program set in a quantum task.

## Contents
<a name="API_ProgramSetValidationFailure_Contents"></a>

 ** programIndex **   <a name="braket-Type-ProgramSetValidationFailure-programIndex"></a>
The index of the program within the program set that failed validation.
Type: Long
Required: Yes

 ** errors **   <a name="braket-Type-ProgramSetValidationFailure-errors"></a>
A list of error messages describing the validation failures that occurred.
Type: Array of strings
Required: No

 ** inputsIndex **   <a name="braket-Type-ProgramSetValidationFailure-inputsIndex"></a>
The index of the input within the program set that failed validation.
Type: Long
Required: No

## See Also
<a name="API_ProgramSetValidationFailure_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/braket-2019-09-01/ProgramSetValidationFailure)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/braket-2019-09-01/ProgramSetValidationFailure)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/braket-2019-09-01/ProgramSetValidationFailure)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Braket. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query braket` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
