---
source_url: https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/cloudwatch-metrics.html
---

End of support notice: On March 31, 2027, AWS will end support for Amazon WorkSpaces Thin Client. After March 31, 2027, you will no longer be able to access the WorkSpaces Thin Client console or WorkSpaces Thin Client resources. For more information, see [Amazon WorkSpaces Thin Client end of support](https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/workspacesthinclient-end-of-support.html).

# Monitor your WorkSpaces Thin Client using CloudWatch metrics
<a name="cloudwatch-metrics"></a>

WorkSpaces Thin Client devices and Amazon CloudWatch are integrated, so you can gather and analyze performance metrics emitted by your WorkSpaces Thin Client devices. You can monitor these metrics using the CloudWatch console, the CloudWatch command line interface, or programmatically using the CloudWatch API. CloudWatch also allows you to set alarms when you reach a specified threshold for a metric.

For more information about using CloudWatch and alarms, see the [Amazon CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/).

**Prerequisites**
There are no prerequisites. Once a WorkSpaces Thin Client device is registered to an Environment, it will begin to emit device metrics.

**Topics**
+ [WorkSpaces Thin Client metrics](#awstc-metrics)

## WorkSpaces Thin Client metrics
<a name="awstc-metrics"></a>

The `AWS/WorkSpacesThinClient` namespace includes the following metrics.

| Metric | Description | Dimensions | Statistics | Units |
| --- | --- | --- | --- | --- |
| DeviceSession | The number of ThinClient devices that are either connected to a device session, or that are not in session. | desktopType | Average, Min, Max, Sum, Sample Count | Count |
| ConnectedDevices | The number of ThinClient devices that are currently online. | n/a | Average, Min, Max, Sum, Sample Count | Count |
| SoftwareSetVersion | The number of ThinClient devices running a given Software Set version. | softwareSetVersion | Average, Min, Max, Sum, Sample Count | Count |
| NetworkConnectionEthernet | The number of ThinClient devices that are currently connected via Ethernet. | n/a | Average, Min, Max, Sum, Sample Count | Count |
| NetworkConnectionWifi | The number of ThinClient devices that are currently connected via WiFi. | n/a | Average, Min, Max, Sum, Sample Count | Count |

Dimensions to WorkSpaces Thin Client metrics

| Dimension | Description |
| --- | --- |
| desktopType | Filters the metric data by the desktop type currently in-session on the device. The device is in-session if a user is logged into a desktop, and if the device is not sleeping. If the device is in-session, the dimension value will be the desktop type used, such as WorkSpaces, WorkSpacesSecureBrowser, or AppStream. If the device is not in-session, the dimension value will be NotInSession. |
| softwareSetVersion | Filters the metric data by the Software Set version installed on the device. The form of the dimension in X.Y.Z, for example 1.4.2. |
