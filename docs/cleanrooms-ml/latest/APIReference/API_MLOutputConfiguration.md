---
source_url: https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_MLOutputConfiguration.html
---

# MLOutputConfiguration
<a name="API_MLOutputConfiguration"></a>

Configuration information about how the exported model artifacts are stored.

## Contents
<a name="API_MLOutputConfiguration_Contents"></a>

 ** roleArn **   <a name="API-Type-MLOutputConfiguration-roleArn"></a>
The Amazon Resource Name (ARN) of the service access role that is used to store the model artifacts.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z]*:iam::[0-9]{12}:role/.+`
Required: Yes

 ** destination **   <a name="API-Type-MLOutputConfiguration-destination"></a>
The Amazon S3 location where exported model artifacts are stored.
Type: [Destination](API_Destination.md) object
Required: No

## See Also
<a name="API_MLOutputConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanroomsml-2023-09-06/MLOutputConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanroomsml-2023-09-06/MLOutputConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanroomsml-2023-09-06/MLOutputConfiguration)
