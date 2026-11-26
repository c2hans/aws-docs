---
source_url: https://docs.aws.amazon.com/apigateway/latest/api/API_JwtConfiguration.html
---

# JwtConfiguration

The JWT configuration returned for a JWT authorizer.

## Contents
<a name="API_JwtConfiguration_Contents"></a>

 ** defaultAlgorithms **   <a name="apigw-Type-JwtConfiguration-defaultAlgorithms"></a>
The signing algorithms configured for the authorizer.
Type: Array of strings
Valid Values: `RS256 | RS384 | RS512 | ES256 | ES384 | ES512`
Required: No

 ** issuers **   <a name="apigw-Type-JwtConfiguration-issuers"></a>
The trusted issuers configured for the authorizer.
Type: Array of [JwtIssuer](API_JwtIssuer.md) objects
Required: No

## See Also
<a name="API_JwtConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apigateway-2015-07-09/JwtConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apigateway-2015-07-09/JwtConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apigateway-2015-07-09/JwtConfiguration)
