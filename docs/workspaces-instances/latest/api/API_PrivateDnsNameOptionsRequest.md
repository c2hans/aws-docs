---
source_url: https://docs.aws.amazon.com/workspaces-instances/latest/api/API_PrivateDnsNameOptionsRequest.html
---

# PrivateDnsNameOptionsRequest
<a name="API_PrivateDnsNameOptionsRequest"></a>

Configures private DNS name settings for WorkSpace Instance.

## Contents
<a name="API_PrivateDnsNameOptionsRequest_Contents"></a>

 ** EnableResourceNameDnsAAAARecord **   <a name="workspacesinstances-Type-PrivateDnsNameOptionsRequest-EnableResourceNameDnsAAAARecord"></a>
Enables DNS AAAA record for resource name resolution.
Type: Boolean
Required: No

 ** EnableResourceNameDnsARecord **   <a name="workspacesinstances-Type-PrivateDnsNameOptionsRequest-EnableResourceNameDnsARecord"></a>
Enables DNS A record for resource name resolution.
Type: Boolean
Required: No

 ** HostnameType **   <a name="workspacesinstances-Type-PrivateDnsNameOptionsRequest-HostnameType"></a>
Specifies the type of hostname configuration.
Type: String
Valid Values: `ip-name | resource-name`
Required: No

## See Also
<a name="API_PrivateDnsNameOptionsRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-instances-2022-07-26/PrivateDnsNameOptionsRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-instances-2022-07-26/PrivateDnsNameOptionsRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-instances-2022-07-26/PrivateDnsNameOptionsRequest)
