---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TargetPlatform.html
---

# TargetPlatform
<a name="API_TargetPlatform"></a>

Contains information about a target platform that you want your model to run on, such as OS, architecture, and accelerators. It is an alternative of `TargetDevice`.

## Contents
<a name="API_TargetPlatform_Contents"></a>

 ** Arch **   <a name="sagemaker-Type-TargetPlatform-Arch"></a>
Specifies a target platform architecture.
+  `X86_64`: 64-bit version of the x86 instruction set.
+  `X86`: 32-bit version of the x86 instruction set.
+  `ARM64`: ARMv8 64-bit CPU.
+  `ARM_EABIHF`: ARMv7 32-bit, Hard Float.
+  `ARM_EABI`: ARMv7 32-bit, Soft Float. Used by Android 32-bit ARM platform.
Type: String
Valid Values: `X86_64 | X86 | ARM64 | ARM_EABI | ARM_EABIHF`
Required: Yes

 ** Os **   <a name="sagemaker-Type-TargetPlatform-Os"></a>
Specifies a target platform OS.
+  `LINUX`: Linux-based operating systems.
+  `ANDROID`: Android operating systems. Android API level can be specified using the `ANDROID_PLATFORM` compiler option. For example, `"CompilerOptions": {'ANDROID_PLATFORM': 28}`
Type: String
Valid Values: `ANDROID | LINUX`
Required: Yes

 ** Accelerator **   <a name="sagemaker-Type-TargetPlatform-Accelerator"></a>
Specifies a target platform accelerator (optional).
+  `NVIDIA`: Nvidia graphics processing unit. It also requires `gpu-code`, `trt-ver`, `cuda-ver` compiler options
+  `MALI`: ARM Mali graphics processor
+  `INTEL_GRAPHICS`: Integrated Intel graphics
Type: String
Valid Values: `INTEL_GRAPHICS | MALI | NVIDIA | NNA`
Required: No

## See Also
<a name="API_TargetPlatform_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/TargetPlatform)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/TargetPlatform)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/TargetPlatform)
