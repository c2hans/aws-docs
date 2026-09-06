---
source_url: https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_ForceEndpointErrorConfiguration.html
---

# ForceEndpointErrorConfiguration
<a name="API_ForceEndpointErrorConfiguration"></a>

The failover settings for the endpoint.

## Contents
<a name="API_ForceEndpointErrorConfiguration_Contents"></a>

 ** EndpointErrorConditions **   <a name="mediapackage-Type-ForceEndpointErrorConfiguration-EndpointErrorConditions"></a>
The failover conditions for the endpoint. The options are:
+  `STALE_MANIFEST` - The manifest stalled and there are no new segments or parts.
+  `INCOMPLETE_MANIFEST` - There is a gap in the manifest.
+  `MISSING_DRM_KEY` - Key rotation is enabled but we're unable to fetch the key for the current key period.
+  `SLATE_INPUT` - The segments which contain slate content are considered to be missing content.
Type: Array of strings
Valid Values: `STALE_MANIFEST | INCOMPLETE_MANIFEST | MISSING_DRM_KEY | SLATE_INPUT`
Required: No

## See Also
<a name="API_ForceEndpointErrorConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediapackagev2-2022-12-25/ForceEndpointErrorConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediapackagev2-2022-12-25/ForceEndpointErrorConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediapackagev2-2022-12-25/ForceEndpointErrorConfiguration)
