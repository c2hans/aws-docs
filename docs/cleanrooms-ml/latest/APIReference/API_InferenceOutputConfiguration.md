---
source_url: https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_InferenceOutputConfiguration.html
---

# InferenceOutputConfiguration
<a name="API_InferenceOutputConfiguration"></a>

Configuration information about how the inference output is stored.

## Contents
<a name="API_InferenceOutputConfiguration_Contents"></a>

 ** members **   <a name="API-Type-InferenceOutputConfiguration-members"></a>
Defines the members that can receive inference output.
Type: Array of [InferenceReceiverMember](API_InferenceReceiverMember.md) objects
Array Members: Fixed number of 1 item.
Required: Yes

 ** accept **   <a name="API-Type-InferenceOutputConfiguration-accept"></a>
The MIME type used to specify the output data.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `.*`
Required: No

## See Also
<a name="API_InferenceOutputConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanroomsml-2023-09-06/InferenceOutputConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanroomsml-2023-09-06/InferenceOutputConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanroomsml-2023-09-06/InferenceOutputConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms ML. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cleanrooms-ml` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
