---
source_url: https://docs.aws.amazon.com/apigateway/latest/api/API_JwtConfigurationInput.html
---

# JwtConfigurationInput

The JWT configuration supplied for a JWT authorizer.

## Contents
<a name="API_JwtConfigurationInput_Contents"></a>

 ** defaultAlgorithms **   <a name="apigw-Type-JwtConfigurationInput-defaultAlgorithms"></a>
The signing algorithms that the authorizer accepts, applied to every issuer. Valid values are `RS256`, `RS384`, `RS512`, `ES256`, `ES384`, and `ES512`.
Type: Array of strings
Valid Values: `RS256 | RS384 | RS512 | ES256 | ES384 | ES512`
Required: Yes

 ** issuers **   <a name="apigw-Type-JwtConfigurationInput-issuers"></a>
The issuers that the authorizer trusts. Issuer URLs must be unique.
Type: Array of [JwtIssuerInput](API_JwtIssuerInput.md) objects
Required: Yes

## See Also
<a name="API_JwtConfigurationInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apigateway-2015-07-09/JwtConfigurationInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apigateway-2015-07-09/JwtConfigurationInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apigateway-2015-07-09/JwtConfigurationInput)
