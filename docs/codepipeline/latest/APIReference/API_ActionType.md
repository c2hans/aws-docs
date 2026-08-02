---
source_url: https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_ActionType.html
---

# ActionType
<a name="API_ActionType"></a>

Returns information about the details of an action type.

## Contents
<a name="API_ActionType_Contents"></a>

 ** id **   <a name="CodePipeline-Type-ActionType-id"></a>
Represents information about an action type.
Type: [ActionTypeId](API_ActionTypeId.md) object
Required: Yes

 ** inputArtifactDetails **   <a name="CodePipeline-Type-ActionType-inputArtifactDetails"></a>
The details of the input artifact for the action, such as its commit ID.
Type: [ArtifactDetails](API_ArtifactDetails.md) object
Required: Yes

 ** outputArtifactDetails **   <a name="CodePipeline-Type-ActionType-outputArtifactDetails"></a>
The details of the output artifact of the action, such as its commit ID.
Type: [ArtifactDetails](API_ArtifactDetails.md) object
Required: Yes

 ** actionConfigurationProperties **   <a name="CodePipeline-Type-ActionType-actionConfigurationProperties"></a>
The configuration properties for the action type.
Type: Array of [ActionConfigurationProperty](API_ActionConfigurationProperty.md) objects
Array Members: Maximum number of 10 items.
Required: No

 ** settings **   <a name="CodePipeline-Type-ActionType-settings"></a>
The settings for the action type.
Type: [ActionTypeSettings](API_ActionTypeSettings.md) object
Required: No

## See Also
<a name="API_ActionType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/ActionType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/ActionType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/ActionType)
