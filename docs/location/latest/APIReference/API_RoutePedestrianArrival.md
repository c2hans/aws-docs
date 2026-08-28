---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_RoutePedestrianArrival.html
---

# RoutePedestrianArrival
<a name="API_RoutePedestrianArrival"></a>

Details corresponding to the arrival for a leg.

Time format:`YYYY-MM-DDThh:mm:ss.sssZ | YYYY-MM-DDThh:mm:ss.sss+hh:mm`

Examples:

 `2020-04-22T17:57:24Z`

 `2020-04-22T17:57:24+02:00`

## Contents
<a name="API_RoutePedestrianArrival_Contents"></a>

 ** Place **   <a name="location-Type-RoutePedestrianArrival-Place"></a>
Place details corresponding to the arrival.
Type: [RoutePedestrianPlace](API_RoutePedestrianPlace.md) object
Required: Yes

 ** Time **   <a name="location-Type-RoutePedestrianArrival-Time"></a>
The arrival time.
Type: String
Pattern: `([1-2][0-9]{3})-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9]|60)(\.[0-9]{0,9})?(Z|[+-]([01][0-9]|2[0-3]):[0-5][0-9])`
Required: No

## See Also
<a name="API_RoutePedestrianArrival_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/RoutePedestrianArrival)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/RoutePedestrianArrival)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/RoutePedestrianArrival)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
