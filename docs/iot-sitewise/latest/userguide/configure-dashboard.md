---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/userguide/configure-dashboard.html
---

# Configure dashboard
<a name="configure-dashboard"></a>

**Note**
The SiteWise Monitor feature is no longer available to new customers. Existing customers can continue to use the service as normal. For more information, see [SiteWise Monitor availability change](https://docs.aws.amazon.com/iot-sitewise/latest/appguide/iotsitewise-monitor-availability-change.html).

 The **Dashboards** section lists the dashboards in the project. Select a dashboard from the list. The **Edit** mode allows you to configure your dashboard by adding widgets and configuring them. The **Preview** button lets you visualize your changes.

![The IoT dashboard Project page with Edit highlighted.](http://docs.aws.amazon.com/iot-sitewise/latest/userguide/images/ai-dashboard-edit.png)

Steps to configure your dashboard:
+ Drag and drop different type of data widgets to the dashboard canvas for data visualization.
+  Add data to the desired widgets, from the **Resource explorer** on the left. The **Resource explorer** consists of **Modeled**, **Unmodeled**, and **Dynamic assets** sections. Search by asset name or property name. Select the property to add and choose **Add**.
+  Fine tune the layout and style by changing the **Configurations** on widgets. Configure components including title, thresholds and other configuration specifics.
+  Configure the time range over which data is displayed.
  +  Choose the time range over which data is displayed. Choose a **Time range** and **Refresh rate** from the top right hand corner, and personalize the range. Choose a rate at which the data is to be refreshed from the menu.
  +  Select the **Time range** on a widget, by using your trackball mouse scroll wheel or Right-click. This moves the time range of display.
+ Choose **Save**.

**Topics**
+ [Resource explorer](resource-exp.md)
+ [Widgets](dashboard-widgets.md)
+ [Configure widgets](dashboard-widgets-conf.md)
+ [Use widgets](dashboard-widgets-manip.md)
+ [Alarms in widgets](alarm-widgets.md)
+ [AWS IoT SiteWise Assistant use in widgets](assistant-widgets.md)
+ [Sample questions to ask AWS IoT SiteWise Assistant](assistant-questions.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
