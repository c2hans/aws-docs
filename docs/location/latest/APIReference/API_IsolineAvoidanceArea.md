---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_IsolineAvoidanceArea.html
---

# IsolineAvoidanceArea
<a name="API_IsolineAvoidanceArea"></a>

Defines an area to avoid when calculating routes. Consists of a primary geometry to avoid, with the ability to specify exception areas within that geometry where travel is permitted.

## Contents
<a name="API_IsolineAvoidanceArea_Contents"></a>

 ** Geometry **   <a name="location-Type-IsolineAvoidanceArea-Geometry"></a>
The primary area to avoid, specified using a bounding box, corridor, polygon, or polyline corridor.
Type: [IsolineAvoidanceAreaGeometry](API_IsolineAvoidanceAreaGeometry.md) object
Required: Yes

 ** Except **   <a name="location-Type-IsolineAvoidanceArea-Except"></a>
Areas within the primary avoidance geometry where travel is allowed. For example, you might want to avoid a neighborhood but allow travel on a major road that passes through it.
Type: Array of [IsolineAvoidanceAreaGeometry](API_IsolineAvoidanceAreaGeometry.md) objects
Required: No

## See Also
<a name="API_IsolineAvoidanceArea_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/IsolineAvoidanceArea)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/IsolineAvoidanceArea)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/IsolineAvoidanceArea)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
