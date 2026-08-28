---
source_url: https://docs.aws.amazon.com/dcv/latest/userguide/using-streaming.html
---

# Managing streaming modes
<a name="using-streaming"></a>

Amazon DCV uses an adaptive protocol that automatically optimizes the streaming mode depending on the network capabilities. However, you can specify whether you prefer to prioritize responsiveness or image quality.
+ Prioritizing responsiveness (**Best responsiveness**) reduces the image quality to improve the frame rate. This option prioritizes faster response times though It might result in lower image quality.
+ Prioritizing image quality (**Best quality**) reduces the responsiveness to provide better image quality. This option prioritizes higher image quality. It might result in longer response times.

This functionality is available on the Windows client, web browser client, Linux client, and macOS client. The steps for setting the streaming mode depend on the client used.

**Topics**
+ [Streaming modes on Windows, Linux, and macOS clients](using-streaming-native.md)
+ [Streaming modes on Web browser client](using-streaming-web.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DCV. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dcv` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
