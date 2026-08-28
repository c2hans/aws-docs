---
source_url: https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_OutlierDetection.html
---

# OutlierDetection
<a name="API_OutlierDetection"></a>

An object that represents the outlier detection for a virtual node's listener.

## Contents
<a name="API_OutlierDetection_Contents"></a>

 ** baseEjectionDuration **   <a name="appmesh-Type-OutlierDetection-baseEjectionDuration"></a>
The base amount of time for which a host is ejected.
Type: [Duration](API_Duration.md) object
Required: Yes

 ** interval **   <a name="appmesh-Type-OutlierDetection-interval"></a>
The time interval between ejection sweep analysis.
Type: [Duration](API_Duration.md) object
Required: Yes

 ** maxEjectionPercent **   <a name="appmesh-Type-OutlierDetection-maxEjectionPercent"></a>
Maximum percentage of hosts in load balancing pool for upstream service that can be ejected. Will eject at least one host regardless of the value.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.
Required: Yes

 ** maxServerErrors **   <a name="appmesh-Type-OutlierDetection-maxServerErrors"></a>
Number of consecutive `5xx` errors required for ejection.
Type: Long
Valid Range: Minimum value of 1.
Required: Yes

## See Also
<a name="API_OutlierDetection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/OutlierDetection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/OutlierDetection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/OutlierDetection)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS App Mesh. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query app-mesh` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
