---
source_url: https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_IncrementalTrainingDataChannel.html
---

# IncrementalTrainingDataChannel
<a name="API_IncrementalTrainingDataChannel"></a>

Defines an incremental training data channel that references a previously trained model. Incremental training allows you to update an existing trained model with new data, building upon the knowledge from a base model rather than training from scratch. This can significantly reduce training time and computational costs while improving model performance with additional data.

## Contents
<a name="API_IncrementalTrainingDataChannel_Contents"></a>

 ** channelName **   <a name="API-Type-IncrementalTrainingDataChannel-channelName"></a>
The name of the incremental training data channel. This name is used to identify the channel during the training process and must be unique within the training job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9\.\-_]+`
Required: Yes

 ** trainedModelArn **   <a name="API-Type-IncrementalTrainingDataChannel-trainedModelArn"></a>
The Amazon Resource Name (ARN) of the base trained model to use for incremental training. This model serves as the starting point for the incremental training process.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:membership/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}/trained-model/[-a-zA-Z0-9_/.]+`
Required: Yes

 ** versionIdentifier **   <a name="API-Type-IncrementalTrainingDataChannel-versionIdentifier"></a>
The version identifier of the base trained model to use for incremental training. If not specified, the latest version of the trained model is used.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

## See Also
<a name="API_IncrementalTrainingDataChannel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanroomsml-2023-09-06/IncrementalTrainingDataChannel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanroomsml-2023-09-06/IncrementalTrainingDataChannel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanroomsml-2023-09-06/IncrementalTrainingDataChannel)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms ML. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cleanrooms-ml` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
