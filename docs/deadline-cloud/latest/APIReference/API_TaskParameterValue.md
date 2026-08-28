---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_TaskParameterValue.html
---

# TaskParameterValue
<a name="API_TaskParameterValue"></a>

The data types for the task parameters.

## Contents
<a name="API_TaskParameterValue_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** chunkInt **   <a name="deadlinecloud-Type-TaskParameterValue-chunkInt"></a>
A range (for example 1-10) or selection of specific (for example 1,3,7,8,10) integers represented as a string.
Type: String
Required: No

 ** float **   <a name="deadlinecloud-Type-TaskParameterValue-float"></a>
A double precision IEEE-754 floating point number represented as a string.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 26.
Pattern: `[-]?(0|[1-9][0-9]*)([.][0-9]+)?([eE][+-]?[0-9]+)?`
Required: No

 ** int **   <a name="deadlinecloud-Type-TaskParameterValue-int"></a>
A signed integer represented as a string.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `[-]?(0|[1-9][0-9]*)`
Required: No

 ** path **   <a name="deadlinecloud-Type-TaskParameterValue-path"></a>
A file system path represented as a string.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** string **   <a name="deadlinecloud-Type-TaskParameterValue-string"></a>
A UTF-8 string.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

## See Also
<a name="API_TaskParameterValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/TaskParameterValue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/TaskParameterValue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/TaskParameterValue)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
