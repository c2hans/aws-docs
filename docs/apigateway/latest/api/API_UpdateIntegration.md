---
source_url: https://docs.aws.amazon.com/apigateway/latest/api/API_UpdateIntegration.html
---

# UpdateIntegration
<a name="API_UpdateIntegration"></a>

Represents an update integration.

## Request Syntax
<a name="API_UpdateIntegration_RequestSyntax"></a>

```
PATCH /restapis/{{restapi_id}}/resources/{{resource_id}}/methods/{{http_method}}/integration HTTP/1.1
Content-type: application/json

{
   "patchOperations": [
      {
         "from": "{{string}}",
         "op": "{{string}}",
         "path": "{{string}}",
         "value": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_UpdateIntegration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [http\_method](#API_UpdateIntegration_RequestSyntax) **   <a name="apigw-UpdateIntegration-request-uri-httpMethod"></a>
Represents an update integration request's HTTP method.
Required: Yes

 ** [resource\_id](#API_UpdateIntegration_RequestSyntax) **   <a name="apigw-UpdateIntegration-request-uri-resourceId"></a>
Represents an update integration request's resource identifier.
Required: Yes

 ** [restapi\_id](#API_UpdateIntegration_RequestSyntax) **   <a name="apigw-UpdateIntegration-request-uri-restApiId"></a>
The string identifier of the associated RestApi.
Required: Yes

## Request Body
<a name="API_UpdateIntegration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [patchOperations](#API_UpdateIntegration_RequestSyntax) **   <a name="apigw-UpdateIntegration-request-patchOperations"></a>
For more information about supported patch operations, see [Patch Operations](patch-operations.md).
Type: Array of [PatchOperation](API_PatchOperation.md) objects
Required: No

## Response Syntax
<a name="API_UpdateIntegration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "cacheKeyParameters": [ "string" ],
   "cacheNamespace": "string",
   "connectionId": "string",
   "connectionType": "string",
   "contentHandling": "string",
   "credentials": "string",
   "httpMethod": "string",
   "integrationResponses": {
      "string" : {
         "contentHandling": "string",
         "responseParameters": {
            "string" : "string"
         },
         "responseTemplates": {
            "string" : "string"
         },
         "selectionPattern": "string",
         "statusCode": "string"
      }
   },
   "integrationTarget": "string",
   "passthroughBehavior": "string",
   "requestParameters": {
      "string" : "string"
   },
   "requestTemplates": {
      "string" : "string"
   },
   "responseTransferMode": "string",
   "timeoutInMillis": number,
   "tlsConfig": {
      "insecureSkipVerification": boolean
   },
   "type": "string",
   "uri": "string"
}
```

