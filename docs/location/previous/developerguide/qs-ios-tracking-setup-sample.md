---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/qs-ios-tracking-setup-sample.html
---

# Tutorial: Set up sample app code
<a name="qs-ios-tracking-setup-sample"></a>

In order to setup the sample code you must have the following tools installed:
+ Git
+ XCode 15.3 or Later
+ iOS Simulator 16 or later

Use this procedure to set up the sample app code:

1. Clone the git repository from this URL: [https://github.com/aws-geospatial/amazon-location-samples-ios/tree/main/tracking-with-geofence-notifications](https://github.com/aws-geospatial/amazon-location-samples-ios/tree/main/tracking-with-geofence-notifications).

1.  Open the `AWSLocationSampleApp.xcodeproj` project file.

1.  Wait for the package resolution process to finish.

1. On the project navigation menu rename `ConfigTemplate.xcconfig` to `Config.xcconfig` and fill in the following values:

   ```
   IDENTITY_POOL_ID = `{{YOUR_IDENTITY_POOL_ID}}`
   MAP_NAME = `{{YOUR_MAP_NAME}}`
   TRACKER_NAME = `{{YOUR_TRACKER_NAME}}`
   WEBSOCKET_URL = `{{YOUR_MQTT_TEST_CLIENT_ENDPOINT}}`
   GEOFENCE_ARN = `{{YOUR_GEOFENCE_COLLECTION_NAME}}`
   ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
