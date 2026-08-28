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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
