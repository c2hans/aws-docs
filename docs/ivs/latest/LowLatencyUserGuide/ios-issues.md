---
source_url: https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/ios-issues.html
---

# Known Issues & Workarounds in the IVS iOS Player SDK
<a name="ios-issues"></a>

This document lists known issues that you might encounter when using the Amazon IVS iOS player SDK and suggests potential workarounds.
+ The player may crash when testing against the arm64e architecture. This only applies when targeting arm64e specifically, and does not apply to App Store builds.

  **Workaround:** Do not use arm64e.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon IVS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ivs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
