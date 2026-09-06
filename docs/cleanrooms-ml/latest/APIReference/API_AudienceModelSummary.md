---
source_url: https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_AudienceModelSummary.html
---

# AudienceModelSummary
<a name="API_AudienceModelSummary"></a>

Information about the audience model.

## Contents
<a name="API_AudienceModelSummary_Contents"></a>

 ** audienceModelArn **   <a name="API-Type-AudienceModelSummary-audienceModelArn"></a>
The Amazon Resource Name (ARN) of the audience model.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:audience-model/[-a-zA-Z0-9_/.]+`
Required: Yes

 ** createTime **   <a name="API-Type-AudienceModelSummary-createTime"></a>
The time at which the audience model was created.
Type: Timestamp
Required: Yes

 ** name **   <a name="API-Type-AudienceModelSummary-name"></a>
The name of the audience model.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `(?!\s*$)[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t]*`
Required: Yes

 ** status **   <a name="API-Type-AudienceModelSummary-status"></a>
The status of the audience model.
Type: String
Valid Values: `CREATE_PENDING | CREATE_IN_PROGRESS | CREATE_FAILED | ACTIVE | DELETE_PENDING | DELETE_IN_PROGRESS | DELETE_FAILED`
Required: Yes

 ** trainingDatasetArn **   <a name="API-Type-AudienceModelSummary-trainingDatasetArn"></a>
The Amazon Resource Name (ARN) of the training dataset that was used for the audience model.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:training-dataset/[-a-zA-Z0-9_/.]+`
Required: Yes

 ** updateTime **   <a name="API-Type-AudienceModelSummary-updateTime"></a>
The most recent time at which the audience model was updated.
Type: Timestamp
Required: Yes

 ** description **   <a name="API-Type-AudienceModelSummary-description"></a>
The description of the audience model.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t\r\n]*`
Required: No

## See Also
<a name="API_AudienceModelSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanroomsml-2023-09-06/AudienceModelSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanroomsml-2023-09-06/AudienceModelSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanroomsml-2023-09-06/AudienceModelSummary)
