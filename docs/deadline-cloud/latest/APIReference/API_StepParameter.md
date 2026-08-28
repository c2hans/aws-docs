---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_StepParameter.html
---

# StepParameter
<a name="API_StepParameter"></a>

The details of a step parameter.

## Contents
<a name="API_StepParameter_Contents"></a>

 ** name **   <a name="deadlinecloud-Type-StepParameter-name"></a>
The name of the parameter.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** type **   <a name="deadlinecloud-Type-StepParameter-type"></a>
The data type of the parameter.
Type: String
Valid Values: `INT | FLOAT | STRING | PATH | CHUNK_INT`
Required: Yes

 ** chunks **   <a name="deadlinecloud-Type-StepParameter-chunks"></a>
The configuration for task chunking.
Type: [StepParameterChunks](API_StepParameterChunks.md) object
Required: No

## See Also
<a name="API_StepParameter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/StepParameter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/StepParameter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/StepParameter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
