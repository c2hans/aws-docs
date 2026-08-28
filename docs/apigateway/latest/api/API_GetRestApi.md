---
source_url: https://docs.aws.amazon.com/apigateway/latest/api/API_GetRestApi.html
---

# GetRestApi
<a name="API_GetRestApi"></a>

Lists the RestApi resource in the collection.

## Request Syntax
<a name="API_GetRestApi_RequestSyntax"></a>

```
GET /restapis/{{restapi_id}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetRestApi_RequestParameters"></a>

The request uses the following URI parameters.

 ** [restapi\_id](#API_GetRestApi_RequestSyntax) **   <a name="apigw-GetRestApi-request-uri-restApiId"></a>
The string identifier of the associated RestApi.
Required: Yes

## Request Body
<a name="API_GetRestApi_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetRestApi_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "apiKeySource": "string",
   "apiStatus": "string",
   "apiStatusMessage": "string",
   "binaryMediaTypes": [ "string" ],
   "createdDate": number,
   "description": "string",
   "disableExecuteApiEndpoint": boolean,
   "endpointAccessMode": "string",
   "endpointConfiguration": {
      "ipAddressType": "string",
      "types": [ "string" ],
      "vpcEndpointIds": [ "string" ]
   },
   "id": "string",
   "minimumCompressionSize": number,
   "name": "string",
   "policy": "string",
   "rootResourceId": "string",
   "securityPolicy": "string",
   "tags": {
      "string" : "string"
   },
   "version": "string",
   "warnings": [ "string" ]
}
```

