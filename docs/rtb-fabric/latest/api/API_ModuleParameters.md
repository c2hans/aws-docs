---
source_url: https://docs.aws.amazon.com/rtb-fabric/latest/api/API_ModuleParameters.html
---

# ModuleParameters
<a name="API_ModuleParameters"></a>

Describes the parameters of a module.

## Contents
<a name="API_ModuleParameters_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** noBid **   <a name="rtbfabric-Type-ModuleParameters-noBid"></a>
Describes the parameters of a no bid module.
Type: [NoBidModuleParameters](API_NoBidModuleParameters.md) object
Required: No

 ** openRtbAttribute **   <a name="rtbfabric-Type-ModuleParameters-openRtbAttribute"></a>
Describes the parameters of an open RTB attribute module.
Type: [OpenRtbAttributeModuleParameters](API_OpenRtbAttributeModuleParameters.md) object
Required: No

 ** rateLimiter **   <a name="rtbfabric-Type-ModuleParameters-rateLimiter"></a>
Describes the parameters of a rate limit.
Type: [RateLimiterModuleParameters](API_RateLimiterModuleParameters.md) object
Required: No

## See Also
<a name="API_ModuleParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rtbfabric-2023-05-15/ModuleParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rtbfabric-2023-05-15/ModuleParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rtbfabric-2023-05-15/ModuleParameters)
