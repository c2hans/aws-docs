---
source_url: https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_SceneSummary.html
---

# SceneSummary
<a name="API_SceneSummary"></a>

An object that contains information about a scene.

## Contents
<a name="API_SceneSummary_Contents"></a>

 ** arn **   <a name="tm-Type-SceneSummary-arn"></a>
The ARN of the scene.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:((aws)|(aws-cn)|(aws-us-gov)):iottwinmaker:[a-z0-9-]+:[0-9]{12}:[\/a-zA-Z0-9_\-\.:]+`
Required: Yes

 ** contentLocation **   <a name="tm-Type-SceneSummary-contentLocation"></a>
The relative path that specifies the location of the content definition file.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[sS]3://[A-Za-z0-9._/-]+`
Required: Yes

 ** creationDateTime **   <a name="tm-Type-SceneSummary-creationDateTime"></a>
The date and time when the scene was created.
Type: Timestamp
Required: Yes

 ** sceneId **   <a name="tm-Type-SceneSummary-sceneId"></a>
The ID of the scene.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z_0-9][a-zA-Z_\-0-9]*[a-zA-Z0-9]+`
Required: Yes

 ** updateDateTime **   <a name="tm-Type-SceneSummary-updateDateTime"></a>
The date and time when the scene was last updated.
Type: Timestamp
Required: Yes

 ** description **   <a name="tm-Type-SceneSummary-description"></a>
The scene description.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `.*`
Required: No

## See Also
<a name="API_SceneSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iottwinmaker-2021-11-29/SceneSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iottwinmaker-2021-11-29/SceneSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iottwinmaker-2021-11-29/SceneSummary)
