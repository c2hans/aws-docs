---
source_url: https://docs.aws.amazon.com/rtb-fabric/latest/api/API_GetUpdate.html
---

# GetUpdate

Returns the status of an update. RTB Fabric keeps a completed update for 90 days after it finishes.

## Request Syntax
<a name="API_GetUpdate_RequestSyntax"></a>

```
GET /gateway/{{gatewayId}}/updates/{{updateId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetUpdate_RequestParameters"></a>

The request uses the following URI parameters.

 ** [gatewayId](#API_GetUpdate_RequestSyntax) **   <a name="rtbfabric-GetUpdate-request-uri-gatewayId"></a>
The unique identifier of the gateway.
Length Constraints: Minimum length of 8. Maximum length of 32.
Pattern: `rtb-gw-[a-z0-9-]{1,25}`
Required: Yes

 ** [updateId](#API_GetUpdate_RequestSyntax) **   <a name="rtbfabric-GetUpdate-request-uri-updateId"></a>
The unique identifier of the update.
Length Constraints: Minimum length of 8. Maximum length of 64.
Pattern: `update-[a-z0-9]{1,57}`
Required: Yes

## Request Body
<a name="API_GetUpdate_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetUpdate_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "update": {
      "createdAt": number,
      "errorDetails": [
         {
            "code": "string",
            "message": "string",
            "resourceIds": [ "string" ]
         }
      ],
      "parameters": { ... },
      "status": "string",
      "target": { ... },
      "type": "string",
      "updateId": "string"
   }
}
```

## Response Elements
<a name="API_GetUpdate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [update](#API_GetUpdate_ResponseSyntax) **   <a name="rtbfabric-GetUpdate-response-update"></a>
The update.
Type: [Update](API_Update.md) object

## Errors
<a name="API_GetUpdate_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request could not be completed because you do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
The request could not be completed because of an internal server error. Try your call again.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The request could not be completed because the resource does not exist.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The request could not be completed because it fails to satisfy the constraints specified by the service.
HTTP Status Code: 400

## See Also
<a name="API_GetUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rtbfabric-2023-05-15/GetUpdate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rtbfabric-2023-05-15/GetUpdate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rtbfabric-2023-05-15/GetUpdate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rtbfabric-2023-05-15/GetUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rtbfabric-2023-05-15/GetUpdate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rtbfabric-2023-05-15/GetUpdate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rtbfabric-2023-05-15/GetUpdate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rtbfabric-2023-05-15/GetUpdate)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/rtbfabric-2023-05-15/GetUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rtbfabric-2023-05-15/GetUpdate)
