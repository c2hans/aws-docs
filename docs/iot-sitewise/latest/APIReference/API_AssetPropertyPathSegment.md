---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_AssetPropertyPathSegment.html
---

# AssetPropertyPathSegment
<a name="API_AssetPropertyPathSegment"></a>

Represents one level between a property and the root of the asset.

## Contents
<a name="API_AssetPropertyPathSegment_Contents"></a>

 ** id **   <a name="iotsitewise-Type-AssetPropertyPathSegment-id"></a>
The ID of the path segment.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: No

 ** name **   <a name="iotsitewise-Type-AssetPropertyPathSegment-name"></a>
The name of the path segment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: No

## See Also
<a name="API_AssetPropertyPathSegment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/AssetPropertyPathSegment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/AssetPropertyPathSegment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/AssetPropertyPathSegment)
