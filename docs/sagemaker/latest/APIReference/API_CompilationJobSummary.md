---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CompilationJobSummary.html
---

# CompilationJobSummary
<a name="API_CompilationJobSummary"></a>

A summary of a model compilation job.

## Contents
<a name="API_CompilationJobSummary_Contents"></a>

 ** CompilationJobArn **   <a name="sagemaker-Type-CompilationJobSummary-CompilationJobArn"></a>
The Amazon Resource Name (ARN) of the model compilation job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:compilation-job/.*`
Required: Yes

 ** CompilationJobName **   <a name="sagemaker-Type-CompilationJobSummary-CompilationJobName"></a>
The name of the model compilation job that you want a summary for.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** CompilationJobStatus **   <a name="sagemaker-Type-CompilationJobSummary-CompilationJobStatus"></a>
The status of the model compilation job.
Type: String
Valid Values: `INPROGRESS | COMPLETED | FAILED | STARTING | STOPPING | STOPPED`
Required: Yes

 ** CreationTime **   <a name="sagemaker-Type-CompilationJobSummary-CreationTime"></a>
The time when the model compilation job was created.
Type: Timestamp
Required: Yes

 ** CompilationEndTime **   <a name="sagemaker-Type-CompilationJobSummary-CompilationEndTime"></a>
The time when the model compilation job completed.
Type: Timestamp
Required: No

 ** CompilationStartTime **   <a name="sagemaker-Type-CompilationJobSummary-CompilationStartTime"></a>
The time when the model compilation job started.
Type: Timestamp
Required: No

 ** CompilationTargetDevice **   <a name="sagemaker-Type-CompilationJobSummary-CompilationTargetDevice"></a>
The type of device that the model will run on after the compilation job has completed.
Type: String
Valid Values: `lambda | ml_m4 | ml_m5 | ml_m6g | ml_c4 | ml_c5 | ml_c6g | ml_p2 | ml_p3 | ml_g4dn | ml_inf1 | ml_inf2 | ml_trn1 | ml_eia2 | jetson_tx1 | jetson_tx2 | jetson_nano | jetson_xavier | rasp3b | rasp4b | imx8qm | deeplens | rk3399 | rk3288 | aisage | sbe_c | qcs605 | qcs603 | sitara_am57x | amba_cv2 | amba_cv22 | amba_cv25 | x86_win32 | x86_win64 | coreml | jacinto_tda4vm | imx8mplus`
Required: No

 ** CompilationTargetPlatformAccelerator **   <a name="sagemaker-Type-CompilationJobSummary-CompilationTargetPlatformAccelerator"></a>
The type of accelerator that the model will run on after the compilation job has completed.
Type: String
Valid Values: `INTEL_GRAPHICS | MALI | NVIDIA | NNA`
Required: No

 ** CompilationTargetPlatformArch **   <a name="sagemaker-Type-CompilationJobSummary-CompilationTargetPlatformArch"></a>
The type of architecture that the model will run on after the compilation job has completed.
Type: String
Valid Values: `X86_64 | X86 | ARM64 | ARM_EABI | ARM_EABIHF`
Required: No

 ** CompilationTargetPlatformOs **   <a name="sagemaker-Type-CompilationJobSummary-CompilationTargetPlatformOs"></a>
The type of OS that the model will run on after the compilation job has completed.
Type: String
Valid Values: `ANDROID | LINUX`
Required: No

 ** LastModifiedTime **   <a name="sagemaker-Type-CompilationJobSummary-LastModifiedTime"></a>
The time when the model compilation job was last modified.
Type: Timestamp
Required: No

## See Also
<a name="API_CompilationJobSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CompilationJobSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CompilationJobSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CompilationJobSummary)
