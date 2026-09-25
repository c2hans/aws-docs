---
source_url: https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_IntegrationCredential.html
---

# IntegrationCredential
<a name="API_IntegrationCredential"></a>

The credential that an integration uses to authenticate with its external system. Exactly one member is set, matching the integration's authentication type.

## Contents
<a name="API_IntegrationCredential_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** apiKeyCredential **   <a name="cloudwatchomni-Type-IntegrationCredential-apiKeyCredential"></a>
An API key credential.
Type: [ApiKeyCredential](API_ApiKeyCredential.md) object
Required: No

 ** oauthClientCredential **   <a name="cloudwatchomni-Type-IntegrationCredential-oauthClientCredential"></a>
Credentials for an OAuth 2.0 client-credentials grant.
Type: [OAuthClientCredential](API_OAuthClientCredential.md) object
Required: No

 ** oauthCodeCredential **   <a name="cloudwatchomni-Type-IntegrationCredential-oauthCodeCredential"></a>
Credentials for an OAuth 2.0 authorization-code grant.
Type: [OAuthCodeCredential](API_OAuthCodeCredential.md) object
Required: No

## See Also
<a name="API_IntegrationCredential_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudwatchomni-2025-01-01/IntegrationCredential)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudwatchomni-2025-01-01/IntegrationCredential)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudwatchomni-2025-01-01/IntegrationCredential)
