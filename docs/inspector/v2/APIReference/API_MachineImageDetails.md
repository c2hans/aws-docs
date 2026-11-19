---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_MachineImageDetails.html
---

# MachineImageDetails

Contains details about an Amazon Machine Image (AMI) that Amazon Inspector scanned directly.

## Contents
<a name="API_MachineImageDetails_Contents"></a>

 ** machineImageId **   <a name="inspector2-Type-MachineImageDetails-machineImageId"></a>
The ID of the machine image, for example `ami-0abcdef1234567890`.
Type: String
Length Constraints: Minimum length of 1.
Pattern: `ami-[0-9a-f]{8,17}`
Required: Yes

 ** architecture **   <a name="inspector2-Type-MachineImageDetails-architecture"></a>
The CPU architecture of the machine image, for example `x86_64` or `arm64`.
Type: String
Valid Values: `X86_64 | ARM64`
Required: No

 ** creationDate **   <a name="inspector2-Type-MachineImageDetails-creationDate"></a>
The date and time that the machine image was created.
Type: Timestamp
Required: No

 ** isPublic **   <a name="inspector2-Type-MachineImageDetails-isPublic"></a>
Indicates whether the machine image is shared publicly.
Type: Boolean
Required: No

 ** name **   <a name="inspector2-Type-MachineImageDetails-name"></a>
The name of the machine image.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** ownerAccountId **   <a name="inspector2-Type-MachineImageDetails-ownerAccountId"></a>
The ID of the account that owns the machine image.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 36.
Pattern: `(\d{12}|[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}|[a-z][a-z0-9-]{4,28}[a-z0-9])`
Required: No

 ** platform **   <a name="inspector2-Type-MachineImageDetails-platform"></a>
The operating system platform of the machine image.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** rootDeviceType **   <a name="inspector2-Type-MachineImageDetails-rootDeviceType"></a>
The root device type of the machine image, either `ebs` or `instance-store`.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** sourceResourceId **   <a name="inspector2-Type-MachineImageDetails-sourceResourceId"></a>
The ID of the Amazon EC2 instance that the machine image was created from, if available.
Type: String
Length Constraints: Minimum length of 1.
Pattern: `i-[0-9a-f]{8,17}`
Required: No

 ** state **   <a name="inspector2-Type-MachineImageDetails-state"></a>
The state of the machine image, for example `available`, `pending`, or `deregistered`.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** virtualizationType **   <a name="inspector2-Type-MachineImageDetails-virtualizationType"></a>
The virtualization type of the machine image, either `hvm` or `paravirtual`.
Type: String
Length Constraints: Minimum length of 1.
Required: No

## See Also
<a name="API_MachineImageDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/MachineImageDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/MachineImageDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/MachineImageDetails)
