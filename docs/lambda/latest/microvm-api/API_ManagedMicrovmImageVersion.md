---
source_url: https://docs.aws.amazon.com/lambda/latest/microvm-api/API_ManagedMicrovmImageVersion.html
---

# ManagedMicrovmImageVersion
<a name="API_ManagedMicrovmImageVersion"></a>

Contains version information for a managed MicroVM image.

## Contents
<a name="API_ManagedMicrovmImageVersion_Contents"></a>

 ** createdAt **   <a name="lambdamicrovm-Type-ManagedMicrovmImageVersion-createdAt"></a>
The timestamp when the version was created.
Type: Timestamp
Required: Yes

 ** imageArn **   <a name="lambdamicrovm-Type-ManagedMicrovmImageVersion-imageArn"></a>
The ARN of the managed MicroVM image.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\s]+`
Required: Yes

 ** imageVersion **   <a name="lambdamicrovm-Type-ManagedMicrovmImageVersion-imageVersion"></a>
The version of the managed MicroVM image.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\s]+`
Required: Yes

 ** status **   <a name="lambdamicrovm-Type-ManagedMicrovmImageVersion-status"></a>
The lifecycle status of the managed MicroVM image version. Valid values: AVAILABLE (the version is available for use) or DEPRECATED (the version is deprecated; do not use it for new MicroVM images).
Type: String
Valid Values: `AVAILABLE | DEPRECATED | RECALLED`
Required: No

 ** supportedCpuConfigurations **   <a name="lambdamicrovm-Type-ManagedMicrovmImageVersion-supportedCpuConfigurations"></a>
The CPU configurations supported by this managed base image version. You can build a MicroVM image for an architecture only on a base image version that lists that architecture.
Type: Array of [CpuConfiguration](API_CpuConfiguration.md) objects
Required: No

 ** updatedAt **   <a name="lambdamicrovm-Type-ManagedMicrovmImageVersion-updatedAt"></a>
The timestamp when the version was last updated.
Type: Timestamp
Required: No

## See Also
<a name="API_ManagedMicrovmImageVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-microvms-2025-09-09/ManagedMicrovmImageVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-microvms-2025-09-09/ManagedMicrovmImageVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-microvms-2025-09-09/ManagedMicrovmImageVersion)
