---
source_url: https://docs.aws.amazon.com/transfer/latest/APIReference/API_DeleteStepDetails.html
---

# DeleteStepDetails
<a name="API_DeleteStepDetails"></a>

The name of the step, used to identify the delete step.

## Contents
<a name="API_DeleteStepDetails_Contents"></a>

 ** Name **   <a name="TransferFamily-Type-DeleteStepDetails-Name"></a>
The name of the step, used as an identifier.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 30.
Pattern: `[\w-]*`
Required: No

 ** SourceFileLocation **   <a name="TransferFamily-Type-DeleteStepDetails-SourceFileLocation"></a>
Specifies which file to use as input to the workflow step: either the output from the previous step, or the originally uploaded file for the workflow.
+ To use the previous file as the input, enter `${previous.file}`. In this case, this workflow step uses the output file from the previous workflow step as input. This is the default value.
+ To use the originally uploaded file location as input for this step, enter `${original.file}`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `\$\{(\w+.)+\w+\}`
Required: No

## See Also
<a name="API_DeleteStepDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transfer-2018-11-05/DeleteStepDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transfer-2018-11-05/DeleteStepDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transfer-2018-11-05/DeleteStepDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Transfer Family. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query transfer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
