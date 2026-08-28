---
source_url: https://docs.aws.amazon.com/ivs/latest/BroadcastSWIntegAPIReference/structures-ClientDescription.html
---

# ClientDescription
<a name="structures-ClientDescription"></a>

Complex type specifying client software and configuration.

## Contents
<a name="structures-ClientDescription-contente"></a>
+ **name**
  + Name of the client software.
  + Type: String
  + Length Constraints: Minimum length of 1. Maximum length of 128.
  + Required: Yes
+ **supported\_codecs**
  + List of codecs that the client explicitly supports. Default: `["h264"]`.
  + Type: Array of strings
  + Valid Element Values: `h264` \| `h265`
  + Required: No
+ **version**
  + Version of the client software.
  + Type: String
  + Length Constraints: Minimum length of 1. Maximum length of 128.
  + Required: Yes

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon IVS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ivs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
