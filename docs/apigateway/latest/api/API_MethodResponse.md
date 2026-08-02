---
source_url: https://docs.aws.amazon.com/apigateway/latest/api/API_MethodResponse.html
---

# MethodResponse
<a name="API_MethodResponse"></a>

Represents a method response of a given HTTP status code returned to the client. The method response is passed from the back end through the associated integration response that can be transformed using a mapping template.

## Contents
<a name="API_MethodResponse_Contents"></a>

 ** responseModels **   <a name="apigw-Type-MethodResponse-responseModels"></a>
Specifies the Model resources used for the response's content-type. Response models are represented as a key/value map, with a content-type as the key and a Model name as the value.
Type: String to string map
Required: No

 ** responseParameters **   <a name="apigw-Type-MethodResponse-responseParameters"></a>
A key-value map specifying required or optional response parameters that API Gateway can send back to the caller. A key defines a method response header and the value specifies whether the associated method response header is required or not. The expression of the key must match the pattern `method.response.header.{name}`, where `name` is a valid and unique header name. API Gateway passes certain integration response data to the method response headers specified here according to the mapping you prescribe in the API's IntegrationResponse. The integration response data that can be mapped include an integration response header expressed in `integration.response.header.{name}`, a static value enclosed within a pair of single quotes (e.g., `'application/json'`), or a JSON expression from the back-end response payload in the form of `integration.response.body.{JSON-expression}`, where `JSON-expression` is a valid JSON expression without the `$` prefix.)
Type: String to boolean map
Required: No

 ** statusCode **   <a name="apigw-Type-MethodResponse-statusCode"></a>
The method response's status code.
Type: String
Pattern: `[1-5]\d\d`
Required: No

## See Also
<a name="API_MethodResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apigateway-2015-07-09/MethodResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apigateway-2015-07-09/MethodResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apigateway-2015-07-09/MethodResponse)
