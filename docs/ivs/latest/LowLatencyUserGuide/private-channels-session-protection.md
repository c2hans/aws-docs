---
source_url: https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/private-channels-session-protection.html
---

# How Session Protection Works
<a name="private-channels-session-protection"></a>

When you request a playback URL with a valid playback token, IVS creates an authorized session and returns playlist and segment URLs that are unique to that session. These subsequent URLs do not contain a visible token parameter, but they are still tied to the authorized session.

Mechanisms are in place to mitigate sharing of session-bound URLs while still allowing legitimate usage patterns (e.g., mobile users switching between WiFi and cellular). If IVS detects unnatural usage, the authorized session is revoked and playback stops for all clients using that session.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon IVS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ivs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
