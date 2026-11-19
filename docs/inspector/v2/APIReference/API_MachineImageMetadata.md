---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_MachineImageMetadata.html
---

# MachineImageMetadata

Contains metadata about a machine image associated with a covered resource.

## Contents
<a name="API_MachineImageMetadata_Contents"></a>

 ** platform **   <a name="inspector2-Type-MachineImageMetadata-platform"></a>
The platform of the machine image.
Type: String
Valid Values: `WINDOWS | LINUX | UNKNOWN`
Required: No

 ** tags **   <a name="inspector2-Type-MachineImageMetadata-tags"></a>
The tags associated with the machine image.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## See Also
<a name="API_MachineImageMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/MachineImageMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/MachineImageMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/MachineImageMetadata)
