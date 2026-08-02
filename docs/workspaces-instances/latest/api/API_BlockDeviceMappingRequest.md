---
source_url: https://docs.aws.amazon.com/workspaces-instances/latest/api/API_BlockDeviceMappingRequest.html
---

# BlockDeviceMappingRequest
<a name="API_BlockDeviceMappingRequest"></a>

Defines device mapping for WorkSpace Instance storage.

## Contents
<a name="API_BlockDeviceMappingRequest_Contents"></a>

 ** DeviceName **   <a name="workspacesinstances-Type-BlockDeviceMappingRequest-DeviceName"></a>
Name of the device for storage mapping.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 32.
Required: No

 ** Ebs **   <a name="workspacesinstances-Type-BlockDeviceMappingRequest-Ebs"></a>
EBS volume configuration for the device.
Type: [EbsBlockDevice](API_EbsBlockDevice.md) object
Required: No

 ** NoDevice **   <a name="workspacesinstances-Type-BlockDeviceMappingRequest-NoDevice"></a>
Indicates device should not be mapped.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 32.
Required: No

 ** VirtualName **   <a name="workspacesinstances-Type-BlockDeviceMappingRequest-VirtualName"></a>
Virtual device name for ephemeral storage.
Type: String
Pattern: `ephemeral(0|[1-9][0-9]{0,2})`
Required: No

## See Also
<a name="API_BlockDeviceMappingRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-instances-2022-07-26/BlockDeviceMappingRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-instances-2022-07-26/BlockDeviceMappingRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-instances-2022-07-26/BlockDeviceMappingRequest)
