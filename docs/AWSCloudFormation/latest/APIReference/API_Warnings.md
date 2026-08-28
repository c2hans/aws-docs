---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_Warnings.html
---

# Warnings
<a name="API_Warnings"></a>

Contains any warnings returned by the `GetTemplateSummary` API action.

## Contents
<a name="API_Warnings_Contents"></a>

 ** UnrecognizedResourceTypes.member.N **
A list of all of the unrecognized resource types. This is only returned if the `TemplateSummaryConfig` parameter has the `TreatUnrecognizedResourceTypesAsWarning` configuration set to `True`.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## See Also
<a name="API_Warnings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/Warnings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/Warnings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/Warnings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
