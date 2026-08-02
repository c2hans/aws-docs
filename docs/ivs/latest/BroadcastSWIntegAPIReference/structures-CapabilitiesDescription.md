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
