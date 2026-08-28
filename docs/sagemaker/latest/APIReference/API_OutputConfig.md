---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_OutputConfig.html
---

# OutputConfig
<a name="API_OutputConfig"></a>

Contains information about the output location for the compiled model and the target device that the model runs on. `TargetDevice` and `TargetPlatform` are mutually exclusive, so you need to choose one between the two to specify your target device or platform. If you cannot find your device you want to use from the `TargetDevice` list, use `TargetPlatform` to describe the platform of your edge device and `CompilerOptions` if there are specific settings that are required or recommended to use for particular TargetPlatform.

## Contents
<a name="API_OutputConfig_Contents"></a>

 ** S3OutputLocation **   <a name="sagemaker-Type-OutputConfig-S3OutputLocation"></a>
Identifies the S3 bucket where you want Amazon SageMaker AI to store the model artifacts. For example, `s3://bucket-name/key-name-prefix`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `(https|s3)://([^/]+)/?(.*)`
Required: Yes

 ** CompilerOptions **   <a name="sagemaker-Type-OutputConfig-CompilerOptions"></a>
Specifies additional parameters for compiler options in JSON format. The compiler options are `TargetPlatform` specific. It is required for NVIDIA accelerators and highly recommended for CPU compilations. For any other cases, it is optional to specify `CompilerOptions.`
+  `DTYPE`: Specifies the data type for the input. When compiling for `ml_*` (except for `ml_inf`) instances using PyTorch framework, provide the data type (dtype) of the model's input. `"float32"` is used if `"DTYPE"` is not specified. Options for data type are:
  + float32: Use either `"float"` or `"float32"`.
  + int64: Use either `"int64"` or `"long"`.

   For example, `{"dtype" : "float32"}`.
+  `CPU`: Compilation for CPU supports the following compiler options.
  +  `mcpu`: CPU micro-architecture. For example, `{'mcpu': 'skylake-avx512'}`
  +  `mattr`: CPU flags. For example, `{'mattr': ['+neon', '+vfpv4']}`
+  `ARM`: Details of ARM CPU compilations.
  +  `NEON`: NEON is an implementation of the Advanced SIMD extension used in ARMv7 processors.

    For example, add `{'mattr': ['+neon']}` to the compiler options if compiling for ARM 32-bit platform with the NEON support.
+  `NVIDIA`: Compilation for NVIDIA GPU supports the following compiler options.
  +  `gpu_code`: Specifies the targeted architecture.
  +  `trt-ver`: Specifies the TensorRT versions in x.y.z. format.
  +  `cuda-ver`: Specifies the CUDA version in x.y format.

  For example, `{'gpu-code': 'sm_72', 'trt-ver': '6.0.1', 'cuda-ver': '10.1'}`
+  `ANDROID`: Compilation for the Android OS supports the following compiler options:
  +  `ANDROID_PLATFORM`: Specifies the Android API levels. Available levels range from 21 to 29. For example, `{'ANDROID_PLATFORM': 28}`.
  +  `mattr`: Add `{'mattr': ['+neon']}` to compiler options if compiling for ARM 32-bit platform with NEON support.
+  `INFERENTIA`: Compilation for target ml\_inf1 uses compiler options passed in as a JSON string. For example, `"CompilerOptions": "\"--verbose 1 --num-neuroncores 2 -O2\""`.

  For information about supported compiler options, see [ Neuron Compiler CLI Reference Guide](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/compiler/neuronx-cc/api-reference-guide/neuron-compiler-cli-reference-guide.html).
+  `CoreML`: Compilation for the CoreML [OutputConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_OutputConfig.html) `TargetDevice` supports the following compiler options:
  +  `class_labels`: Specifies the classification labels file name inside input tar.gz file. For example, `{"class_labels": "imagenet_labels_1000.txt"}`. Labels inside the txt file should be separated by newlines.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 1024.
