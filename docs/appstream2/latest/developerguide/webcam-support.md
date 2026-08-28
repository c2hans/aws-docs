---
source_url: https://docs.aws.amazon.com/appstream2/latest/developerguide/webcam-support.html
---

# Enabling and Disabling Webcam Support
<a name="webcam-support"></a>

WorkSpaces Applications supports real-time audio-video (AV) by redirecting local webcam video input to WorkSpaces Applications streaming sessions. This capability enables your users to use their local webcam for video and audio conferencing within an WorkSpaces Applications streaming session. With real-time AV and support for real-time audio, your users can collaborate by using familiar video and audio conferencing applications without having to leave their WorkSpaces Applications streaming session.

To use this feature, you must use a Linux WorkSpaces Applications image that uses a Linux WorkSpaces Applications agent released on or after September 21, 2022.

**Note**
Real-time AV is not supported for stream.standard.small instances powered by Rocky Linux or Red Hat Enterprise Linux. Users don't see the Camera and Mic icons on the client toolbar.

The real-time AV feature is enabled by default for Linux streaming sessions. To configure webcam permissions for your users on a Linux image builder, create `/etc/appstream/appstream.conf` and add the following contents:

**Note**
Specify **1** to enable webcam, or **0** to disable webcam.

```
[webcam]
permission = 1
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
