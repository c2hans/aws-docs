---
source_url: https://docs.aws.amazon.com/apigateway/latest/api/API_CreateUsagePlan.html
---

# CreateUsagePlan
<a name="API_CreateUsagePlan"></a>

Creates a usage plan with the throttle and quota limits, as well as the associated API stages, specified in the payload.

## Request Syntax
<a name="API_CreateUsagePlan_RequestSyntax"></a>

```
POST /usageplans HTTP/1.1
Content-type: application/json

{
   "apiStages": [
      {
         "apiId": "{{string}}",
         "stage": "{{string}}",
         "throttle": {
            "{{string}}" : {
               "burstLimit": {{number}},
               "rateLimit": {{number}}
            }
         }
      }
   ],
   "description": "{{string}}",
   "name": "{{string}}",
   "quota": {
      "limit": {{number}},
      "offset": {{number}},
      "period": "{{string}}"
   },
   "tags": {
      "{{string}}" : "{{string}}"
   },
   "throttle": {
      "burstLimit": {{number}},
      "rateLimit": {{number}}
   }
}
```

## URI Request Parameters
<a name="API_CreateUsagePlan_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateUsagePlan_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [apiStages](#API_CreateUsagePlan_RequestSyntax) **   <a name="apigw-CreateUsagePlan-request-apiStages"></a>
The associated API stages of the usage plan.
Type: Array of [ApiStage](API_ApiStage.md) objects
Required: No

 ** [description](#API_CreateUsagePlan_RequestSyntax) **   <a name="apigw-CreateUsagePlan-request-description"></a>
The description of the usage plan.
Type: String
Required: No

 ** [name](#API_CreateUsagePlan_RequestSyntax) **   <a name="apigw-CreateUsagePlan-request-name"></a>
The name of the usage plan.
Type: String
Required: Yes

 ** [quota](#API_CreateUsagePlan_RequestSyntax) **   <a name="apigw-CreateUsagePlan-request-quota"></a>
The quota of the usage plan.
Type: [QuotaSettings](API_QuotaSettings.md) object
Required: No

 ** [tags](#API_CreateUsagePlan_RequestSyntax) **   <a name="apigw-CreateUsagePlan-request-tags"></a>
The key-value map of strings. The valid character set is [a-zA-Z\+-=.\_:/]. The tag key can be up to 128 characters and must not start with `aws:`. The tag value can be up to 256 characters.
Type: String to string map
Required: No

 ** [throttle](#API_CreateUsagePlan_RequestSyntax) **   <a name="apigw-CreateUsagePlan-request-throttle"></a>
The throttling limits of the usage plan.
Type: [ThrottleSettings](API_ThrottleSettings.md) object
Required: No

## Response Syntax
<a name="API_CreateUsagePlan_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "apiStages": [
      {
         "apiId": "string",
         "stage": "string",
         "throttle": {
            "string" : {
               "burstLimit": number,
               "rateLimit": number
            }
         }
      }
   ],
   "description": "string",
   "id": "string",
   "name": "string",
   "productCode": "string",
   "quota": {
      "limit": number,
      "offset": number,
      "period": "string"
   },
   "tags": {
      "string" : "string"
   },
   "throttle": {
      "burstLimit": number,
      "rateLimit": number
   }
}
```

## Response Elements
<a name="API_CreateUsagePlan_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [apiStages](#API_CreateUsagePlan_ResponseSyntax) **   <a name="apigw-CreateUsagePlan-response-apiStages"></a>
The associated API stages of a usage plan.
Type: Array of [ApiStage](API_ApiStage.md) objects

 ** [description](#API_CreateUsagePlan_ResponseSyntax) **   <a name="apigw-CreateUsagePlan-response-description"></a>
The description of a usage plan.
Type: String

 ** [id](#API_CreateUsagePlan_ResponseSyntax) **   <a name="apigw-CreateUsagePlan-response-id"></a>
The identifier of a UsagePlan resource.
Type: String

 ** [name](#API_CreateUsagePlan_ResponseSyntax) **   <a name="apigw-CreateUsagePlan-response-name"></a>
The name of a usage plan.
Type: String

 ** [productCode](#API_CreateUsagePlan_ResponseSyntax) **   <a name="apigw-CreateUsagePlan-response-productCode"></a>
The AWS Marketplace product identifier to associate with the usage plan as a SaaS product on the AWS Marketplace.
Type: String

 ** [quota](#API_CreateUsagePlan_ResponseSyntax) **   <a name="apigw-CreateUsagePlan-response-quota"></a>
The target maximum number of permitted requests per a given unit time interval.
Type: [QuotaSettings](API_QuotaSettings.md) object

 ** [tags](#API_CreateUsagePlan_ResponseSyntax) **   <a name="apigw-CreateUsagePlan-response-tags"></a>
The collection of tags. Each tag element is associated with a given resource.
Type: String to string map

 ** [throttle](#API_CreateUsagePlan_ResponseSyntax) **   <a name="apigw-CreateUsagePlan-response-throttle"></a>
A map containing method level throttling information for API stage in a usage plan.
Type: [ThrottleSettings](API_ThrottleSettings.md) object

## Errors
<a name="API_CreateUsagePlan_Errors"></a>

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
<a name="API_CreateUsagePlan_Examples"></a>

### Create a usage plan
<a name="API_CreateUsagePlan_Example_1"></a>

This example illustrates one usage of CreateUsagePlan.

#### Sample Request
<a name="API_CreateUsagePlan_Example_1_Request"></a>

```
POST /usageplans HTTP/1.1
Content-Type: application/json
Host: apigateway.us-east-1.amazonaws.com
X-Amz-Date: 20160805T013511Z
Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/20160805/us-east-1/apigateway/aws4_request, SignedHeaders=content-length;content-type;host;x-amz-date, Signature={sigv4_hash}
Cache-Control: no-cache
Postman-Token: c3ffa588-50e0-aa0c-234e-f191671564a9

{
  "name": "Plan_G",
  "description": "my plan",
  "apiStages": [ {
    "stage": "testStage",
    "apiId": "kdwpu39c2k"
  }],
  "quota": {
    "period": "DAY",
    "offset": 0,
    "limit": 500
  },
  "throttle": {
    "rateLimit": 100,
    "burstLimit": 200
  }
}
```

#### Sample Response
<a name="API_CreateUsagePlan_Example_1_Response"></a>

```
{
  "_links": {
    "curies": [
      {
        "href": "https://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-usage-{rel}.html",
        "name": "usage",
        "templated": true
      },
      {
        "href": "https://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-usageplan-{rel}.html",
        "name": "usageplan",
        "templated": true
      },
      {
        "href": "https://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-usageplankey-{rel}.html",
        "name": "usageplankey",
        "templated": true
      }
    ],
    "self": {
      "href": "/usageplans/1puccm"
    },
    "usage:get": {
      "href": "/usageplans/1puccm/usage?startDate=2016-07-06&endDate=2016-08-05"
    },
    "usageplan:delete": {
      "href": "/usageplans/1puccm"
    },
    "usageplan:update": {
      "href": "/usageplans/1puccm"
    },
    "usageplan:usageplankeys": {
      "href": "/usageplans/1puccm/keys"
    },
    "usageplankey:create": {
      "href": "/usageplans/1puccm/keys"
    }
  },
  "apiStages": {
    "stage": "testStage",
    "apiId": "kdwpu39c2k"
  },
  "description": "my plan",
  "id": "1puccm",
  "name": "Plan_G",
  "quota": {
    "period": "DAY",
    "offset": 0,
    "limit": 500
  },
  "throttle": {
    "rateLimit": 100,
    "burstLimit": 200
  }
}
```

## See Also
<a name="API_CreateUsagePlan_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/apigateway-2015-07-09/CreateUsagePlan)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/apigateway-2015-07-09/CreateUsagePlan)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apigateway-2015-07-09/CreateUsagePlan)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/apigateway-2015-07-09/CreateUsagePlan)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apigateway-2015-07-09/CreateUsagePlan)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/apigateway-2015-07-09/CreateUsagePlan)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/apigateway-2015-07-09/CreateUsagePlan)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/apigateway-2015-07-09/CreateUsagePlan)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/apigateway-2015-07-09/CreateUsagePlan)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apigateway-2015-07-09/CreateUsagePlan)
