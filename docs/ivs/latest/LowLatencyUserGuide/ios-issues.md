---
source_url: https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/ios-issues.html
---

# Known Issues & Workarounds in the IVS iOS Player SDK
<a name="ios-issues"></a>

This document lists known issues that you might encounter when using the Amazon IVS iOS player SDK and suggests potential workarounds.
+ The player may crash when testing against the arm64e architecture. This only applies when targeting arm64e specifically, and does not apply to App Store builds.

  **Workaround:** Do not use arm64e.