## Response Elements
<a name="API_GetRestApi_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [apiKeySource](#API_GetRestApi_ResponseSyntax) **   <a name="apigw-GetRestApi-response-apiKeySource"></a>
The source of the API key for metering requests according to a usage plan. Valid values are: >`HEADER` to read the API key from the `X-API-Key` header of a request. `AUTHORIZER` to read the API key from the `UsageIdentifierKey` from a custom authorizer.
Type: String
Valid Values: `HEADER | AUTHORIZER`

 ** [apiStatus](#API_GetRestApi_ResponseSyntax) **   <a name="apigw-GetRestApi-response-apiStatus"></a>
The ApiStatus of the RestApi.
Type: String
Valid Values: `UPDATING | AVAILABLE | PENDING | FAILED`

 ** [apiStatusMessage](#API_GetRestApi_ResponseSyntax) **   <a name="apigw-GetRestApi-response-apiStatusMessage"></a>
 The status message of the RestApi. When the status message is `UPDATING` you can still invoke it.
Type: String

 ** [binaryMediaTypes](#API_GetRestApi_ResponseSyntax) **   <a name="apigw-GetRestApi-response-binaryMediaTypes"></a>
The list of binary media types supported by the RestApi. By default, the RestApi supports only UTF-8-encoded text payloads.
Type: Array of strings

 ** [createdDate](#API_GetRestApi_ResponseSyntax) **   <a name="apigw-GetRestApi-response-createdDate"></a>
The timestamp when the API was created.
Type: Timestamp

 ** [description](#API_GetRestApi_ResponseSyntax) **   <a name="apigw-GetRestApi-response-description"></a>
The API's description.
Type: String

 ** [disableExecuteApiEndpoint](#API_GetRestApi_ResponseSyntax) **   <a name="apigw-GetRestApi-response-disableExecuteApiEndpoint"></a>
Specifies whether clients can invoke your API by using the default `execute-api` endpoint. By default, clients can invoke your API with the default `https://{api_id}.execute-api.{region}.amazonaws.com` endpoint. To require that clients use a custom domain name to invoke your API, disable the default endpoint.
Type: Boolean

 ** [endpointAccessMode](#API_GetRestApi_ResponseSyntax) **   <a name="apigw-GetRestApi-response-endpointAccessMode"></a>
 The endpoint access mode of the RestApi.
Type: String
Valid Values: `BASIC | STRICT`

 ** [endpointConfiguration](#API_GetRestApi_ResponseSyntax) **   <a name="apigw-GetRestApi-response-endpointConfiguration"></a>
The endpoint configuration of this RestApi showing the endpoint types and IP address types of the API.
Type: [EndpointConfiguration](API_EndpointConfiguration.md) object

 ** [id](#API_GetRestApi_ResponseSyntax) **   <a name="apigw-GetRestApi-response-id"></a>
The API's identifier. This identifier is unique across all of your APIs in API Gateway.
Type: String

 ** [minimumCompressionSize](#API_GetRestApi_ResponseSyntax) **   <a name="apigw-GetRestApi-response-minimumCompressionSize"></a>
A nullable integer that is used to enable compression (with non-negative between 0 and 10485760 (10M) bytes, inclusive) or disable compression (with a null value) on an API. When compression is enabled, compression or decompression is not applied on the payload if the payload size is smaller than this value. Setting it to zero allows compression for any payload size.
Type: Integer

 ** [name](#API_GetRestApi_ResponseSyntax) **   <a name="apigw-GetRestApi-response-name"></a>
The API's name.
Type: String

 ** [policy](#API_GetRestApi_ResponseSyntax) **   <a name="apigw-GetRestApi-response-policy"></a>
A stringified JSON policy document that applies to this RestApi regardless of the caller and Method configuration.
Type: String

 ** [rootResourceId](#API_GetRestApi_ResponseSyntax) **   <a name="apigw-GetRestApi-response-rootResourceId"></a>
The API's root resource ID.
Type: String

 ** [securityPolicy](#API_GetRestApi_ResponseSyntax) **   <a name="apigw-GetRestApi-response-securityPolicy"></a>
 The Transport Layer Security (TLS) version \+ cipher suite for this RestApi.
Type: String
Valid Values: `TLS_1_0 | TLS_1_2 | SecurityPolicy_TLS13_1_3_2025_09 | SecurityPolicy_TLS13_1_3_FIPS_2025_09 | SecurityPolicy_TLS13_1_2_PFS_PQ_2025_09 | SecurityPolicy_TLS13_1_2_FIPS_PQ_2025_09 | SecurityPolicy_TLS13_1_2_PQ_2025_09 | SecurityPolicy_TLS13_1_2_2021_06 | SecurityPolicy_TLS13_2025_EDGE | SecurityPolicy_TLS12_PFS_2025_EDGE | SecurityPolicy_TLS12_2018_EDGE`

 ** [tags](#API_GetRestApi_ResponseSyntax) **   <a name="apigw-GetRestApi-response-tags"></a>
The collection of tags. Each tag element is associated with a given resource.
Type: String to string map

 ** [version](#API_GetRestApi_ResponseSyntax) **   <a name="apigw-GetRestApi-response-version"></a>
A version identifier for the API.
Type: String

 ** [warnings](#API_GetRestApi_ResponseSyntax) **   <a name="apigw-GetRestApi-response-warnings"></a>
The warning messages reported when `failonwarnings` is turned on during API import.
Type: Array of strings

## Errors
<a name="API_GetRestApi_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.
HTTP Status Code: 400

 ** NotFoundException **
The requested resource is not found. Make sure that the request URI is correct.
HTTP Status Code: 404

 ** TooManyRequestsException **
The request has reached its throttling limit. Retry after the specified time period.
HTTP Status Code: 429

 ** UnauthorizedException **
The request is denied because the caller has insufficient permissions.
HTTP Status Code: 401

## Examples
<a name="API_GetRestApi_Examples"></a>

### Retrieve information about a REST API
<a name="API_GetRestApi_Example_1"></a>

This example illustrates one usage of GetRestApi.

#### Sample Request
<a name="API_GetRestApi_Example_1_Request"></a>

```
GET /restapis/0n1anifwvf HTTP/1.1
Content-Type: application/json
Host: apigateway.us-east-1.amazonaws.com
X-Amz-Date: 20160601T182517Z
Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/20160601/us-east-1/apigateway/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature={sig4_hash}
```

#### Sample Response
<a name="API_GetRestApi_Example_1_Response"></a>

```
{
  "_links": {
    "curies": [
      {
        "href": "https://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-authorizer-{rel}.html",
        "name": "authorizer",
        "templated": true
      },
      {
        "href": "https://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-deployment-{rel}.html",
        "name": "deployment",
        "templated": true
      },
      {
        "href": "https://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-model-{rel}.html",
        "name": "model",
        "templated": true
      },
      {
        "href": "https://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-resource-{rel}.html",
        "name": "resource",
        "templated": true
      },
      {
        "href": "https://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-restapi-{rel}.html",
        "name": "restapi",
        "templated": true
      },
      {
        "href": "https://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-stage-{rel}.html",
        "name": "stage",
        "templated": true
      }
    ],
    "self": {
      "href": "/restapis/0n1anifwvf"
    },
    "authorizer:by-id": {
      "href": "/restapis/0n1anifwvf/authorizers/{authorizer_id}",
      "templated": true
    },
    "authorizer:create": {
      "href": "/restapis/0n1anifwvf/authorizers"
    },
    "deployment:by-id": {
      "href": "/restapis/0n1anifwvf/deployments/{deployment_id}{?embed}",
      "templated": true
    },
    "deployment:create": {
      "href": "/restapis/0n1anifwvf/deployments"
    },
    "model:by-name": {
      "href": "/restapis/0n1anifwvf/models/{model_name}?flatten=false",
      "templated": true
    },
    "model:create": {
      "href": "/restapis/0n1anifwvf/models"
    },
    "resource:by-id": {
      "href": "/restapis/0n1anifwvf/resources/{resource_id}{?embed}",
      "templated": true
    },
    "resource:create": {
      "href": "/restapis/0n1anifwvf/resources/ny9qrywoj2"
    },
    "restapi:authorizers": {
      "href": "/restapis/0n1anifwvf/authorizers"
    },
    "restapi:delete": {
      "href": "/restapis/0n1anifwvf"
    },
    "restapi:deployments": {
      "href": "/restapis/0n1anifwvf/deployments{?limit}",
      "templated": true
    },
    "restapi:models": {
      "href": "/restapis/0n1anifwvf/models"
    },
    "restapi:resources": {
      "href": "/restapis/0n1anifwvf/resources{?limit,embed}",
      "templated": true
    },
    "restapi:stages": {
      "href": "/restapis/0n1anifwvf/stages{?deployment_id}",
      "templated": true
    },
    "restapi:update": {
      "href": "/restapis/0n1anifwvf"
    },
    "stage:by-name": {
      "href": "/restapis/0n1anifwvf/stages/{stage_name}",
      "templated": true
    },
    "stage:create": {
      "href": "/restapis/0n1anifwvf/stages"
    }
  },
  "createdDate": "2016-04-05T19:58:27Z",
  "description": "Your first API with Amazon API Gateway. This is a sample API that integrates via HTTP with our demo Pet Store endpoints",
  "id": "0n1anifwvf",
  "rootResourceId" : "1abcd23e4f",
  "name": "PetStore"
}
```

## See Also
<a name="API_GetRestApi_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/apigateway-2015-07-09/GetRestApi)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/apigateway-2015-07-09/GetRestApi)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apigateway-2015-07-09/GetRestApi)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/apigateway-2015-07-09/GetRestApi)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apigateway-2015-07-09/GetRestApi)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/apigateway-2015-07-09/GetRestApi)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/apigateway-2015-07-09/GetRestApi)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/apigateway-2015-07-09/GetRestApi)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/apigateway-2015-07-09/GetRestApi)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apigateway-2015-07-09/GetRestApi)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon API Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apigateway` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