Pattern: `.*`
Required: No

 ** KmsKeyId **   <a name="sagemaker-Type-OutputConfig-KmsKeyId"></a>
The AWS Key Management Service key (AWS KMS) that Amazon SageMaker AI uses to encrypt your output models with Amazon S3 server-side encryption after compilation job. If you don't provide a KMS key ID, Amazon SageMaker AI uses the default KMS key for Amazon S3 for your role's account. For more information, see [KMS-Managed Encryption Keys](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingKMSEncryption.html) in the *Amazon Simple Storage Service Developer Guide.*
The KmsKeyId can be any of the following formats:
+ Key ID: `1234abcd-12ab-34cd-56ef-1234567890ab`
+ Key ARN: `arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`
+ Alias name: `alias/ExampleAlias`
+ Alias name ARN: `arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias`
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[a-zA-Z0-9:/_-]*`
Required: No

 ** TargetDevice **   <a name="sagemaker-Type-OutputConfig-TargetDevice"></a>
Identifies the target device or the machine learning instance that you want to run your model on after the compilation has completed. Alternatively, you can specify OS, architecture, and accelerator using [TargetPlatform](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TargetPlatform.html) fields. It can be used instead of `TargetPlatform`.
Currently `ml_trn1` is available only in US East (N. Virginia) Region, and `ml_inf2` is available only in US East (Ohio) Region.
Type: String
Valid Values: `lambda | ml_m4 | ml_m5 | ml_m6g | ml_c4 | ml_c5 | ml_c6g | ml_p2 | ml_p3 | ml_g4dn | ml_inf1 | ml_inf2 | ml_trn1 | ml_eia2 | jetson_tx1 | jetson_tx2 | jetson_nano | jetson_xavier | rasp3b | rasp4b | imx8qm | deeplens | rk3399 | rk3288 | aisage | sbe_c | qcs605 | qcs603 | sitara_am57x | amba_cv2 | amba_cv22 | amba_cv25 | x86_win32 | x86_win64 | coreml | jacinto_tda4vm | imx8mplus`
Required: No

 ** TargetPlatform **   <a name="sagemaker-Type-OutputConfig-TargetPlatform"></a>
Contains information about a target platform that you want your model to run on, such as OS, architecture, and accelerators. It is an alternative of `TargetDevice`.
The following examples show how to configure the `TargetPlatform` and `CompilerOptions` JSON strings for popular target platforms:
+ Raspberry Pi 3 Model B\+

   `"TargetPlatform": {"Os": "LINUX", "Arch": "ARM_EABIHF"},`

   ` "CompilerOptions": {'mattr': ['+neon']}`
+ Jetson TX2

   `"TargetPlatform": {"Os": "LINUX", "Arch": "ARM64", "Accelerator": "NVIDIA"},`

   ` "CompilerOptions": {'gpu-code': 'sm_62', 'trt-ver': '6.0.1', 'cuda-ver': '10.0'}`
+ EC2 m5.2xlarge instance OS

   `"TargetPlatform": {"Os": "LINUX", "Arch": "X86_64", "Accelerator": "NVIDIA"},`

   ` "CompilerOptions": {'mcpu': 'skylake-avx512'}`
+ RK3399

   `"TargetPlatform": {"Os": "LINUX", "Arch": "ARM64", "Accelerator": "MALI"}`
+ ARMv7 phone (CPU)

   `"TargetPlatform": {"Os": "ANDROID", "Arch": "ARM_EABI"},`

   ` "CompilerOptions": {'ANDROID_PLATFORM': 25, 'mattr': ['+neon']}`
+ ARMv8 phone (CPU)

   `"TargetPlatform": {"Os": "ANDROID", "Arch": "ARM64"},`

   ` "CompilerOptions": {'ANDROID_PLATFORM': 29}`
Type: [TargetPlatform](API_TargetPlatform.md) object
Required: No

## See Also
<a name="API_OutputConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/OutputConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/OutputConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/OutputConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
