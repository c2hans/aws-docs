---
source_url: https://docs.aws.amazon.com/ivs/latest/BroadcastSWIntegAPIReference/structures-GpuDescription.html
---

# GpuDescription
<a name="structures-GpuDescription"></a>

Object specifying client GPU characteristics.

## Contents
<a name="structures-GpuDescription-contente"></a>
+ **dedicated\_video\_memory**
  + Size of the dedicated GPU memory in bytes. Providing a value allows IVS to better assess system capabilities, but it is not required.
  + Type: Integer
  + Valid Range: Minimum value of 1.
  + Required: No
+ **device\_id**
  + The GPU’s driver-provided device ID, expressed as a decimal integer. For example, the NVIDIA RTX 4080 uses PCIe device ID (0x2704), which is decimal 9988.
  + Type: Integer
  + Required: Yes
+ **driver\_version**
  + Version of the GPU driver.
  + Type: String
  + Length Constraints: Minimum length of 1. Maximum length of 128.
  + Required: Yes
+ **luid**
  + Uniquely identifies a GPU on a system with multiple GPUs. The value can be any local identifier used on the system to identify GPUs.
  + Type: String
  + Required: No
+ **model**
  + Model name of the GPU. It must exactly match the full name provided by the GPU’s manufacturer. Otherwise, the GPU may not be recognized by IVS.
  + Type: String
  + Length Constraints: Minimum length of 1. Maximum length of 4096.
  + Required: Yes
+ **shared\_system\_memory**
  + Size of the shared GPU memory in bytes. Providing a value allows IVS to better assess system capabilities, but it is not required.
  + Type: Integer
  + Valid Range: Minimum value of 1.
  + Required: No
+ **vendor\_id**
  + The GPU’s driver-provided vendor ID, expressed as a decimal integer. For example, the NVIDIA RTX 4080 uses PCIe vendor ID (0x10DE), which is decimal 4318.
  + Type: Integer
  + Required: Yes
