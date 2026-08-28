---
source_url: https://docs.aws.amazon.com/comprehend/latest/APIReference/API_EntityRecognizerMetadata.html
---

# EntityRecognizerMetadata
<a name="API_EntityRecognizerMetadata"></a>

Detailed information about an entity recognizer.

## Contents
<a name="API_EntityRecognizerMetadata_Contents"></a>

 ** EntityTypes **   <a name="comprehend-Type-EntityRecognizerMetadata-EntityTypes"></a>
Entity types from the metadata of an entity recognizer.
Type: Array of [EntityRecognizerMetadataEntityTypesListItem](API_EntityRecognizerMetadataEntityTypesListItem.md) objects
Required: No

 ** EvaluationMetrics **   <a name="comprehend-Type-EntityRecognizerMetadata-EvaluationMetrics"></a>
Detailed information about the accuracy of an entity recognizer.
Type: [EntityRecognizerEvaluationMetrics](API_EntityRecognizerEvaluationMetrics.md) object
Required: No

 ** NumberOfTestDocuments **   <a name="comprehend-Type-EntityRecognizerMetadata-NumberOfTestDocuments"></a>
 The number of documents in the input data that were used to test the entity recognizer. Typically this is 10 to 20 percent of the input documents.
Type: Integer
Required: No

 ** NumberOfTrainedDocuments **   <a name="comprehend-Type-EntityRecognizerMetadata-NumberOfTrainedDocuments"></a>
 The number of documents in the input data that were used to train the entity recognizer. Typically this is 80 to 90 percent of the input documents.
Type: Integer
Required: No

## See Also
<a name="API_EntityRecognizerMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehend-2017-11-27/EntityRecognizerMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehend-2017-11-27/EntityRecognizerMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehend-2017-11-27/EntityRecognizerMetadata)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Comprehend. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query comprehend` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
