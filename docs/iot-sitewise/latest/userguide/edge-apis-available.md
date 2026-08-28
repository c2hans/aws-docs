---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/userguide/edge-apis-available.html
---

# All available AWS IoT SiteWise Edge device APIs
<a name="edge-apis-available"></a>

AWS IoT SiteWise provides a variety of APIs to use on edge devices so that you can complete tasks locally on the device. Some of the available edge APIs include retrieving asset models, creating and updating asset properties, and sending data streams to the cloud. By leveraging these APIs, you can build solutions that can operate in environments with intermittent or limited network connectivity.

## Available AWS IoT SiteWise APIs
<a name="edge-apis-available-sw"></a>

The following AWS IoT SiteWise APIs are available on edge devices:
+ [ListAssetModels](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ListAssetModels.html)
+ [DescribeAssetModel](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeAssetModel.html)
+ [ListAssets](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ListAssets.html)
+ [DescribeAsset](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeAsset.html)
+ [DescribeAssetProperty](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeAssetProperty.html)
+ [ListAssociatedAssets](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ListAssociatedAssets.html)
+ [GetAssetPropertyAggregates](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_GetAssetPropertyAggregates.html)
+ [GetAssetPropertyValue](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_GetAssetPropertyValue.html)
+ [GetAssetPropertyValueHistory](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_GetAssetPropertyValueHistory.html)
+ [ListDashboards](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ListDashboards.html)
+ [ListPortals](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ListPortals.html)
+ [ListProjectAssets](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ListProjectAssets.html)
+ [ListProjects](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ListProjects.html)
+ [DescribeDashboard](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeDashboard.html)
+ [DescribePortal](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribePortal.html)
+ [DescribeProject](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeProject.html)

## Available edge-only APIs
<a name="edge-apis-available-local"></a>

The following APIs are used locally on devices on the edge:
+ [Authenticate](edge-local-apis.md#edge-local-apis-authenticate) – Use this API to get the SigV4 temporary credentials that you'll use to make API calls.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
