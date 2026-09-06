---
source_url: https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_ConnectionApiKeyAuthResponseParameters.html
---

# ConnectionApiKeyAuthResponseParameters
<a name="API_ConnectionApiKeyAuthResponseParameters"></a>

Contains the authorization parameters for the connection if API Key is specified as the authorization type.

## Contents
<a name="API_ConnectionApiKeyAuthResponseParameters_Contents"></a>

 ** ApiKeyName **   <a name="eventbridge-Type-ConnectionApiKeyAuthResponseParameters-ApiKeyName"></a>
The name of the header to use for the `APIKeyValue` used for authorization.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^[ \t]*[^\x00-\x1F:\x7F]+([ \t]+[^\x00-\x1F:\x7F]+)*[ \t]*$`
Required: No

## See Also
<a name="API_ConnectionApiKeyAuthResponseParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridge-2015-10-07/ConnectionApiKeyAuthResponseParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridge-2015-10-07/ConnectionApiKeyAuthResponseParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridge-2015-10-07/ConnectionApiKeyAuthResponseParameters)
