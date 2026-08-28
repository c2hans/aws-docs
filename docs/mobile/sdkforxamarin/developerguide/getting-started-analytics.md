---
source_url: https://docs.aws.amazon.com/mobile/sdkforxamarin/developerguide/getting-started-analytics.html
---

The AWS Mobile SDK for Xamarin is now included in the AWS SDK for .NET. This guide references the archived version of the Mobile SDK for Xamarin.

# Tracking App Usage Data with Amazon Mobile Analytics
<a name="getting-started-analytics"></a>

Amazon Mobile Analytics allows you to measure app usage and app revenue. By tracking key trends such as new vs. returning users, app revenue, user retention, and custom in-app behavior events, you can make data-driven decisions to increase engagement and monetization for your app.

The tutorial below explains how to integrate Mobile Analytics with your app.

## Project Setup
<a name="project-setup"></a>

### Prerequisites
<a name="prerequisites"></a>

You must complete all of the instructions on the [Setting Up the AWS Mobile SDK for .NET and Xamarin](setup.md) before beginning this tutorial.

### Create an App in the Mobile Analytics Console
<a name="create-an-app-in-the-mobile-analytics-console"></a>

Go to the [Amazon Mobile Analytics console](https://aws.amazon.com/mobileanalytics/) and create an app. Note the `appId` value, as you’ll need it later. When you are creating an app in the Mobile Analytics Console you will need to specify your identity pool ID. For instructions on creating an identity pool, see [Setting Up the AWS Mobile SDK for .NET and Xamarin](setup.md).

To learn more about working in the console, see the [Amazon Mobile Analytics User Guide](https://docs.aws.amazon.com/mobileanalytics/latest/ug/).

### Set Permissions for Mobile Analytics
<a name="set-permissions-for-mobile-analytics"></a>

The default policy associated with the roles that you created during setup grant your application access to Mobile Analytics. No further configuration is required.

### Add NuGet Package for Mobile Analytics to Your Project
<a name="add-nuget-package-for-mobile-analytics-to-your-project"></a>

Follow Step 4 of the instructions in [Setting Up the AWS Mobile SDK for .NET and Xamarin](setup.md) to add the Mobile Analytics NuGet package to your project.

### Configure Mobile Analytics Settings
<a name="configure-mobile-analytics-settings"></a>

Mobile Analytics defines some settings that can be configured in the awsconfig.xml file:

```
var config = new MobileAnalyticsManagerConfig();
config.AllowUseDataNetwork = true;
config.DBWarningThreshold = 0.9f;
config.MaxDBSize = 5242880;
config.MaxRequestSize = 102400;
config.SessionTimeout = 5;
```
+ AllowUseDataNetwork - A boolean that specifies if the session events are sent on the data network.
+ DBWarningThreshold - This is the limit on the size of the database which, once reached, will generate warning logs.
+ MaxDBSize - This is the size of the SQLIte Database. When the database reaches the maximum size, any additional events are dropped.
+ MaxRequestSize - This is the maximum size of the request in Bytes that should be transmitted in an HTTP request to the mobile analytics service.
+ SessionTimeout - This the time interval after an application goes to background and when session can be terminated.

The settings shown above are the default values for each configuration item.

## Initialize MobileAnalyticsManager
<a name="initialize-mobileanalyticsmanager"></a>

To initialize your MobileAnalyticsManager, call GetOrCreateInstance on your `MobileAnalyticsManager`, passing in your AWS credentials, your region, your Mobile Analytics application ID, and your optional config object:

```
var manager = MobileAnalyticsManager.GetOrCreateInstance(
  "APP_ID",
  "Credentials",
  "RegionEndPoint",
  config
);
```

## Track Session Events
<a name="track-session-events"></a>

### Xamarin Android
<a name="xamarin-android"></a>

Override the activity’s `OnPause()` and `OnResume()` methods to record session events.

```
protected override void OnResume()
{
    manager.ResumeSession();
    base.OnResume();
}

protected override void OnPause()
{
    manager.PauseSession();
    base.OnPause();
}
```

This needs to be implemented for each activity in your application.

### Xamarin iOS
<a name="xamarin-ios"></a>

In your AppDelegate.cs:

```
public override void DidEnterBackground(UIApplication application)
{
    manager.PauseSession();
}

public override void WillEnterForeground(UIApplication application)
{
    manager.ResumeSession();
}
```

For more information on Mobile Analytics, see [Amazon Mobile Analytics](analytics.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Mobile SDK for Xamarin. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mobile` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
