---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/qs-ios-tracking-usage.html
---

# Tutorial: Use the sample app
<a name="qs-ios-tracking-usage"></a>

After setting up the sample code you can now run the app on an iOS simulator or a physical device.

1. Build and run the app.

1. The app will ask you for location and notification permissions. You need to allow them.

1. Press the **Cognito Configuration** button.

1. Save the configuration.

1. You can now see the Filter options for time, distance and accuracy. Use them as per your need.

1. Go to **Tracking** tab in the app and you will see the map and **Start Tracking** button.

1. If you have installed the app on a simulator you may want to simulate location changes. This can be done in **Features** under the **Location** menu option. For example select **Features**, then **Location**, then **Freeway Drive**.

1. Press the **Start Tracking** button. You should see the tracking points on the map.

1. The app is also tracking the locations in the background. So, when you move the app in the background it will ask for your permission to continue tracking in background mode.

1. You can stop the tracking by tapping on **Stop Tracking** button.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
