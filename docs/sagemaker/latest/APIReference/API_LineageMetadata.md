---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_LineageMetadata.html
---

# LineageMetadata
<a name="API_LineageMetadata"></a>

 The metadata that tracks relationships between ML artifacts, actions, and contexts.

## Contents
<a name="API_LineageMetadata_Contents"></a>

 ** ActionArns **   <a name="sagemaker-Type-LineageMetadata-ActionArns"></a>
 The Amazon Resource Name (ARN) of the lineage action.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 5 items.
Key Length Constraints: Minimum length of 0. Maximum length of 2048.
Value Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** ArtifactArns **   <a name="sagemaker-Type-LineageMetadata-ArtifactArns"></a>
 The Amazon Resource Name (ARN) of the lineage artifact.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 5 items.
Key Length Constraints: Minimum length of 0. Maximum length of 2048.
Value Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** Associations **   <a name="sagemaker-Type-LineageMetadata-Associations"></a>
 The lineage associations.
Type: Array of [AssociationInfo](API_AssociationInfo.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** ContextArns **   <a name="sagemaker-Type-LineageMetadata-ContextArns"></a>
 The Amazon Resource Name (ARN) of the lineage context.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 5 items.
Key Length Constraints: Minimum length of 0. Maximum length of 2048.
Value Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

## See Also
<a name="API_LineageMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/LineageMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/LineageMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/LineageMetadata)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
