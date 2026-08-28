---
source_url: https://docs.aws.amazon.com/ivs/latest/BroadcastSWIntegAPIReference/structures-ClientConfigurationStatus.html
---

# ClientConfigurationStatus
<a name="structures-ClientConfigurationStatus"></a>

Object specifying errors or warnings to be exposed to the broadcaster. Refer to [Handling Warnings and Errors](https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/multitrack-video-sw-integration.html#multitrack-video-sw-integration-auto-stream-use-getclientconfig-errors) for more information.

## Contents
<a name="structures-ClientConfigurationStatus-contente"></a>
+ **html\_en\_us**
  + HTML informational text to render and display to the user.
  + Type: String
  + Length Constraints: Minimum length of 1. Maximum length of 4096.
  + Required: Yes
+ **result**
  + Severity of the information.
  + Type: String
  + Valid Values: `error` \| `warning`
  + Required: Yes

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon IVS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ivs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
