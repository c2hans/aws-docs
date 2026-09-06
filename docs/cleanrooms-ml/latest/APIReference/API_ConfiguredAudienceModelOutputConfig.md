---
source_url: https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_ConfiguredAudienceModelOutputConfig.html
---

# ConfiguredAudienceModelOutputConfig
<a name="API_ConfiguredAudienceModelOutputConfig"></a>

Configuration information necessary for the configure audience model output.

## Contents
<a name="API_ConfiguredAudienceModelOutputConfig_Contents"></a>

 ** destination **   <a name="API-Type-ConfiguredAudienceModelOutputConfig-destination"></a>
Defines the Amazon S3 bucket where the configured audience is stored.
Type: [AudienceDestination](API_AudienceDestination.md) object
Required: Yes

 ** roleArn **   <a name="API-Type-ConfiguredAudienceModelOutputConfig-roleArn"></a>
The ARN of the IAM role that can write the Amazon S3 bucket.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z]*:iam::[0-9]{12}:role/.+`
Required: Yes

## See Also
<a name="API_ConfiguredAudienceModelOutputConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanroomsml-2023-09-06/ConfiguredAudienceModelOutputConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanroomsml-2023-09-06/ConfiguredAudienceModelOutputConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanroomsml-2023-09-06/ConfiguredAudienceModelOutputConfig)
