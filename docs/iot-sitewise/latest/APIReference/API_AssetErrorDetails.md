---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_AssetErrorDetails.html
---

# AssetErrorDetails
<a name="API_AssetErrorDetails"></a>

Contains error details for the requested associate project asset action.

## Contents
<a name="API_AssetErrorDetails_Contents"></a>

 ** assetId **   <a name="iotsitewise-Type-AssetErrorDetails-assetId"></a>
The ID of the asset, in UUID format.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: Yes

 ** code **   <a name="iotsitewise-Type-AssetErrorDetails-code"></a>
The error code.
Type: String
Valid Values: `INTERNAL_FAILURE`
Required: Yes

 ** message **   <a name="iotsitewise-Type-AssetErrorDetails-message"></a>
The error message.
Type: String
Required: Yes

## See Also
<a name="API_AssetErrorDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/AssetErrorDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/AssetErrorDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/AssetErrorDetails)
