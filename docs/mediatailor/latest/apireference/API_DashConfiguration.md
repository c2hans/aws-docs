---
source_url: https://docs.aws.amazon.com/mediatailor/latest/apireference/API_DashConfiguration.html
---

# DashConfiguration
<a name="API_DashConfiguration"></a>

The configuration for DASH content.

## Contents
<a name="API_DashConfiguration_Contents"></a>

 ** DualStackManifestEndpointPrefix **   <a name="mediatailor-Type-DashConfiguration-DualStackManifestEndpointPrefix"></a>
The dual-stack (IPv4 and IPv6) URL that MediaTailor generates to initiate a playback session. The session uses server-side reporting.
Type: String
Required: No

 ** ManifestEndpointPrefix **   <a name="mediatailor-Type-DashConfiguration-ManifestEndpointPrefix"></a>
The URL that MediaTailor generates to initiate a playback session. The session uses server-side reporting.
Type: String
Required: No

 ** MpdLocation **   <a name="mediatailor-Type-DashConfiguration-MpdLocation"></a>
The setting that controls whether MediaTailor includes the Location tag in DASH manifests. MediaTailor populates the Location tag with the URL for manifest update requests, to be used by players that don't support sticky redirects. Disable this if you have CDN routing rules set up for accessing MediaTailor manifests, and you are either using client-side reporting or your players support sticky HTTP redirects. Valid values are `DISABLED` and `EMT_DEFAULT`. The `EMT_DEFAULT` setting enables the inclusion of the tag and is the default value.
Type: String
Required: No

 ** OriginManifestType **   <a name="mediatailor-Type-DashConfiguration-OriginManifestType"></a>
The setting that controls whether MediaTailor handles manifests from the origin server as multi-period manifests or single-period manifests. If your origin server produces single-period manifests, set this to `SINGLE_PERIOD`. The default setting is `MULTI_PERIOD`. For multi-period manifests, omit this setting or set it to `MULTI_PERIOD`.
Type: String
Valid Values: `SINGLE_PERIOD | MULTI_PERIOD`
Required: No

## See Also
<a name="API_DashConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediatailor-2018-04-23/DashConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediatailor-2018-04-23/DashConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediatailor-2018-04-23/DashConfiguration)
