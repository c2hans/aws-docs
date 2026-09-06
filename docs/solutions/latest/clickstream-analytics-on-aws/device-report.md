---
source_url: https://docs.aws.amazon.com/solutions/latest/clickstream-analytics-on-aws/device-report.html
---

# Device report
<a name="device-report"></a>

 The Device Report provides insights into the devices, operating systems, and browsers used by your app or website users. This data helps you understand your user base and optimize for the most common configurations.

**Note**
This article describes the default report. You can customize the report by applying filters or comparisons or by changing the dimensions, metrics, or charts in QuickSight. For more information, refer to [Visualizing data in Quick](https://docs.aws.amazon.com/quicksight/latest/user/working-with-visuals.html).

## View the report
<a name="view-the-report-4"></a>

1.  Access the dashboard for your application. Refer to [Access dashboard](dashboards-1.md#view-dashboards).

1.  In the dashboard, choose the sheet with name of `Device`.

## Data sources
<a name="where-the-data-comes-from-4"></a>

 Device reports are created based on the following QuickSight dataset:

 Retention report are created based on the following QuickSight dataset:

|  **QuickSight dataset**  |  **Redshift view / table**  |  **Description**  |
| --- | --- | --- |
| Device-<app>-<project>  | clickstream\_device\_user\_device\_view  | This dataset stores data on the device information per each user for each day.  |
| Crash\_Rate-<app>-<project>  | clickstream\_device\_crash\_rate  | This dataset stores data on the crash rate for each app version for each day. |

## Dimensions
<a name="dimensions-and-metrics-4"></a>

 The report includes the following dimensions:

|  **Dimension**  |  **Description**  |  **How it's calculated**  |
| --- | --- | --- |
| App version  | The version of the app  | Derived from the app\_version field automatically collected by Clickstream SDK or manually set by HTTP API.  |
| Device  | The device name associated with the event.  | For mobile app, it is derived from model\_name field automatically collected by Clickstream SDK or manually set in HTTP request. For web, it is the device\_ua\_device that parsed from User Agent.  |
| Device screen resolution  | The screen resolution of the device  | Concatenation of screen\_width and screen\_height values  |
| Browser  | The name of the browser  | From the value of device\_ua\_browser field which parsed from the User Agent.  |
| Operating system  | The operating system of the device.  | For mobile app, it is derived from platform field automatically collected by Clickstream SDK or manually set in HTTP request. For web, it is the device\_ua\_operating\_system that parsed from User Agent.  |
| Operating system version | The operating system version of the device.  | For mobile app, it is derived from os\_version field automatically collected by Clickstream SDK or manually set in HTTP request. For web, it is the device\_ua\_operating\_system\_version that parsed from User Agent. |

## Metrics
<a name="metrics-2"></a>

 The report includes the following metrics:

|  **Metric**  |  **Definition**  |  **How it's calculated**  |
| --- | --- | --- |
| Active users  | Number of active users that had triggered any event. | Count distinct user\_id or user\_pseudo\_id (if user\_id is not available).  |
| Crash rate | The percentage of the users experiencing app. | Number of distinct user with '\_app\_exception' events / Total active users |

## Sample dashboard
<a name="sample-dashboard-5"></a>

Below image is a sample dashboard for your reference.

![Dashboard showing active users by platform, operating system, browser, device, and app version.](http://docs.aws.amazon.com/solutions/latest/clickstream-analytics-on-aws/images/device.png)
