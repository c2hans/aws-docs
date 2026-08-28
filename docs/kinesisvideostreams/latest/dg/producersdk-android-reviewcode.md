---
source_url: https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/producersdk-android-reviewcode.html
---

# Run and verify the code
<a name="producersdk-android-reviewcode"></a>

To run the Android example application for the [Android producer library](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/producer-sdk-android.html), do the following.

1. Connect to an Android device.

1. Choose **Run**, **Run...**, and choose **Edit configurations...**.

1. Choose the plus icon (**\+**), **Android App**. In the **Name** field, enter **AmazonKinesisVideoDemoApp**. In the **Module** pulldown, choose **AmazonKinesisVideoDemoApp**. Choose **OK**.

1. Choose **Run**, **Run**.

1. In the **Select Deployment Target** screen, choose your connected device, and choose **OK**.

1. In the **AWSKinesisVideoDemoApp** application on the device, choose **Create new account**.

1. Enter values for **USERNAME**, **Password**, **Given name**, **Email address**, and **Phone number**, and then choose **Sign up**.
**Note**
These values have the following constraints:
**Password:** Must contain uppercase and lowercase letters, numbers, and special characters. You can change these constraints in your User pool page on the [Amazon Cognito console](https://console.aws.amazon.com/cognito/home).
**Email address:** Must be a valid address so that you can receive a confirmation code.
**Phone number:** Must be in the following format: **\+{{<Country code>}}{{<Number>}}**, for example, **\+12065551212**.

1. Enter the code that you receive by email, and choose **Confirm**. Choose **Ok**.

1. On the next page, keep the default values, and choose **Stream**.

1. Sign in to the AWS Management Console and open the [Kinesis Video Streams console](https://console.aws.amazon.com/kinesisvideo/home/) in the US West (Oregon) Region.

   On the **Manage Streams** page, choose **demo-stream**.

1. The streaming video plays in the embedded player. You might need to wait a short time (up to ten seconds under typical bandwidth and processor conditions) while the frames accumulate before the video appears.
**Note**
If the device's screen rotates (for example, from portrait to landscape), the application stops streaming video.

The code example creates a stream. As the `MediaSource` in the code starts, it begins sending frames from the camera to the `KinesisVideoClient`. The client then sends the data to a Kinesis video stream named **demo-stream**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kinesis Video Streams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kinesisvideostreams` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
