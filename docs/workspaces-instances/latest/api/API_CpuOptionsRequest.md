---
source_url: https://docs.aws.amazon.com/workspaces-instances/latest/api/API_CpuOptionsRequest.html
---

# CpuOptionsRequest
<a name="API_CpuOptionsRequest"></a>

Configures CPU-specific settings for WorkSpace Instance.

## Contents
<a name="API_CpuOptionsRequest_Contents"></a>

 ** AmdSevSnp **   <a name="workspacesinstances-Type-CpuOptionsRequest-AmdSevSnp"></a>
AMD Secure Encrypted Virtualization configuration.
Type: String
Valid Values: `enabled | disabled`
Required: No

 ** CoreCount **   <a name="workspacesinstances-Type-CpuOptionsRequest-CoreCount"></a>
Number of CPU cores to allocate.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** NestedVirtualization **   <a name="workspacesinstances-Type-CpuOptionsRequest-NestedVirtualization"></a>
Specifies whether to enable or disable nested virtualization.
Type: String
Valid Values: `enabled | disabled`
Required: No

 ** ThreadsPerCore **   <a name="workspacesinstances-Type-CpuOptionsRequest-ThreadsPerCore"></a>
Number of threads per CPU core.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_CpuOptionsRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-instances-2022-07-26/CpuOptionsRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-instances-2022-07-26/CpuOptionsRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-instances-2022-07-26/CpuOptionsRequest)
