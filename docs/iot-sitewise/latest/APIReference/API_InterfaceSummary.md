---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_InterfaceSummary.html
---

# InterfaceSummary
<a name="API_InterfaceSummary"></a>

Contains summary information about an interface that a property belongs to.

## Contents
<a name="API_InterfaceSummary_Contents"></a>

 ** interfaceAssetModelId **   <a name="iotsitewise-Type-InterfaceSummary-interfaceAssetModelId"></a>
The ID of the interface asset model that contains this property.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: Yes

 ** interfaceAssetModelPropertyId **   <a name="iotsitewise-Type-InterfaceSummary-interfaceAssetModelPropertyId"></a>
The ID of the property in the interface asset model that corresponds to this property.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: Yes

## See Also
<a name="API_InterfaceSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/InterfaceSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/InterfaceSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/InterfaceSummary)
