---
source_url: https://docs.aws.amazon.com/toolkit-for-visual-studio/latest/user-guide/cloudwatch-log-overview.html
---

# Working with CloudWatch Logs in Visual Studio
<a name="cloudwatch-log-overview"></a>

Amazon CloudWatch Logs integration allows you to monitor, store, and access CloudWatch Logs from the AWS Toolkit for Visual Studio with Amazon Q. Having access to CloudWatch Logs features—without the need to leave your IDE—improves efficiency by simplifying the CloudWatch Logs development process and reducing disruptions to your work flow. The following topics describe how to work with the basic features and functions of the CloudWatch Logs integration.

**Topics**
+ [CloudWatch Log Groups](#cloudwatch-log-overview-groups)
+ [CloudWatch Log Streams](#cloudwatch-log-overview-logstream)
+ [CloudWatch Log Events](#cloudwatch-log-overview-logevents)
+ [Additional access to CloudWatch Logs](#cloudwatch-log-overview-additional)

## CloudWatch Log Groups
<a name="cloudwatch-log-overview-groups"></a>

A `log group` is a group of `log streams` that share the same retention, monitoring, and access control settings. There is no limit on the number of log streams that can belong to one log group.

### Viewing Log Groups
<a name="cloudwatch-log-overview-groups-view"></a>

The `View Log Groups` feature displays a list of log groups in the CloudWatch Log Groups Explorer.

To access the View Log Groups feature and open the CloudWatch Log Groups Explorer, complete the following steps.

1. From the AWS Explorer, expand **Amazon CloudWatch**.

1. Double-click **Log Groups** or open the context menu (right-click) and select **View**, to open the **CloudWatch Log Groups Explorer**.
**Note**
The CloudWatch Log Groups Explorer will open in the same window location as the Solutions Explorer.

### Filtering Log Groups
<a name="cloudwatch-log-overview-groups-filter"></a>

Your individual account is able to contain thousands of different log groups. To simplify your search for specific groups, use the `filtering` feature described below.

1. From the **CloudWatch Log Groups Explorer**, set your cursor in the search bar located at the top of the window.

1. Start typing a prefix related to the log groups that you're looking for.

1. **CloudWatch Log Groups Explorer** is automatically updated to show results matching the search terms you specified in the previous step.

### Delete Log Groups
<a name="cloudwatch-log-overview-groups-delete"></a>

To delete a specific log group, refer to the following procedure.

1. From the **CloudWatch Log Groups Explorer**, right-click the Log Group that you want to delete.

1. When prompted, confirm that you want to delete the currently selected Log Group.

1. Choosing the **Yes** button deletes the selected log group, then refreshes the **CloudWatch Log Groups Explorer**.

### Refresh Log Groups
<a name="cloudwatch-log-overview-groups-refresh"></a>

To refresh the current list of log groups displayed in the **CloudWatch Log Groups Explorer**, choose the **Refresh icon** button located in the **toolbar**.

### Copy Log Group ARN
<a name="cloudwatch-log-overview-groups-copyarn"></a>

To copy the ARN of a specific log group, complete the steps described below.

1. From the **CloudWatch Log Groups Explorer**, right-click the Log Group you want to copy an ARN from.

1. Choose the **Copy ARN** option from the menu.

1. The ARN is now copied to your local clipboard and ready to paste.

## CloudWatch Log Streams
<a name="cloudwatch-log-overview-logstream"></a>

A log stream is a sequence of log events that share the same source.

**Note**
When viewing log streams, be aware of the following properties:
By default the log streams are sorted by the most-recent event time stamp.
Columns associated with a log stream can be sorted in either ascending or descending order, by toggling the **caret** located in the column headers.
Filtered entries can only be sorted by **Log Stream Name**.

### Viewing Log Streams
<a name="cloudwatch-log-overview-logstream-view"></a>

1. From the **CloudWatch Log Groups Explorer** double-click a Log Group, or right-click a log group and select **View Log Stream** from the context menu.

1. A new tab will open in the **document** window, which contains a list of log streams associated with your log group.

### Filtering Log Streams
<a name="cloudwatch-log-overview-logstream-filter"></a>

1. From the **Log Streams** tab, in the **document** window, set your cursor in the search bar.

1. Start typing a prefix related to the log stream that you're looking for.

1. As you type, the current display automatically updates to filter your Log Streams by your input.

### Refresh Log Streams
<a name="cloudwatch-log-overview-logstream-refresh"></a>

To refresh the current list of log streams displayed in the **document** window, choose the **Refresh icon** button, located in the **toolbar**, next to the **search bar**.

### Copy Log Streams ARN
<a name="cloudwatch-log-overview-logstream-copyarn"></a>

To copy the ARN of a specific log stream, complete the steps described below.

1. From the **Log Streams** tab, in the **document** window, right-click the log stream you want to copy an ARN from.

1. Choose the **Copy ARN** option from the menu.

1. The ARN is now copied to your local clipboard and ready to paste.

### Download Log Streams
<a name="cloudwatch-log-overview-logstream-delete"></a>

The **Export Log Stream** feature downloads and stores the selected log stream locally, where it can be accessed by custom tools and software for additional processing.

1. From the **Log Streams** tab, in the **document** window, right-click the log stream you want to download.

1. Choose **Export Log Stream** to open the **Export to a text file** dialog.

1. Choose the location where you want to store the file locally and specify a name in the provided text field.

1. Confirm the download by selecting **OK**. The status of the download is displayed in the **Visual Studio Task Status Center**

## CloudWatch Log Events
<a name="cloudwatch-log-overview-logevents"></a>

Log events are records of activity recorded by the application or resource being monitored by CloudWatch.

### Log Event actions
<a name="cloudwatch-log-overview-logevents-actions"></a>

Log events are displayed as a table. By default, the events are sorted from the oldest event to the most recent.

The following actions are associated with log events in Visual Studio:
+ Wrapped-text mode: You can toggle wrapped-text by clicking an event.
+ Text-wrap button: located in the `document window toolbar`, this button toggles text-wrap on and off, for all entries.
+ Copy messages to your clipboard: select the messages you want to copy, then right-click the selection and choose **Copy** (keyboard shortcut `Ctrl + C`).

### Viewing Log Events
<a name="cloudwatch-log-overview-logevents-view"></a>

1. From the **document** window, choose a tab that contains a list of log streams.

1. Double-click a log stream, or right-click a log stream and select **View Log Stream** from the menu.

1. A new **log event** tab will open in the **document** window, which contains a table of log events associated with your chosen log stream.

### Filtering Log Events
<a name="cloudwatch-log-overview-logevents-filter"></a>

There are three ways for you to filter log events: by content, time range, or both. To filter your log events by both content and time range, start by filtering your messages by either content or time range, then filter those results by the other method.

To filter your log events by content:

1. From the **log event** tab, in the **document** window, set your cursor in the search bar, located at the top of the window.

1. Start typing a term or phrase related to the log events that you're searching for.

1. As you type, the current display automatically begins to filter your log events.
**Note**
Filter patterns are case sensitive. You can improve search results by enclosing exact terms, and phrases, with non-alphanumeric characters in double quotation marks (\*""\*). For more detailed information about filter patterns, see the [Filter and Pattern Syntax](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/FilterAndPatternSyntax.html) topic in the Amazon CloudWatch guide.

To view log events generated during a specific time range:

1. From the **log event** tab, in the **document** window, choose the **Calendar icon** button, located in the **toolbar**.

1. Using the provided fields, specify the time range that you want to search.

1. The filtered results update automatically as you specify the date and time constraints.
**Note**
The **Clear Filter** option clears all of your current date-and-time filter selections.

### Refresh Log Events
<a name="cloudwatch-log-overview-logevents-refresh"></a>

To refresh the current list of log events displayed in the **log event** tab, choose the **Refresh icon** button, located in the **toolbar**.

## Additional access to CloudWatch Logs
<a name="cloudwatch-log-overview-additional"></a>

You can access CloudWatch Logs associated with other AWS services and resources directly from the AWS Toolkit in Visual Studio.

### Lambda
<a name="cloudwatch-log-overview-additional-lambda"></a>

To view log streams that are associated with a Lambda function:

**Note**
Your Lambda execution role must have appropriate permissions to send logs to CloudWatch Logs. For more information about the Lambda permissions required for CloudWatch Logs, see the [https://docs.aws.amazon.com/lambda/latest/dg/monitoring-cloudwatchlogs.html#monitoring-cloudwatchlogs-prereqs](https://docs.aws.amazon.com/lambda/latest/dg/monitoring-cloudwatchlogs.html#monitoring-cloudwatchlogs-prereqs)

1. From the AWS Toolkit Explorer, expand **Lambda**.

1. right-click the function you want to view, then choose **View Logs** to open the associated log streams in the **document** window.

To view log streams using the Lambda integration `function view`:

1. From the AWS Toolkit Explorer, expand **Lambda**.

1. right-click the function you want to view, then choose **View Function** to open the function view in the **document** window.

1. From the `function view`, switch to the **Logs** tab, the log streams associated with the chosen Lambda function are displayed.

### ECS
<a name="cloudwatch-log-overview-additional-ecs"></a>

To view log resources that are associated with an ECS Task Container, complete the following procedure.

**Note**
In order for the Amazon ECS service to send logs to CloudWatch, each container for a given Amazon ECS Task must meet the required configuration. For additional information about the required set up and configurations, please see the guide [Using the AWS Logs Log Driver](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using_awslogs.html).

1. From the AWS Toolkit Explorer, expand **Amazon ECS**.

1. Choose the Amazon ECS Cluster that you want to view to open a new **ECS Cluster** tab, in the **document** window.

1. From the navigation menu, located on the left side of the **ECS Cluster** tab, choose **Tasks** to list all tasks associated with the cluster.

1. From the **Tasks** display, select a task and choose the **View Logs** link, located in the bottom-left corner.
**Note**
This display lists all tasks contained in the cluster, the `View Logs` link is only visible for each task that meets the required logs configuration.
If a Task is only associated with a single container, the **View Logs** link opens that container's log stream.
If a Task is associated with multiple containers, the **View Logs** link opens the **View CloudWatch Logs for ECS Task** dialog, use the **Container:** drop-down menu to choose the container you want to view Logs for, then choose **OK**.

1. A new tab opens in the **document** window displaying the log streams associated with your container selection.
