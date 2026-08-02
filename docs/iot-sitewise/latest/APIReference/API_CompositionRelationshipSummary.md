---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CompositionRelationshipSummary.html
---

# CompositionRelationshipSummary
<a name="API_CompositionRelationshipSummary"></a>

Contains a summary of the components of the composite model.

## Contents
<a name="API_CompositionRelationshipSummary_Contents"></a>

 ** assetModelCompositeModelId **   <a name="iotsitewise-Type-CompositionRelationshipSummary-assetModelCompositeModelId"></a>
The ID of a composite model on this asset model.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: Yes

 ** assetModelCompositeModelType **   <a name="iotsitewise-Type-CompositionRelationshipSummary-assetModelCompositeModelType"></a>
The composite model type. Valid values are `AWS/ALARM`, `CUSTOM`, or ` AWS/L4E_ANOMALY`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: Yes

 ** assetModelId **   <a name="iotsitewise-Type-CompositionRelationshipSummary-assetModelId"></a>
The ID of the asset model, in UUID format.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: Yes

## See Also
<a name="API_CompositionRelationshipSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/CompositionRelationshipSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/CompositionRelationshipSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/CompositionRelationshipSummary)
