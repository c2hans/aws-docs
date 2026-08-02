---
source_url: https://docs.aws.amazon.com/location/previous/APIReference/API_Step.html
---

# Step
<a name="API_Step"></a>

 Represents an element of a leg within a route. A step contains instructions for how to move to the next step in the leg.

## Contents
<a name="API_Step_Contents"></a>

 ** Distance **   <a name="location-Type-Step-Distance"></a>
The travel distance between the step's `StartPosition` and `EndPosition`.
Type: Double
Valid Range: Minimum value of 0.
Required: Yes

 ** DurationSeconds **   <a name="location-Type-Step-DurationSeconds"></a>
The estimated travel time, in seconds, from the step's `StartPosition` to the `EndPosition`. . The travel mode and departure time that you specify in the request determines the calculated time.
Type: Double
Valid Range: Minimum value of 0.
Required: Yes

 ** EndPosition **   <a name="location-Type-Step-EndPosition"></a>
The end position of a step. If the position the last step in the leg, this position is the same as the end position of the leg.
Type: Array of doubles
Array Members: Fixed number of 2 items.
Required: Yes

 ** StartPosition **   <a name="location-Type-Step-StartPosition"></a>
The starting position of a step. If the position is the first step in the leg, this position is the same as the start position of the leg.
Type: Array of doubles
Array Members: Fixed number of 2 items.
Required: Yes

 ** GeometryOffset **   <a name="location-Type-Step-GeometryOffset"></a>
Represents the start position, or index, in a sequence of steps within the leg's line string geometry. For example, the index of the first step in a leg geometry is `0`.
Included in the response for queries that set `IncludeLegGeometry` to `True`.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_Step_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/location-2020-11-19/Step)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/location-2020-11-19/Step)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/location-2020-11-19/Step)
