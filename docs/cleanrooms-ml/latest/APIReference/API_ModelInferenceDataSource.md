---
source_url: https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_ModelInferenceDataSource.html
---

# ModelInferenceDataSource
<a name="API_ModelInferenceDataSource"></a>

Defines information about the data source used for model inference.

## Contents
<a name="API_ModelInferenceDataSource_Contents"></a>

 ** mlInputChannelArn **   <a name="API-Type-ModelInferenceDataSource-mlInputChannelArn"></a>
The Amazon Resource Name (ARN) of the ML input channel for this model inference data source.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:membership/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}/ml-input-channel/[-a-zA-Z0-9_/.]+`
Required: Yes

## See Also
<a name="API_ModelInferenceDataSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanroomsml-2023-09-06/ModelInferenceDataSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanroomsml-2023-09-06/ModelInferenceDataSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanroomsml-2023-09-06/ModelInferenceDataSource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms ML. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cleanrooms-ml` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
