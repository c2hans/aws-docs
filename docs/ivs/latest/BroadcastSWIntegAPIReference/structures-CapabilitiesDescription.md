---
source_url: https://docs.aws.amazon.com/ivs/latest/BroadcastSWIntegAPIReference/structures-CapabilitiesDescription.html
---

# CapabilitiesDescription
<a name="structures-CapabilitiesDescription"></a>

Complex type specifying client hardware and software characteristics.

## Contents
<a name="structures-CapabilitiesDescription-contente"></a>
+ **cpu**
  + Client CPU characteristics.
  + Type: [CpuDescription](structures-CpuDescription.md) object
  + Required: Yes
+ **gaming\_features**
  + Client gaming features.
  + Type: [GamingFeaturesDescription](structures-GamingFeaturesDescription.md) object
  + Required: Yes
+ **gpu**
  + Client GPU characteristics.
  + Type: Array of [GpuDescription](structures-GpuDescription.md) objects
  + Required: Yes
+ **memory**
  + Client memory characteristics.
  + Type: [MemoryDescription](structures-MemoryDescription.md) object
  + Required: Yes
+ **system**
  + Client system characteristics.
  + Type: [SystemDescription](structures-SystemDescription.md) object
  + Required: Yes

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon IVS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ivs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
