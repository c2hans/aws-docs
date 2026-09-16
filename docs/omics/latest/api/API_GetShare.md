---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_GetShare.html
---

# GetShare
<a name="API_GetShare"></a>

Retrieves the metadata for the specified resource share.

## Request Syntax
<a name="API_GetShare_RequestSyntax"></a>

```
GET /share/{{shareId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetShare_RequestParameters"></a>

The request uses the following URI parameters.

 ** [shareId](#API_GetShare_RequestSyntax) **   <a name="omics-GetShare-request-uri-shareId"></a>
The ID of the share.
Required: Yes

## Request Body
<a name="API_GetShare_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetShare_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "share": {
      "creationTime": "string",
      "ownerId": "string",
      "principalSubscriber": "string",
      "resourceArn": "string",
      "resourceId": "string",
      "shareId": "string",
      "shareName": "string",
      "status": "string",
      "statusMessage": "string",
      "updateTime": "string"
   }
}
```

## Response Elements
<a name="API_GetShare_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [share](#API_GetShare_ResponseSyntax) **   <a name="omics-GetShare-response-share"></a>
A resource share details object. The object includes the status, the resourceArn, and ownerId.
Type: [ShareDetails](API_ShareDetails.md) object

## Errors
<a name="API_GetShare_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The request cannot be applied to the target resource in its current state.
HTTP Status Code: 409

 ** InternalServerException **
An unexpected error occurred. Try the request again.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The target resource was not found in the current Region.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The request exceeds a service quota.
HTTP Status Code: 402

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_GetShare_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/omics-2022-11-28/GetShare)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/omics-2022-11-28/GetShare)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/GetShare)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/omics-2022-11-28/GetShare)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/GetShare)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/omics-2022-11-28/GetShare)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/omics-2022-11-28/GetShare)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/omics-2022-11-28/GetShare)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/omics-2022-11-28/GetShare)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/GetShare)
