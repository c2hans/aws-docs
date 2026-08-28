---
source_url: https://docs.aws.amazon.com/apigateway/latest/api/API_GetDeployment.html
---

# GetDeployment
<a name="API_GetDeployment"></a>

Gets information about a Deployment resource.

## Request Syntax
<a name="API_GetDeployment_RequestSyntax"></a>

```
GET /restapis/{{restapi_id}}/deployments/{{deployment_id}}?embed={{embed}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetDeployment_RequestParameters"></a>

The request uses the following URI parameters.

 ** [deployment\_id](#API_GetDeployment_RequestSyntax) **   <a name="apigw-GetDeployment-request-uri-deploymentId"></a>
The identifier of the Deployment resource to get information about.
Required: Yes

 ** [embed](#API_GetDeployment_RequestSyntax) **   <a name="apigw-GetDeployment-request-uri-embed"></a>
A query parameter to retrieve the specified embedded resources of the returned Deployment resource in the response. In a REST API call, this `embed` parameter value is a list of comma-separated strings, as in `GET /restapis/{restapi_id}/deployments/{deployment_id}?embed=var1,var2`. The SDK and other platform-dependent libraries might use a different format for the list. Currently, this request supports only retrieval of the embedded API summary this way. Hence, the parameter value must be a single-valued list containing only the `"apisummary"` string. For example, `GET /restapis/{restapi_id}/deployments/{deployment_id}?embed=apisummary`.

 ** [restapi\_id](#API_GetDeployment_RequestSyntax) **   <a name="apigw-GetDeployment-request-uri-restApiId"></a>
The string identifier of the associated RestApi.
Required: Yes

## Request Body
<a name="API_GetDeployment_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetDeployment_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "apiSummary": {
      "string" : {
         "string" : {
            "apiKeyRequired": boolean,
            "authorizationType": "string"
         }
      }
   },
   "createdDate": number,
   "description": "string",
   "id": "string"
}
```

## Response Elements
<a name="API_GetDeployment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [apiSummary](#API_GetDeployment_ResponseSyntax) **   <a name="apigw-GetDeployment-response-apiSummary"></a>
A summary of the RestApi at the date and time that the deployment resource was created.
Type: String to string to [MethodSnapshot](API_MethodSnapshot.md) object map map

 ** [createdDate](#API_GetDeployment_ResponseSyntax) **   <a name="apigw-GetDeployment-response-createdDate"></a>
The date and time that the deployment resource was created.
Type: Timestamp

 ** [description](#API_GetDeployment_ResponseSyntax) **   <a name="apigw-GetDeployment-response-description"></a>
The description for the deployment resource.
Type: String

 ** [id](#API_GetDeployment_ResponseSyntax) **   <a name="apigw-GetDeployment-response-id"></a>
The identifier for the deployment resource.
Type: String

## Errors
<a name="API_GetDeployment_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.
HTTP Status Code: 400

 ** NotFoundException **
The requested resource is not found. Make sure that the request URI is correct.
HTTP Status Code: 404

 ** ServiceUnavailableException **
The requested service is not available. For details see the accompanying error message. Retry after the specified time period.
HTTP Status Code: 503

 ** TooManyRequestsException **
The request has reached its throttling limit. Retry after the specified time period.
HTTP Status Code: 429

 ** UnauthorizedException **
The request is denied because the caller has insufficient permissions.
HTTP Status Code: 401

## Examples
<a name="API_GetDeployment_Examples"></a>

### Retrieve a deployment
<a name="API_GetDeployment_Example_1"></a>

This example illustrates one usage of GetDeployment.

#### Sample Request
<a name="API_GetDeployment_Example_1_Request"></a>

```
GET /restapis/{restapi_id}/deployments/{deployment-id}?embed=apisummary HTTP/1.1
Content-Type: application/json
Host: apigateway.us-east-1.amazonaws.com
X-Amz-Date: 20160520T055303Z
Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/20160520/us-east-1/apigateway/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature={hash}
Cache-Control: no-cache
```

#### Sample Response
<a name="API_GetDeployment_Example_1_Response"></a>

```
{
"_links": {
  "curies": {
    "href": "https://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-deployment-{rel}.html",
    "name": "deployment",
    "templated": true
  },
  "self": {
    "href": "/restapis/{restapi-id}/deployments/{deployment-id}"
  },
  "deployment:delete": {
    "href": "/restapis/{restapi-id}/deployments/{deployment-id}"
  },
  "deployment:stages": {
    "href": "/restapis/{restapi-id}/stages?deployment_id={deployment-id}"
  },
  "deployment:update": {
    "href": "/restapis/{restapi-id}/deployments/{deployment-id}"
  }
},
"apiSummary": {
  "/petstorewalkthrough/pets/{petId}": {
    "GET": {
      "apiKeyRequired": false,
      "authorizationType": "NONE"
    }
  },
  "/mydemoawsproxy": {
    "GET": {
      "apiKeyRequired": false,
      "authorizationType": "NONE"
    }
  }
},
"createdDate": "2016-02-12T22:20:25Z",
"id": "{deployment-id}"
}
```

## See Also
<a name="API_GetDeployment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/apigateway-2015-07-09/GetDeployment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/apigateway-2015-07-09/GetDeployment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apigateway-2015-07-09/GetDeployment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/apigateway-2015-07-09/GetDeployment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apigateway-2015-07-09/GetDeployment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/apigateway-2015-07-09/GetDeployment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/apigateway-2015-07-09/GetDeployment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/apigateway-2015-07-09/GetDeployment)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/apigateway-2015-07-09/GetDeployment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apigateway-2015-07-09/GetDeployment)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon API Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apigateway` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
