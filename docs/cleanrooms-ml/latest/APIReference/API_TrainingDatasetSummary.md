---
source_url: https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_TrainingDatasetSummary.html
---

# TrainingDatasetSummary
<a name="API_TrainingDatasetSummary"></a>

Provides information about the training dataset.

## Contents
<a name="API_TrainingDatasetSummary_Contents"></a>

 ** createTime **   <a name="API-Type-TrainingDatasetSummary-createTime"></a>
The time at which the training dataset was created.
Type: Timestamp
Required: Yes

 ** name **   <a name="API-Type-TrainingDatasetSummary-name"></a>
The name of the training dataset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `(?!\s*$)[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t]*`
Required: Yes

 ** status **   <a name="API-Type-TrainingDatasetSummary-status"></a>
The status of the training dataset.
Type: String
Valid Values: `ACTIVE`
Required: Yes

 ** trainingDatasetArn **   <a name="API-Type-TrainingDatasetSummary-trainingDatasetArn"></a>
The Amazon Resource Name (ARN) of the training dataset.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:training-dataset/[-a-zA-Z0-9_/.]+`
Required: Yes

 ** updateTime **   <a name="API-Type-TrainingDatasetSummary-updateTime"></a>
The most recent time at which the training dataset was updated.
Type: Timestamp
Required: Yes

 ** description **   <a name="API-Type-TrainingDatasetSummary-description"></a>
The description of the training dataset.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t\r\n]*`
Required: No

## See Also
<a name="API_TrainingDatasetSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanroomsml-2023-09-06/TrainingDatasetSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanroomsml-2023-09-06/TrainingDatasetSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanroomsml-2023-09-06/TrainingDatasetSummary)
