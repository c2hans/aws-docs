---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_TargetResource.html
---

# TargetResource
<a name="API_TargetResource"></a>

The resource the action will be taken on. This can include asset-based resources and computation model resources.

## Contents
<a name="API_TargetResource_Contents"></a>

 ** assetId **   <a name="iotsitewise-Type-TargetResource-assetId"></a>
The ID of the asset, in UUID format.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: No

 ** computationModelId **   <a name="iotsitewise-Type-TargetResource-computationModelId"></a>
The ID of the computation model.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: No

## See Also
<a name="API_TargetResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/TargetResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/TargetResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/TargetResource)
