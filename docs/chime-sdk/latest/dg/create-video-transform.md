---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/create-video-transform.html
---

# Creating the VideoTransformDevice object for the Amazon Chime SDK
<a name="create-video-transform"></a>

The following example shows how to create a `VideoTransformDevice` object that contains the `VideoFxProcessor`.

```
// assuming that logger and videoInputDevice have already been set
const videoTransformDevice = new DefaultVideoTransformDevice(
  logger,
  videoInputDevice,
  [videoFxProcessor]
);
```
