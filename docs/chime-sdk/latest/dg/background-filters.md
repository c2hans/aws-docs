---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/background-filters.html
---

# Integrating background filters into a client application for the Amazon Chime SDK
<a name="background-filters"></a>

This section explains how to programmatically filter video backgrounds by using background blur 2.0 and background replacement 2.0. To add a background filter to a video stream, you create a `VideoFxProcessor` that contains a `VideoFxConfig` object. You then insert that processor into a `VideoTransformDevice`.

The background filter processor uses a TensorFlow Lite machine learning model, JavaScript Web Workers, and WebAssembly to apply a filter to the background of each frame in the video stream. These assets are downloaded at runtime when you create a `VideoFxProcessor`.

The [browser demo application on GitHub](https://github.com/aws/amazon-chime-sdk-js/tree/main/demos/browser) uses the new background blur and replacement filters. To try them, launch the demo with `npm run start`, join the meeting, then click the camera to enable video. Open the **Apply Filter** menu (![Button with a circle and a downward arrow.](http://docs.aws.amazon.com/chime-sdk/latest/dg/images/blur-apply-filter-initial.png)) and choose one of the **Background Blur 2.0** or **Background Replacement 2.0** options.

**Topics**
+ [About using background filters for the Amazon Chime SDK](about-bg-filters.md)
+ [Using a content-security policy with the Amazon Chime SDK client library for JavaScript](content-security.md)
+ [Adding background filters to your application for the Amazon Chime SDK](add-filters.md)
+ [Example background filter for the Amazon Chime SDK](example-bg-filter.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
