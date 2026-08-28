---
source_url: https://docs.aws.amazon.com/elemental-inference/latest/APIReference/API_CreateOutput.html
---

# CreateOutput
<a name="API_CreateOutput"></a>

Contains configuration information about one output in a feed. It is used in the AssociateFeed and the CreateFeed actions.

## Contents
<a name="API_CreateOutput_Contents"></a>

 ** name **   <a name="elementalinference-Type-CreateOutput-name"></a>
A name for the output.
Type: String
Pattern: `[a-zA-Z0-9]([a-zA-Z0-9-_]{0,126}[a-zA-Z0-9])?`
Required: Yes

 ** outputConfig **   <a name="elementalinference-Type-CreateOutput-outputConfig"></a>
A typed property for an output in a feed. It identifies the action for Elemental Inference to perform. It also provides a repository for the results of that action. For example, CroppingConfig output will contain the metadata for the crop feature.
Type: [OutputConfig](API_OutputConfig.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** status **   <a name="elementalinference-Type-CreateOutput-status"></a>
The status to assign to the output.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: Yes

 ** description **   <a name="elementalinference-Type-CreateOutput-description"></a>
A description for the output.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\w \-\.',@:;]*`
Required: No

## See Also
<a name="API_CreateOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elementalinference-2018-11-14/CreateOutput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elementalinference-2018-11-14/CreateOutput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elementalinference-2018-11-14/CreateOutput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Inference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-inference` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
