---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/example-stream-position-updates.html
---

# Example: Stream Position Updates
<a name="example-stream-position-updates"></a>

![Map showing tracker locations along a river with pink highlighted areas and information panel.](http://docs.aws.amazon.com/location/previous/developerguide/images/samples/sampleappgeofenceKVS1.png)

**Kinesis Stream To Tracker App**: This sample demonstrates how to use Kinesis Data Stream to post tracker updates with Amazon Location Service. The sample is a deployable lambda application written in python that can be integrated with a Kinesis Data Stream to consume the Kinesis events and batch update device positions.

Repository link: [ Amazon Location Amazon Kinesis Data Streams Stream To Tracker App](https://github.com/aws-geospatial/amazon-location-stream-device-data-to-tracker-lambda)

For more information on tracking and geofences, see the [Geofences and Trackers](https://docs.aws.amazon.com/location/previous/developerguide/geofence-tracker-concepts.html) documentation. Developers can deploy the app by following the [AWS's Serverless Application Repository](https://docs.aws.amazon.com/serverlessrepo/latest/devguide/serverlessrepo-how-to-consume.html) documentation, or dicretly from the [Lambda console](https://console.aws.amazon.com/lambda/home#/create/app?applicationId=arn:aws:serverlessrepo:us-east-1:003883091127:applications/kinesis-stream-device-data-to-amazon-location-tracker).

**Device Position Streaming Sample App**: This code example shows how to stream device position data to a Kinesis Data Stream and how geofence notifications work. This app depends on the Kinesis Stream to Tracker Sample App, listed above, to be running for the streamed tracker positions to be updated in Amazon Location Service.

Repository link: [Amazon Location Device Position Streaming Sample App](https://github.com/aws-geospatial/amazon-location-samples-react/tree/main/tracking-data-streaming)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
