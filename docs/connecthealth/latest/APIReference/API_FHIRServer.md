---
source_url: https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_FHIRServer.html
---

# FHIRServer
<a name="API_FHIRServer"></a>

FHIR server configuration for input data source

## Contents
<a name="API_FHIRServer_Contents"></a>

 ** fhirEndpoint **   <a name="connecthealth-Type-FHIRServer-fhirEndpoint"></a>
FHIR server endpoint URL for accessing patient data.
Type: String
Pattern: `https?://[a-zA-Z0-9\-._~:/?#\[\]@!$&'()*+,;=%]+`
Required: Yes

 ** oauthToken **   <a name="connecthealth-Type-FHIRServer-oauthToken"></a>
OAuth token for authenticating with the FHIR server.
Type: String
Pattern: `.*[\s\S]*\S[\s\S]*.*`
Required: No

## See Also
<a name="API_FHIRServer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connecthealth-2025-01-29/FHIRServer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connecthealth-2025-01-29/FHIRServer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connecthealth-2025-01-29/FHIRServer)
