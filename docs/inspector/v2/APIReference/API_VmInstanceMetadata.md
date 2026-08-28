---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_VmInstanceMetadata.html
---

# VmInstanceMetadata
<a name="API_VmInstanceMetadata"></a>

Contains metadata about a virtual machine (VM) instance associated with a covered resource.

## Contents
<a name="API_VmInstanceMetadata_Contents"></a>

 ** inventoryHash **   <a name="inspector2-Type-VmInstanceMetadata-inventoryHash"></a>
The inventory hash of the VM instance.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** platform **   <a name="inspector2-Type-VmInstanceMetadata-platform"></a>
The platform of the VM instance.
Type: String
Valid Values: `WINDOWS | LINUX | UNKNOWN`
Required: No

 ** tags **   <a name="inspector2-Type-VmInstanceMetadata-tags"></a>
The tags associated with the VM instance.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** vmImageReference **   <a name="inspector2-Type-VmInstanceMetadata-vmImageReference"></a>
The image reference of the VM instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## See Also
<a name="API_VmInstanceMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/VmInstanceMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/VmInstanceMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/VmInstanceMetadata)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
