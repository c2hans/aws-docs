---
source_url: https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_HttpGatewayRoutePrefixRewrite.html
---

# HttpGatewayRoutePrefixRewrite
<a name="API_HttpGatewayRoutePrefixRewrite"></a>

An object representing the beginning characters of the route to rewrite.

## Contents
<a name="API_HttpGatewayRoutePrefixRewrite_Contents"></a>

 ** defaultPrefix **   <a name="appmesh-Type-HttpGatewayRoutePrefixRewrite-defaultPrefix"></a>
The default prefix used to replace the incoming route prefix when rewritten.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** value **   <a name="appmesh-Type-HttpGatewayRoutePrefixRewrite-value"></a>
The value used to replace the incoming route prefix when rewritten.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

## See Also
<a name="API_HttpGatewayRoutePrefixRewrite_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/HttpGatewayRoutePrefixRewrite)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/HttpGatewayRoutePrefixRewrite)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/HttpGatewayRoutePrefixRewrite)
