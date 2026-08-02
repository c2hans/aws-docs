---
source_url: https://docs.aws.amazon.com/outposts/latest/APIReference/API_RackSpecificationDetails.html
---

# RackSpecificationDetails
<a name="API_RackSpecificationDetails"></a>

The physical specification details for a rack in a quote option.

## Contents
<a name="API_RackSpecificationDetails_Contents"></a>

 ** EC2Capacities **   <a name="outposts-Type-RackSpecificationDetails-EC2Capacities"></a>
The Amazon EC2 capacities for the rack.
Type: Array of [EC2Capacity](API_EC2Capacity.md) objects
Required: No

 ** RackDepthInches **   <a name="outposts-Type-RackSpecificationDetails-RackDepthInches"></a>
The depth of the rack in inches.
Type: Float
Required: No

 ** RackHeightInches **   <a name="outposts-Type-RackSpecificationDetails-RackHeightInches"></a>
The height of the rack in inches.
Type: Float
Required: No

 ** RackId **   <a name="outposts-Type-RackSpecificationDetails-RackId"></a>
The ID of the rack.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 20.
Pattern: `^[\S \n]+$`
Required: No

 ** RackPowerDrawKva **   <a name="outposts-Type-RackSpecificationDetails-RackPowerDrawKva"></a>
The maximum power draw of the rack in kVA.
Type: Float
Required: No

 ** RackUnitHeight **   <a name="outposts-Type-RackSpecificationDetails-RackUnitHeight"></a>
The rack unit height.
+  `HEIGHT_42U` - 42 rack units.
+  `HEIGHT_2U` - 2 rack units.
+  `HEIGHT_1U` - 1 rack unit.
Type: String
Valid Values: `HEIGHT_42U | HEIGHT_2U | HEIGHT_1U`
Required: No

 ** RackUse **   <a name="outposts-Type-RackSpecificationDetails-RackUse"></a>
The use of the rack. Valid values are `COMPUTE` and `NETWORKING`.
Type: String
Valid Values: `NETWORKING | COMPUTE`
Required: No

 ** RackWeightLbs **   <a name="outposts-Type-RackSpecificationDetails-RackWeightLbs"></a>
The weight of the rack in pounds.
Type: Float
Required: No

 ** RackWidthInches **   <a name="outposts-Type-RackSpecificationDetails-RackWidthInches"></a>
The width of the rack in inches.
Type: Float
Required: No

## See Also
<a name="API_RackSpecificationDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/outposts-2019-12-03/RackSpecificationDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/outposts-2019-12-03/RackSpecificationDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/outposts-2019-12-03/RackSpecificationDetails)
