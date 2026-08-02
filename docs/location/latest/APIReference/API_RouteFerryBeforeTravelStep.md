---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_RouteFerryBeforeTravelStep.html
---

# RouteFerryBeforeTravelStep
<a name="API_RouteFerryBeforeTravelStep"></a>

Steps of a leg that must be performed before the travel portion of the leg.

## Contents
<a name="API_RouteFerryBeforeTravelStep_Contents"></a>

 ** Duration **   <a name="location-Type-RouteFerryBeforeTravelStep-Duration"></a>
Duration of the step.
 **Unit**: `seconds`
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: Yes

 ** Type **   <a name="location-Type-RouteFerryBeforeTravelStep-Type"></a>
Type of the step.
Type: String
Valid Values: `Board`
Required: Yes

 ** Instruction **   <a name="location-Type-RouteFerryBeforeTravelStep-Instruction"></a>
Brief description of the step in the requested language.
Only available when the TravelStepType is Default.
Type: String
Required: No

## See Also
<a name="API_RouteFerryBeforeTravelStep_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/RouteFerryBeforeTravelStep)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/RouteFerryBeforeTravelStep)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/RouteFerryBeforeTravelStep)
