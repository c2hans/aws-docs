---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/add-filters.html
---

# Adding background filters to your application for the Amazon Chime SDK
<a name="add-filters"></a>

The process of adding background filters follows these broad steps:
+ Check for supported browsers.
+ Create a `VideoFxConfig` object with the configuration you want to use.
+ Use the configuration object to create a `VideoFxProcessor` object.
+ Include the `VideoFxProcessor` object in a `VideoTransformDevice` .
+ Use the `VideoTransformDevice` to start the video input.

**Note**
To complete those steps, you must first:
Create a `Logger`.
Choose a video device of class `MediaDeviceInfo`.
Successfully join a `MeetingSession`.

Steps in the following sections explain how to complete the process.

**Topics**
+ [Checking for support before offering a filter for the Amazon Chime SDK](support-check.md)
+ [Creating a VideoFxConfig object for the Amazon Chime SDK](create-videofxconfig.md)
+ [Creating a VideoFxProcessor object for the Amazon Chime SDK](create-videofxprocessor.md)
+ [Configuring the VideoFxProcessor object for the Amazon Chime SDK](configure-videofxprocessor.md)
+ [Creating the VideoTransformDevice object for the Amazon Chime SDK](create-video-transform.md)
+ [Starting video input for the Amazon Chime SDK](start-video-input.md)
+ [Tuning resource utilization for the Amazon Chime SDK](tuning.md)
