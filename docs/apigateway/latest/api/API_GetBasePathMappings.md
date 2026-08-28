---
source_url: https://docs.aws.amazon.com/apigateway/latest/api/API_GetBasePathMappings.html
---

# GetBasePathMappings
<a name="API_GetBasePathMappings"></a>

Represents a collection of BasePathMapping resources.

## Request Syntax
<a name="API_GetBasePathMappings_RequestSyntax"></a>

```
GET /domainnames/{{domain_name}}/basepathmappings?domainNameId={{domainNameId}}&limit={{limit}}&position={{position}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetBasePathMappings_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domain\_name](#API_GetBasePathMappings_RequestSyntax) **   <a name="apigw-GetBasePathMappings-request-uri-domainName"></a>
The domain name of a BasePathMapping resource.
Required: Yes

 ** [domainNameId](#API_GetBasePathMappings_RequestSyntax) **   <a name="apigw-GetBasePathMappings-request-uri-domainNameId"></a>
 The identifier for the domain name resource. Supported only for private custom domain names.

 ** [limit](#API_GetBasePathMappings_RequestSyntax) **   <a name="apigw-GetBasePathMappings-request-uri-limit"></a>
The maximum number of returned results per page. The default value is 25 and the maximum value is 500.

 ** [position](#API_GetBasePathMappings_RequestSyntax) **   <a name="apigw-GetBasePathMappings-request-uri-position"></a>
The current pagination position in the paged result set.

## Request Body
<a name="API_GetBasePathMappings_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetBasePathMappings_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "item": [
      {
         "basePath": "string",
         "restApiId": "string",
         "stage": "string"
      }
   ],
   "position": "string"
}
```

## Response Elements
<a name="API_GetBasePathMappings_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [item](#API_GetBasePathMappings_ResponseSyntax) **   <a name="apigw-GetBasePathMappings-response-item"></a>
The current page of elements from this collection.
Type: Array of [BasePathMapping](API_BasePathMapping.md) objects

 ** [position](#API_GetBasePathMappings_ResponseSyntax) **   <a name="apigw-GetBasePathMappings-response-position"></a>
The current pagination position in the paged result set.
Type: String

## Errors
<a name="API_GetBasePathMappings_Errors"></a>

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
<a name="API_GetBasePathMappings_Examples"></a>

### Get the base path mappings of a custom domain name
<a name="API_GetBasePathMappings_Example_1"></a>

This example illustrates one usage of GetBasePathMappings.

#### Sample Request
<a name="API_GetBasePathMappings_Example_1_Request"></a>

```
GET /domainnames/a.b.c.com/basepathmappings HTTP/1.1
Content-Type: application/json
Host: apigateway.us-east-1.amazonaws.com
X-Amz-Date: 20160615T221921Z
Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/20160615/us-east-1/apigateway/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature={sig4_hash}
```

#### Sample Response
<a name="API_GetBasePathMappings_Example_1_Response"></a>

```
{
  "_links": {
    "curies": {
      "href": "https://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-basepathmapping-{rel}.html",
      "name": "basepathmapping",
      "templated": true
    },
    "self": {
      "href": "/domainnames/a.b.c.com/basepathmappings{?limit}",
      "templated": true
    },
    "basepathmapping:by-path": {
      "href": "/domainnames/a.b.c.com/basepathmappings/{base_path}",
      "templated": true
    },
    "basepathmapping:create": {
      "href": "/domainnames/a.b.c.com/basepathmappings"
    },
    "item": [
      {
        "href": "/domainnames/a.b.c.com/basepathmappings/my-service-api"
      },
      {
        "href": "/domainnames/a.b.c.com/basepathmappings/my-sample-api"
      }
    ]
  },
  "_embedded": {
    "item": [
      {
        "_links": {
          "self": {
            "href": "/domainnames/a.b.c.com/basepathmappings/my-service-api"
          },
          "basepathmapping:create": {
            "href": "/domainnames/a.b.c.com/basepathmappings"
          },
          "basepathmapping:delete": {
            "href": "/domainnames/a.b.c.com/basepathmappings/my-service-api"
          },
          "basepathmapping:update": {
            "href": "/domainnames/a.b.c.com/basepathmappings/my-service-api"
          }
        },
        "basepath": "my-service-api",
        "restApiId": "fugvjdxtri",
        "stage": "stage2"
      },
      {
        "_links": {
          "self": {
            "href": "/domainnames/a.b.c.com/basepathmappings/my-sample-api"
          },
          "basepathmapping:create": {
            "href": "/domainnames/a.b.c.com/basepathmappings"
          },
          "basepathmapping:delete": {
            "href": "/domainnames/a.b.c.com/basepathmappings/my-sample-api"
          },
          "basepathmapping:update": {
            "href": "/domainnames/a.b.c.com/basepathmappings/my-sample-api"
          }
        },
        "basepath": "my-sample-api",
        "restApiId": "fugvjdxtri",
        "stage": "stage1"
      }
    ]
  }
}
```

## See Also
<a name="API_GetBasePathMappings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/apigateway-2015-07-09/GetBasePathMappings)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/apigateway-2015-07-09/GetBasePathMappings)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apigateway-2015-07-09/GetBasePathMappings)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/apigateway-2015-07-09/GetBasePathMappings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apigateway-2015-07-09/GetBasePathMappings)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/apigateway-2015-07-09/GetBasePathMappings)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/apigateway-2015-07-09/GetBasePathMappings)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/apigateway-2015-07-09/GetBasePathMappings)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/apigateway-2015-07-09/GetBasePathMappings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apigateway-2015-07-09/GetBasePathMappings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon API Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apigateway` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
