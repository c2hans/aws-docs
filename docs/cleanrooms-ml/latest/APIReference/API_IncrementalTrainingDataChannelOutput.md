---
source_url: https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_IncrementalTrainingDataChannelOutput.html
---

# IncrementalTrainingDataChannelOutput
<a name="API_IncrementalTrainingDataChannelOutput"></a>

Contains information about an incremental training data channel that was used to create a trained model. This structure provides details about the base model and channel configuration used during incremental training.

## Contents
<a name="API_IncrementalTrainingDataChannelOutput_Contents"></a>

 ** channelName **   <a name="API-Type-IncrementalTrainingDataChannelOutput-channelName"></a>
The name of the incremental training data channel that was used.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9\.\-_]+`
Required: Yes

 ** modelName **   <a name="API-Type-IncrementalTrainingDataChannelOutput-modelName"></a>
The name of the base trained model that was used for incremental training.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `(?!\s*$)[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t]*`
Required: Yes

 ** versionIdentifier **   <a name="API-Type-IncrementalTrainingDataChannelOutput-versionIdentifier"></a>
The version identifier of the trained model that was used for incremental training.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

## See Also
<a name="API_IncrementalTrainingDataChannelOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanroomsml-2023-09-06/IncrementalTrainingDataChannelOutput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanroomsml-2023-09-06/IncrementalTrainingDataChannelOutput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanroomsml-2023-09-06/IncrementalTrainingDataChannelOutput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms ML. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cleanrooms-ml` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
