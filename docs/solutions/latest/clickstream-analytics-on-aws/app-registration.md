---
source_url: https://docs.aws.amazon.com/solutions/latest/clickstream-analytics-on-aws/app-registration.html
---

# App registration
<a name="app-registration"></a>

After the data pipeline transitions to an **Active** state, register your application(s) with the pipeline to enable the reception of clickstream data. After the application is added, you can integrate the SDK into your application to send data to the pipeline. Complete the following steps to register an application to a data pipeline.

**Steps**

1. Sign in to Clickstream Analytics on AWS Console.

1. In the left navigation pane, choose **Projects**, then select a project you want to register app, click its title, and it will bring you to the project page.

1. Click on **\+ Add application** to start adding application to the pipeline.

1. Complete the form by filling in the following fields:
   + **App name:** Provide a name for your app.
   + **App ID: **The system will generate one ID based on the name, which you can customize if needed.
   + **App reporting time zone:** Specify a reporting time zone for your app. This time zone is used by the preset dashboard to calculate daily metrics.
   + **Description:** Provide a description for your app.
   + **Android package name:** Provide a package name if your app has an Android client.
   + **App Bundle ID: **Provide the bundle ID if your app has an iOS client.

1. Choose **Register App & Generate SDK Instruction**, and wait for the registration to be completed.

1. You should now see tabs for SDK integration for different platforms. Choose the relevant tab to view detailed instructions on adding the SDK to your application. Follow the provided steps to integrate the SDK. For certain platforms, you can choose the **Download the config json file** button to obtain the configuration file.

The pipeline update with the newly added application takes approximately 3 to 5 minutes. After the pipeline status returns to **Active**, it is ready to receive data from your application.
