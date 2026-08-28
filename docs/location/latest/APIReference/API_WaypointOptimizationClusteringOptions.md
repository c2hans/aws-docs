---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointOptimizationClusteringOptions.html
---

# WaypointOptimizationClusteringOptions
<a name="API_WaypointOptimizationClusteringOptions"></a>

Options for WaypointOptimizationClustering.

## Contents
<a name="API_WaypointOptimizationClusteringOptions_Contents"></a>

 ** Algorithm **   <a name="location-Type-WaypointOptimizationClusteringOptions-Algorithm"></a>
The algorithm to be used. `DrivingDistance` assigns all the waypoints that are within driving distance of each other into a single cluster. `TopologySegment` assigns all the waypoints that are within the same topology segment into a single cluster. A Topology segment is a linear stretch of road between two junctions.
Type: String
Valid Values: `DrivingDistance | TopologySegment`
Required: Yes

 ** DrivingDistanceOptions **   <a name="location-Type-WaypointOptimizationClusteringOptions-DrivingDistanceOptions"></a>
Driving distance options to be used when the clustering algorithm is DrivingDistance.
Type: [WaypointOptimizationDrivingDistanceOptions](API_WaypointOptimizationDrivingDistanceOptions.md) object
Required: No

## See Also
<a name="API_WaypointOptimizationClusteringOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/WaypointOptimizationClusteringOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/WaypointOptimizationClusteringOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/WaypointOptimizationClusteringOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