## Response Elements
<a name="API_UpdateIntegration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [cacheKeyParameters](#API_UpdateIntegration_ResponseSyntax) **   <a name="apigw-UpdateIntegration-response-cacheKeyParameters"></a>
A list of request parameters whose values API Gateway caches. To be valid values for `cacheKeyParameters`, these parameters must also be specified for Method `requestParameters`.
Type: Array of strings

 ** [cacheNamespace](#API_UpdateIntegration_ResponseSyntax) **   <a name="apigw-UpdateIntegration-response-cacheNamespace"></a>
Specifies a group of related cached parameters. By default, API Gateway uses the resource ID as the `cacheNamespace`. You can specify the same `cacheNamespace` across resources to return the same cached data for requests to different resources.
Type: String

 ** [connectionId](#API_UpdateIntegration_ResponseSyntax) **   <a name="apigw-UpdateIntegration-response-connectionId"></a>
The ID of the VpcLink used for the integration when `connectionType=VPC_LINK` and undefined, otherwise.
Type: String

 ** [connectionType](#API_UpdateIntegration_ResponseSyntax) **   <a name="apigw-UpdateIntegration-response-connectionType"></a>
The type of the network connection to the integration endpoint. The valid value is `INTERNET` for connections through the public routable internet or `VPC_LINK` for private connections between API Gateway and a network load balancer in a VPC. The default value is `INTERNET`.
Type: String
Valid Values: `INTERNET | VPC_LINK`

 ** [contentHandling](#API_UpdateIntegration_ResponseSyntax) **   <a name="apigw-UpdateIntegration-response-contentHandling"></a>
Specifies how to handle request payload content type conversions. Supported values are `CONVERT_TO_BINARY` and `CONVERT_TO_TEXT`, with the following behaviors:
If this property is not defined, the request payload will be passed through from the method request to integration request without modification, provided that the `passthroughBehavior` is configured to support payload pass-through.
Type: String
Valid Values: `CONVERT_TO_BINARY | CONVERT_TO_TEXT`

 ** [credentials](#API_UpdateIntegration_ResponseSyntax) **   <a name="apigw-UpdateIntegration-response-credentials"></a>
Specifies the credentials required for the integration, if any. For AWS integrations, three options are available. To specify an IAM Role for API Gateway to assume, use the role's Amazon Resource Name (ARN). To require that the caller's identity be passed through from the request, specify the string `arn:aws:iam::\*:user/\*`. To use resource-based permissions on supported AWS services, specify null.
Type: String

 ** [httpMethod](#API_UpdateIntegration_ResponseSyntax) **   <a name="apigw-UpdateIntegration-response-httpMethod"></a>
Specifies the integration's HTTP method type. For the Type property, if you specify `MOCK`, this property is optional. For Lambda integrations, you must set the integration method to `POST`. For all other types, you must specify this property.
Type: String

 ** [integrationResponses](#API_UpdateIntegration_ResponseSyntax) **   <a name="apigw-UpdateIntegration-response-integrationResponses"></a>
Specifies the integration's responses.
Type: String to [IntegrationResponse](API_IntegrationResponse.md) object map

 ** [integrationTarget](#API_UpdateIntegration_ResponseSyntax) **   <a name="apigw-UpdateIntegration-response-integrationTarget"></a>
 The ALB or NLB listener to send the request to.
Type: String

 ** [passthroughBehavior](#API_UpdateIntegration_ResponseSyntax) **   <a name="apigw-UpdateIntegration-response-passthroughBehavior"></a>
Specifies how the method request body of an unmapped content type will be passed through the integration request to the back end without transformation. A content type is unmapped if no mapping template is defined in the integration or the content type does not match any of the mapped content types, as specified in `requestTemplates`. The valid value is one of the following: `WHEN_NO_MATCH`: passes the method request body through the integration request to the back end without transformation when the method request content type does not match any content type associated with the mapping templates defined in the integration request. `WHEN_NO_TEMPLATES`: passes the method request body through the integration request to the back end without transformation when no mapping template is defined in the integration request. If a template is defined when this option is selected, the method request of an unmapped content-type will be rejected with an HTTP 415 Unsupported Media Type response. `NEVER`: rejects the method request with an HTTP 415 Unsupported Media Type response when either the method request content type does not match any content type associated with the mapping templates defined in the integration request or no mapping template is defined in the integration request.
Type: String

 ** [requestParameters](#API_UpdateIntegration_ResponseSyntax) **   <a name="apigw-UpdateIntegration-response-requestParameters"></a>
A key-value map specifying request parameters that are passed from the method request to the back end. The key is an integration request parameter name and the associated value is a method request parameter value or static value that must be enclosed within single quotes and pre-encoded as required by the back end. The method request parameter value must match the pattern of `method.request.{location}.{name}`, where `location` is `querystring`, `path`, or `header` and `name` must be a valid and unique method request parameter name.
Type: String to string map

 ** [requestTemplates](#API_UpdateIntegration_ResponseSyntax) **   <a name="apigw-UpdateIntegration-response-requestTemplates"></a>
Represents a map of Velocity templates that are applied on the request payload based on the value of the Content-Type header sent by the client. The content type value is the key in this map, and the template (as a String) is the value.
Type: String to string map

 ** [responseTransferMode](#API_UpdateIntegration_ResponseSyntax) **   <a name="apigw-UpdateIntegration-response-responseTransferMode"></a>
 The response transfer mode of the integration.
Type: String
Valid Values: `BUFFERED | STREAM`

 ** [timeoutInMillis](#API_UpdateIntegration_ResponseSyntax) **   <a name="apigw-UpdateIntegration-response-timeoutInMillis"></a>
Custom timeout between 50 and 29,000 milliseconds. The default value is 29,000 milliseconds or 29 seconds. You can increase the default value to longer than 29 seconds for Regional or private APIs only.
Type: Integer

 ** [tlsConfig](#API_UpdateIntegration_ResponseSyntax) **   <a name="apigw-UpdateIntegration-response-tlsConfig"></a>
Specifies the TLS configuration for an integration.
Type: [TlsConfig](API_TlsConfig.md) object

 ** [type](#API_UpdateIntegration_ResponseSyntax) **   <a name="apigw-UpdateIntegration-response-type"></a>
Specifies an API method integration type. The valid value is one of the following:
For the HTTP and HTTP proxy integrations, each integration can specify a protocol (`http/https`), port and path. Standard 80 and 443 ports are supported as well as custom ports above 1024. An HTTP or HTTP proxy integration with a `connectionType` of `VPC_LINK` is referred to as a private integration and uses a VpcLink to connect API Gateway to a network load balancer of a VPC.
Type: String
Valid Values: `HTTP | AWS | MOCK | HTTP_PROXY | AWS_PROXY`

 ** [uri](#API_UpdateIntegration_ResponseSyntax) **   <a name="apigw-UpdateIntegration-response-uri"></a>
Specifies Uniform Resource Identifier (URI) of the integration endpoint.
For `HTTP` or `HTTP_PROXY` integrations, the URI must be a fully formed, encoded HTTP(S) URL according to the RFC-3986 specification for standard integrations. If `connectionType` is `VPC_LINK` specify the Network Load Balancer DNS name. For `AWS` or `AWS_PROXY` integrations, the URI is of the form `arn:aws:apigateway:{region}:{subdomain.service|service}:path|action/{service_api}`. Here, {Region} is the API Gateway region (e.g., us-east-1); {service} is the name of the integrated AWS service (e.g., s3); and {subdomain} is a designated subdomain supported by certain AWS service for fast host-name lookup. action can be used for an AWS service action-based API, using an Action={name}&{p1}={v1}&p2={v2}... query string. The ensuing {service\_api} refers to a supported action {name} plus any required input parameters. Alternatively, path can be used for an AWS service path-based API. The ensuing service\_api refers to the path to an AWS service resource, including the region of the integrated AWS service, if applicable. For example, for integration with the S3 API of GetObject, the uri can be either `arn:aws:apigateway:us-west-2:s3:action/GetObject&Bucket={bucket}&Key={key}` or `arn:aws:apigateway:us-west-2:s3:path/{bucket}/{key}`
Type: String

## Errors
<a name="API_UpdateIntegration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.
HTTP Status Code: 400

 ** ConflictException **
The request configuration has conflicts. For details, see the accompanying error message.
HTTP Status Code: 409

 ** LimitExceededException **
The request exceeded the rate limit. Retry after the specified time period.
HTTP Status Code: 429

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
<a name="API_UpdateIntegration_Examples"></a>

### Remove, add, and replace a request template
<a name="API_UpdateIntegration_Example_1"></a>

This example illustrates one usage of UpdateIntegration.

#### Sample Request
<a name="API_UpdateIntegration_Example_1_Request"></a>

```
PATCH /restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration HTTP/1.1
Content-Type: application/json
Host: apigateway.us-east-1.amazonaws.com
X-Amz-Date: 20160614T234104Z
Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/20160614/us-east-1/apigateway/aws4_request, SignedHeaders=content-length;content-type;host;x-amz-date, Signature={sig4_hash}

{
  "patchOperations" : [ {
    "op" : "remove",
    "path" : "/requestTemplates/application~1xml"
  },
  {
    "op" : "add",
    "path" : "/requestTemplates/application~1xml",
    "value" : "

    3
   "
  },
  {
    "op" : "replace",
    "path" : "/requestTemplates/application~1xml",
    "value" : "

    3
   "
  } ]
}
```

#### Sample Response
<a name="API_UpdateIntegration_Example_1_Response"></a>

```
{
  "_links": {
    "curies": [
      {
        "href": "https://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-integration-{rel}.html",
        "name": "integration",
        "templated": true
      },
      {
        "href": "https://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-integration-response-{rel}.html",
        "name": "integrationresponse",
        "templated": true
      }
    ],
    "self": {
      "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration"
    },
    "integration:delete": {
      "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration"
    },
    "integration:responses": {
      "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200",
      "name": "200",
      "title": "200"
    },
    "integration:update": {
      "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration"
    },
    "integrationresponse:put": {
      "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/{status_code}",
      "templated": true
    }
  },
  "cacheKeyParameters": [],
  "cacheNamespace": "3kzxbg5sa2",
  "credentials": "arn:aws:iam::123456789012:role/apigAwsProxyRole",
  "httpMethod": "POST",
  "passthroughBehavior": "WHEN_NO_MATCH",
  "requestParameters": {
    "integration.request.header.Content-Type": "'application/x-amz-json-1.1'"
  },
  "requestTemplates": {
    "application/xml": "

    3
   ",
    "application/json": "{\n}"
  },
  "type": "AWS",
  "uri": "arn:aws:apigateway:us-east-1:kinesis:action/ListStreams",
  "_embedded": {
    "integration:responses": {
      "_links": {
        "self": {
          "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200",
          "name": "200",
          "title": "200"
        },
        "integrationresponse:delete": {
          "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200"
        },
        "integrationresponse:update": {
          "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200"
        }
      },
      "responseParameters": {
        "method.response.header.Content-Type": "'application/xml'"
      },
      "responseTemplates": {
        "application/json": "$util.urlDecode(\"%3CkinesisStreams%3E#foreach($stream in $input.path('$.StreamNames'))%3Cstream%3E%3Cname%3E$stream%3C/name%3E%3C/stream%3E#end%3C/kinesisStreams%3E\")\n"
      },
      "statusCode": "200"
    }
  }
}
```

## See Also
<a name="API_UpdateIntegration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/apigateway-2015-07-09/UpdateIntegration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/apigateway-2015-07-09/UpdateIntegration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apigateway-2015-07-09/UpdateIntegration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/apigateway-2015-07-09/UpdateIntegration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apigateway-2015-07-09/UpdateIntegration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/apigateway-2015-07-09/UpdateIntegration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/apigateway-2015-07-09/UpdateIntegration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/apigateway-2015-07-09/UpdateIntegration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/apigateway-2015-07-09/UpdateIntegration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apigateway-2015-07-09/UpdateIntegration)
