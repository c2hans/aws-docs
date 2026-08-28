---
source_url: https://docs.aws.amazon.com/ivs/latest/BroadcastSWIntegAPIReference/structures-SystemDescription.html
---

# SystemDescription
<a name="structures-SystemDescription"></a>

Object specifying client system characteristics.

## Contents
<a name="structures-SystemDescription-contente"></a>
+ **arm**
  + Indicates that system architecture is ARM based. Default: `false` (not based on ARM).
  + Type: Boolean
  + Required: No
+ **arm\_emulation**
  + Indicates that the system can emulate ARM architecture. Default: `false` (emulation not available).
  + Type: Boolean
  + Required: No
+ **bits**
  + Indicates 32-bit or 64-bit operating system. Providing a value allows IVS to better assess system capabilities, but it is not required.
  + Type: Integer
  + Valid Values: 32 \| 64
  + Required: No
+ **build**
  + Build of the operating system.
  + Type: Integer
  + Required: Yes
+ **name**
  + Name of the operating system.
  + Type: String
  + Valid Value: `Windows`
  + Required: Yes
+ **release**
  + Release of the operating system.
  + Type: String
  + Required: Yes
+ **revision**
  + Revision of the operating system.
  + Type: String
  + Required: Yes
+ **version**
  + Version of the operating system.
  + Type: String
  + Length Constraints: Minimum length of 1. Maximum length of 128.
  + Required: Yes

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon IVS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ivs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
