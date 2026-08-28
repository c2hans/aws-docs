---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_Circle.html
---

# Circle
<a name="API_Circle"></a>

Geometry defined as a circle. The circle defines the routing boundary area. Any waypoints outside the circle will result in a route matrix entry error.

You can specify a `Circle` directly in the request, or it will be auto-derived when `AutoCircle` is used. When `AutoCircle` is set in the request, the response routing boundary will return `Circle` derived from the `AutoCircle` settings.

## Contents
<a name="API_Circle_Contents"></a>

 ** Center **   <a name="location-Type-Circle-Center"></a>
Center of the Circle in World Geodetic System (WGS 84) format: [longitude, latitude].
Example: `[-123.1174, 49.2847]` represents the position with longitude `-123.1174` and latitude `49.2847`.
Type: Array of doubles
Array Members: Fixed number of 2 items.
Required: Yes

 ** Radius **   <a name="location-Type-Circle-Radius"></a>
Radius of the Circle.
 **Unit**: `meters`
Valid Range: Minimum value of 0. Maximum value of 200000.
Type: Double
Required: Yes

## See Also
<a name="API_Circle_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/Circle)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/Circle)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/Circle)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
