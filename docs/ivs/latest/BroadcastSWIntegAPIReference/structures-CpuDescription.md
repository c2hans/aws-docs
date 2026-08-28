---
source_url: https://docs.aws.amazon.com/ivs/latest/BroadcastSWIntegAPIReference/structures-CpuDescription.html
---

# CpuDescription
<a name="structures-CpuDescription"></a>

Object specifying client CPU characteristics

## Contents
<a name="structures-CpuDescription-contente"></a>
+ **logical\_cores**
  + Number of logical cores.
  + Type: Integer
  + Valid Range: Minimum value of 1.
  + Unit: Count
  + Required: No
+ **name**
  + Vendor and descriptive model name.
  + Type: String
  + Length Constraints: Minimum length of 1. Maximum length of 4096.
  + Required: Yes
+ **physical\_cores**
  + Number of physical cores.
  + Type: Integer
  + Valid Range: Minimum value of 1.
  + Unit: Count
  + Required: No
+ **speed**
  + CPU clock frequency. Intel CPUs support base, minimum, and maximum frequency; please report the base frequency. AMD CPUs support minimum and maximum frequency; please report the maximum frequency.
  + Type: Integer
  + Valid Range: Minimum value of 1.
  + Unit: MHz
  + Required: No

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon IVS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ivs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
