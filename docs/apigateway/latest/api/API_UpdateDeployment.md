---
source_url: https://docs.aws.amazon.com/apigateway/latest/api/API_UpdateDeployment.html
---

# UpdateDeployment
<a name="API_UpdateDeployment"></a>

Changes information about a Deployment resource.

## Request Syntax
<a name="API_UpdateDeployment_RequestSyntax"></a>

```
PATCH /restapis/{{restapi_id}}/deployments/{{deployment_id}} HTTP/1.1
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
<a name="API_UpdateDeployment_RequestParameters"></a>

The request uses the following URI parameters.

 ** [deployment\_id](#API_UpdateDeployment_RequestSyntax) **   <a name="apigw-UpdateDeployment-request-uri-deploymentId"></a>
The replacement identifier for the Deployment resource to change information about.
Required: Yes

 ** [restapi\_id](#API_UpdateDeployment_RequestSyntax) **   <a name="apigw-UpdateDeployment-request-uri-restApiId"></a>
The string identifier of the associated RestApi.
Required: Yes

## Request Body
<a name="API_UpdateDeployment_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [patchOperations](#API_UpdateDeployment_RequestSyntax) **   <a name="apigw-UpdateDeployment-request-patchOperations"></a>
For more information about supported patch operations, see [Patch Operations](patch-operations.md).
Type: Array of [PatchOperation](API_PatchOperation.md) objects
Required: No

## Response Syntax
<a name="API_UpdateDeployment_ResponseSyntax"></a>

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
<a name="API_UpdateDeployment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [apiSummary](#API_UpdateDeployment_ResponseSyntax) **   <a name="apigw-UpdateDeployment-response-apiSummary"></a>
A summary of the RestApi at the date and time that the deployment resource was created.
Type: String to string to [MethodSnapshot](API_MethodSnapshot.md) object map map

 ** [createdDate](#API_UpdateDeployment_ResponseSyntax) **   <a name="apigw-UpdateDeployment-response-createdDate"></a>
The date and time that the deployment resource was created.
Type: Timestamp

 ** [description](#API_UpdateDeployment_ResponseSyntax) **   <a name="apigw-UpdateDeployment-response-description"></a>
The description for the deployment resource.
Type: String

 ** [id](#API_UpdateDeployment_ResponseSyntax) **   <a name="apigw-UpdateDeployment-response-id"></a>
The identifier for the deployment resource.
Type: String

## Errors
<a name="API_UpdateDeployment_Errors"></a>

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
<a name="API_UpdateDeployment_Examples"></a>

### Update a deployment description
<a name="API_UpdateDeployment_Example_1"></a>

This example illustrates one usage of UpdateDeployment.

#### Sample Request
<a name="API_UpdateDeployment_Example_1_Request"></a>

```
PATCH /restapis/fugvjdxtri/deployments/dzacq7 HTTP/1.1
Content-Type: application/json
Host: apigateway.us-east-1.amazonaws.com
X-Amz-Date: 20160603T192159Z
Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/20160603/us-east-1/apigateway/aws4_request, SignedHeaders=content-length;content-type;host;x-amz-date, Signature={sig4_hash}

{
  "patchOperations" : [ {
    "op" : "replace",
    "path" : "/description",
    "value" : "Updated first deployment"
  } ]
}
```

#### Sample Response
<a name="API_UpdateDeployment_Example_1_Response"></a>

```
{
  "_links": {
    "curies": {
      "href": "https://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-deployment-{rel}.html",
      "name": "deployment",
      "templated": true
    },
    "self": {
      "href": "/restapis/fugvjdxtri/deployments/dzacq7"
    },
    "deployment:delete": {
      "href": "/restapis/fugvjdxtri/deployments/dzacq7"
    },
    "deployment:stages": {
      "href": "/restapis/fugvjdxtri/stages?deployment_id=dzacq7"
    },
    "deployment:update": {
      "href": "/restapis/fugvjdxtri/deployments/dzacq7"
    }
  },
  "createdDate": "2016-06-03T17:56:06Z",
  "description": "Updated first deployment",
  "id": "dzacq7"
}
```

## See Also
<a name="API_UpdateDeployment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/apigateway-2015-07-09/UpdateDeployment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/apigateway-2015-07-09/UpdateDeployment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apigateway-2015-07-09/UpdateDeployment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/apigateway-2015-07-09/UpdateDeployment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apigateway-2015-07-09/UpdateDeployment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/apigateway-2015-07-09/UpdateDeployment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/apigateway-2015-07-09/UpdateDeployment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/apigateway-2015-07-09/UpdateDeployment)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/apigateway-2015-07-09/UpdateDeployment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apigateway-2015-07-09/UpdateDeployment)
