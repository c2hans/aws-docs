---
source_url: https://docs.aws.amazon.com/fis/latest/APIReference/API_ExperimentActionState.html
---

# ExperimentActionState
<a name="API_ExperimentActionState"></a>

Describes the state of an action.

## Contents
<a name="API_ExperimentActionState_Contents"></a>

 ** reason **   <a name="fis-Type-ExperimentActionState-reason"></a>
The reason for the state.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `[\s\S]+`
Required: No

 ** status **   <a name="fis-Type-ExperimentActionState-status"></a>
The state of the action.
Type: String
Valid Values: `pending | initiating | running | completed | cancelled | stopping | stopped | failed | skipped`
Required: No

## See Also
<a name="API_ExperimentActionState_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fis-2020-12-01/ExperimentActionState)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fis-2020-12-01/ExperimentActionState)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fis-2020-12-01/ExperimentActionState)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Fault Injection Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fis` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
