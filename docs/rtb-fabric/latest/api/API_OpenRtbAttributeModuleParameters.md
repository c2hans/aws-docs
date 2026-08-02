---
source_url: https://docs.aws.amazon.com/rtb-fabric/latest/api/API_OpenRtbAttributeModuleParameters.html
---

# OpenRtbAttributeModuleParameters
<a name="API_OpenRtbAttributeModuleParameters"></a>

Describes the parameters of an open RTB attribute module.

## Contents
<a name="API_OpenRtbAttributeModuleParameters_Contents"></a>

 ** action **   <a name="rtbfabric-Type-OpenRtbAttributeModuleParameters-action"></a>
Describes a bid action.
Type: [Action](API_Action.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** filterConfiguration **   <a name="rtbfabric-Type-OpenRtbAttributeModuleParameters-filterConfiguration"></a>
Describes the configuration of a filter.
Type: Array of [Filter](API_Filter.md) objects
Required: Yes

 ** filterType **   <a name="rtbfabric-Type-OpenRtbAttributeModuleParameters-filterType"></a>
The filter type.
Type: String
Valid Values: `INCLUDE | EXCLUDE`
Required: Yes

 ** holdbackPercentage **   <a name="rtbfabric-Type-OpenRtbAttributeModuleParameters-holdbackPercentage"></a>
The hold back percentage.
Type: Float
Valid Range: Minimum value of 0. Maximum value of 100.
Required: Yes

## See Also
<a name="API_OpenRtbAttributeModuleParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rtbfabric-2023-05-15/OpenRtbAttributeModuleParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rtbfabric-2023-05-15/OpenRtbAttributeModuleParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rtbfabric-2023-05-15/OpenRtbAttributeModuleParameters)
