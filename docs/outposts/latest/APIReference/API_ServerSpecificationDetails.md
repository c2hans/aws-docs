---
source_url: https://docs.aws.amazon.com/outposts/latest/APIReference/API_ServerSpecificationDetails.html
---

# ServerSpecificationDetails
<a name="API_ServerSpecificationDetails"></a>

The physical specification details for a server in a quote option.

## Contents
<a name="API_ServerSpecificationDetails_Contents"></a>

 ** EC2Capacities **   <a name="outposts-Type-ServerSpecificationDetails-EC2Capacities"></a>
The Amazon EC2 capacities for the server.
Type: Array of [EC2Capacity](API_EC2Capacity.md) objects
Required: No

 ** RackUnitHeight **   <a name="outposts-Type-ServerSpecificationDetails-RackUnitHeight"></a>
The rack unit height of the server.
+  `HEIGHT_2U` - 2 rack units.
+  `HEIGHT_1U` - 1 rack unit.
Type: String
Valid Values: `HEIGHT_42U | HEIGHT_2U | HEIGHT_1U`
Required: No

 ** ServerDepthInches **   <a name="outposts-Type-ServerSpecificationDetails-ServerDepthInches"></a>
The depth of the server in inches.
Type: Float
Required: No

 ** ServerHeightInches **   <a name="outposts-Type-ServerSpecificationDetails-ServerHeightInches"></a>
The height of the server in inches.
Type: Float
Required: No

 ** ServerPowerDrawKva **   <a name="outposts-Type-ServerSpecificationDetails-ServerPowerDrawKva"></a>
The maximum power draw of the server in kVA.
Type: Float
Required: No

 ** ServerWeightLbs **   <a name="outposts-Type-ServerSpecificationDetails-ServerWeightLbs"></a>
The weight of the server in pounds.
Type: Float
Required: No

 ** ServerWidthInches **   <a name="outposts-Type-ServerSpecificationDetails-ServerWidthInches"></a>
The width of the server in inches.
Type: Float
Required: No

## See Also
<a name="API_ServerSpecificationDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/outposts-2019-12-03/ServerSpecificationDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/outposts-2019-12-03/ServerSpecificationDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/outposts-2019-12-03/ServerSpecificationDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Outposts. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query outposts` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
