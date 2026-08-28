---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_WorkflowParameter.html
---

# WorkflowParameter
<a name="API_WorkflowParameter"></a>

Contains a key/value pair that sets the named workflow parameter.

## Contents
<a name="API_WorkflowParameter_Contents"></a>

 ** name **   <a name="imagebuilder-Type-WorkflowParameter-name"></a>
The name of the workflow parameter to set.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[^\x00]+`
Required: Yes

 ** value **   <a name="imagebuilder-Type-WorkflowParameter-value"></a>
Sets the value for the named workflow parameter.
Type: Array of strings
Length Constraints: Minimum length of 0.
Pattern: `[^\x00]*`
Required: Yes

## See Also
<a name="API_WorkflowParameter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/WorkflowParameter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/WorkflowParameter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/WorkflowParameter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for EC2 Image Builder. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query imagebuilder` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
