---
source_url: https://docs.aws.amazon.com/apigateway/latest/api/API_GetUsagePlan.html
---

# GetUsagePlan
<a name="API_GetUsagePlan"></a>

Gets a usage plan of a given plan identifier.

## Request Syntax
<a name="API_GetUsagePlan_RequestSyntax"></a>

```
GET /usageplans/{{usageplanId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetUsagePlan_RequestParameters"></a>

The request uses the following URI parameters.

 ** [usageplanId](#API_GetUsagePlan_RequestSyntax) **   <a name="apigw-GetUsagePlan-request-uri-usagePlanId"></a>
The identifier of the UsagePlan resource to be retrieved.
Required: Yes

## Request Body
<a name="API_GetUsagePlan_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetUsagePlan_ResponseSyntax"></a>

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
<a name="API_GetUsagePlan_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [apiStages](#API_GetUsagePlan_ResponseSyntax) **   <a name="apigw-GetUsagePlan-response-apiStages"></a>
The associated API stages of a usage plan.
Type: Array of [ApiStage](API_ApiStage.md) objects

 ** [description](#API_GetUsagePlan_ResponseSyntax) **   <a name="apigw-GetUsagePlan-response-description"></a>
The description of a usage plan.
Type: String

 ** [id](#API_GetUsagePlan_ResponseSyntax) **   <a name="apigw-GetUsagePlan-response-id"></a>
The identifier of a UsagePlan resource.
Type: String

 ** [name](#API_GetUsagePlan_ResponseSyntax) **   <a name="apigw-GetUsagePlan-response-name"></a>
The name of a usage plan.
Type: String

 ** [productCode](#API_GetUsagePlan_ResponseSyntax) **   <a name="apigw-GetUsagePlan-response-productCode"></a>
The AWS Marketplace product identifier to associate with the usage plan as a SaaS product on the AWS Marketplace.
Type: String

 ** [quota](#API_GetUsagePlan_ResponseSyntax) **   <a name="apigw-GetUsagePlan-response-quota"></a>
The target maximum number of permitted requests per a given unit time interval.
Type: [QuotaSettings](API_QuotaSettings.md) object

 ** [tags](#API_GetUsagePlan_ResponseSyntax) **   <a name="apigw-GetUsagePlan-response-tags"></a>
The collection of tags. Each tag element is associated with a given resource.
Type: String to string map

 ** [throttle](#API_GetUsagePlan_ResponseSyntax) **   <a name="apigw-GetUsagePlan-response-throttle"></a>
A map containing method level throttling information for API stage in a usage plan.
Type: [ThrottleSettings](API_ThrottleSettings.md) object

## Errors
<a name="API_GetUsagePlan_Errors"></a>

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
<a name="API_GetUsagePlan_Examples"></a>

### Retrieve information about a usage plan
<a name="API_GetUsagePlan_Example_1"></a>

This example illustrates one usage of GetUsagePlan.

#### Sample Request
<a name="API_GetUsagePlan_Example_1_Request"></a>

```
GET /usageplans/n371pt HTTP/1.1
Content-Type: application/json
Host: apigateway.us-east-1.amazonaws.com
X-Amz-Date: 20160805T012305Z
Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/20160805/us-east-1/apigateway/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature={sigvv4_hash}
Response
```

#### Sample Response
<a name="API_GetUsagePlan_Example_1_Response"></a>

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
      "href": "/usageplans/n371pt"
    },
    "usage:get": {
      "href": "/usageplans/n371pt/usage?startDate=2016-07-06&endDate=2016-08-05"
    },
    "usageplan:delete": {
      "href": "/usageplans/n371pt"
    },
    "usageplan:update": {
      "href": "/usageplans/n371pt"
    },
    "usageplan:usageplankeys": {
      "href": "/usageplans/n371pt/keys"
    },
    "usageplankey:create": {
      "href": "/usageplans/n371pt/keys"
    }
  },
  "apiStages": {
    "stage": "testStage",
    "apiId": "kdwpu39c2k"
  },
  "id": "n371pt",
  "name": "Plan_D",
  "quota": {
    "period": "DAY",
    "offset": 0,
    "limit": 5
  },
  "throttle": {
    "rateLimit": 100,
    "burstLimit": 200
  }
}
```

## See Also
<a name="API_GetUsagePlan_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/apigateway-2015-07-09/GetUsagePlan)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/apigateway-2015-07-09/GetUsagePlan)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apigateway-2015-07-09/GetUsagePlan)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/apigateway-2015-07-09/GetUsagePlan)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apigateway-2015-07-09/GetUsagePlan)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/apigateway-2015-07-09/GetUsagePlan)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/apigateway-2015-07-09/GetUsagePlan)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/apigateway-2015-07-09/GetUsagePlan)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/apigateway-2015-07-09/GetUsagePlan)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apigateway-2015-07-09/GetUsagePlan)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon API Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apigateway` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
