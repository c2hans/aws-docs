---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/create-videofxprocessor.html
---

# Creating a VideoFxProcessor object for the Amazon Chime SDK
<a name="create-videofxprocessor"></a>

When creating the `VideoFxProcessor` object, AWS servers download the runtime assets, or a browser cache loads the assets. If network or CSP configurations prevent access to the assets, the `VideoFx.create` operation throws an exception. The resulting VideoFxProcessor is configured as a no-op processor, which won’t affect the video stream.

```
let videoFxProcessor: VideoFxProcessor | undefined = undefined;
try {
  videoFxProcessor = await VideoFxProcessor.create(logger, videoFxConfig);
} catch (error) {
  logger.warn(error.toString());
}
```

`VideoFxProcessor.create` also attempts to load the image from `backgroundReplacement.backgroundImageURL`. If the image fails to load, the processor throws an exception. The processor also throws exceptions for other reasons, such as invalid configurations, unsupported browsers, or underpowered hardware.
