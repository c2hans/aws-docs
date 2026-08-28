---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/qs-android-tracking-use.html
---

# Tutorial: Use the sample app
<a name="qs-android-tracking-use"></a>

This guide walks you through the process of setting up and using the sample Android tracking application. By following the step-by-step instructions outlined in this section, you'll learn how to configure the necessary AWS resources, integrate the tracking functionality into the sample app, and deploy it to your Android device.

To use the sample follow these procedures:
+ **Create a `custom.properties`**:

  To configure your `custom.properties` file, follow these steps:

  1. Open your preferred text editor or IDE.

  1. Create a new file.

  1. Save the file with the name `custom.properties`.

  1. Update the `custom.properties` with the following code sample, and replace the `MQTT_END_POINT`, `POLICY_NAME`, `GEOFENCE_COLLECTION_NAME`, and `TOPIC_TRACKER` with your resoucre names:

     ```
     MQTT_END_POINT={{YOUR_END_POINT}}.us-east-1.amazonaws.com
     POLICY_NAME={{YOUR_POLICY}}
     GEOFENCE_COLLECTION_NAME={{YOUR_GEOFENCE}}
     TOPIC_TRACKER={{YOUR_TRACKER}}
     ```

  1. Clean and Rebuild the project. After this, you can run the project.
+ **Sign In**:

  To sign in to the application, follow the below steps:

  1. Press the **Sign In** button.

  1. Provide an **Identity Pool Id**, **Tracker name**, and a **Map name**.

  1. Press **Sign In** again to finish.
+ **Manage Filters**:

  Open the configuration screen, and perform the following:

  1. Toggle filters on or off using the switch UI.

  1. Update Time and Distance filters when needed.
+ **Tracking Operations:**

  Open the tracking screen and perform the following:
  + You can start and stop tracking in foreground, background, or in battery-saver mode by pressing the respective buttons.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
