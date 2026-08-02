---
source_url: https://docs.aws.amazon.com/apigateway/latest/api/API_UpdateUsagePlan.html
---

# UpdateUsagePlan
<a name="API_UpdateUsagePlan"></a>

Updates a usage plan of a given plan Id.

## Request Syntax
<a name="API_UpdateUsagePlan_RequestSyntax"></a>

```
PATCH /usageplans/{{usageplanId}} HTTP/1.1
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
<a name="API_UpdateUsagePlan_RequestParameters"></a>

The request uses the following URI parameters.

 ** [usageplanId](#API_UpdateUsagePlan_RequestSyntax) **   <a name="apigw-UpdateUsagePlan-request-uri-usagePlanId"></a>
The Id of the to-be-updated usage plan.
Required: Yes

## Request Body
<a name="API_UpdateUsagePlan_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [patchOperations](#API_UpdateUsagePlan_RequestSyntax) **   <a name="apigw-UpdateUsagePlan-request-patchOperations"></a>
For more information about supported patch operations, see [Patch Operations](patch-operations.md).
Type: Array of [PatchOperation](API_PatchOperation.md) objects
Required: No

## Response Syntax
<a name="API_UpdateUsagePlan_ResponseSyntax"></a>

```
HTTP/1.1 200
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
<a name="API_UpdateUsagePlan_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [apiStages](#API_UpdateUsagePlan_ResponseSyntax) **   <a name="apigw-UpdateUsagePlan-response-apiStages"></a>
The associated API stages of a usage plan.
Type: Array of [ApiStage](API_ApiStage.md) objects

 ** [description](#API_UpdateUsagePlan_ResponseSyntax) **   <a name="apigw-UpdateUsagePlan-response-description"></a>
The description of a usage plan.
Type: String

 ** [id](#API_UpdateUsagePlan_ResponseSyntax) **   <a name="apigw-UpdateUsagePlan-response-id"></a>
The identifier of a UsagePlan resource.
Type: String

 ** [name](#API_UpdateUsagePlan_ResponseSyntax) **   <a name="apigw-UpdateUsagePlan-response-name"></a>
The name of a usage plan.
Type: String

 ** [productCode](#API_UpdateUsagePlan_ResponseSyntax) **   <a name="apigw-UpdateUsagePlan-response-productCode"></a>
The AWS Marketplace product identifier to associate with the usage plan as a SaaS product on the AWS Marketplace.
Type: String

 ** [quota](#API_UpdateUsagePlan_ResponseSyntax) **   <a name="apigw-UpdateUsagePlan-response-quota"></a>
The target maximum number of permitted requests per a given unit time interval.
Type: [QuotaSettings](API_QuotaSettings.md) object

 ** [tags](#API_UpdateUsagePlan_ResponseSyntax) **   <a name="apigw-UpdateUsagePlan-response-tags"></a>
The collection of tags. Each tag element is associated with a given resource.
Type: String to string map

 ** [throttle](#API_UpdateUsagePlan_ResponseSyntax) **   <a name="apigw-UpdateUsagePlan-response-throttle"></a>
A map containing method level throttling information for API stage in a usage plan.
Type: [ThrottleSettings](API_ThrottleSettings.md) object

## Errors
<a name="API_UpdateUsagePlan_Errors"></a>

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
<a name="API_UpdateUsagePlan_Examples"></a>

### Update a usage plan
<a name="API_UpdateUsagePlan_Example_1"></a>

This example illustrates one usage of UpdateUsagePlan.

#### Sample Request
<a name="API_UpdateUsagePlan_Example_1_Request"></a>

```
PATCH /usageplans/w0mvrr HTTP/1.1
Content-Type: application/json
Host: apigateway.us-east-1.amazonaws.com
X-Amz-Date: 20160805T200901Z
Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/20160805/us-east-1/apigateway/aws4_request, SignedHeaders=content-length;content-type;host;x-amz-date, Signature={sigv4_hash}

{
    "patchOperations" : [ {
       "op": "add",
       "path": "/apiStages",
       "value": "o81lxisefl:Stage_A"
    },
    {
       "op": "replace",
       "path": "/name",
       "value": "new-plan-name"
    },
    {
       "op": "replace",
       "path": "/description",
       "value": "new-plan-description"
    },
    {
        "op": "replace",
        "path": "/quota/period",
        "value": "MONTH"
    },
    {
        "op": "replace",
        "path": "/quota/limit",
        "value": "1300"
    },
    {
        "op": "replace",
        "path": "/quota/offset",
        "value": "5"
    }]
}
```

#### Sample Response
<a name="API_UpdateUsagePlan_Example_1_Response"></a>

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
      "href": "/usageplans/w0mvrr"
    },
    "usage:get": {
      "href": "/usageplans/w0mvrr/usage?startDate=2016-07-06&endDate=2016-08-05"
    },
    "usageplan:delete": {
      "href": "/usageplans/w0mvrr"
    },
    "usageplan:update": {
      "href": "/usageplans/w0mvrr"
    },
    "usageplan:usageplankeys": {
      "href": "/usageplans/w0mvrr/keys"
    },
    "usageplankey:create": {
      "href": "/usageplans/w0mvrr/keys"
    }
  },
  "apiStages": {
    "stage": "Stage_A",
    "apiId": "o81lxisefl"
  },
  "description": "new-plan-description",
  "id": "w0mvrr",
  "name": "new-plan-name",
  "quota": {
    "period": "MONTH",
    "offset": 5,
    "limit": 1300
  },
  "throttle": {
    "rateLimit": 100,
    "burstLimit": 200
  }
}
```

## See Also
<a name="API_UpdateUsagePlan_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/apigateway-2015-07-09/UpdateUsagePlan)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/apigateway-2015-07-09/UpdateUsagePlan)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apigateway-2015-07-09/UpdateUsagePlan)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/apigateway-2015-07-09/UpdateUsagePlan)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apigateway-2015-07-09/UpdateUsagePlan)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/apigateway-2015-07-09/UpdateUsagePlan)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/apigateway-2015-07-09/UpdateUsagePlan)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/apigateway-2015-07-09/UpdateUsagePlan)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/apigateway-2015-07-09/UpdateUsagePlan)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apigateway-2015-07-09/UpdateUsagePlan)
