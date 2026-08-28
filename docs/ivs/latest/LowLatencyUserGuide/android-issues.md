---
source_url: https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/android-issues.html
---

# Known Issues & Workarounds in the IVS Android Player SDK
<a name="android-issues"></a>

This document lists known issues that you might encounter when using the Amazon IVS Android player SDK and suggests potential workarounds.
+ The Android player SDK has a runtime dependency on OkHttp version 4.x. Using OkHttp version 3.x may cause instability or crashes due to an API signature mismatch and OkHttp backwards compatibility issues. Specifically, the player depends on OkHttp version 4.2.2, but it should be compatible with any 4.x version.

  **Workaround:** Use a 4.x version of OkHttp or remove OkHttp from your application.
+ When using an Android 11 (API level 30) emulator, you may experience video-layout issues (specifically, zooming of the stream).

  **Workaround:** Play back on the real device instead.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon IVS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ivs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
