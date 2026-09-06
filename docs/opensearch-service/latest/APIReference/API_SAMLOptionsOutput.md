---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_SAMLOptionsOutput.html
---

# SAMLOptionsOutput
<a name="API_SAMLOptionsOutput"></a>

Describes the SAML application configured for the domain.

## Contents
<a name="API_SAMLOptionsOutput_Contents"></a>

 ** Enabled **   <a name="opensearchservice-Type-SAMLOptionsOutput-Enabled"></a>
True if SAML is enabled.
Type: Boolean
Required: No

 ** Idp **   <a name="opensearchservice-Type-SAMLOptionsOutput-Idp"></a>
Describes the SAML identity provider's information.
Type: [SAMLIdp](API_SAMLIdp.md) object
Required: No

 ** RolesKey **   <a name="opensearchservice-Type-SAMLOptionsOutput-RolesKey"></a>
The key used for matching the SAML roles attribute.
Type: String
Required: No

 ** SessionTimeoutMinutes **   <a name="opensearchservice-Type-SAMLOptionsOutput-SessionTimeoutMinutes"></a>
The duration, in minutes, after which a user session becomes inactive.
Type: Integer
Required: No

 ** SubjectKey **   <a name="opensearchservice-Type-SAMLOptionsOutput-SubjectKey"></a>
The key used for matching the SAML subject attribute.
Type: String
Required: No

## See Also
<a name="API_SAMLOptionsOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/SAMLOptionsOutput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/SAMLOptionsOutput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/SAMLOptionsOutput)
